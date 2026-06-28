# MedOps Automation Pipeline & Hermes Integration Spec
**Document ID:** MS-0002  
**System:** MedOps Intelligence OS — Thought Reliquary (Ubuntu 24.04, 192.168.4.100)  
**Stack:** Hermes Orchestration · Claude API (Sonnet) · Ollama/Llama 3.1 8B · Python 3.12 · Docker  
**Author:** John Burroughs, Perioperative Supply Chain Specialist, UIHC  
**Companion:** MS-0001 — Data Architecture & Output Formats  
**Status:** Implementation Spec — v1.0  

---

## Overview

MS-0001 defined what the MedOps OS produces: device briefs, competitive matrices, substitution recommendations, emerging tech reports. This document defines how those outputs are generated — the automation layer that makes the system run with minimal manual intervention.

The core architecture is a Python pipeline orchestrated by Hermes, running on the Thought Reliquary. Three trigger types initiate the pipeline: on-demand requests (John queries a device DI directly), scheduled digests (Monday morning category intelligence), and alert-mode monitoring (immediate notification on recall or MAUDE spike for anything in the active formulary).

All code in this document is production-ready Python 3.12. Run it.

---

## Section 1: The Hermes Integration

### 1.1 Hermes MedOps Module Responsibilities

Hermes acts as the orchestration layer — it does not perform data collection or synthesis itself. Its job is to detect triggers, route execution to the correct pipeline function, handle retries and failures, and deliver output.

**Responsibilities by phase:**

| Phase | Hermes Action | Downstream |
|---|---|---|
| Trigger detection | Monitor for manual input, cron schedule, or alert condition | `pipeline.py` entrypoint |
| Data collection routing | Sequence ACCESSGUDID → OpenFDA → PubMed calls | `accessgudid.py`, `openfda.py`, `pubmed.py` |
| Claude API briefing | Pass normalized data to synthesis functions | `synthesizer.py` |
| Output routing | Save to knowledge base, optionally flag for human review, generate PDF | `knowledge_base.py`, `formatter.py` |
| Alert management | Recall and MAUDE spike detection; notification dispatch | `alerts.py` |

### 1.2 The Three Trigger Types

**Trigger 1 — On-Demand:** John enters a device DI, UDI, or catalog number. System generates a full device brief and saves it to the knowledge base. Ideal for VAC prep and product evaluations.

**Trigger 2 — Scheduled:** Weekly cron on Monday morning. Pulls new 510(k) clearances and recalls across all watched categories. Synthesizes into the Weekly Intelligence Digest. Delivered to email or Notion page by 8:00 AM.

**Trigger 3 — Alert:** Any device currently in the active formulary that receives a Class I or II recall or shows a MAUDE event spike (configurable threshold) triggers an immediate notification. This runs as a daily monitor.

### 1.3 Hermes Task Definitions

Hermes uses YAML task definitions. Each task defines trigger type, required inputs, execution steps, error handling, and output routing. The MedOps module registers three task definitions.

---

**Task Definition 1: On-Demand Device Brief**

```yaml
# medops_tasks.yaml — Task 1 of 3
task_name: device_brief_on_demand
version: "1.0"
description: "Full device evaluation brief from DI, UDI, or catalog number"
trigger:
  type: manual
  interface: cli           # invoked via: hermes run device_brief_on_demand --di "00843197107103"
  timeout_seconds: 120

inputs:
  - name: device_identifier
    type: string
    required: true
    description: "DI, full UDI string, or manufacturer catalog number"
  - name: output_format
    type: string
    required: false
    default: "markdown"
    allowed_values: ["markdown", "json", "pdf"]
  - name: include_substitutes
    type: boolean
    required: false
    default: true

steps:
  - step: resolve_identifier
    module: medops.accessgudid
    function: resolve_device_identifier
    inputs:
      identifier: "{{ inputs.device_identifier }}"
    outputs:
      - di
      - brand_name
      - product_code
      - gmdn_term
    on_failure:
      action: abort
      message: "Could not resolve identifier in ACCESSGUDID. Verify DI or UDI."

  - step: accessgudid_full_lookup
    module: medops.accessgudid
    function: get_device_by_di
    inputs:
      di: "{{ steps.resolve_identifier.outputs.di }}"
    outputs:
      - accessgudid_data
    on_failure:
      action: abort

  - step: openfda_enrichment
    module: medops.openfda
    function: get_device_full_fda_profile
    inputs:
      product_code: "{{ steps.resolve_identifier.outputs.product_code }}"
      brand_name: "{{ steps.resolve_identifier.outputs.brand_name }}"
    parallel:
      - function: get_510k_by_product_code
        output: fda_510k_data
      - function: get_recalls_by_product_code
        output: recall_data
      - function: get_maude_events
        output: maude_data
    on_failure:
      action: continue_with_warning
      message: "Partial FDA data — brief will note missing fields."

  - step: pubmed_literature
    module: medops.pubmed
    function: search_device_literature
    inputs:
      device_name: "{{ steps.resolve_identifier.outputs.brand_name }}"
      product_code: "{{ steps.resolve_identifier.outputs.product_code }}"
      max_results: 15
    outputs:
      - pubmed_abstracts
    on_failure:
      action: continue_with_warning

  - step: substitution_candidates
    module: medops.pipeline
    function: find_substitutes
    condition: "{{ inputs.include_substitutes == true }}"
    inputs:
      di: "{{ steps.resolve_identifier.outputs.di }}"
    outputs:
      - substitute_candidates
    on_failure:
      action: continue_with_warning

  - step: claude_brief_generation
    module: medops.synthesizer
    function: generate_device_brief
    inputs:
      accessgudid_data: "{{ steps.accessgudid_full_lookup.outputs.accessgudid_data }}"
      fda_data: "{{ steps.openfda_enrichment.outputs.fda_510k_data }}"
      maude_data: "{{ steps.openfda_enrichment.outputs.maude_data }}"
      recall_data: "{{ steps.openfda_enrichment.outputs.recall_data }}"
      pubmed_abstracts: "{{ steps.pubmed_literature.outputs.pubmed_abstracts }}"
      substitute_candidates: "{{ steps.substitution_candidates.outputs.substitute_candidates }}"
    outputs:
      - brief_markdown
      - anomaly_flags
    timeout_seconds: 60
    on_failure:
      action: abort
      message: "Claude API synthesis failed. Check ANTHROPIC_API_KEY and connectivity."

  - step: output_and_archive
    module: medops.knowledge_base
    function: save_brief
    inputs:
      brief_markdown: "{{ steps.claude_brief_generation.outputs.brief_markdown }}"
      accessgudid_data: "{{ steps.accessgudid_full_lookup.outputs.accessgudid_data }}"
      anomaly_flags: "{{ steps.claude_brief_generation.outputs.anomaly_flags }}"
      output_format: "{{ inputs.output_format }}"
    outputs:
      - case_id
      - output_path

output:
  success_message: "Device brief generated. Case ID: {{ steps.output_and_archive.outputs.case_id }}"
  output_path: "{{ steps.output_and_archive.outputs.output_path }}"
  
notifications:
  on_anomaly_flag:
    condition: "{{ steps.claude_brief_generation.outputs.anomaly_flags | length > 0 }}"
    message: "ANOMALY FLAGS detected in device brief {{ steps.output_and_archive.outputs.case_id }}: {{ steps.claude_brief_generation.outputs.anomaly_flags }}"
    channel: console
```

---

**Task Definition 2: Scheduled Weekly Category Digest**

```yaml
# medops_tasks.yaml — Task 2 of 3
task_name: medops_weekly_digest
version: "1.0"
description: "Weekly intelligence digest across all watched device categories"
trigger:
  type: cron
  schedule: "0 8 * * 1"    # Every Monday at 08:00 local time
  timezone: "America/Chicago"
  timeout_seconds: 600

inputs:
  - name: categories
    type: list
    required: false
    default: null             # null = all categories from watch_config.yaml
  - name: lookback_days
    type: integer
    required: false
    default: 7
  - name: delivery_channel
    type: string
    required: false
    default: "notion"
    allowed_values: ["notion", "email", "file"]

steps:
  - step: load_watch_config
    module: medops.pipeline
    function: load_category_watch_config
    inputs:
      config_path: "/app/data/watch_config.yaml"
      category_filter: "{{ inputs.categories }}"
    outputs:
      - watch_list

  - step: fetch_new_510k_clearances
    module: medops.openfda
    function: get_new_510k_clearances_by_product_codes
    inputs:
      product_codes: "{{ steps.load_watch_config.outputs.watch_list | map(attribute='product_codes') | flatten }}"
      days_back: "{{ inputs.lookback_days }}"
    outputs:
      - new_clearances

  - step: fetch_recall_activity
    module: medops.openfda
    function: get_recalls_for_watch_list
    inputs:
      watch_list: "{{ steps.load_watch_config.outputs.watch_list }}"
      days_back: "{{ inputs.lookback_days }}"
    outputs:
      - recall_events

  - step: fetch_maude_volumes
    module: medops.alerts
    function: check_maude_spikes
    inputs:
      days_lookback: "{{ inputs.lookback_days }}"
    outputs:
      - maude_alerts

  - step: fetch_pubmed_updates
    module: medops.pubmed
    function: search_device_literature_batch
    inputs:
      watch_list: "{{ steps.load_watch_config.outputs.watch_list }}"
      days_back: "{{ inputs.lookback_days }}"
    outputs:
      - literature_updates

  - step: generate_digest
    module: medops.synthesizer
    function: generate_weekly_digest
    inputs:
      new_clearances: "{{ steps.fetch_new_510k_clearances.outputs.new_clearances }}"
      recall_events: "{{ steps.fetch_recall_activity.outputs.recall_events }}"
      maude_alerts: "{{ steps.fetch_maude_volumes.outputs.maude_alerts }}"
      literature_updates: "{{ steps.fetch_pubmed_updates.outputs.literature_updates }}"
      watch_list: "{{ steps.load_watch_config.outputs.watch_list }}"
      period_label: "Week of {{ now | date('YYYY-MM-DD') }}"
    outputs:
      - digest_markdown
      - digest_summary

  - step: deliver_digest
    module: medops.pipeline
    function: deliver_digest
    inputs:
      digest_markdown: "{{ steps.generate_digest.outputs.digest_markdown }}"
      channel: "{{ inputs.delivery_channel }}"
    outputs:
      - delivery_confirmation

output:
  success_message: "Weekly digest delivered via {{ inputs.delivery_channel }}. Summary: {{ steps.generate_digest.outputs.digest_summary }}"
```

---

**Task Definition 3: Alert Monitor (Recall & MAUDE)**

```yaml
# medops_tasks.yaml — Task 3 of 3
task_name: medops_alert_monitor
version: "1.0"
description: "Daily check for recalls and MAUDE spikes against active formulary"
trigger:
  type: cron
  schedule: "0 9 * * *"    # Daily at 09:00 local time
  timezone: "America/Chicago"
  timeout_seconds: 300

inputs:
  - name: alert_channel
    type: string
    required: false
    default: "console"
    allowed_values: ["console", "email", "notion"]
  - name: maude_lookback_days
    type: integer
    required: false
    default: 30

steps:
  - step: load_formulary
    module: medops.knowledge_base
    function: get_formulary_devices
    outputs:
      - formulary_devices

  - step: check_recalls
    module: medops.alerts
    function: check_recalls_for_formulary
    inputs:
      formulary_devices: "{{ steps.load_formulary.outputs.formulary_devices }}"
    outputs:
      - recall_alerts

  - step: check_maude_spikes
    module: medops.alerts
    function: check_maude_spikes
    inputs:
      formulary_devices: "{{ steps.load_formulary.outputs.formulary_devices }}"
      days_lookback: "{{ inputs.maude_lookback_days }}"
    outputs:
      - maude_alerts

  - step: combine_and_deduplicate
    module: medops.alerts
    function: combine_alerts
    inputs:
      recall_alerts: "{{ steps.check_recalls.outputs.recall_alerts }}"
      maude_alerts: "{{ steps.check_maude_spikes.outputs.maude_alerts }}"
    outputs:
      - active_alerts

  - step: send_alerts
    condition: "{{ steps.combine_and_deduplicate.outputs.active_alerts | length > 0 }}"
    module: medops.alerts
    function: send_alert_batch
    inputs:
      alerts: "{{ steps.combine_and_deduplicate.outputs.active_alerts }}"
      channel: "{{ inputs.alert_channel }}"
    outputs:
      - notification_ids

  - step: log_to_knowledge_base
    module: medops.knowledge_base
    function: log_alerts
    inputs:
      alerts: "{{ steps.combine_and_deduplicate.outputs.active_alerts }}"

output:
  success_message: "Alert check complete. {{ steps.combine_and_deduplicate.outputs.active_alerts | length }} active alert(s)."
```

---

## Section 2: The Full Python Pipeline

### Module Structure

```
medops/
├── __init__.py
├── config.py           # API keys, base URLs, settings
├── accessgudid.py      # ACCESSGUDID API client
├── openfda.py          # OpenFDA API client
├── pubmed.py           # PubMed E-utilities client
├── synthesizer.py      # Claude API synthesis functions
├── formatter.py        # Output format generators
├── knowledge_base.py   # SQLite archive management
├── alerts.py           # Recall and MAUDE alert monitoring
├── pipeline.py         # Main orchestration
└── cli.py              # Command-line interface
```

---

### `medops/__init__.py`

```python
"""
MedOps Intelligence OS — MS-0002
Perioperative Supply Chain Automation Pipeline
University of Iowa Health Care — Thought Reliquary
"""

__version__ = "1.0.0"
__author__ = "John Burroughs"
__document_id__ = "MS-0002"
```

---

### `medops/config.py`

```python
"""
MedOps Configuration
All environment variables, base URLs, rate limit settings, and category configs.
"""

import os
from pathlib import Path

# ── Base URLs ───────────────────────────────────────────────────────────────

ACCESSGUDID_BASE = "https://accessgudid.nlm.nih.gov/api/v2/"
ACCESSGUDID_LOOKUP = f"{ACCESSGUDID_BASE}devices/lookup.json"
ACCESSGUDID_PARSE_UDI = f"{ACCESSGUDID_BASE}parse_udi"
ACCESSGUDID_BULK_RSS = "https://accessgudid.nlm.nih.gov/download.rss?files=full"
ACCESSGUDID_DOWNLOAD_BASE = "https://accessgudid.nlm.nih.gov/download"

OPENFDA_BASE = "https://api.fda.gov/device/"
OPENFDA_MAUDE = f"{OPENFDA_BASE}event.json"
OPENFDA_510K = f"{OPENFDA_BASE}510k.json"
OPENFDA_RECALLS = f"{OPENFDA_BASE}recall.json"
OPENFDA_ENFORCEMENT = f"{OPENFDA_BASE}enforcement.json"
OPENFDA_CLASSIFICATION = f"{OPENFDA_BASE}classification.json"
OPENFDA_PMA = f"{OPENFDA_BASE}pma.json"
OPENFDA_UDI = f"{OPENFDA_BASE}udi.json"
OPENFDA_REGISTRATIONS = f"{OPENFDA_BASE}registrationlisting.json"

PUBMED_BASE = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/"
PUBMED_SEARCH = f"{PUBMED_BASE}esearch.fcgi"
PUBMED_FETCH = f"{PUBMED_BASE}efetch.fcgi"
PUBMED_SUMMARY = f"{PUBMED_BASE}esummary.fcgi"

# ── API Keys ─────────────────────────────────────────────────────────────────

OPENFDA_API_KEY = os.getenv("OPENFDA_API_KEY", "")
ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY", "")
NOTION_API_KEY = os.getenv("NOTION_API_KEY", "")
PUBMED_API_KEY = os.getenv("PUBMED_API_KEY", "")    # Optional; increases PubMed rate limit

# ── Rate Limits ──────────────────────────────────────────────────────────────

# OpenFDA: 240/min with key, 40/min without; 4 req/sec burst limit
OPENFDA_DELAY_WITH_KEY = 0.26       # seconds between requests
OPENFDA_DELAY_WITHOUT_KEY = 1.6
OPENFDA_BACKOFF_BASE = 2.0          # exponential backoff base (seconds)
OPENFDA_MAX_RETRIES = 4
OPENFDA_MAX_SKIP = 25000            # Hard cap on skip + limit

# ACCESSGUDID: no documented limit; conservative 0.5s delay
ACCESSGUDID_DELAY = 0.5

# PubMed: 3 req/sec without key, 10 req/sec with key
PUBMED_DELAY_WITH_KEY = 0.12
PUBMED_DELAY_WITHOUT_KEY = 0.35

# Claude API
CLAUDE_MODEL = os.getenv("CLAUDE_MODEL", "claude-sonnet-4-5")
CLAUDE_MAX_TOKENS = 4096
CLAUDE_TEMPERATURE = 0.2            # Low temp for factual synthesis

# ── Paths ────────────────────────────────────────────────────────────────────

DATA_DIR = Path(os.getenv("MEDOPS_DATA_DIR", "/app/data"))
DB_PATH = DATA_DIR / "medops.db"
GMDN_INDEX_PATH = DATA_DIR / "gmdn_index.db"
GUDID_BULK_PATH = DATA_DIR / "gudid_bulk"
WATCH_CONFIG_PATH = DATA_DIR / "watch_config.yaml"
BRIEFS_DIR = DATA_DIR / "briefs"
DIGESTS_DIR = DATA_DIR / "digests"

# Create dirs if needed
for d in [DATA_DIR, GUDID_BULK_PATH, BRIEFS_DIR, DIGESTS_DIR]:
    d.mkdir(parents=True, exist_ok=True)

# ── Notion Database IDs ──────────────────────────────────────────────────────

NOTION_DEVICE_REGISTRY_DB = os.getenv("NOTION_DEVICE_REGISTRY_DB", "")
NOTION_EVALUATION_QUEUE_DB = os.getenv("NOTION_EVALUATION_QUEUE_DB", "")
NOTION_MATRICES_DB = os.getenv("NOTION_MATRICES_DB", "")
NOTION_ALERTS_LOG_DB = os.getenv("NOTION_ALERTS_LOG_DB", "")

# ── Notification Settings ────────────────────────────────────────────────────

ALERT_EMAIL_TO = os.getenv("ALERT_EMAIL_TO", "")
ALERT_EMAIL_FROM = os.getenv("ALERT_EMAIL_FROM", "medops@thoughtreliquary.local")
SMTP_HOST = os.getenv("SMTP_HOST", "localhost")
SMTP_PORT = int(os.getenv("SMTP_PORT", "25"))

# ── Category Configuration (inline defaults; overridden by watch_config.yaml) ─

DEFAULT_MAUDE_LOOKBACK_DAYS = 30
DEFAULT_RECALL_LOOKBACK_YEARS = 5
DEFAULT_510K_LOOKBACK_DAYS = 7
DEFAULT_PUBMED_MAX_RESULTS = 15

# Device classes for formulary classification
DEVICE_CLASS_LABELS = {"1": "Class I", "2": "Class II", "3": "Class III"}

# Recall severity for alert routing
RECALL_SEVERITY_MAP = {
    "Class I": "CRITICAL",
    "Class II": "HIGH",
    "Class III": "LOW",
}
```

---

### `medops/accessgudid.py`

```python
"""
ACCESSGUDID API Client
Handles all lookups against the NLM ACCESSGUDID v2 API.

Endpoints used:
  GET https://accessgudid.nlm.nih.gov/api/v2/devices/lookup.json?di={DI}
  GET https://accessgudid.nlm.nih.gov/api/v2/devices/lookup.json?udi={UDI}
  GET https://accessgudid.nlm.nih.gov/api/v2/parse_udi?udi={UDI}
"""

import time
import logging
import requests
from typing import Optional
from medops.config import (
    ACCESSGUDID_LOOKUP,
    ACCESSGUDID_PARSE_UDI,
    ACCESSGUDID_DELAY,
)

logger = logging.getLogger(__name__)

_last_request_time: float = 0.0


def _get(params: dict) -> dict:
    """Rate-limited GET against ACCESSGUDID lookup endpoint."""
    global _last_request_time
    elapsed = time.time() - _last_request_time
    if elapsed < ACCESSGUDID_DELAY:
        time.sleep(ACCESSGUDID_DELAY - elapsed)
    try:
        resp = requests.get(ACCESSGUDID_LOOKUP, params=params, timeout=15)
        _last_request_time = time.time()
        resp.raise_for_status()
        return resp.json()
    except requests.exceptions.HTTPError as e:
        if resp.status_code == 404:
            logger.warning(f"ACCESSGUDID: Device not found — params={params}")
            return {}
        raise


def _normalize_device_record(raw: dict) -> dict:
    """
    Flatten the nested ACCESSGUDID response into a clean, uniform dict.
    Handles optional fields gracefully.
    """
    if not raw or "gudid" not in raw:
        return {}

    dev = raw["gudid"]["device"]

    # Product codes may be a dict (single) or list; normalize to list
    raw_pc = dev.get("productCodes", {}).get("fdaProductCode", {})
    if isinstance(raw_pc, dict):
        product_codes = [raw_pc] if raw_pc else []
    else:
        product_codes = raw_pc or []

    # GMDN terms — normalize to list
    raw_gmdn = dev.get("gmdnTerms", {}).get("gmdn", {})
    if isinstance(raw_gmdn, dict):
        gmdn_terms = [raw_gmdn] if raw_gmdn else []
    else:
        gmdn_terms = raw_gmdn or []

    # Identifiers — normalize to list
    raw_ids = dev.get("identifiers", {}).get("identifier", {})
    if isinstance(raw_ids, dict):
        identifiers = [raw_ids] if raw_ids else []
    else:
        identifiers = raw_ids or []

    # Primary DI is the first identifier of type "Primary"
    primary_di = next(
        (i["deviceId"] for i in identifiers if i.get("deviceIdType") == "Primary"),
        dev.get("identifiers", {}).get("identifier", {}).get("deviceId", "")
    )

    sterilization = dev.get("sterilization", {})
    sterilization_methods_raw = sterilization.get("methodTypes", {}).get("methodType", [])
    if isinstance(sterilization_methods_raw, str):
        sterilization_methods = [sterilization_methods_raw]
    elif isinstance(sterilization_methods_raw, dict):
        sterilization_methods = [sterilization_methods_raw.get("sterilizationMethodType", "")]
    else:
        sterilization_methods = [
            m.get("sterilizationMethodType", "") for m in sterilization_methods_raw
        ]

    contacts = dev.get("contacts", {}).get("customerContact", {})

    return {
        # Core identification
        "primary_di": primary_di,
        "brand_name": dev.get("brandName", ""),
        "version_model_number": dev.get("versionModelNumber", ""),
        "catalog_number": dev.get("catalogNumber", ""),
        "device_description": dev.get("deviceDescription", ""),
        "company_name": dev.get("companyName", ""),
        "duns_number": dev.get("dunsNumber", ""),
        "public_device_record_key": dev.get("publicDeviceRecordKey", ""),
        "device_count": dev.get("deviceCount", ""),
        # Regulatory
        "product_codes": [
            {
                "product_code": pc.get("productCode", ""),
                "product_code_name": pc.get("productCodeName", ""),
            }
            for pc in product_codes
        ],
        "primary_product_code": product_codes[0].get("productCode", "") if product_codes else "",
        "device_class": product_codes[0].get("deviceClass", "") if product_codes else "",
        "regulation_number": product_codes[0].get("regulationNumber", "") if product_codes else "",
        "life_sustain_support_flag": product_codes[0].get("lifeSustainSupportFlag", "") if product_codes else "",
        "implant_flag": product_codes[0].get("implantFlag", "") if product_codes else "",
        "premarket_submission_number": dev.get("premarketSubmissions", {}).get(
            "premarketSubmission", {}).get("submissionNumber", ""),
        # GMDN
        "gmdn_terms": [
            {
                "gmdn_pt_name": g.get("gmdnPTName", ""),
                "gmdn_pt_definition": g.get("gmdnPTDefinition", ""),
                "gmdn_pt_code": g.get("gmdnPTCode", ""),
                "implantable": g.get("implantableDeviceDescription", ""),
            }
            for g in gmdn_terms
        ],
        "primary_gmdn_name": gmdn_terms[0].get("gmdnPTName", "") if gmdn_terms else "",
        "primary_gmdn_code": gmdn_terms[0].get("gmdnPTCode", "") if gmdn_terms else "",
        # Device characteristics
        "mri_safety_status": dev.get("MRISafetyStatus", ""),
        "single_use": dev.get("singleUse", False),
        "device_sterile": sterilization.get("deviceSterile", False),
        "sterilization_prior_to_use": sterilization.get("sterilizationPriorToUse", False),
        "sterilization_methods": sterilization_methods,
        "labeled_contains_nrl": dev.get("labeledContainsNRL", False),
        "labeled_no_nrl": dev.get("labeledNoNRL", False),
        "rx": dev.get("rx", False),
        "otc": dev.get("otc", False),
        "is_kit": dev.get("deviceKit", False),
        "combination_product": dev.get("deviceCombinationProduct", False),
        "hctp": dev.get("deviceHCTP", False),
        # Distribution
        "commercial_distribution_status": dev.get("deviceCommDistributionStatus", ""),
        "distribution_end_date": dev.get("deviceCommDistributionEndDate", ""),
        "device_record_status": dev.get("deviceRecordStatus", ""),
        # Sizes
        "device_sizes": dev.get("deviceSizes", {}).get("deviceSize", []),
        # Contact
        "customer_phone": contacts.get("phone", ""),
        "customer_email": contacts.get("email", ""),
        # Storage
        "storage_handling": dev.get("storageHandling", {}).get("storageHandlingEntry", []),
        # Identifiers list (all DIs for this device family)
        "identifiers": identifiers,
    }


def get_device_by_di(di: str) -> dict:
    """
    Look up a device by its Device Identifier (DI).
    Returns normalized device record dict.
    """
    logger.info(f"ACCESSGUDID lookup by DI: {di}")
    raw = _get({"di": di})
    return _normalize_device_record(raw)


def get_device_by_udi(udi: str) -> dict:
    """
    Look up a device by its full UDI string (percent-encoded internally).
    Returns normalized device record dict.
    """
    logger.info(f"ACCESSGUDID lookup by UDI: {udi[:30]}...")
    raw = _get({"udi": udi})
    return _normalize_device_record(raw)


def parse_udi(udi: str) -> dict:
    """
    Parse a full UDI string into DI + production identifier components.
    Uses the ACCESSGUDID Parse UDI endpoint.
    Returns raw parsed UDI dict.
    """
    global _last_request_time
    elapsed = time.time() - _last_request_time
    if elapsed < ACCESSGUDID_DELAY:
        time.sleep(ACCESSGUDID_DELAY - elapsed)

    resp = requests.get(ACCESSGUDID_PARSE_UDI, params={"udi": udi}, timeout=15)
    _last_request_time = time.time()
    resp.raise_for_status()
    return resp.json()


def resolve_device_identifier(identifier: str) -> dict:
    """
    Attempt to resolve an identifier that could be a DI, full UDI, or catalog number.
    Returns a dict with: di, brand_name, product_code, gmdn_term, gmdn_code, resolution_method.

    Resolution order:
    1. Try direct DI lookup (ACCESSGUDID v2)
    2. Try UDI parse (if identifier looks like a full UDI — contains issuing agency prefix)
    3. Raise ValueError if neither resolves
    """
    # Heuristic: full UDIs typically start with (01) or have GS1/HIBCC/ICCBBA prefix patterns
    looks_like_udi = (
        identifier.startswith("(01)") or
        identifier.startswith("/") or
        len(identifier) > 20 and not identifier.isdigit()
    )

    device_data = {}

    if not looks_like_udi:
        # Try DI lookup first
        device_data = get_device_by_di(identifier)
        if device_data:
            method = "di_lookup"
        else:
            # Try as UDI
            try:
                parsed = parse_udi(identifier)
                di = parsed.get("udi", {}).get("di", "")
                if di:
                    device_data = get_device_by_di(di)
                    method = "udi_parse"
            except Exception:
                pass
    else:
        try:
            parsed = parse_udi(identifier)
            di = parsed.get("udi", {}).get("di", "")
            if di:
                device_data = get_device_by_di(di)
                method = "udi_parse"
        except Exception:
            device_data = get_device_by_di(identifier)
            method = "di_fallback"

    if not device_data:
        raise ValueError(
            f"Could not resolve identifier '{identifier}' in ACCESSGUDID. "
            "Verify the DI or UDI string is correct."
        )

    return {
        "di": device_data.get("primary_di", identifier),
        "brand_name": device_data.get("brand_name", ""),
        "product_code": device_data.get("primary_product_code", ""),
        "gmdn_term": device_data.get("primary_gmdn_name", ""),
        "gmdn_code": device_data.get("primary_gmdn_code", ""),
        "company_name": device_data.get("company_name", ""),
        "resolution_method": method if 'method' in dir() else "unknown",
    }


def search_devices_by_gmdn(gmdn_term: str, limit: int = 20) -> list:
    """
    Search for devices by GMDN term name via OpenFDA UDI endpoint (ACCESSGUDID mirror).
    GMDN reverse lookup is not directly available via the ACCESSGUDID v2 API;
    use the OpenFDA UDI mirror instead, or use the local GMDN index (see pipeline.py).

    Returns list of normalized device records.
    """
    import requests as req
    from medops.config import OPENFDA_UDI, OPENFDA_API_KEY, OPENFDA_DELAY_WITH_KEY

    params = {
        "search": f'gmdn_terms.gmdn_pt_name:"{gmdn_term}"',
        "limit": min(limit, 100),
    }
    if OPENFDA_API_KEY:
        params["api_key"] = OPENFDA_API_KEY

    time.sleep(OPENFDA_DELAY_WITH_KEY if OPENFDA_API_KEY else 1.5)
    resp = req.get(OPENFDA_UDI, params=params, timeout=20)

    if resp.status_code == 404:
        logger.warning(f"No GMDN results found for term: {gmdn_term}")
        return []

    resp.raise_for_status()
    results = resp.json().get("results", [])

    # OpenFDA UDI records have different structure; normalize minimally
    normalized = []
    for r in results:
        normalized.append({
            "primary_di": r.get("public_device_record_key", ""),
            "brand_name": r.get("brand_name", ""),
            "company_name": r.get("company_name", ""),
            "version_model_number": r.get("version_or_model_number", ""),
            "catalog_number": r.get("catalog_number", ""),
            "commercial_distribution_status": r.get("commercial_distribution_status", ""),
            "single_use": r.get("is_single_use", False),
            "device_sterile": r.get("is_sterile", False),
            "mri_safety_status": r.get("mri_safety", ""),
            "primary_gmdn_name": gmdn_term,
        })

    return normalized
```

---

### `medops/openfda.py`

```python
"""
OpenFDA API Client
Handles all queries against the FDA's OpenFDA device endpoints.

Rate limits: 240 req/min with API key, 40/min without.
Hard skip cap: skip + limit <= 25,000.
All functions include exponential backoff on 429 responses.
"""

import time
import logging
import requests
from datetime import datetime, timedelta
from typing import Optional
from medops.config import (
    OPENFDA_BASE, OPENFDA_MAUDE, OPENFDA_510K,
    OPENFDA_RECALLS, OPENFDA_ENFORCEMENT, OPENFDA_CLASSIFICATION,
    OPENFDA_PMA, OPENFDA_UDI, OPENFDA_REGISTRATIONS,
    OPENFDA_API_KEY, OPENFDA_DELAY_WITH_KEY, OPENFDA_DELAY_WITHOUT_KEY,
    OPENFDA_BACKOFF_BASE, OPENFDA_MAX_RETRIES, OPENFDA_MAX_SKIP,
    DEFAULT_RECALL_LOOKBACK_YEARS, DEFAULT_MAUDE_LOOKBACK_DAYS,
    DEVICE_CLASS_LABELS, RECALL_SEVERITY_MAP,
)

logger = logging.getLogger(__name__)

_delay = OPENFDA_DELAY_WITH_KEY if OPENFDA_API_KEY else OPENFDA_DELAY_WITHOUT_KEY
_last_request_time: float = 0.0


def _query(endpoint: str, params: dict, retries: int = 0) -> dict:
    """
    Make a rate-limited, retry-capable request to an OpenFDA endpoint.
    Handles 429 (rate limit), 500 (server error), and 404 (no results) gracefully.
    """
    global _last_request_time

    elapsed = time.time() - _last_request_time
    if elapsed < _delay:
        time.sleep(_delay - elapsed)

    if OPENFDA_API_KEY:
        params["api_key"] = OPENFDA_API_KEY

    try:
        resp = requests.get(endpoint, params=params, timeout=20)
        _last_request_time = time.time()

        if resp.status_code == 429:
            if retries >= OPENFDA_MAX_RETRIES:
                raise RuntimeError(f"OpenFDA rate limit exceeded after {OPENFDA_MAX_RETRIES} retries.")
            wait = OPENFDA_BACKOFF_BASE ** (retries + 1)
            logger.warning(f"OpenFDA 429 — backing off {wait:.1f}s (retry {retries + 1})")
            time.sleep(wait)
            return _query(endpoint, params, retries + 1)

        if resp.status_code == 404:
            return {"meta": {}, "results": []}

        if resp.status_code >= 500:
            if retries >= OPENFDA_MAX_RETRIES:
                raise RuntimeError(f"OpenFDA server error {resp.status_code}")
            wait = OPENFDA_BACKOFF_BASE ** (retries + 1)
            logger.warning(f"OpenFDA {resp.status_code} — retrying in {wait:.1f}s")
            time.sleep(wait)
            return _query(endpoint, params, retries + 1)

        resp.raise_for_status()
        return resp.json()

    except requests.exceptions.Timeout:
        if retries < OPENFDA_MAX_RETRIES:
            time.sleep(OPENFDA_BACKOFF_BASE ** (retries + 1))
            return _query(endpoint, params, retries + 1)
        raise


def _paginate(endpoint: str, search: str, limit: int = 100, max_records: int = 500) -> list:
    """
    Paginate through OpenFDA results, respecting the 25,000 skip cap.
    For datasets larger than 25,000, use date-range segmentation externally.
    """
    results = []
    skip = 0
    effective_max = min(max_records, OPENFDA_MAX_SKIP)

    while True:
        if skip + limit > effective_max:
            limit = effective_max - skip
            if limit <= 0:
                break

        data = _query(endpoint, {"search": search, "limit": limit, "skip": skip})
        batch = data.get("results", [])
        results.extend(batch)

        total = data.get("meta", {}).get("results", {}).get("total", 0)
        if len(batch) < limit or skip + limit >= min(total, effective_max):
            break

        skip += limit

    return results


def _date_range_search(years_back: int) -> str:
    """Generate OpenFDA date range search string for recall/MAUDE queries."""
    end_date = datetime.now()
    start_date = end_date - timedelta(days=years_back * 365)
    return f"[{start_date.strftime('%Y%m%d')}+TO+{end_date.strftime('%Y%m%d')}]"


def _days_back_search(field: str, days: int) -> str:
    """Generate OpenFDA date range for a specific field, N days back."""
    end_date = datetime.now()
    start_date = end_date - timedelta(days=days)
    return (
        f"{field}:[{start_date.strftime('%Y%m%d')}+TO+{end_date.strftime('%Y%m%d')}]"
    )


# ── 510(k) Functions ──────────────────────────────────────────────────────────

def get_510k_by_applicant(company: str, limit: int = 50) -> list:
    """
    Get 510(k) clearances submitted by a specific company.
    Sorted by decision_date descending.
    """
    results = _paginate(
        OPENFDA_510K,
        search=f'applicant:"{company}"',
        limit=limit,
        max_records=500,
    )
    return sorted(results, key=lambda x: x.get("decision_date", ""), reverse=True)


def get_510k_by_product_code(product_code: str, limit: int = 100) -> list:
    """
    Get all 510(k) clearances for a given FDA product code.
    Useful for landscape analysis of a device category.
    """
    results = _paginate(
        OPENFDA_510K,
        search=f"product_code:{product_code}",
        limit=limit,
        max_records=2000,
    )
    return sorted(results, key=lambda x: x.get("decision_date", ""), reverse=True)


def get_new_510k_clearances_by_product_codes(
    product_codes: list[str], days_back: int = 7
) -> list:
    """
    Get recent 510(k) clearances for a list of product codes.
    Used in the weekly digest.
    """
    results = []
    for code in product_codes:
        search = (
            f"product_code:{code} AND "
            f"{_days_back_search('decision_date', days_back)}"
        )
        batch = _paginate(OPENFDA_510K, search=search, limit=50, max_records=100)
        for r in batch:
            r["_query_product_code"] = code
        results.extend(batch)
    return sorted(results, key=lambda x: x.get("decision_date", ""), reverse=True)


def get_510k_for_di(di: str, accessgudid_data: dict) -> dict:
    """
    Get the 510(k) record corresponding to a specific device DI.
    Chains ACCESSGUDID product code and premarket submission number to 510(k) lookup.

    Returns the most relevant 510(k) record (premarket submission number match if available,
    else most recent for the product code).
    """
    # Try direct submission number match first
    submission_number = accessgudid_data.get("premarket_submission_number", "")
    if submission_number and submission_number.startswith("K"):
        data = _query(
            OPENFDA_510K,
            {"search": f'k_number:"{submission_number}"', "limit": 1}
        )
        results = data.get("results", [])
        if results:
            return results[0]

    # Fall back to product code lookup (most recent clearance)
    product_code = accessgudid_data.get("primary_product_code", "")
    company = accessgudid_data.get("company_name", "")
    if product_code and company:
        data = _query(
            OPENFDA_510K,
            {
                "search": f'product_code:{product_code} AND applicant:"{company}"',
                "limit": 1,
                "sort": "decision_date:desc",
            }
        )
        results = data.get("results", [])
        if results:
            return results[0]

    if product_code:
        data = _query(
            OPENFDA_510K,
            {"search": f"product_code:{product_code}", "limit": 1, "sort": "decision_date:desc"}
        )
        results = data.get("results", [])
        if results:
            return results[0]

    return {}


# ── Recall Functions ──────────────────────────────────────────────────────────

def get_recalls_by_firm(firm_name: str, years_back: int = DEFAULT_RECALL_LOOKBACK_YEARS) -> list:
    """
    Get all device recalls for a given firm name.
    """
    results = _paginate(
        OPENFDA_RECALLS,
        search=f'recalling_firm:"{firm_name}"',
        max_records=1000,
    )
    return sorted(results, key=lambda x: x.get("recall_initiation_date", ""), reverse=True)


def get_recalls_by_product_code(product_code: str, years_back: int = DEFAULT_RECALL_LOOKBACK_YEARS) -> list:
    """
    Get all device recalls for a given FDA product code.
    """
    results = _paginate(
        OPENFDA_RECALLS,
        search=f"product_code:{product_code}",
        max_records=500,
    )
    return sorted(results, key=lambda x: x.get("recall_initiation_date", ""), reverse=True)


def get_recalls_for_watch_list(watch_list: list, days_back: int = 7) -> list:
    """
    Get recall activity for all product codes in the watch list.
    Used in the weekly digest.
    """
    results = []
    for watch in watch_list:
        for code in watch.get("product_codes", []):
            search = (
                f"product_code:{code} AND "
                f"{_days_back_search('recall_initiation_date', days_back)}"
            )
            batch = _paginate(OPENFDA_RECALLS, search=search, limit=50, max_records=100)
            for r in batch:
                r["_watch_category"] = watch.get("category", "")
            results.extend(batch)
    return sorted(results, key=lambda x: x.get("recall_initiation_date", ""), reverse=True)


def check_di_for_active_recalls(di: str, product_code: str = "", brand_name: str = "") -> list:
    """
    Check if a specific DI or its product code has active (ongoing) recalls.
    Used in formulary alert monitoring.
    Returns list of active recall records.
    """
    active_recalls = []

    # Check by product code
    if product_code:
        results = _paginate(
            OPENFDA_RECALLS,
            search=f'product_code:{product_code} AND status:"Ongoing"',
            max_records=100,
        )
        active_recalls.extend(results)

    # Check by brand name (broader net)
    if brand_name and not active_recalls:
        results = _paginate(
            OPENFDA_RECALLS,
            search=f'product_description:"{brand_name}" AND status:"Ongoing"',
            max_records=50,
        )
        active_recalls.extend(results)

    # Deduplicate by recall number
    seen = set()
    unique = []
    for r in active_recalls:
        key = r.get("recall_number", r.get("product_description", ""))
        if key not in seen:
            seen.add(key)
            unique.append(r)

    return unique


# ── MAUDE Functions ───────────────────────────────────────────────────────────

def get_maude_events(brand_name: str, years_back: int = 3, limit: int = 100) -> list:
    """
    Get MAUDE adverse event reports for a device by brand name.
    Sorted by date_received descending.
    """
    results = _paginate(
        OPENFDA_MAUDE,
        search=f'device.brand_name:"{brand_name}"',
        limit=limit,
        max_records=500,
    )
    return sorted(results, key=lambda x: x.get("date_received", ""), reverse=True)


def get_maude_count_by_product_code(product_code: str) -> dict:
    """
    Get aggregate MAUDE event counts by brand name for a product code.
    Returns dict mapping brand_name -> count.
    Used for competitive adverse event comparison.
    """
    data = _query(
        OPENFDA_MAUDE,
        {"search": f"device.product_code:{product_code}", "count": "device.brand_name.exact"}
    )
    results = data.get("results", [])
    return {r["term"]: r["count"] for r in results}


def get_maude_event_volume(
    brand_name: str, product_code: str = "", days_lookback: int = DEFAULT_MAUDE_LOOKBACK_DAYS
) -> int:
    """
    Get the count of MAUDE events for a device in the last N days.
    Used for spike detection in the alert monitor.
    """
    date_filter = _days_back_search("date_received", days_lookback)
    search_parts = [date_filter]

    if product_code:
        search_parts.append(f"device.product_code:{product_code}")
    else:
        search_parts.append(f'device.brand_name:"{brand_name}"')

    data = _query(
        OPENFDA_MAUDE,
        {"search": " AND ".join(search_parts), "limit": 1}
    )
    return data.get("meta", {}).get("results", {}).get("total", 0)


def get_maude_baseline_volume(brand_name: str, product_code: str = "") -> float:
    """
    Estimate baseline MAUDE event rate using the prior 90–365 day period.
    Returns average events per 30 days.
    """
    end = datetime.now() - timedelta(days=90)
    start = end - timedelta(days=275)  # ~9 months prior to the 90-day lookback
    date_range = f"date_received:[{start.strftime('%Y%m%d')}+TO+{end.strftime('%Y%m%d')}]"

    search_parts = [date_range]
    if product_code:
        search_parts.append(f"device.product_code:{product_code}")
    else:
        search_parts.append(f'device.brand_name:"{brand_name}"')

    data = _query(
        OPENFDA_MAUDE,
        {"search": " AND ".join(search_parts), "limit": 1}
    )
    total_in_period = data.get("meta", {}).get("results", {}).get("total", 0)
    # 9-month baseline → per-30-day rate
    return (total_in_period / 9.0) if total_in_period else 0.0


def get_device_full_fda_profile(product_code: str, brand_name: str) -> dict:
    """
    Convenience wrapper: fetch 510(k), recall, and MAUDE data for a device.
    Returns structured dict with all three datasets.
    """
    return {
        "510k": get_510k_by_product_code(product_code, limit=10),
        "recalls": get_recalls_by_product_code(product_code),
        "maude_recent": get_maude_events(brand_name, years_back=3, limit=50),
        "maude_brand_counts": get_maude_count_by_product_code(product_code),
    }


# ── Classification Functions ─────────────────────────────────────────────────

def get_device_classification(product_code: str) -> dict:
    """
    Get FDA device classification details for a product code.
    Returns device class, regulation number, review panel, implant flag.
    """
    data = _query(
        OPENFDA_CLASSIFICATION,
        {"search": f"product_code:{product_code}", "limit": 1}
    )
    results = data.get("results", [])
    if not results:
        return {}

    r = results[0]
    return {
        "product_code": r.get("product_code", ""),
        "device_name": r.get("device_name", ""),
        "device_class": r.get("device_class", ""),
        "device_class_label": DEVICE_CLASS_LABELS.get(r.get("device_class", ""), "Unknown"),
        "regulation_number": r.get("regulation_number", ""),
        "review_panel": r.get("review_panel", ""),
        "medical_specialty": r.get("medical_specialty_description", ""),
        "submission_type": r.get("submission_type_id", ""),
        "third_party_flag": r.get("third_party_flag", ""),
        "life_sustain_support_flag": r.get("life_sustain_support_flag", ""),
        "implant_flag": r.get("implant_flag", ""),
        "gmp_exempt_flag": r.get("gmp_exempt_flag", ""),
        "definition": r.get("definition", ""),
    }
```

---

### `medops/pubmed.py`

```python
"""
PubMed E-utilities Client
Retrieves and parses clinical literature for device evaluation briefs.

Endpoints:
  esearch.fcgi — search by query, returns PMIDs
  efetch.fcgi  — fetch full record XML by PMID
  esummary.fcgi — fetch record summaries by PMID
"""

import time
import logging
import requests
import xml.etree.ElementTree as ET
from datetime import datetime, timedelta
from medops.config import (
    PUBMED_SEARCH, PUBMED_FETCH, PUBMED_SUMMARY,
    PUBMED_API_KEY, PUBMED_DELAY_WITH_KEY, PUBMED_DELAY_WITHOUT_KEY,
    DEFAULT_PUBMED_MAX_RESULTS,
)

logger = logging.getLogger(__name__)

_delay = PUBMED_DELAY_WITH_KEY if PUBMED_API_KEY else PUBMED_DELAY_WITHOUT_KEY
_last_request_time: float = 0.0


def _get(url: str, params: dict) -> requests.Response:
    global _last_request_time
    elapsed = time.time() - _last_request_time
    if elapsed < _delay:
        time.sleep(_delay - elapsed)
    if PUBMED_API_KEY:
        params["api_key"] = PUBMED_API_KEY
    resp = requests.get(url, params=params, timeout=20)
    _last_request_time = time.time()
    resp.raise_for_status()
    return resp


def _build_search_query(device_name: str, category: str = "", product_code: str = "") -> str:
    """
    Build a PubMed search query optimized for device evaluation literature.
    Filters for clinical relevance: clinical trial, RCT, systematic review, meta-analysis.
    """
    base_terms = []

    # Device name — quoted for precision
    if device_name:
        base_terms.append(f'"{device_name}"[Title/Abstract]')

    # Category-level MeSH terms
    category_mesh = {
        "hemostatics": "Hemostatics[MeSH]",
        "sutures": "Sutures[MeSH]",
        "spine_implants": "Spinal Fusion[MeSH] OR Intervertebral Disc[MeSH]",
        "total_joints": "Arthroplasty, Replacement[MeSH]",
        "staplers": "Surgical Stapling[MeSH]",
        "wound_care": "Wound Healing[MeSH] OR Skin Transplantation[MeSH]",
        "breast_implants": "Breast Implants[MeSH]",
        "ophthalmology": "Phacoemulsification[MeSH] OR Lens Implantation, Intraocular[MeSH]",
        "robotics": "Robotic Surgical Procedures[MeSH]",
    }

    if category and category in category_mesh:
        base_terms.append(f"({category_mesh[category]})")

    # Publication type filter — clinical relevance
    pub_type_filter = (
        "(Clinical Trial[pt] OR Randomized Controlled Trial[pt] OR "
        "Systematic Review[pt] OR Meta-Analysis[pt] OR "
        "Comparative Study[pt] OR Multicenter Study[pt])"
    )

    # English language and human subjects
    lang_filter = "English[Language]"
    species_filter = "Humans[MeSH]"

    # Date filter — last 10 years
    cutoff_year = datetime.now().year - 10
    date_filter = f"{cutoff_year}/01/01:3000/12/31[dp]"

    query_parts = [" OR ".join(base_terms)] if base_terms else [device_name]
    query_parts.extend([pub_type_filter, lang_filter, species_filter, date_filter])

    return " AND ".join(f"({p})" for p in query_parts)


def _search_pmids(query: str, max_results: int = DEFAULT_PUBMED_MAX_RESULTS) -> list[str]:
    """Run a PubMed search and return list of PMIDs."""
    resp = _get(PUBMED_SEARCH, {
        "db": "pubmed",
        "term": query,
        "retmax": max_results,
        "retmode": "json",
        "sort": "relevance",
    })
    data = resp.json()
    return data.get("esearchresult", {}).get("idlist", [])


def _fetch_abstracts(pmids: list[str]) -> list[dict]:
    """
    Fetch full abstract data for a list of PMIDs.
    Returns list of dicts: pmid, title, abstract, authors, pub_date, journal, doi.
    """
    if not pmids:
        return []

    resp = _get(PUBMED_FETCH, {
        "db": "pubmed",
        "id": ",".join(pmids),
        "rettype": "abstract",
        "retmode": "xml",
    })

    articles = []
    try:
        root = ET.fromstring(resp.text)
        for article in root.findall(".//PubmedArticle"):
            medline = article.find("MedlineCitation")
            if medline is None:
                continue

            art = medline.find("Article")
            if art is None:
                continue

            # PMID
            pmid_el = medline.find("PMID")
            pmid = pmid_el.text if pmid_el is not None else ""

            # Title
            title_el = art.find("ArticleTitle")
            title = "".join(title_el.itertext()) if title_el is not None else ""

            # Abstract
            abstract_el = art.find("Abstract")
            if abstract_el is not None:
                abstract = " ".join(
                    "".join(t.itertext())
                    for t in abstract_el.findall("AbstractText")
                )
            else:
                abstract = ""

            # Authors
            author_list = art.find("AuthorList")
            authors = []
            if author_list is not None:
                for author in author_list.findall("Author"):
                    last = author.findtext("LastName", "")
                    fore = author.findtext("ForeName", "")
                    if last:
                        authors.append(f"{last} {fore}".strip())

            # Journal
            journal_el = art.find("Journal")
            journal = ""
            pub_date = ""
            if journal_el is not None:
                journal = journal_el.findtext("Title", "") or journal_el.findtext(
                    "ISOAbbreviation", ""
                )
                pub_date_el = journal_el.find(".//PubDate")
                if pub_date_el is not None:
                    year = pub_date_el.findtext("Year", "")
                    month = pub_date_el.findtext("Month", "")
                    pub_date = f"{year} {month}".strip()

            # DOI
            doi = ""
            for id_el in article.findall(".//ArticleId"):
                if id_el.get("IdType") == "doi":
                    doi = id_el.text or ""
                    break

            articles.append({
                "pmid": pmid,
                "title": title.strip(),
                "abstract": abstract.strip(),
                "authors": authors[:6],   # cap at 6 authors
                "first_author": authors[0] if authors else "",
                "pub_date": pub_date,
                "journal": journal,
                "doi": doi,
                "pubmed_url": f"https://pubmed.ncbi.nlm.nih.gov/{pmid}/",
            })

    except ET.ParseError as e:
        logger.error(f"PubMed XML parse error: {e}")

    return articles


def _is_clinically_relevant(article: dict) -> bool:
    """
    Filter for clinical relevance.
    Excludes: in vitro only, animal studies, editorials, letters without data,
    articles with no abstract, obvious manufacturer-only studies.
    """
    abstract = article.get("abstract", "").lower()
    title = article.get("title", "").lower()

    # Reject if no abstract
    if not abstract:
        return False

    # Reject obvious non-clinical
    exclusion_signals = [
        "in vitro", "in-vitro", "animal model", "rat model", "mouse model",
        "cadaveric study", "finite element", "computational model",
        "editorial", "letter to the editor",
    ]
    for signal in exclusion_signals:
        if signal in abstract or signal in title:
            return False

    # Require clinical content signals
    inclusion_signals = [
        "patient", "clinical", "trial", "outcomes", "complication",
        "surgery", "operative", "hospital", "cohort", "randomized",
        "prospective", "retrospective",
    ]
    return any(s in abstract or s in title for s in inclusion_signals)


def search_device_literature(
    device_name: str,
    category: str = "",
    product_code: str = "",
    max_results: int = DEFAULT_PUBMED_MAX_RESULTS,
) -> list[dict]:
    """
    Search PubMed for clinical literature relevant to a specific device.
    Returns filtered list of dicts with: pmid, title, abstract, authors,
    pub_date, journal, doi, pubmed_url.
    """
    query = _build_search_query(device_name, category, product_code)
    logger.info(f"PubMed search: {device_name} | query length: {len(query)}")

    pmids = _search_pmids(query, max_results=max_results * 2)  # fetch extra for filtering
    articles = _fetch_abstracts(pmids)
    filtered = [a for a in articles if _is_clinically_relevant(a)]

    return filtered[:max_results]


def search_device_literature_batch(
    watch_list: list, days_back: int = 7
) -> list[dict]:
    """
    Search PubMed for recent literature across all watched categories.
    Used in the weekly digest.
    Returns list of articles with added _watch_category field.
    """
    results = []
    for watch in watch_list:
        category = watch.get("category", "")
        # Use category name as the primary search term
        articles = search_device_literature(
            device_name=category.replace("_", " "),
            category=category,
            max_results=5,
        )
        for a in articles:
            a["_watch_category"] = category
        results.extend(articles)
    return results
```

---

### `medops/synthesizer.py`

```python
"""
Claude API Synthesis Functions
Generates all LLM-synthesized outputs: device briefs, competitive matrices,
substitution recommendations, emerging tech briefs, weekly digests, anomaly flags.

All synthesis uses Claude Sonnet via direct Anthropic SDK calls.
System prompts are tuned for a perioperative supply chain professional audience:
precise, evidence-based, clinically grounded. Not conversational.
"""

import json
import logging
from typing import Optional
import anthropic
from medops.config import ANTHROPIC_API_KEY, CLAUDE_MODEL, CLAUDE_MAX_TOKENS, CLAUDE_TEMPERATURE

logger = logging.getLogger(__name__)

_client: Optional[anthropic.Anthropic] = None


def _get_client() -> anthropic.Anthropic:
    global _client
    if _client is None:
        _client = anthropic.Anthropic(api_key=ANTHROPIC_API_KEY)
    return _client


def _call_claude(system_prompt: str, user_content: str, max_tokens: int = CLAUDE_MAX_TOKENS) -> str:
    """Base Claude API call with error handling."""
    client = _get_client()
    try:
        response = client.messages.create(
            model=CLAUDE_MODEL,
            max_tokens=max_tokens,
            temperature=CLAUDE_TEMPERATURE,
            system=system_prompt,
            messages=[{"role": "user", "content": user_content}],
        )
        return response.content[0].text
    except anthropic.APIError as e:
        logger.error(f"Claude API error: {e}")
        raise


# ─────────────────────────────────────────────────────────────────────────────
# DEVICE BRIEF
# ─────────────────────────────────────────────────────────────────────────────

DEVICE_BRIEF_SYSTEM_PROMPT = """You are a perioperative supply chain analyst at a major academic medical center. Your audience is the Value Analysis Committee (VAC) and supply chain leadership. You produce structured, evidence-based device evaluation briefs.

STANDARDS:
- Factual precision: cite specific 510(k) numbers, MAUDE event counts, recall classes as provided in the data. Never invent or extrapolate specific regulatory numbers.
- Evidence hierarchy: RCT and registry data > retrospective cohort > case series > manufacturer claims. Flag manufacturer-sponsored studies explicitly.
- Risk framing: MAUDE adverse event counts must be contextualized by market volume when data permits. Raw counts without denominator are noted as incomplete.
- Clinical tone: professional, precise, no marketing language. State limitations where data is incomplete or absent.
- Recommendations must be qualified: "approve for formulary addition," "approve conditionally pending X," "defer pending Y," or "reject — reason."

OUTPUT FORMAT: Return structured Markdown with the following sections exactly:
## Device Identification
## Regulatory Status
## Safety Record
## Clinical Evidence Summary
## Formulary Recommendation
## Substitution Candidates
## Data Completeness Notes
## References"""

def generate_device_brief(
    accessgudid_data: dict,
    fda_data: dict,
    maude_data: list,
    recall_data: list,
    pubmed_abstracts: list,
    substitute_candidates: list = None,
) -> str:
    """
    Generate a full device evaluation brief from multi-source data.
    Returns Markdown string.
    """
    # Build structured data payload for Claude
    payload = {
        "device_record": {
            "brand_name": accessgudid_data.get("brand_name", ""),
            "company_name": accessgudid_data.get("company_name", ""),
            "primary_di": accessgudid_data.get("primary_di", ""),
            "catalog_number": accessgudid_data.get("catalog_number", ""),
            "version_model": accessgudid_data.get("version_model_number", ""),
            "product_code": accessgudid_data.get("primary_product_code", ""),
            "device_class": accessgudid_data.get("device_class", ""),
            "gmdn_term": accessgudid_data.get("primary_gmdn_name", ""),
            "gmdn_code": accessgudid_data.get("primary_gmdn_code", ""),
            "mri_safety": accessgudid_data.get("mri_safety_status", ""),
            "single_use": accessgudid_data.get("single_use", ""),
            "sterile": accessgudid_data.get("device_sterile", ""),
            "sterilization_methods": accessgudid_data.get("sterilization_methods", []),
            "implant_flag": accessgudid_data.get("implant_flag", ""),
            "commercial_distribution_status": accessgudid_data.get("commercial_distribution_status", ""),
            "premarket_submission_number": accessgudid_data.get("premarket_submission_number", ""),
            "device_description": accessgudid_data.get("device_description", ""),
        },
        "clearances_510k": fda_data.get("510k", [])[:3],     # Top 3 most recent
        "active_recalls": [
            r for r in recall_data if r.get("status", "") == "Ongoing"
        ],
        "historical_recalls": [
            r for r in recall_data if r.get("status", "") != "Ongoing"
        ][:5],
        "maude_recent_30_days": len([
            e for e in maude_data
            if e.get("date_received", "") >= ""   # date filter applied upstream
        ]),
        "maude_brand_context": fda_data.get("maude_brand_counts", {}),
        "maude_recent_events": maude_data[:5],   # Last 5 event summaries
        "literature": [
            {
                "pmid": a.get("pmid", ""),
                "title": a.get("title", ""),
                "abstract": a.get("abstract", "")[:600],   # truncate for token budget
                "pub_date": a.get("pub_date", ""),
                "journal": a.get("journal", ""),
                "doi": a.get("doi", ""),
            }
            for a in (pubmed_abstracts or [])[:8]
        ],
        "substitution_candidates": (substitute_candidates or [])[:5],
    }

    user_content = f"""Generate a complete device evaluation brief for the following device data.

DATA:
{json.dumps(payload, indent=2)}

Produce the full structured brief per the format in your instructions. Be specific with all numbers from the data. Note any missing fields explicitly in the Data Completeness Notes section."""

    return _call_claude(DEVICE_BRIEF_SYSTEM_PROMPT, user_content, max_tokens=3000)


# ─────────────────────────────────────────────────────────────────────────────
# COMPETITIVE MATRIX
# ─────────────────────────────────────────────────────────────────────────────

COMPETITIVE_MATRIX_SYSTEM_PROMPT = """You are a perioperative supply chain analyst. You produce structured competitive device matrices for Value Analysis Committee review.

For each device in the comparison:
- Extract and present ALL provided regulatory, safety, and clinical data
- Do not fill gaps with assumptions; mark missing data as "Not provided"
- Flag any device with an active recall or >3 MAUDE events in 30 days with a ⚠️ marker
- Conclude with a ranked recommendation (1 = preferred) and the specific rationale for ranking

OUTPUT FORMAT: Return structured Markdown. Lead with a comparison table, then narrative summary per device, then ranked recommendation."""

def generate_competitive_matrix(devices_list: list) -> str:
    """
    Generate a competitive comparison matrix for a list of devices.
    devices_list: list of dicts, each containing accessgudid_data + fda_data for one device.
    Returns Markdown string.
    """
    payload = []
    for d in devices_list:
        gudid = d.get("accessgudid_data", {})
        fda = d.get("fda_data", {})
        payload.append({
            "brand_name": gudid.get("brand_name", ""),
            "company": gudid.get("company_name", ""),
            "di": gudid.get("primary_di", ""),
            "catalog_number": gudid.get("catalog_number", ""),
            "gmdn_term": gudid.get("primary_gmdn_name", ""),
            "device_class": gudid.get("device_class", ""),
            "mri_safety": gudid.get("mri_safety_status", ""),
            "single_use": gudid.get("single_use", ""),
            "sterile": gudid.get("device_sterile", ""),
            "510k": fda.get("510k", [{}])[0].get("k_number", "") if fda.get("510k") else "",
            "clearance_date": fda.get("510k", [{}])[0].get("decision_date", "") if fda.get("510k") else "",
            "active_recalls": len([r for r in fda.get("recalls", []) if r.get("status") == "Ongoing"]),
            "maude_recent_events": d.get("maude_recent_count", 0),
            "maude_brand_total": fda.get("maude_brand_counts", {}).get(
                gudid.get("brand_name", ""), "N/A"
            ),
            "literature_summary": d.get("literature_summary", ""),
        })

    user_content = f"""Generate a competitive comparison matrix for these {len(payload)} devices.

DEVICE DATA:
{json.dumps(payload, indent=2)}

Required sections:
1. Comparison table (all devices × all dimensions)
2. Individual device narrative (3–5 sentences per device)
3. Ranked recommendation with rationale
4. VAC decision summary (1 paragraph)"""

    return _call_claude(COMPETITIVE_MATRIX_SYSTEM_PROMPT, user_content, max_tokens=3500)


# ─────────────────────────────────────────────────────────────────────────────
# SUBSTITUTION RECOMMENDATION
# ─────────────────────────────────────────────────────────────────────────────

SUBSTITUTION_RECOMMENDATION_SYSTEM_PROMPT = """You are a perioperative supply chain analyst conducting a formulary substitution assessment. Your audience is the VAC and supply chain leadership.

A substitution assessment must cover:
1. Regulatory equivalence (same product code, same GMDN, same device class)
2. Technical specification comparison (material, sterility, MRI safety, sizes covered)
3. Safety record differential (recalls, MAUDE comparison — note absolute counts AND relative context)
4. Clinical evidence on equivalence (is there head-to-head data, or only parallel literature?)
5. Implementation risk (sterile processing impact, staff training, transition timeline)
6. Cost impact (if pricing data provided; otherwise note "pricing data not available in this system")
7. Final recommendation: APPROVE SUBSTITUTION / CONDITIONAL APPROVAL / DO NOT SUBSTITUTE

Conditional approval must specify the condition (e.g., "pending surgeon consultation," "pending size coverage verification for procedure X").
Do not recommend substitution for PMA devices using 510(k) equivalents."""

def generate_substitution_recommendation(
    device_a_data: dict,
    device_b_data: dict,
    comparison_data: dict = None,
) -> str:
    """
    Generate a substitution recommendation comparing Device A (current) to Device B (proposed).
    Returns Markdown string.
    """
    payload = {
        "current_device_a": {
            "brand_name": device_a_data.get("accessgudid_data", {}).get("brand_name", ""),
            "company": device_a_data.get("accessgudid_data", {}).get("company_name", ""),
            "di": device_a_data.get("accessgudid_data", {}).get("primary_di", ""),
            "product_code": device_a_data.get("accessgudid_data", {}).get("primary_product_code", ""),
            "gmdn": device_a_data.get("accessgudid_data", {}).get("primary_gmdn_name", ""),
            "device_class": device_a_data.get("accessgudid_data", {}).get("device_class", ""),
            "active_recalls": len([
                r for r in device_a_data.get("fda_data", {}).get("recalls", [])
                if r.get("status") == "Ongoing"
            ]),
            "maude_brand_count": device_a_data.get("fda_data", {}).get(
                "maude_brand_counts", {}
            ).get(device_a_data.get("accessgudid_data", {}).get("brand_name", ""), "N/A"),
        },
        "proposed_device_b": {
            "brand_name": device_b_data.get("accessgudid_data", {}).get("brand_name", ""),
            "company": device_b_data.get("accessgudid_data", {}).get("company_name", ""),
            "di": device_b_data.get("accessgudid_data", {}).get("primary_di", ""),
            "product_code": device_b_data.get("accessgudid_data", {}).get("primary_product_code", ""),
            "gmdn": device_b_data.get("accessgudid_data", {}).get("primary_gmdn_name", ""),
            "device_class": device_b_data.get("accessgudid_data", {}).get("device_class", ""),
            "active_recalls": len([
                r for r in device_b_data.get("fda_data", {}).get("recalls", [])
                if r.get("status") == "Ongoing"
            ]),
            "maude_brand_count": device_b_data.get("fda_data", {}).get(
                "maude_brand_counts", {}
            ).get(device_b_data.get("accessgudid_data", {}).get("brand_name", ""), "N/A"),
        },
        "gmdn_match": (
            device_a_data.get("accessgudid_data", {}).get("primary_gmdn_code") ==
            device_b_data.get("accessgudid_data", {}).get("primary_gmdn_code")
        ),
        "product_code_match": (
            device_a_data.get("accessgudid_data", {}).get("primary_product_code") ==
            device_b_data.get("accessgudid_data", {}).get("primary_product_code")
        ),
        "additional_comparison_data": comparison_data or {},
    }

    user_content = f"""Conduct a formulary substitution assessment.

DATA:
{json.dumps(payload, indent=2)}

Produce the full substitution recommendation per your instructions."""

    return _call_claude(SUBSTITUTION_RECOMMENDATION_SYSTEM_PROMPT, user_content, max_tokens=2500)


# ─────────────────────────────────────────────────────────────────────────────
# EMERGING TECHNOLOGY BRIEF
# ─────────────────────────────────────────────────────────────────────────────

EMERGING_TECH_SYSTEM_PROMPT = """You are a perioperative supply chain analyst. You produce emerging technology intelligence briefs for supply chain leadership and VAC committees.

An emerging technology brief covers:
1. Technology description and mechanism of action
2. Current regulatory status (cleared, investigational, pipeline)
3. Clinical evidence status (published RCTs, registry data, or only bench/animal data)
4. Key vendors and competitive landscape
5. Supply chain readiness assessment (is this ready for formulary evaluation?)
6. Recommended next action (monitor, schedule evaluation, defer)

Be specific about what is known vs. what is speculative. Flag vendor-sponsored data."""

def generate_emerging_tech_brief(tech_description: str, search_results: list) -> str:
    """
    Generate an emerging technology brief.
    tech_description: free text description of the technology/category.
    search_results: list of dicts from FDA + PubMed searches.
    Returns Markdown string.
    """
    payload = {
        "technology_description": tech_description,
        "search_results": search_results[:10],
    }

    user_content = f"""Generate an emerging technology intelligence brief.

TECHNOLOGY / QUERY:
{tech_description}

SEARCH RESULTS:
{json.dumps(search_results[:10], indent=2)}

Produce the full brief per your instructions."""

    return _call_claude(EMERGING_TECH_SYSTEM_PROMPT, user_content, max_tokens=2000)


# ─────────────────────────────────────────────────────────────────────────────
# WEEKLY DIGEST
# ─────────────────────────────────────────────────────────────────────────────

WEEKLY_DIGEST_SYSTEM_PROMPT = """You are a perioperative supply chain analyst. You produce a weekly intelligence digest for a supply chain director at an academic medical center. 

This digest surfaces actionable information from the past 7 days across all monitored device categories. Style: similar to a well-edited briefing document — structured, scannable, action-oriented. Not a data dump.

Structure:
## Week of [DATE] — MedOps Intelligence Digest

### ⚡ Action Required
Items requiring immediate attention (Class I/II recalls, critical MAUDE spikes)

### 📋 510(k) Clearances — Watched Categories  
New clearances in monitored categories (last 7 days)

### 🔔 Recall Activity
New and ongoing recalls in monitored categories

### 📊 MAUDE Monitoring
Adverse event volume changes above threshold for formulary devices

### 📚 Literature Updates
Notable new clinical literature for active evaluation targets

### 🔭 Category Intelligence
Brief narrative commentary on each watched category with notable developments

---

Keep each section concise. Bullet points over paragraphs. Flag any item needing a full device brief with: [BRIEF NEEDED]"""

def generate_weekly_digest(
    new_clearances: list,
    recall_events: list,
    maude_alerts: list,
    literature_updates: list,
    watch_list: list,
    period_label: str,
) -> tuple[str, str]:
    """
    Generate the weekly intelligence digest.
    Returns tuple of (full_markdown, summary_string).
    """
    payload = {
        "period": period_label,
        "new_510k_clearances": new_clearances[:20],
        "recall_events": recall_events[:15],
        "maude_alerts": [
            {
                "device": a.get("device_di", ""),
                "brand": a.get("brand_name", ""),
                "alert_type": a.get("alert_type", ""),
                "description": a.get("description", ""),
                "severity": a.get("severity", ""),
            }
            for a in maude_alerts[:10]
        ],
        "literature_updates": [
            {
                "category": a.get("_watch_category", ""),
                "title": a.get("title", ""),
                "journal": a.get("journal", ""),
                "pmid": a.get("pmid", ""),
                "pub_date": a.get("pub_date", ""),
            }
            for a in literature_updates[:15]
        ],
        "watch_categories": [w.get("category", "") for w in watch_list],
    }

    user_content = f"""Generate the weekly MedOps Intelligence Digest.

PERIOD: {period_label}
DATA:
{json.dumps(payload, indent=2)}

Generate the full digest in the format specified in your instructions."""

    digest = _call_claude(WEEKLY_DIGEST_SYSTEM_PROMPT, user_content, max_tokens=3000)

    # Generate a short summary for Hermes output
    action_required = len([r for r in recall_events if r.get("classification") in ("Class I", "Class II")])
    summary = (
        f"{period_label} — "
        f"{len(new_clearances)} new 510(k) clearances, "
        f"{len(recall_events)} recall events, "
        f"{len(maude_alerts)} MAUDE alerts, "
        f"{action_required} items requiring action."
    )

    return digest, summary


# ─────────────────────────────────────────────────────────────────────────────
# ANOMALY FLAGS
# ─────────────────────────────────────────────────────────────────────────────

ANOMALY_SYSTEM_PROMPT = """You are a perioperative supply chain safety analyst. Review the provided device data and identify any red flags that require immediate human attention.

Flag categories (return only flags that are genuinely present):
- ACTIVE_CLASS_I_RECALL: Device has an active Class I recall
- ACTIVE_CLASS_II_RECALL: Device has an active Class II recall
- HIGH_MAUDE_VOLUME: Adverse event volume notably elevated vs. market context
- MRI_UNSAFE: Device labeled MR Unsafe (relevant for OR with intraoperative MRI)
- DISTRIBUTION_ENDED: Commercial distribution has ended (supply continuity risk)
- NO_510K_OR_PMA: No premarket clearance number found (regulatory gap)
- COMBINATION_PRODUCT: Device is a combination product (complex procurement/regulatory pathway)
- HCTP_PRODUCT: Device regulated as HCT/P — different procurement workflow required
- DATA_GAP_CRITICAL: Critical data fields are missing that prevent safety assessment

Return a JSON array of flag strings only. If no flags, return empty array [].
Example: ["ACTIVE_CLASS_II_RECALL", "DISTRIBUTION_ENDED"]"""

def flag_anomalies(device_data: dict) -> list[str]:
    """
    Scan device data for anomalies requiring human attention.
    Returns list of flag strings.
    """
    # Fast local checks before calling Claude (save tokens for clear-cut cases)
    quick_flags = []

    recalls = device_data.get("fda_data", {}).get("recalls", [])
    active_recalls = [r for r in recalls if r.get("status") == "Ongoing"]
    for r in active_recalls:
        cls = r.get("classification", "")
        if cls == "Class I":
            quick_flags.append("ACTIVE_CLASS_I_RECALL")
        elif cls == "Class II":
            quick_flags.append("ACTIVE_CLASS_II_RECALL")

    gudid = device_data.get("accessgudid_data", {})
    if gudid.get("mri_safety_status") == "MR Unsafe":
        quick_flags.append("MRI_UNSAFE")
    if gudid.get("commercial_distribution_status", "").lower().startswith("not"):
        quick_flags.append("DISTRIBUTION_ENDED")
    if gudid.get("hctp"):
        quick_flags.append("HCTP_PRODUCT")
    if gudid.get("combination_product"):
        quick_flags.append("COMBINATION_PRODUCT")

    # For nuanced flags, use Claude
    payload = {
        "device_class": gudid.get("device_class", ""),
        "premarket_submission_number": gudid.get("premarket_submission_number", ""),
        "maude_recent_count": device_data.get("maude_recent_count", 0),
        "maude_brand_context": device_data.get("fda_data", {}).get("maude_brand_counts", {}),
        "brand_name": gudid.get("brand_name", ""),
        "commercial_distribution_status": gudid.get("commercial_distribution_status", ""),
        "device_description_missing": not gudid.get("device_description", ""),
        "catalog_number_missing": not gudid.get("catalog_number", ""),
        "active_recall_count": len(active_recalls),
    }

    try:
        user_content = f"Review this device data and return anomaly flags:\n{json.dumps(payload, indent=2)}"
        response = _call_claude(ANOMALY_SYSTEM_PROMPT, user_content, max_tokens=256)
        # Parse JSON array from response
        response = response.strip()
        if response.startswith("["):
            claude_flags = json.loads(response)
        else:
            # Extract JSON array if embedded in text
            import re
            match = re.search(r'\[.*?\]', response, re.DOTALL)
            claude_flags = json.loads(match.group()) if match else []
    except Exception as e:
        logger.warning(f"Anomaly flag Claude call failed: {e}")
        claude_flags = []

    all_flags = list(set(quick_flags + claude_flags))
    return all_flags
```

---

### `medops/knowledge_base.py`

```python
"""
MedOps Knowledge Base
SQLite-backed local storage for all generated intelligence.
All data stays on the Thought Reliquary. No cloud sync for formulary data.
"""

import sqlite3
import json
import uuid
import logging
from datetime import datetime
from contextlib import contextmanager
from pathlib import Path
from medops.config import DB_PATH, BRIEFS_DIR

logger = logging.getLogger(__name__)


@contextmanager
def _db_connection():
    conn = sqlite3.connect(str(DB_PATH))
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA journal_mode=WAL")     # Write-ahead logging for concurrency
    conn.execute("PRAGMA foreign_keys=ON")
    try:
        yield conn
        conn.commit()
    except Exception:
        conn.rollback()
        raise
    finally:
        conn.close()


def initialize_database():
    """Create all tables if they don't exist. Safe to run on every startup."""
    schema = """
    CREATE TABLE IF NOT EXISTS devices (
        di                          TEXT PRIMARY KEY,
        brand_name                  TEXT NOT NULL,
        company_name                TEXT,
        catalog_number              TEXT,
        version_model_number        TEXT,
        primary_product_code        TEXT,
        device_class                TEXT,
        gmdn_term                   TEXT,
        gmdn_code                   TEXT,
        mri_safety_status           TEXT,
        single_use                  INTEGER,
        device_sterile              INTEGER,
        implant_flag                TEXT,
        commercial_distribution_status TEXT,
        premarket_submission_number TEXT,
        raw_accessgudid_json        TEXT,
        first_seen                  TEXT NOT NULL,
        last_updated                TEXT NOT NULL
    );

    CREATE TABLE IF NOT EXISTS device_briefs (
        case_id             TEXT PRIMARY KEY,
        di                  TEXT NOT NULL,
        brand_name          TEXT,
        company_name        TEXT,
        product_code        TEXT,
        category            TEXT,
        brief_markdown      TEXT NOT NULL,
        anomaly_flags       TEXT,         -- JSON array
        active_recalls      INTEGER DEFAULT 0,
        maude_event_count   INTEGER DEFAULT 0,
        recommendation      TEXT,         -- approve/conditional/defer/reject
        generated_at        TEXT NOT NULL,
        generated_by        TEXT DEFAULT 'claude_sonnet',
        output_file_path    TEXT,
        FOREIGN KEY (di) REFERENCES devices(di)
    );

    CREATE TABLE IF NOT EXISTS competitive_matrices (
        matrix_id           TEXT PRIMARY KEY,
        category            TEXT NOT NULL,
        device_count        INTEGER,
        matrix_markdown     TEXT NOT NULL,
        device_dis          TEXT,         -- JSON array of DIs included
        top_recommendation  TEXT,
        generated_at        TEXT NOT NULL,
        output_file_path    TEXT
    );

    CREATE TABLE IF NOT EXISTS substitution_recommendations (
        recommendation_id   TEXT PRIMARY KEY,
        di_current          TEXT NOT NULL,
        di_proposed         TEXT NOT NULL,
        brand_current       TEXT,
        brand_proposed      TEXT,
        recommendation_text TEXT NOT NULL,
        decision            TEXT,         -- APPROVE/CONDITIONAL/DO_NOT_SUBSTITUTE
        condition           TEXT,         -- if conditional
        generated_at        TEXT NOT NULL,
        approved_by         TEXT,
        approval_date       TEXT
    );

    CREATE TABLE IF NOT EXISTS formulary (
        di                  TEXT PRIMARY KEY,
        brand_name          TEXT NOT NULL,
        company_name        TEXT,
        category            TEXT NOT NULL,
        product_code        TEXT,
        gmdn_code           TEXT,
        status              TEXT DEFAULT 'active',  -- active/under_review/removed
        added_date          TEXT NOT NULL,
        last_reviewed       TEXT,
        removal_date        TEXT,
        removal_reason      TEXT,
        notes               TEXT,
        gpo_contract_ref    TEXT,
        FOREIGN KEY (di) REFERENCES devices(di)
    );

    CREATE TABLE IF NOT EXISTS alerts (
        alert_id            TEXT PRIMARY KEY,
        device_di           TEXT NOT NULL,
        brand_name          TEXT,
        alert_type          TEXT NOT NULL,  -- recall/maude_spike/distribution_ended
        severity            TEXT NOT NULL,  -- CRITICAL/HIGH/MEDIUM/LOW
        description         TEXT NOT NULL,
        source_reference    TEXT,
        detected_date       TEXT NOT NULL,
        acknowledged        INTEGER DEFAULT 0,
        acknowledged_by     TEXT,
        acknowledged_date   TEXT,
        action_taken        TEXT,
        resolved            INTEGER DEFAULT 0,
        resolved_date       TEXT
    );

    CREATE TABLE IF NOT EXISTS category_watches (
        watch_id            TEXT PRIMARY KEY,
        category            TEXT NOT NULL UNIQUE,
        product_codes       TEXT,           -- JSON array
        vendor_names        TEXT,           -- JSON array
        alert_threshold_maude INTEGER DEFAULT 5,
        active              INTEGER DEFAULT 1,
        created_date        TEXT NOT NULL,
        last_run            TEXT
    );

    CREATE TABLE IF NOT EXISTS emerging_tech (
        tech_id             TEXT PRIMARY KEY,
        technology_name     TEXT NOT NULL,
        category            TEXT,
        brief_markdown      TEXT NOT NULL,
        regulatory_status   TEXT,
        readiness_level     TEXT,  -- monitor/evaluate/defer
        generated_at        TEXT NOT NULL,
        follow_up_date      TEXT
    );

    CREATE INDEX IF NOT EXISTS idx_briefs_di ON device_briefs(di);
    CREATE INDEX IF NOT EXISTS idx_briefs_category ON device_briefs(category);
    CREATE INDEX IF NOT EXISTS idx_briefs_generated_at ON device_briefs(generated_at);
    CREATE INDEX IF NOT EXISTS idx_formulary_category ON formulary(category);
    CREATE INDEX IF NOT EXISTS idx_formulary_status ON formulary(status);
    CREATE INDEX IF NOT EXISTS idx_alerts_di ON alerts(device_di);
    CREATE INDEX IF NOT EXISTS idx_alerts_acknowledged ON alerts(acknowledged);
    CREATE INDEX IF NOT EXISTS idx_devices_product_code ON devices(primary_product_code);
    CREATE INDEX IF NOT EXISTS idx_devices_company ON devices(company_name);
    """
    with _db_connection() as conn:
        conn.executescript(schema)
    logger.info(f"Database initialized at {DB_PATH}")


def _upsert_device(conn: sqlite3.Connection, accessgudid_data: dict):
    """Insert or update a device record from ACCESSGUDID data."""
    now = datetime.utcnow().isoformat()
    conn.execute("""
        INSERT INTO devices (
            di, brand_name, company_name, catalog_number, version_model_number,
            primary_product_code, device_class, gmdn_term, gmdn_code,
            mri_safety_status, single_use, device_sterile, implant_flag,
            commercial_distribution_status, premarket_submission_number,
            raw_accessgudid_json, first_seen, last_updated
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ON CONFLICT(di) DO UPDATE SET
            brand_name = excluded.brand_name,
            commercial_distribution_status = excluded.commercial_distribution_status,
            raw_accessgudid_json = excluded.raw_accessgudid_json,
            last_updated = excluded.last_updated
    """, (
        accessgudid_data.get("primary_di", ""),
        accessgudid_data.get("brand_name", ""),
        accessgudid_data.get("company_name", ""),
        accessgudid_data.get("catalog_number", ""),
        accessgudid_data.get("version_model_number", ""),
        accessgudid_data.get("primary_product_code", ""),
        accessgudid_data.get("device_class", ""),
        accessgudid_data.get("primary_gmdn_name", ""),
        accessgudid_data.get("primary_gmdn_code", ""),
        accessgudid_data.get("mri_safety_status", ""),
        int(bool(accessgudid_data.get("single_use", False))),
        int(bool(accessgudid_data.get("device_sterile", False))),
        accessgudid_data.get("implant_flag", ""),
        accessgudid_data.get("commercial_distribution_status", ""),
        accessgudid_data.get("premarket_submission_number", ""),
        json.dumps(accessgudid_data),
        now,
        now,
    ))


def save_brief(brief_data: dict) -> tuple[str, str]:
    """
    Save a generated device brief to the knowledge base.
    Returns (case_id, output_file_path).
    """
    case_id = f"BRIEF-{datetime.utcnow().strftime('%Y%m%d')}-{str(uuid.uuid4())[:8].upper()}"
    now = datetime.utcnow().isoformat()

    accessgudid_data = brief_data.get("accessgudid_data", {})
    brief_markdown = brief_data.get("brief_markdown", "")
    anomaly_flags = brief_data.get("anomaly_flags", [])
    output_format = brief_data.get("output_format", "markdown")

    # Save markdown file
    di = accessgudid_data.get("primary_di", "unknown")
    safe_name = accessgudid_data.get("brand_name", "device").replace("/", "_").replace(" ", "_")
    output_filename = f"{case_id}_{safe_name}.md"
    output_path = BRIEFS_DIR / output_filename
    output_path.write_text(brief_markdown, encoding="utf-8")

    with _db_connection() as conn:
        _upsert_device(conn, accessgudid_data)
        conn.execute("""
            INSERT INTO device_briefs (
                case_id, di, brand_name, company_name, product_code, category,
                brief_markdown, anomaly_flags, active_recalls, maude_event_count,
                recommendation, generated_at, output_file_path
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            case_id,
            di,
            accessgudid_data.get("brand_name", ""),
            accessgudid_data.get("company_name", ""),
            accessgudid_data.get("primary_product_code", ""),
            brief_data.get("category", ""),
            brief_markdown,
            json.dumps(anomaly_flags),
            brief_data.get("active_recall_count", 0),
            brief_data.get("maude_event_count", 0),
            brief_data.get("recommendation", ""),
            now,
            str(output_path),
        ))

    logger.info(f"Brief saved: {case_id} → {output_path}")
    return case_id, str(output_path)


def get_brief_by_id(case_id: str) -> dict:
    """Retrieve a brief by its case ID."""
    with _db_connection() as conn:
        row = conn.execute(
            "SELECT * FROM device_briefs WHERE case_id = ?", (case_id,)
        ).fetchone()
    if row:
        d = dict(row)
        d["anomaly_flags"] = json.loads(d.get("anomaly_flags") or "[]")
        return d
    return {}


def search_briefs(query: str, category: str = None) -> list[dict]:
    """
    Full-text search across device briefs by brand name, company, or markdown content.
    """
    with _db_connection() as conn:
        if category:
            rows = conn.execute("""
                SELECT case_id, di, brand_name, company_name, category,
                       recommendation, generated_at, output_file_path
                FROM device_briefs
                WHERE category = ? AND (
                    brand_name LIKE ? OR company_name LIKE ? OR brief_markdown LIKE ?
                )
                ORDER BY generated_at DESC
                LIMIT 50
            """, (category, f"%{query}%", f"%{query}%", f"%{query}%")).fetchall()
        else:
            rows = conn.execute("""
                SELECT case_id, di, brand_name, company_name, category,
                       recommendation, generated_at, output_file_path
                FROM device_briefs
                WHERE brand_name LIKE ? OR company_name LIKE ? OR brief_markdown LIKE ?
                ORDER BY generated_at DESC
                LIMIT 50
            """, (f"%{query}%", f"%{query}%", f"%{query}%")).fetchall()
    return [dict(r) for r in rows]


def get_formulary_devices() -> list[dict]:
    """Return all active formulary devices."""
    with _db_connection() as conn:
        rows = conn.execute("""
            SELECT f.*, d.primary_product_code, d.device_class,
                   d.gmdn_code, d.mri_safety_status, d.commercial_distribution_status
            FROM formulary f
            LEFT JOIN devices d ON f.di = d.di
            WHERE f.status = 'active'
            ORDER BY f.category, f.brand_name
        """).fetchall()
    return [dict(r) for r in rows]


def add_to_formulary(di: str, category: str, notes: str = "", gpo_contract_ref: str = ""):
    """Add a device to the active formulary."""
    with _db_connection() as conn:
        # Verify device exists in devices table
        device = conn.execute("SELECT * FROM devices WHERE di = ?", (di,)).fetchone()
        if not device:
            raise ValueError(f"Device DI {di} not found in knowledge base. Run a device brief first.")

        conn.execute("""
            INSERT INTO formulary (
                di, brand_name, company_name, category, product_code, gmdn_code,
                status, added_date, notes, gpo_contract_ref
            )
            SELECT di, brand_name, company_name, ?, primary_product_code, gmdn_code,
                   'active', ?, ?, ?
            FROM devices WHERE di = ?
            ON CONFLICT(di) DO UPDATE SET
                status = 'active',
                notes = excluded.notes,
                gpo_contract_ref = excluded.gpo_contract_ref
        """, (category, datetime.utcnow().isoformat(), notes, gpo_contract_ref, di))
    logger.info(f"Added {di} to formulary in category: {category}")


def remove_from_formulary(di: str, reason: str):
    """Remove a device from the active formulary."""
    with _db_connection() as conn:
        conn.execute("""
            UPDATE formulary SET
                status = 'removed',
                removal_date = ?,
                removal_reason = ?
            WHERE di = ?
        """, (datetime.utcnow().isoformat(), reason, di))
    logger.info(f"Removed {di} from formulary: {reason}")


def log_alerts(alerts: list):
    """Persist a list of Alert objects to the alerts table."""
    now = datetime.utcnow().isoformat()
    with _db_connection() as conn:
        for alert in alerts:
            alert_id = f"ALERT-{str(uuid.uuid4())[:12].upper()}"
            conn.execute("""
                INSERT OR IGNORE INTO alerts (
                    alert_id, device_di, brand_name, alert_type, severity,
                    description, source_reference, detected_date
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                alert_id,
                getattr(alert, "device_di", ""),
                getattr(alert, "brand_name", ""),
                getattr(alert, "alert_type", ""),
                getattr(alert, "severity", ""),
                getattr(alert, "description", ""),
                getattr(alert, "source_reference", ""),
                now,
            ))
```

---

### `medops/alerts.py`

```python
"""
MedOps Alert System
Monitors active formulary devices for recall activity and MAUDE event spikes.
Dispatches alerts via configured channel (console, email, or Notion).
"""

import logging
import smtplib
from dataclasses import dataclass, field
from datetime import datetime
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from typing import Optional
from medops.config import (
    ALERT_EMAIL_TO, ALERT_EMAIL_FROM, SMTP_HOST, SMTP_PORT,
    RECALL_SEVERITY_MAP, DEFAULT_MAUDE_LOOKBACK_DAYS,
)

logger = logging.getLogger(__name__)


@dataclass
class Alert:
    device_di: str
    brand_name: str
    alert_type: str           # recall | maude_spike | distribution_ended
    severity: str             # CRITICAL | HIGH | MEDIUM | LOW
    description: str
    source_reference: str = ""
    date: str = field(default_factory=lambda: datetime.utcnow().isoformat())
    action_required: str = ""
    category: str = ""


def check_recalls_for_formulary(formulary_devices: list = None) -> list[Alert]:
    """
    Check every active formulary device against OpenFDA recall endpoint.
    Returns list of Alert objects for any active recalls found.
    """
    from medops.knowledge_base import get_formulary_devices
    from medops.openfda import check_di_for_active_recalls

    if formulary_devices is None:
        formulary_devices = get_formulary_devices()

    alerts = []
    for device in formulary_devices:
        di = device.get("di", "")
        brand_name = device.get("brand_name", "")
        product_code = device.get("primary_product_code", device.get("product_code", ""))
        category = device.get("category", "")

        try:
            active_recalls = check_di_for_active_recalls(di, product_code, brand_name)
        except Exception as e:
            logger.warning(f"Recall check failed for {di}: {e}")
            continue

        for recall in active_recalls:
            classification = recall.get("classification", "Class III")
            severity = RECALL_SEVERITY_MAP.get(classification, "LOW")
            recall_number = recall.get("recall_number", "")
            reason = recall.get("reason_for_recall", "")

            alert = Alert(
                device_di=di,
                brand_name=brand_name,
                alert_type="recall",
                severity=severity,
                description=(
                    f"{classification} recall — {recall.get('recalling_firm', '')}. "
                    f"Reason: {reason[:200]}. "
                    f"Recall #: {recall_number}."
                ),
                source_reference=recall_number,
                action_required=(
                    "Remove from active inventory immediately and notify clinical staff."
                    if severity == "CRITICAL"
                    else "Review within 24 hours and assess inventory impact."
                ),
                category=category,
            )
            alerts.append(alert)
            logger.warning(f"RECALL ALERT [{severity}]: {brand_name} — {recall_number}")

    return alerts


def check_maude_spikes(
    formulary_devices: list = None,
    days_lookback: int = DEFAULT_MAUDE_LOOKBACK_DAYS,
    watch_list: list = None,
) -> list[Alert]:
    """
    Detect MAUDE adverse event spikes for formulary devices.
    Compares recent event volume to baseline (prior 9-month period).
    Threshold: >3x baseline OR absolute count > category threshold from watch_config.

    Returns list of Alert objects.
    """
    from medops.knowledge_base import get_formulary_devices
    from medops.openfda import get_maude_event_volume, get_maude_baseline_volume

    if formulary_devices is None:
        formulary_devices = get_formulary_devices()

    # Build category thresholds from watch_list if provided
    category_thresholds = {}
    if watch_list:
        for w in watch_list:
            category_thresholds[w.get("category", "")] = w.get("alert_threshold_maude", 5)

    alerts = []
    for device in formulary_devices:
        di = device.get("di", "")
        brand_name = device.get("brand_name", "")
        product_code = device.get("primary_product_code", device.get("product_code", ""))
        category = device.get("category", "")

        try:
            recent_count = get_maude_event_volume(brand_name, product_code, days_lookback)
            baseline_monthly = get_maude_baseline_volume(brand_name, product_code)
        except Exception as e:
            logger.warning(f"MAUDE check failed for {di}: {e}")
            continue

        # Spike threshold: 3x monthly baseline OR above category absolute threshold
        baseline_in_period = baseline_monthly * (days_lookback / 30.0)
        spike_threshold = max(baseline_in_period * 3, 1)
        abs_threshold = category_thresholds.get(category, 5)

        if recent_count >= spike_threshold or recent_count >= abs_threshold:
            severity = "HIGH" if recent_count >= spike_threshold * 2 else "MEDIUM"
            alert = Alert(
                device_di=di,
                brand_name=brand_name,
                alert_type="maude_spike",
                severity=severity,
                description=(
                    f"MAUDE spike detected: {recent_count} events in last {days_lookback} days "
                    f"vs. baseline {baseline_in_period:.1f} events/period "
                    f"(x{recent_count / max(baseline_in_period, 0.1):.1f} baseline). "
                    f"Product code: {product_code}."
                ),
                source_reference=f"OpenFDA device/event.json — product_code:{product_code}",
                action_required=f"Review MAUDE reports for {brand_name}. Consider scheduling formal device review.",
                category=category,
            )
            alerts.append(alert)
            logger.warning(f"MAUDE SPIKE [{severity}]: {brand_name} — {recent_count} events in {days_lookback}d")

    return alerts


def combine_alerts(recall_alerts: list[Alert], maude_alerts: list[Alert]) -> list[Alert]:
    """
    Combine and deduplicate alerts. Sort by severity (CRITICAL first).
    """
    severity_order = {"CRITICAL": 0, "HIGH": 1, "MEDIUM": 2, "LOW": 3}
    combined = recall_alerts + maude_alerts

    # Deduplicate by (device_di, alert_type, source_reference)
    seen = set()
    unique = []
    for alert in combined:
        key = (alert.device_di, alert.alert_type, alert.source_reference)
        if key not in seen:
            seen.add(key)
            unique.append(alert)

    return sorted(unique, key=lambda a: severity_order.get(a.severity, 99))


def send_alert(alert: Alert, channel: str = "console"):
    """Send a single alert via the configured channel."""
    send_alert_batch([alert], channel)


def send_alert_batch(alerts: list[Alert], channel: str = "console") -> list[str]:
    """
    Send a batch of alerts via the configured channel.
    Returns list of notification IDs (confirmation references).
    """
    if not alerts:
        return []

    if channel == "console":
        return _send_alerts_console(alerts)
    elif channel == "email":
        return _send_alerts_email(alerts)
    elif channel == "notion":
        return _send_alerts_notion(alerts)
    else:
        logger.warning(f"Unknown alert channel: {channel}. Falling back to console.")
        return _send_alerts_console(alerts)


def _send_alerts_console(alerts: list[Alert]) -> list[str]:
    ids = []
    print("\n" + "="*60)
    print(f"MedOps ALERT NOTIFICATION — {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    print("="*60)
    for alert in alerts:
        print(f"\n[{alert.severity}] {alert.alert_type.upper()}: {alert.brand_name}")
        print(f"  DI: {alert.device_di}")
        print(f"  {alert.description}")
        if alert.action_required:
            print(f"  ACTION: {alert.action_required}")
        ids.append(f"CONSOLE-{alert.device_di[:8]}")
    print("="*60 + "\n")
    return ids


def _send_alerts_email(alerts: list[Alert]) -> list[str]:
    if not ALERT_EMAIL_TO:
        logger.error("ALERT_EMAIL_TO not configured. Cannot send email alerts.")
        return _send_alerts_console(alerts)

    subject = f"MedOps Alert: {len(alerts)} device alert(s) — {datetime.now().strftime('%Y-%m-%d')}"
    critical = [a for a in alerts if a.severity == "CRITICAL"]
    if critical:
        subject = f"⚠️ CRITICAL — {subject}"

    body_lines = [
        f"MedOps Intelligence OS — Alert Notification",
        f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} UTC",
        f"Total alerts: {len(alerts)}",
        "",
    ]
    for alert in alerts:
        body_lines.extend([
            f"{'='*50}",
            f"[{alert.severity}] {alert.alert_type.upper()}",
            f"Device: {alert.brand_name} (DI: {alert.device_di})",
            f"Category: {alert.category}",
            f"Description: {alert.description}",
            f"Action Required: {alert.action_required}",
            f"Detected: {alert.date}",
            "",
        ])

    body = "\n".join(body_lines)

    try:
        msg = MIMEMultipart()
        msg["From"] = ALERT_EMAIL_FROM
        msg["To"] = ALERT_EMAIL_TO
        msg["Subject"] = subject
        msg.attach(MIMEText(body, "plain"))

        with smtplib.SMTP(SMTP_HOST, SMTP_PORT) as server:
            server.sendmail(ALERT_EMAIL_FROM, [ALERT_EMAIL_TO], msg.as_string())

        logger.info(f"Alert email sent to {ALERT_EMAIL_TO}: {len(alerts)} alerts")
        return [f"EMAIL-{a.device_di[:8]}" for a in alerts]
    except Exception as e:
        logger.error(f"Email alert failed: {e}. Falling back to console.")
        return _send_alerts_console(alerts)


def _send_alerts_notion(alerts: list[Alert]) -> list[str]:
    """Route to Notion integration module."""
    try:
        from medops.notion import update_alert_log_batch
        ids = []
        for alert in alerts:
            page_id = update_alert_log_batch(alert)
            ids.append(page_id or f"NOTION-{alert.device_di[:8]}")
        return ids
    except Exception as e:
        logger.error(f"Notion alert failed: {e}. Falling back to console.")
        return _send_alerts_console(alerts)
```

---

### `medops/formatter.py`

```python
"""
Output Format Generators
Converts knowledge base content to various output formats.
"""

import json
import logging
from datetime import datetime
from pathlib import Path
from medops.config import BRIEFS_DIR, DIGESTS_DIR

logger = logging.getLogger(__name__)


def save_markdown(content: str, filename: str, directory: Path = BRIEFS_DIR) -> str:
    """Save markdown content to file. Returns file path."""
    path = directory / filename
    path.write_text(content, encoding="utf-8")
    return str(path)


def save_json(data: dict, filename: str, directory: Path = BRIEFS_DIR) -> str:
    """Save dict as JSON. Returns file path."""
    path = directory / filename
    path.write_text(json.dumps(data, indent=2, default=str), encoding="utf-8")
    return str(path)


def format_brief_header(accessgudid_data: dict, case_id: str) -> str:
    """Generate standardized document header for a device brief."""
    return f"""---
Document ID: {case_id}
Device: {accessgudid_data.get('brand_name', 'Unknown')}
Manufacturer: {accessgudid_data.get('company_name', '')}
DI: {accessgudid_data.get('primary_di', '')}
Product Code: {accessgudid_data.get('primary_product_code', '')}
Generated: {datetime.utcnow().strftime('%Y-%m-%d %H:%M UTC')}
System: MedOps Intelligence OS (MS-0002) — Thought Reliquary
---

"""


def format_digest_header(period_label: str) -> str:
    """Generate standardized header for the weekly digest."""
    return f"""---
MedOps Weekly Intelligence Digest
Period: {period_label}
Generated: {datetime.utcnow().strftime('%Y-%m-%d %H:%M UTC')}
System: MedOps Intelligence OS (MS-0002) — UIHC Perioperative Supply Chain
---

"""


def devices_to_table(devices: list[dict], columns: list[str]) -> str:
    """Convert a list of device dicts to a Markdown table."""
    if not devices:
        return "_No devices found._\n"

    header = "| " + " | ".join(columns) + " |"
    separator = "|" + "|".join(["-" * (len(c) + 2) for c in columns]) + "|"
    rows = []
    for d in devices:
        row = "| " + " | ".join(str(d.get(col, "")) for col in columns) + " |"
        rows.append(row)

    return "\n".join([header, separator] + rows) + "\n"
```

---

### `medops/pipeline.py`

```python
"""
MedOps Pipeline Orchestration
Main entry point for all pipeline runs. Called by Hermes task definitions.
Also the CLI daemon entry point.
"""

import yaml
import json
import logging
import argparse
import sys
from datetime import datetime
from pathlib import Path
from medops.config import WATCH_CONFIG_PATH, DIGESTS_DIR
from medops import knowledge_base as kb

logger = logging.getLogger(__name__)


def setup_logging(level: str = "INFO"):
    logging.basicConfig(
        level=getattr(logging, level.upper(), logging.INFO),
        format="%(asctime)s [%(name)s] %(levelname)s: %(message)s",
        handlers=[
            logging.StreamHandler(sys.stdout),
            logging.FileHandler("/app/data/medops.log"),
        ],
    )


def load_category_watch_config(
    config_path: str = None, category_filter: list = None
) -> list:
    """Load watch_config.yaml. Filter by categories if specified."""
    path = Path(config_path or WATCH_CONFIG_PATH)
    if not path.exists():
        logger.warning(f"Watch config not found at {path}. Using empty watch list.")
        return []

    with open(path) as f:
        config = yaml.safe_load(f)

    watch_list = config.get("category_watches", [])
    if category_filter:
        watch_list = [w for w in watch_list if w.get("category") in category_filter]
    return watch_list


# ── On-Demand Pipelines ──────────────────────────────────────────────────────

def run_device_brief(identifier: str, output_format: str = "markdown",
                     include_substitutes: bool = True) -> str:
    """
    Full pipeline for a single device brief.
    Returns case_id.
    """
    from medops.accessgudid import resolve_device_identifier, get_device_by_di
    from medops.openfda import get_device_full_fda_profile, get_510k_for_di
    from medobs.pubmed import search_device_literature
    from medops.synthesizer import generate_device_brief, flag_anomalies
    from medops.formatter import format_brief_header

    logger.info(f"run_device_brief: {identifier}")

    # Step 1: Resolve identifier
    resolved = resolve_device_identifier(identifier)
    di = resolved["di"]

    # Step 2: Full ACCESSGUDID record
    accessgudid_data = get_device_by_di(di)

    # Step 3: FDA profile
    fda_data = get_device_full_fda_profile(
        accessgudid_data.get("primary_product_code", ""),
        accessgudid_data.get("brand_name", ""),
    )
    fda_510k = get_510k_for_di(di, accessgudid_data)
    if fda_510k and not fda_data.get("510k"):
        fda_data["510k"] = [fda_510k]

    # Step 4: PubMed
    pubmed_abstracts = search_device_literature(
        device_name=accessgudid_data.get("brand_name", ""),
        product_code=accessgudid_data.get("primary_product_code", ""),
        max_results=15,
    )

    # Step 5: Substitutes
    substitute_candidates = []
    if include_substitutes:
        try:
            substitutes = find_substitutes(di)
            substitute_candidates = [
                {
                    "di": s.di,
                    "brand_name": s.brand_name,
                    "company": s.company_name,
                    "gmdn_match": s.gmdn_match,
                    "score": s.score,
                    "active_recalls": s.active_recalls,
                }
                for s in substitutes[:5]
            ]
        except Exception as e:
            logger.warning(f"Substitution search failed: {e}")

    # Step 6: Anomaly flags (fast local check)
    device_data_for_flags = {
        "accessgudid_data": accessgudid_data,
        "fda_data": fda_data,
    }
    anomaly_flags = flag_anomalies(device_data_for_flags)

    # Step 7: Claude brief generation
    brief_markdown = generate_device_brief(
        accessgudid_data=accessgudid_data,
        fda_data=fda_data,
        maude_data=fda_data.get("maude_recent", []),
        recall_data=fda_data.get("recalls", []),
        pubmed_abstracts=pubmed_abstracts,
        substitute_candidates=substitute_candidates,
    )

    # Add header
    brief_markdown = format_brief_header(accessgudid_data, "TBD") + brief_markdown

    # Step 8: Save
    case_id, output_path = kb.save_brief({
        "accessgudid_data": accessgudid_data,
        "brief_markdown": brief_markdown,
        "anomaly_flags": anomaly_flags,
        "active_recall_count": len([r for r in fda_data.get("recalls", []) if r.get("status") == "Ongoing"]),
        "maude_event_count": len(fda_data.get("maude_recent", [])),
        "output_format": output_format,
    })

    if anomaly_flags:
        logger.warning(f"Anomaly flags for {di}: {anomaly_flags}")

    print(f"\n✓ Device brief complete. Case ID: {case_id}")
    print(f"  Output: {output_path}")
    if anomaly_flags:
        print(f"  ⚠️  Anomaly flags: {', '.join(anomaly_flags)}")

    return case_id


def run_competitive_matrix(category: str, device_list: list = None) -> str:
    """
    Full matrix pipeline for a device category or explicit device list.
    Returns matrix_id.
    """
    import uuid
    from medops.accessgudid import get_device_by_di
    from medops.openfda import get_device_full_fda_profile
    from medops.pubmed import search_device_literature
    from medops.synthesizer import generate_competitive_matrix
    from medops.config import DATA_DIR

    logger.info(f"run_competitive_matrix: category={category}")

    if not device_list:
        # Pull from formulary for this category
        formulary = kb.get_formulary_devices()
        device_list = [d["di"] for d in formulary if d.get("category") == category]

    if not device_list:
        raise ValueError(f"No devices found for category: {category}")

    devices_data = []
    for di in device_list:
        accessgudid_data = get_device_by_di(di)
        fda_data = get_device_full_fda_profile(
            accessgudid_data.get("primary_product_code", ""),
            accessgudid_data.get("brand_name", ""),
        )
        literature = search_device_literature(
            accessgudid_data.get("brand_name", ""), category, max_results=5
        )
        devices_data.append({
            "accessgudid_data": accessgudid_data,
            "fda_data": fda_data,
            "literature_summary": " | ".join(a["title"] for a in literature[:3]),
            "maude_recent_count": len(fda_data.get("maude_recent", [])),
        })

    matrix_markdown = generate_competitive_matrix(devices_data)

    # Save
    matrix_id = f"MATRIX-{datetime.utcnow().strftime('%Y%m%d')}-{str(uuid.uuid4())[:8].upper()}"
    output_path = DATA_DIR / "matrices" / f"{matrix_id}_{category}.md"
    output_path.parent.mkdir(exist_ok=True)
    output_path.write_text(matrix_markdown, encoding="utf-8")

    with kb._db_connection() as conn:
        conn.execute("""
            INSERT INTO competitive_matrices
            (matrix_id, category, device_count, matrix_markdown, device_dis, generated_at, output_file_path)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (
            matrix_id, category, len(devices_data), matrix_markdown,
            json.dumps(device_list), datetime.utcnow().isoformat(), str(output_path)
        ))

    print(f"\n✓ Competitive matrix complete. Matrix ID: {matrix_id}")
    print(f"  Output: {output_path}")
    return matrix_id


def run_substitution_analysis(di_a: str, di_b: str) -> str:
    """Full substitution analysis pipeline comparing Device A to Device B."""
    import uuid
    from medops.accessgudid import get_device_by_di
    from medops.openfda import get_device_full_fda_profile
    from medops.synthesizer import generate_substitution_recommendation
    from medops.config import DATA_DIR

    logger.info(f"run_substitution_analysis: A={di_a} B={di_b}")

    def get_full_profile(di):
        accessgudid_data = get_device_by_di(di)
        fda_data = get_device_full_fda_profile(
            accessgudid_data.get("primary_product_code", ""),
            accessgudid_data.get("brand_name", ""),
        )
        return {"accessgudid_data": accessgudid_data, "fda_data": fda_data}

    device_a = get_full_profile(di_a)
    device_b = get_full_profile(di_b)

    recommendation_text = generate_substitution_recommendation(device_a, device_b)

    # Save
    rec_id = f"SUB-{datetime.utcnow().strftime('%Y%m%d')}-{str(uuid.uuid4())[:8].upper()}"
    output_path = DATA_DIR / "substitutions" / f"{rec_id}.md"
    output_path.parent.mkdir(exist_ok=True)
    output_path.write_text(recommendation_text, encoding="utf-8")

    with kb._db_connection() as conn:
        conn.execute("""
            INSERT INTO substitution_recommendations
            (recommendation_id, di_current, di_proposed, brand_current, brand_proposed,
             recommendation_text, generated_at)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (
            rec_id, di_a, di_b,
            device_a["accessgudid_data"].get("brand_name", ""),
            device_b["accessgudid_data"].get("brand_name", ""),
            recommendation_text,
            datetime.utcnow().isoformat(),
        ))

    print(f"\n✓ Substitution analysis complete. ID: {rec_id}")
    print(f"  Output: {output_path}")
    return rec_id


def run_scheduled_digest(categories: list = None, delivery_channel: str = "notion"):
    """Weekly digest pipeline. Called by Hermes cron Monday 08:00."""
    from medops.openfda import (
        get_new_510k_clearances_by_product_codes,
        get_recalls_for_watch_list,
    )
    from medops.pubmed import search_device_literature_batch
    from medops.alerts import check_maude_spikes
    from medops.synthesizer import generate_weekly_digest
    from medops.formatter import format_digest_header

    logger.info("run_scheduled_digest starting")

    watch_list = load_category_watch_config(category_filter=categories)
    if not watch_list:
        logger.warning("No watch list configured. Digest will be empty.")

    product_codes = [
        code
        for w in watch_list
        for code in w.get("product_codes", [])
    ]

    new_clearances = get_new_510k_clearances_by_product_codes(product_codes, days_back=7)
    recall_events = get_recalls_for_watch_list(watch_list, days_back=7)
    maude_alerts = check_maude_spikes(watch_list=watch_list)
    literature_updates = search_device_literature_batch(watch_list, days_back=7)

    period_label = f"Week of {datetime.now().strftime('%B %d, %Y')}"
    digest_markdown, summary = generate_weekly_digest(
        new_clearances, recall_events, maude_alerts, literature_updates,
        watch_list, period_label
    )

    header = format_digest_header(period_label)
    full_digest = header + digest_markdown

    # Save digest file
    filename = f"digest_{datetime.now().strftime('%Y%m%d')}.md"
    digest_path = DIGESTS_DIR / filename
    digest_path.write_text(full_digest, encoding="utf-8")
    logger.info(f"Digest saved: {digest_path}")

    # Deliver
    deliver_digest(full_digest, channel=delivery_channel)
    print(f"\n✓ Weekly digest complete: {summary}")
    print(f"  Saved: {digest_path}")


def deliver_digest(digest_markdown: str, channel: str = "notion") -> str:
    """Deliver the completed digest via the configured channel."""
    if channel == "notion":
        try:
            from medops.notion import create_digest_page
            return create_digest_page(digest_markdown)
        except Exception as e:
            logger.error(f"Notion delivery failed: {e}. Saving to file only.")
    elif channel == "email":
        from medops.alerts import _send_alerts_email
        # Re-use email infra with digest content
        try:
            import smtplib
            from email.mime.text import MIMEText
            from medops.config import ALERT_EMAIL_TO, ALERT_EMAIL_FROM, SMTP_HOST, SMTP_PORT
            msg = MIMEText(digest_markdown, "plain")
            msg["Subject"] = f"MedOps Weekly Digest — {datetime.now().strftime('%Y-%m-%d')}"
            msg["From"] = ALERT_EMAIL_FROM
            msg["To"] = ALERT_EMAIL_TO
            with smtplib.SMTP(SMTP_HOST, SMTP_PORT) as server:
                server.sendmail(ALERT_EMAIL_FROM, [ALERT_EMAIL_TO], msg.as_string())
            return "email_sent"
        except Exception as e:
            logger.error(f"Email delivery failed: {e}")
    return "file_only"


def run_recall_alert_check(alert_channel: str = "console"):
    """Daily recall and MAUDE alert check. Called by Hermes cron."""
    from medops.alerts import (
        check_recalls_for_formulary, check_maude_spikes,
        combine_alerts, send_alert_batch
    )

    logger.info("run_recall_alert_check starting")

    recall_alerts = check_recalls_for_formulary()
    maude_alerts = check_maude_spikes()
    active_alerts = combine_alerts(recall_alerts, maude_alerts)

    if active_alerts:
        kb.log_alerts(active_alerts)
        send_alert_batch(active_alerts, channel=alert_channel)
        print(f"\n⚠️  {len(active_alerts)} alert(s) detected and dispatched.")
    else:
        print("\n✓ Alert check complete. No active alerts.")

    return active_alerts


# ── GMDN Substitution Engine ─────────────────────────────────────────────────

def find_substitutes(di: str) -> list:
    """
    Find clinically equivalent substitution candidates for a given DI.
    See Section 5 for full implementation.
    """
    from medops.substitution import find_substitutes as _find_substitutes
    return _find_substitutes(di)


# ── Daemon Mode ───────────────────────────────────────────────────────────────

def run_daemon():
    """Daemon mode: initialize DB and wait for Hermes task invocations."""
    setup_logging()
    logger.info("MedOps pipeline daemon starting on Thought Reliquary")
    kb.initialize_database()
    logger.info("Database initialized. Awaiting Hermes task invocations.")
    # In daemon mode, pipeline functions are called directly by Hermes
    # via subprocess invocations with --mode flags (see docker CMD)
    import time
    while True:
        time.sleep(60)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="MedOps Pipeline — Thought Reliquary")
    parser.add_argument(
        "--mode",
        choices=["daemon", "brief", "matrix", "substitution", "digest", "recall_check", "maude_monitor"],
        required=True,
    )
    parser.add_argument("--di", help="Device Identifier for brief/substitution modes")
    parser.add_argument("--di-b", help="Second DI for substitution comparison")
    parser.add_argument("--category", help="Category for matrix/digest modes")
    parser.add_argument("--channel", default="console", help="Alert/delivery channel")
    parser.add_argument("--log-level", default="INFO")
    args = parser.parse_args()

    setup_logging(args.log_level)
    kb.initialize_database()

    if args.mode == "daemon":
        run_daemon()
    elif args.mode == "brief":
        if not args.di:
            print("ERROR: --di required for brief mode")
            sys.exit(1)
        run_device_brief(args.di)
    elif args.mode == "matrix":
        if not args.category:
            print("ERROR: --category required for matrix mode")
            sys.exit(1)
        run_competitive_matrix(args.category)
    elif args.mode == "substitution":
        if not args.di or not args.di_b:
            print("ERROR: --di and --di-b required for substitution mode")
            sys.exit(1)
        run_substitution_analysis(args.di, args.di_b)
    elif args.mode == "digest":
        run_scheduled_digest(delivery_channel=args.channel)
    elif args.mode in ("recall_check", "maude_monitor"):
        run_recall_alert_check(alert_channel=args.channel)
```

---

## Section 3: The Knowledge Base Architecture

### 3.1 Why Local SQLite on the Thought Reliquary

Device data from ACCESSGUDID and OpenFDA is public regulatory data — no PHI, no HIPAA restrictions. However, the **formulary itself** — which devices UIHC uses, at what contract status, under review by whom, targeted for substitution — is sensitive institutional procurement intelligence. It reveals contracting strategy, vendor relationships, and cost management priorities. This data does not belong in a cloud database or third-party API.

SQLite on the Thought Reliquary (192.168.4.100, `/app/data/medops.db`) is appropriate: persistent, queryable, backed up to local storage, zero external exposure. Docker volume mount ensures data survives container restarts.

### 3.2 Complete SQLite Schema

```sql
-- MedOps Knowledge Base Schema
-- Document: MS-0002 | System: Thought Reliquary (192.168.4.100)

-- ── Devices ──────────────────────────────────────────────────────────────────
CREATE TABLE IF NOT EXISTS devices (
    di                              TEXT PRIMARY KEY,
    brand_name                      TEXT NOT NULL,
    company_name                    TEXT,
    catalog_number                  TEXT,
    version_model_number            TEXT,
    primary_product_code            TEXT,
    device_class                    TEXT CHECK(device_class IN ('1','2','3','')),
    gmdn_term                       TEXT,
    gmdn_code                       TEXT,
    mri_safety_status               TEXT,
    single_use                      INTEGER DEFAULT 0 CHECK(single_use IN (0,1)),
    device_sterile                  INTEGER DEFAULT 0 CHECK(device_sterile IN (0,1)),
    implant_flag                    TEXT,
    commercial_distribution_status  TEXT,
    premarket_submission_number     TEXT,
    raw_accessgudid_json            TEXT,
    first_seen                      TEXT NOT NULL,
    last_updated                    TEXT NOT NULL
);

CREATE INDEX IF NOT EXISTS idx_devices_product_code   ON devices(primary_product_code);
CREATE INDEX IF NOT EXISTS idx_devices_company        ON devices(company_name);
CREATE INDEX IF NOT EXISTS idx_devices_gmdn_code      ON devices(gmdn_code);

-- ── Device Briefs ─────────────────────────────────────────────────────────────
CREATE TABLE IF NOT EXISTS device_briefs (
    case_id             TEXT PRIMARY KEY,
    di                  TEXT NOT NULL,
    brand_name          TEXT,
    company_name        TEXT,
    product_code        TEXT,
    category            TEXT,
    brief_markdown      TEXT NOT NULL,
    anomaly_flags       TEXT,       -- JSON array: ["ACTIVE_CLASS_II_RECALL", ...]
    active_recalls      INTEGER DEFAULT 0,
    maude_event_count   INTEGER DEFAULT 0,
    recommendation      TEXT CHECK(recommendation IN
                            ('approve','conditional','defer','reject','')),
    generated_at        TEXT NOT NULL,
    generated_by        TEXT DEFAULT 'claude_sonnet',
    output_file_path    TEXT,
    FOREIGN KEY (di) REFERENCES devices(di)
);

CREATE INDEX IF NOT EXISTS idx_briefs_di            ON device_briefs(di);
CREATE INDEX IF NOT EXISTS idx_briefs_category      ON device_briefs(category);
CREATE INDEX IF NOT EXISTS idx_briefs_generated_at  ON device_briefs(generated_at DESC);
CREATE INDEX IF NOT EXISTS idx_briefs_recommendation ON device_briefs(recommendation);

-- ── Competitive Matrices ──────────────────────────────────────────────────────
CREATE TABLE IF NOT EXISTS competitive_matrices (
    matrix_id           TEXT PRIMARY KEY,
    category            TEXT NOT NULL,
    device_count        INTEGER,
    matrix_markdown     TEXT NOT NULL,
    device_dis          TEXT,       -- JSON array of DIs
    top_recommendation  TEXT,
    generated_at        TEXT NOT NULL,
    output_file_path    TEXT
);

CREATE INDEX IF NOT EXISTS idx_matrices_category ON competitive_matrices(category);

-- ── Substitution Recommendations ─────────────────────────────────────────────
CREATE TABLE IF NOT EXISTS substitution_recommendations (
    recommendation_id   TEXT PRIMARY KEY,
    di_current          TEXT NOT NULL,
    di_proposed         TEXT NOT NULL,
    brand_current       TEXT,
    brand_proposed      TEXT,
    recommendation_text TEXT NOT NULL,
    decision            TEXT CHECK(decision IN
                            ('APPROVE','CONDITIONAL','DO_NOT_SUBSTITUTE','')),
    condition_text      TEXT,
    generated_at        TEXT NOT NULL,
    approved_by         TEXT,
    approval_date       TEXT,
    FOREIGN KEY (di_current)  REFERENCES devices(di),
    FOREIGN KEY (di_proposed) REFERENCES devices(di)
);

-- ── Active Formulary ──────────────────────────────────────────────────────────
CREATE TABLE IF NOT EXISTS formulary (
    di                  TEXT PRIMARY KEY,
    brand_name          TEXT NOT NULL,
    company_name        TEXT,
    category            TEXT NOT NULL,
    product_code        TEXT,
    gmdn_code           TEXT,
    status              TEXT DEFAULT 'active'
                            CHECK(status IN ('active','under_review','removed')),
    added_date          TEXT NOT NULL,
    last_reviewed       TEXT,
    removal_date        TEXT,
    removal_reason      TEXT,
    notes               TEXT,
    gpo_contract_ref    TEXT,       -- reference only; no prices stored
    FOREIGN KEY (di) REFERENCES devices(di)
);

CREATE INDEX IF NOT EXISTS idx_formulary_category   ON formulary(category);
CREATE INDEX IF NOT EXISTS idx_formulary_status     ON formulary(status);

-- ── Alerts ────────────────────────────────────────────────────────────────────
CREATE TABLE IF NOT EXISTS alerts (
    alert_id            TEXT PRIMARY KEY,
    device_di           TEXT NOT NULL,
    brand_name          TEXT,
    category            TEXT,
    alert_type          TEXT NOT NULL
                            CHECK(alert_type IN ('recall','maude_spike','distribution_ended','other')),
    severity            TEXT NOT NULL
                            CHECK(severity IN ('CRITICAL','HIGH','MEDIUM','LOW')),
    description         TEXT NOT NULL,
    source_reference    TEXT,
    detected_date       TEXT NOT NULL,
    acknowledged        INTEGER DEFAULT 0 CHECK(acknowledged IN (0,1)),
    acknowledged_by     TEXT,
    acknowledged_date   TEXT,
    action_taken        TEXT,
    resolved            INTEGER DEFAULT 0 CHECK(resolved IN (0,1)),
    resolved_date       TEXT
);

CREATE INDEX IF NOT EXISTS idx_alerts_di            ON alerts(device_di);
CREATE INDEX IF NOT EXISTS idx_alerts_acknowledged  ON alerts(acknowledged);
CREATE INDEX IF NOT EXISTS idx_alerts_severity      ON alerts(severity);
CREATE INDEX IF NOT EXISTS idx_alerts_detected      ON alerts(detected_date DESC);

-- ── Category Watches ──────────────────────────────────────────────────────────
CREATE TABLE IF NOT EXISTS category_watches (
    watch_id                TEXT PRIMARY KEY,
    category                TEXT NOT NULL UNIQUE,
    product_codes           TEXT,       -- JSON array: ["FTL","FTM","OZO"]
    vendor_names            TEXT,       -- JSON array: ["Integra","Baxter"]
    alert_threshold_maude   INTEGER DEFAULT 5,
    active                  INTEGER DEFAULT 1 CHECK(active IN (0,1)),
    created_date            TEXT NOT NULL,
    last_run                TEXT
);

-- ── Emerging Technology ───────────────────────────────────────────────────────
CREATE TABLE IF NOT EXISTS emerging_tech (
    tech_id             TEXT PRIMARY KEY,
    technology_name     TEXT NOT NULL,
    category            TEXT,
    brief_markdown      TEXT NOT NULL,
    regulatory_status   TEXT,       -- cleared/investigational/pipeline/not_fda
    readiness_level     TEXT CHECK(readiness_level IN ('monitor','evaluate','defer','')),
    generated_at        TEXT NOT NULL,
    follow_up_date      TEXT
);

-- ── GMDN Bulk Index (separate file: gmdn_index.db) ───────────────────────────
-- Built from ACCESSGUDID full release bulk download
-- CREATE TABLE IF NOT EXISTS gmdn_device_index (
--     di                              TEXT NOT NULL,
--     gmdn_pt_code                    TEXT NOT NULL,
--     gmdn_pt_name                    TEXT NOT NULL,
--     brand_name                      TEXT,
--     company_name                    TEXT,
--     primary_product_code            TEXT,
--     device_class                    TEXT,
--     single_use                      INTEGER,
--     device_sterile                  INTEGER,
--     mri_safety_status               TEXT,
--     commercial_distribution_status  TEXT,
--     PRIMARY KEY (di, gmdn_pt_code)
-- );
-- CREATE INDEX IF NOT EXISTS idx_gmdn_by_code ON gmdn_device_index(gmdn_pt_code);
-- CREATE INDEX IF NOT EXISTS idx_gmdn_by_name ON gmdn_device_index(gmdn_pt_name);
```

### 3.3 The CLI Interface

```python
# medops/cli.py
"""
MedOps Command-Line Interface
Direct query interface for the knowledge base and pipeline triggers.

Usage:
  python medops/cli.py brief --di "00843197107103"
  python medops/cli.py brief --di "00843197107103" --format pdf
  python medops/cli.py matrix --category hemostatics
  python medops/cli.py substitution --a "DI_A" --b "DI_B"
  python medops/cli.py alerts --active
  python medops/cli.py alerts --ack ALERT-ID
  python medops/cli.py search "biologic tissue spine"
  python medops/cli.py formulary --list
  python medops/cli.py formulary --add DI --category hemostatics
  python medops/cli.py formulary --remove DI --reason "recalled"
  python medops/cli.py digest --run
  python medops/cli.py db --init
"""

import argparse
import json
import sys
from datetime import datetime


def cmd_brief(args):
    """Generate or retrieve a device brief."""
    if args.di:
        from medops.pipeline import run_device_brief
        run_device_brief(args.di, output_format=args.format or "markdown")
    elif args.id:
        from medops.knowledge_base import get_brief_by_id
        brief = get_brief_by_id(args.id)
        if brief:
            print(brief.get("brief_markdown", ""))
        else:
            print(f"Brief not found: {args.id}")
    else:
        print("ERROR: --di or --id required")
        sys.exit(1)


def cmd_matrix(args):
    """Run or retrieve a competitive matrix."""
    if args.run or args.category:
        from medops.pipeline import run_competitive_matrix
        devices = args.devices.split(",") if args.devices else None
        run_competitive_matrix(args.category, device_list=devices)
    else:
        print("ERROR: --category required")
        sys.exit(1)


def cmd_substitution(args):
    """Run a substitution analysis."""
    if not args.a or not args.b:
        print("ERROR: --a and --b required")
        sys.exit(1)
    from medops.pipeline import run_substitution_analysis
    run_substitution_analysis(args.a, args.b)


def cmd_alerts(args):
    """View or manage alerts."""
    from medops.knowledge_base import _db_connection

    if args.active:
        with _db_connection() as conn:
            rows = conn.execute("""
                SELECT alert_id, device_di, brand_name, alert_type, severity,
                       description, detected_date, acknowledged
                FROM alerts
                WHERE resolved = 0
                ORDER BY
                    CASE severity
                        WHEN 'CRITICAL' THEN 1
                        WHEN 'HIGH' THEN 2
                        WHEN 'MEDIUM' THEN 3
                        WHEN 'LOW' THEN 4
                    END,
                    detected_date DESC
            """).fetchall()
        if not rows:
            print("No active alerts.")
        else:
            print(f"\nActive Alerts ({len(rows)}):")
            print("-" * 70)
            for r in rows:
                ack = "✓ Acked" if r["acknowledged"] else "⚠ Unacked"
                print(f"[{r['severity']}] {r['alert_id']} | {r['brand_name']} | {r['alert_type']}")
                print(f"  {r['description'][:100]}...")
                print(f"  Detected: {r['detected_date'][:10]} | {ack}")
                print()

    elif args.ack:
        with _db_connection() as conn:
            conn.execute("""
                UPDATE alerts SET acknowledged = 1,
                acknowledged_by = 'cli', acknowledged_date = ?
                WHERE alert_id = ?
            """, (datetime.utcnow().isoformat(), args.ack))
        print(f"Alert {args.ack} acknowledged.")

    elif args.resolve:
        action = input("Describe action taken: ")
        with _db_connection() as conn:
            conn.execute("""
                UPDATE alerts SET resolved = 1, resolved_date = ?, action_taken = ?
                WHERE alert_id = ?
            """, (datetime.utcnow().isoformat(), action, args.resolve))
        print(f"Alert {args.resolve} resolved.")

    elif args.run_check:
        from medops.pipeline import run_recall_alert_check
        run_recall_alert_check(alert_channel=args.channel or "console")


def cmd_search(args):
    """Search the knowledge base."""
    if not args.query:
        print("ERROR: search query required")
        sys.exit(1)
    from medops.knowledge_base import search_briefs
    results = search_briefs(args.query, category=args.category)
    if not results:
        print(f"No results for: {args.query}")
    else:
        print(f"\n{len(results)} result(s) for '{args.query}':")
        print("-" * 60)
        for r in results:
            print(f"  {r['case_id']} | {r['brand_name']} ({r['company_name']})")
            print(f"    Category: {r['category']} | Rec: {r['recommendation']}")
            print(f"    Generated: {r['generated_at'][:10]} | File: {r['output_file_path']}")
            print()


def cmd_formulary(args):
    """Manage the active formulary."""
    from medops.knowledge_base import (
        get_formulary_devices, add_to_formulary, remove_from_formulary
    )

    if args.list:
        devices = get_formulary_devices()
        if not devices:
            print("Formulary is empty.")
        else:
            print(f"\nActive Formulary ({len(devices)} devices):\n")
            current_cat = None
            for d in devices:
                if d["category"] != current_cat:
                    current_cat = d["category"]
                    print(f"\n  [{current_cat.upper()}]")
                print(f"    {d['di'][:20]} | {d['brand_name']} — {d['company_name']}")
                if d.get("gpo_contract_ref"):
                    print(f"      GPO: {d['gpo_contract_ref']}")

    elif args.add:
        if not args.category:
            print("ERROR: --category required with --add")
            sys.exit(1)
        add_to_formulary(
            args.add, args.category,
            notes=args.notes or "",
            gpo_contract_ref=args.gpo or ""
        )
        print(f"Added {args.add} to formulary in category: {args.category}")

    elif args.remove:
        if not args.reason:
            args.reason = input("Removal reason: ")
        remove_from_formulary(args.remove, args.reason)
        print(f"Removed {args.remove} from formulary.")


def cmd_digest(args):
    """Run or view digests."""
    if args.run:
        from medops.pipeline import run_scheduled_digest
        run_scheduled_digest(
            categories=args.categories.split(",") if args.categories else None,
            delivery_channel=args.channel or "file"
        )


def cmd_db(args):
    """Database management commands."""
    if args.init:
        from medops.knowledge_base import initialize_database
        initialize_database()
        print("Database initialized.")
    elif args.gmdn_build:
        from medops.substitution import build_gmdn_index
        build_gmdn_index()


def main():
    parser = argparse.ArgumentParser(
        prog="medops",
        description="MedOps Intelligence OS — CLI Interface (MS-0002)"
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    # brief
    p_brief = subparsers.add_parser("brief", help="Device brief commands")
    p_brief.add_argument("--di", help="Device Identifier")
    p_brief.add_argument("--id", help="Retrieve existing brief by case ID")
    p_brief.add_argument("--format", choices=["markdown", "json", "pdf"], default="markdown")
    p_brief.set_defaults(func=cmd_brief)

    # matrix
    p_matrix = subparsers.add_parser("matrix", help="Competitive matrix commands")
    p_matrix.add_argument("--category", required=True, help="Device category")
    p_matrix.add_argument("--devices", help="Comma-separated DI list (optional)")
    p_matrix.add_argument("--run", action="store_true")
    p_matrix.set_defaults(func=cmd_matrix)

    # substitution
    p_sub = subparsers.add_parser("substitution", help="Substitution analysis")
    p_sub.add_argument("--a", required=True, help="Current device DI")
    p_sub.add_argument("--b", required=True, help="Proposed substitute DI")
    p_sub.set_defaults(func=cmd_substitution)

    # alerts
    p_alert = subparsers.add_parser("alerts", help="Alert management")
    p_alert.add_argument("--active", action="store_true", help="List active alerts")
    p_alert.add_argument("--ack", metavar="ALERT_ID", help="Acknowledge an alert")
    p_alert.add_argument("--resolve", metavar="ALERT_ID", help="Resolve an alert")
    p_alert.add_argument("--run-check", action="store_true", help="Run alert check now")
    p_alert.add_argument("--channel", default="console")
    p_alert.set_defaults(func=cmd_alerts)

    # search
    p_search = subparsers.add_parser("search", help="Search knowledge base")
    p_search.add_argument("query", help="Search terms")
    p_search.add_argument("--category", help="Filter by category")
    p_search.set_defaults(func=cmd_search)

    # formulary
    p_form = subparsers.add_parser("formulary", help="Formulary management")
    p_form.add_argument("--list", action="store_true")
    p_form.add_argument("--add", metavar="DI")
    p_form.add_argument("--remove", metavar="DI")
    p_form.add_argument("--category")
    p_form.add_argument("--reason")
    p_form.add_argument("--notes")
    p_form.add_argument("--gpo", help="GPO contract reference")
    p_form.set_defaults(func=cmd_formulary)

    # digest
    p_digest = subparsers.add_parser("digest", help="Weekly digest")
    p_digest.add_argument("--run", action="store_true")
    p_digest.add_argument("--categories", help="Comma-separated category filter")
    p_digest.add_argument("--channel", default="file")
    p_digest.set_defaults(func=cmd_digest)

    # db
    p_db = subparsers.add_parser("db", help="Database management")
    p_db.add_argument("--init", action="store_true", help="Initialize database schema")
    p_db.add_argument("--gmdn-build", action="store_true", help="Build GMDN bulk index")
    p_db.set_defaults(func=cmd_db)

    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
```

---

## Section 4: The Scheduled Intelligence Digest

### 4.1 The Weekly Category Digest

The digest is modeled on a well-edited intelligence brief — scannable, action-oriented, no raw data dumps. John should be able to read it in under 10 minutes and know exactly what requires action, what to monitor, and what's noise.

Hermes generates and delivers it every Monday at 08:00 CST — after the recall check (07:00) and before the workday starts.

### 4.2 Category Watch Configuration (`watch_config.yaml`)

This file lives at `/app/data/watch_config.yaml` on the Thought Reliquary. Edit it directly to add or remove categories, vendors, product codes, and alert thresholds.

```yaml
# MedOps Category Watch Configuration
# Document: MS-0002 | File: /app/data/watch_config.yaml
# Edit to add/remove categories, vendors, product codes, MAUDE thresholds
# Product codes: 3-letter FDA classification codes from device/classification.json

category_watches:

  - category: hemostatics
    vendors:
      - Integra LifeSciences
      - Baxter Healthcare
      - Ethicon
      - BD
    product_codes:
      - FTL   # Hemostat, Absorbable, Foam
      - FTM   # Hemostat, Topical (Thrombin)
      - OZO   # Oxidized Regenerated Cellulose (SURGICEL family)
      - FRZ   # Gelatin sponge hemostatic
    alert_threshold_maude: 5
    notes: "Monitor FLOSEAL vs. SURGIFLO cost parity. SURGICEL supply disruptions Q1."

  - category: endo_mechanicals
    vendors:
      - Medtronic
      - Ethicon
      - Applied Medical
      - B. Braun Aesculap
    product_codes:
      - KZE   # Staple, Surgical, Absorbable
      - MQP   # Trocar, Laparoscopic
      - FRB   # Staple, Surgical, Non-Absorbable
      - IYO   # Clip, Ligating
    alert_threshold_maude: 8
    notes: "GST powered stapler evaluation active. Monitor Medtronic Signia competitive data."

  - category: sutures
    vendors:
      - Ethicon
      - Medtronic Covidien
      - B. Braun
      - Teleflex
    product_codes:
      - GAK   # Suture, Absorbable
      - GAL   # Suture, Nonabsorbable
      - GEI   # Suture, Barbed (knotless)
    alert_threshold_maude: 3
    notes: "Antibiotic-coated suture (VICRYL Plus) evidence review ongoing. GPO contract renewal Q3."

  - category: total_joints
    vendors:
      - Zimmer Biomet
      - Stryker
      - DePuy Synthes
      - Smith+Nephew
    product_codes:
      - HRS   # Hip, Femoral, Total
      - KWQ   # Knee, Total
      - KWR   # Knee, Revision
      - KRT   # Hip, Acetabular
    alert_threshold_maude: 3
    notes: "AJRR annual data Q2 expected. Mako vs. ROSA robotic program evaluation H2."

  - category: spine_implants
    vendors:
      - Medtronic
      - Stryker
      - DePuy Synthes
      - NuVasive
      - Globus Medical
    product_codes:
      - KYD   # Intervertebral Fusion Device (TLIF/PLIF)
      - MUY   # Spine, Intervertebral Cage
      - KWQ   # Pedicle Screw System
      - LQJ   # Vertebral Body Replacement
    alert_threshold_maude: 3
    notes: "Globus+NuVasive merger — contract renegotiation window open. ExcelsiusGPS evaluation pending."

  - category: wound_biologics
    vendors:
      - Integra LifeSciences
      - MiMedx
      - Organogenesis
      - Avita Medical
      - Smith+Nephew
    product_codes:
      - MRY   # Skin Substitute (dermal regeneration)
      - OZO   # Wound care biological
      - KZJ   # Burn wound dressing
    alert_threshold_maude: 3
    notes: "HCT/P products (MiMedx, EpiFix) tracked separately — verify AATB accreditation annually."

  - category: allografts_biologics
    vendors:
      - MiMedx
      - Artivion
      - Organogenesis
      - Osiris Therapeutics
      - RTI Surgical
    product_codes:
      - OZP   # Allograft, orthopedic soft tissue
      - MRY   # Acellular dermal matrix
    alert_threshold_maude: 2
    notes: "21 CFR 1271 — not device pathway. AATB accreditation verification required. FDA registration check annual."

  - category: breast_implants
    vendors:
      - Allergan (AbbVie)
      - Mentor (J&J)
      - Sientra
    product_codes:
      - QDD   # Breast Implant, Silicone Gel (Class III, PMA)
      - QDE   # Breast Implant, Saline
      - MRK   # Tissue Expander
    alert_threshold_maude: 2
    notes: "All Class III/PMA. BIA-ALCL monitoring — MAUDE spikes warrant immediate review. Boxed warning 2021."

  - category: ophthalmic_devices
    vendors:
      - Alcon
      - Johnson & Johnson Vision
      - Bausch + Lomb
      - Glaukos
    product_codes:
      - HQL   # Intraocular Lens
      - HQM   # Phacoemulsification System disposables
      - QSO   # MIGS (minimally invasive glaucoma)
    alert_threshold_maude: 5
    notes: "Phaco system capital replacement planning FY27. IOL cartridge compatibility critical."

  - category: surgical_robotics
    vendors:
      - Intuitive Surgical
      - Stryker (Mako)
      - Zimmer Biomet (ROSA)
      - Globus Medical (ExcelsiusGPS)
      - DePuy Synthes (VELYS)
    product_codes:
      - OZO   # Robotic surgery system
      - GZB   # Robotic surgical instruments
    alert_threshold_maude: 5
    notes: "da Vinci 5 availability timeline monitoring. Mako install base MAUDE normalization needed."

  - category: xenografts_synthetic
    vendors:
      - Integra LifeSciences
      - LifeNet Health
      - RTI Surgical (Enovis)
    product_codes:
      - MRY   # Acellular dermal matrix / xenograft
      - OZK   # Collagen matrix device
    alert_threshold_maude: 3
    notes: "SurgiMend/PriMatrix fetal bovine collagen. GPO contract ADM pricing high-leverage category."
```

---

## Section 5: ACCESSGUDID Substitution Cross-Reference Engine

### 5.1 The Technical Architecture

GMDN codes are the spine of the substitution algorithm. Devices sharing a GMDN Preferred Term Name have "substantially similar generic features" — this is the regulatory foundation for formulary substitution analysis.

**The core constraint:** ACCESSGUDID v2 API provides forward lookup (DI → GMDN) but not reverse lookup (GMDN → all DIs). Direct GMDN reverse search is available via the OpenFDA UDI mirror for subsets, but the complete, reliable path uses a local index built from the ACCESSGUDID full bulk download.

### 5.2 Complete `substitution.py` Module

```python
# medops/substitution.py
"""
ACCESSGUDID Substitution Cross-Reference Engine
Uses GMDN codes as the clinical equivalence spine.

The substitution algorithm:
  Step 1: Get Device A GMDN term from ACCESSGUDID
  Step 2: Search local GMDN index for all devices with same GMDN code
  Step 3: Filter by device class, single-use, sterility, distribution status
  Step 4: For each candidate: run OpenFDA recall + MAUDE check
  Step 5: Score each candidate on safety/regulatory equivalence
  Step 6: Return ranked SubstitutionCandidate list

GMDN Index: Built from ACCESSGUDID full bulk download (see build_gmdn_index()).
            Stored at /app/data/gmdn_index.db — separate from main medops.db.
            Rebuild monthly after new full release.
"""

import io
import csv
import logging
import sqlite3
import requests
import zipfile
import xml.etree.ElementTree as ET
from dataclasses import dataclass, field
from pathlib import Path
from typing import Optional
from medops.config import (
    GMDN_INDEX_PATH, GUDID_BULK_PATH, ACCESSGUDID_BULK_RSS,
    OPENFDA_DELAY_WITH_KEY, OPENFDA_API_KEY,
)

logger = logging.getLogger(__name__)


@dataclass
class SubstitutionCandidate:
    di: str
    brand_name: str
    company_name: str
    catalog_number: str
    version_model_number: str
    gmdn_pt_name: str
    gmdn_pt_code: str
    primary_product_code: str
    device_class: str
    single_use: bool
    device_sterile: bool
    mri_safety_status: str
    commercial_distribution_status: str
    # Scoring fields
    score: float = 0.0
    active_recalls: int = 0
    maude_recent_count: int = 0
    gmdn_match: bool = True
    product_code_match: bool = False
    device_class_match: bool = False
    single_use_match: bool = False
    sterile_match: bool = False
    disqualified: bool = False
    disqualification_reason: str = ""
    # Source
    source: str = "gmdn_index"     # gmdn_index | openfda_udi_api


def _get_gmdn_index_connection() -> sqlite3.Connection:
    conn = sqlite3.connect(str(GMDN_INDEX_PATH))
    conn.row_factory = sqlite3.Row
    return conn


def _init_gmdn_index_schema(conn: sqlite3.Connection):
    conn.executescript("""
        CREATE TABLE IF NOT EXISTS gmdn_device_index (
            di                              TEXT NOT NULL,
            gmdn_pt_code                    TEXT NOT NULL,
            gmdn_pt_name                    TEXT NOT NULL,
            brand_name                      TEXT,
            company_name                    TEXT,
            catalog_number                  TEXT,
            version_model_number            TEXT,
            primary_product_code            TEXT,
            device_class                    TEXT,
            single_use                      INTEGER,
            device_sterile                  INTEGER,
            mri_safety_status               TEXT,
            commercial_distribution_status  TEXT,
            PRIMARY KEY (di, gmdn_pt_code)
        );
        CREATE INDEX IF NOT EXISTS idx_gmdn_code ON gmdn_device_index(gmdn_pt_code);
        CREATE INDEX IF NOT EXISTS idx_gmdn_name ON gmdn_device_index(gmdn_pt_name);
        CREATE INDEX IF NOT EXISTS idx_gmdn_company ON gmdn_device_index(company_name);
        CREATE INDEX IF NOT EXISTS idx_gmdn_product_code ON gmdn_device_index(primary_product_code);
        CREATE INDEX IF NOT EXISTS idx_gmdn_distribution ON gmdn_device_index(commercial_distribution_status);
    """)
    conn.commit()


def _get_latest_full_release_url() -> str:
    """Parse the ACCESSGUDID RSS feed to get the latest full release ZIP URL."""
    resp = requests.get(ACCESSGUDID_BULK_RSS, timeout=30)
    resp.raise_for_status()
    root = ET.fromstring(resp.text)
    # RSS items — find first item with 'full' in the link
    for item in root.findall(".//item"):
        link = item.findtext("link", "")
        if "full" in link.lower() and link.endswith(".zip"):
            return link
    # Fallback pattern if RSS structure differs
    for item in root.findall(".//{*}item"):
        for child in item:
            if "enclosure" in child.tag.lower():
                url = child.get("url", "")
                if url and "full" in url.lower():
                    return url
    raise RuntimeError("Could not parse latest full release URL from ACCESSGUDID RSS")


def build_gmdn_index(
    bulk_zip_url: str = None,
    force_rebuild: bool = False,
) -> int:
    """
    Build the local GMDN device index from the ACCESSGUDID full release bulk download.

    This is the foundation for the reverse GMDN lookup used in substitution analysis.
    The bulk download contains pipe-delimited CSV files including a GMDN terms file.

    ACCESSGUDID full release format (pipe-delimited CSVs):
      - device.txt           — core device fields
      - identifier.txt       — DI identifiers
      - productcode.txt      — product codes per device
      - device_gmdn.txt      — GMDN terms per device (this is the key file)
      - sterilization.txt    — sterilization data

    Rebuild schedule: monthly, after the 1st-of-month full release.
    Estimated time: 15–45 minutes on first run (5M+ records).
    Estimated storage: ~2–4 GB SQLite file.

    Returns: count of records indexed.
    """
    if not force_rebuild and GMDN_INDEX_PATH.exists():
        conn = _get_gmdn_index_connection()
        count = conn.execute("SELECT COUNT(*) FROM gmdn_device_index").fetchone()[0]
        conn.close()
        if count > 0:
            logger.info(f"GMDN index already exists with {count} records. Use force_rebuild=True to rebuild.")
            return count

    # Get download URL
    if not bulk_zip_url:
        logger.info("Fetching latest ACCESSGUDID full release URL from RSS...")
        bulk_zip_url = _get_latest_full_release_url()

    logger.info(f"Downloading ACCESSGUDID full release: {bulk_zip_url}")
    logger.info("This will take 10–30 minutes depending on network speed.")

    # Stream download (file is ~500MB–1GB compressed)
    zip_path = GUDID_BULK_PATH / "gudid_full_release.zip"
    with requests.get(bulk_zip_url, stream=True, timeout=300) as resp:
        resp.raise_for_status()
        total_size = int(resp.headers.get("content-length", 0))
        downloaded = 0
        with open(zip_path, "wb") as f:
            for chunk in resp.iter_content(chunk_size=1024 * 1024):  # 1MB chunks
                f.write(chunk)
                downloaded += len(chunk)
                if total_size:
                    pct = (downloaded / total_size) * 100
                    print(f"\r  Download progress: {pct:.1f}%", end="", flush=True)
    print()
    logger.info(f"Download complete: {zip_path} ({zip_path.stat().st_size / 1e9:.2f} GB)")

    # Initialize index database
    conn = _get_gmdn_index_connection()
    _init_gmdn_index_schema(conn)

    # Parse the bulk ZIP
    logger.info("Parsing bulk download and building GMDN index...")
    records_loaded = 0

    with zipfile.ZipFile(str(zip_path)) as z:
        filenames = z.namelist()
        logger.info(f"ZIP contains {len(filenames)} files: {filenames[:10]}...")

        # Load core device data first
        device_data = {}
        device_file = next(
            (f for f in filenames if f.lower().endswith("device.txt") and "gmdn" not in f.lower()),
            None
        )
        if device_file:
            logger.info(f"Loading device data from: {device_file}")
            with z.open(device_file) as f:
                reader = csv.DictReader(
                    io.TextIOWrapper(f, encoding="utf-8", errors="replace"),
                    delimiter="|",
                )
                for row in reader:
                    di = row.get("primaryDI", "").strip()
                    if di:
                        device_data[di] = {
                            "brand_name": row.get("brandName", "").strip(),
                            "company_name": row.get("companyName", "").strip(),
                            "catalog_number": row.get("catalogNumber", "").strip(),
                            "version_model": row.get("versionModelNumber", "").strip(),
                            "single_use": 1 if row.get("singleUse", "").lower() in ("true", "yes", "y", "1") else 0,
                            "device_sterile": 1 if row.get("deviceSterile", "").lower() in ("true", "yes", "y", "1") else 0,
                            "mri_safety": row.get("MRISafetyStatus", "").strip(),
                            "distribution_status": row.get("deviceCommDistributionStatus", "").strip(),
                        }
            logger.info(f"Loaded {len(device_data)} device records")

        # Load product codes
        product_codes = {}
        pc_file = next((f for f in filenames if "productcode" in f.lower()), None)
        if pc_file:
            logger.info(f"Loading product codes from: {pc_file}")
            with z.open(pc_file) as f:
                reader = csv.DictReader(
                    io.TextIOWrapper(f, encoding="utf-8", errors="replace"),
                    delimiter="|",
                )
                for row in reader:
                    di = row.get("primaryDI", "").strip()
                    if di and di not in product_codes:  # take first product code
                        product_codes[di] = {
                            "product_code": row.get("productCode", "").strip(),
                            "device_class": row.get("deviceClass", "").strip(),
                        }

        # Load GMDN terms (the key file for substitution)
        gmdn_file = next(
            (f for f in filenames if "gmdn" in f.lower() and f.lower().endswith(".txt")),
            None
        )
        if gmdn_file:
            logger.info(f"Loading GMDN data from: {gmdn_file}")
            batch = []
            BATCH_SIZE = 10000

            with z.open(gmdn_file) as f:
                reader = csv.DictReader(
                    io.TextIOWrapper(f, encoding="utf-8", errors="replace"),
                    delimiter="|",
                )
                for row in reader:
                    di = row.get("primaryDI", "").strip()
                    gmdn_code = row.get("gmdnPTCode", "").strip()
                    gmdn_name = row.get("gmdnPTName", "").strip()

                    if not di or not gmdn_code:
                        continue

                    dev = device_data.get(di, {})
                    pc = product_codes.get(di, {})

                    batch.append((
                        di, gmdn_code, gmdn_name,
                        dev.get("brand_name", ""),
                        dev.get("company_name", ""),
                        dev.get("catalog_number", ""),
                        dev.get("version_model", ""),
                        pc.get("product_code", ""),
                        pc.get("device_class", ""),
                        dev.get("single_use", 0),
                        dev.get("device_sterile", 0),
                        dev.get("mri_safety", ""),
                        dev.get("distribution_status", ""),
                    ))

                    if len(batch) >= BATCH_SIZE:
                        conn.executemany("""
                            INSERT OR REPLACE INTO gmdn_device_index VALUES
                            (?,?,?,?,?,?,?,?,?,?,?,?,?)
                        """, batch)
                        conn.commit()
                        records_loaded += len(batch)
                        print(f"\r  Indexed {records_loaded:,} GMDN records...", end="", flush=True)
                        batch = []

                # Final batch
                if batch:
                    conn.executemany("""
                        INSERT OR REPLACE INTO gmdn_device_index VALUES
                        (?,?,?,?,?,?,?,?,?,?,?,?,?)
                    """, batch)
                    conn.commit()
                    records_loaded += len(batch)

        else:
            logger.error("GMDN file not found in bulk ZIP. Cannot build GMDN index.")

    conn.close()
    print()
    logger.info(f"GMDN index built: {records_loaded:,} records → {GMDN_INDEX_PATH}")
    return records_loaded


def _lookup_by_gmdn_code(
    gmdn_code: str,
    exclude_di: str,
    device_class: str = "",
    single_use: bool = None,
    device_sterile: bool = None,
) -> list[sqlite3.Row]:
    """Query the local GMDN index for all devices with a given GMDN code."""
    if not GMDN_INDEX_PATH.exists():
        raise FileNotFoundError(
            f"GMDN index not found at {GMDN_INDEX_PATH}. "
            "Run: python medops/cli.py db --gmdn-build"
        )

    conn = _get_gmdn_index_connection()
    query_parts = ["gmdn_pt_code = ?", "di != ?", "commercial_distribution_status = 'In Commercial Distribution'"]
    params = [gmdn_code, exclude_di]

    if device_class:
        query_parts.append("device_class = ?")
        params.append(device_class)
    if single_use is not None:
        query_parts.append("single_use = ?")
        params.append(int(single_use))
    if device_sterile is not None:
        query_parts.append("device_sterile = ?")
        params.append(int(device_sterile))

    where = " AND ".join(query_parts)
    rows = conn.execute(
        f"SELECT * FROM gmdn_device_index WHERE {where} LIMIT 200",
        params,
    ).fetchall()
    conn.close()
    return rows


def _score_candidate(
    candidate: SubstitutionCandidate,
    reference_device: dict,
) -> float:
    """
    Score a substitution candidate relative to the reference device.

    Scoring dimensions (total 100 points):
    - Device class match:     25 pts
    - Product code match:     20 pts
    - Single-use match:       15 pts
    - Sterile match:          15 pts
    - No active recalls:      15 pts
    - Low MAUDE volume:        5 pts
    - In commercial distrib:   5 pts

    Penalties:
    - Any active Class I recall: -50 (forces to bottom of ranking)
    - Active Class II recall:    -25
    - High MAUDE spike:          -10
    """
    score = 0.0

    # Device class match
    if candidate.device_class == reference_device.get("device_class", ""):
        score += 25
        candidate.device_class_match = True

    # Product code match (same regulatory category)
    if candidate.primary_product_code == reference_device.get("primary_product_code", ""):
        score += 20
        candidate.product_code_match = True

    # Single-use match
    ref_single_use = bool(reference_device.get("single_use", False))
    if candidate.single_use == ref_single_use:
        score += 15
        candidate.single_use_match = True

    # Sterility match
    ref_sterile = bool(reference_device.get("device_sterile", False))
    if candidate.device_sterile == ref_sterile:
        score += 15
        candidate.sterile_match = True

    # Safety record
    if candidate.active_recalls == 0:
        score += 15
    elif candidate.active_recalls >= 1:
        # Recall type penalties applied in find_substitutes after scoring
        pass

    # MAUDE volume (low = good; this is a relative signal)
    if candidate.maude_recent_count == 0:
        score += 5
    elif candidate.maude_recent_count <= 3:
        score += 2

    # Distribution status (already filtered, but confirm)
    if candidate.commercial_distribution_status == "In Commercial Distribution":
        score += 5

    return score


def find_substitutes(di: str) -> list[SubstitutionCandidate]:
    """
    Find ranked substitution candidates for a given Device Identifier.

    Algorithm:
      1. Look up reference device in ACCESSGUDID
      2. Get GMDN code and device class for filtering
      3. Query GMDN index for all devices sharing the GMDN code
         (filtered: same device class, same single-use, same sterility, in distribution)
      4. For each candidate: check OpenFDA recalls and MAUDE event volume
      5. Score and rank candidates
      6. Return sorted list (highest score first)

    Falls back to OpenFDA UDI API if local GMDN index is not available.
    """
    from medops.accessgudid import get_device_by_di
    from medops.openfda import (
        check_di_for_active_recalls,
        get_maude_event_volume,
    )

    logger.info(f"find_substitutes: {di}")

    # Step 1: Get reference device
    reference = get_device_by_di(di)
    if not reference:
        raise ValueError(f"Device {di} not found in ACCESSGUDID")

    gmdn_code = reference.get("primary_gmdn_code", "")
    gmdn_name = reference.get("primary_gmdn_name", "")
    device_class = reference.get("device_class", "")
    single_use = bool(reference.get("single_use", False))
    device_sterile = bool(reference.get("device_sterile", False))

    if not gmdn_code and not gmdn_name:
        logger.warning(f"No GMDN code found for DI {di}. Substitution search limited.")

    # Step 2: Query GMDN index
    candidates = []
    index_available = GMDN_INDEX_PATH.exists()

    if index_available and gmdn_code:
        logger.info(f"Querying GMDN index for code: {gmdn_code}")
        rows = _lookup_by_gmdn_code(
            gmdn_code=gmdn_code,
            exclude_di=di,
            device_class=device_class,
            single_use=single_use,
            device_sterile=device_sterile,
        )
        for row in rows:
            candidates.append(SubstitutionCandidate(
                di=row["di"],
                brand_name=row["brand_name"] or "",
                company_name=row["company_name"] or "",
                catalog_number=row["catalog_number"] or "",
                version_model_number=row["version_model_number"] or "",
                gmdn_pt_name=row["gmdn_pt_name"] or "",
                product_code=row["primary_product_code"] or "",
                device_class=row["device_class"] or "",
                mri_safety_status=row["mri_safety_status"] or "",
                single_use=(row["single_use"] == 1),
                device_sterile=(row["device_sterile"] == 1),
                commercial_distribution_status=row["commercial_distribution_status"] or "",
            ))
    else:
        # Fallback: query OpenFDA UDI endpoint by GMDN name
        logger.info(f"GMDN index unavailable. Querying OpenFDA UDI by GMDN name: {gmdn_name}")
        from medops.openfda import _client as fda_client
        try:
            results = fda_client.query(
                "device/udi.json",
                {
                    "search": f'gmdn_terms.gmdn_pt_name:"{gmdn_name}"',
                    "limit": 100,
                }
            )
            for rec in results.get("results", []):
                if rec.get("di") == di:
                    continue
                if rec.get("device_comm_distribution_status") != "In Commercial Distribution":
                    continue
                gmdn_terms = rec.get("gmdn_terms", [{}])
                pt_name = gmdn_terms[0].get("gmdn_pt_name", "") if gmdn_terms else ""
                candidates.append(SubstitutionCandidate(
                    di=rec.get("di", ""),
                    brand_name=rec.get("brand_name", ""),
                    company_name=rec.get("company_name", ""),
                    catalog_number=rec.get("catalog_number", ""),
                    version_model_number=rec.get("version_or_model_number", ""),
                    gmdn_pt_name=pt_name,
                    product_code=rec.get("product_codes", [{}])[0].get("product_code", "") if rec.get("product_codes") else "",
                    device_class=rec.get("device_class", ""),
                    mri_safety_status=rec.get("mri_safety_status", ""),
                    single_use=bool(rec.get("single_use", False)),
                    device_sterile=bool(rec.get("sterilization", {}).get("device_sterile", False)),
                    commercial_distribution_status=rec.get("device_comm_distribution_status", ""),
                ))
        except Exception as exc:
            logger.error(f"OpenFDA UDI fallback failed: {exc}")

    if not candidates:
        logger.warning(f"No substitution candidates found for DI {di} (GMDN: {gmdn_name})")
        return []

    # Step 3: Enrich each candidate with recall and MAUDE data
    logger.info(f"Enriching {len(candidates)} candidates with recall/MAUDE data...")
    for cand in candidates:
        try:
            recall_result = check_di_for_active_recalls(cand.di, cand.company_name)
            cand.active_recalls = recall_result.get("active_count", 0)
            cand.recall_classes = recall_result.get("classes", [])
        except Exception as exc:
            logger.warning(f"Recall check failed for {cand.di}: {exc}")
            cand.active_recalls = -1  # Unknown

        try:
            maude_vol = get_maude_event_volume(cand.brand_name, days_back=90)
            cand.maude_recent_count = maude_vol
        except Exception as exc:
            logger.warning(f"MAUDE check failed for {cand.di}: {exc}")
            cand.maude_recent_count = -1  # Unknown

    # Step 4: Score all candidates
    for cand in candidates:
        cand.equivalence_score = _score_candidate(cand, reference)

    # Apply Class I recall penalty (forces to bottom)
    for cand in candidates:
        if "Class I" in cand.recall_classes:
            cand.equivalence_score -= 50
        elif "Class II" in cand.recall_classes:
            cand.equivalence_score -= 25
        if cand.maude_recent_count > 10:
            cand.equivalence_score -= 10

    # Step 5: Sort descending by score, filter score < 0 to tail
    candidates.sort(key=lambda c: c.equivalence_score, reverse=True)
    logger.info(f"find_substitutes: returning {len(candidates)} ranked candidates for DI {di}")
    return candidates


def format_substitution_report(
    reference_di: str,
    reference_device: dict,
    candidates: list[SubstitutionCandidate],
) -> dict:
    """
    Format the full substitution analysis report as a structured dict.
    Suitable for passing to synthesizer.py for Claude narrative generation.
    """
    return {
        "reference": {
            "di": reference_di,
            "brand_name": reference_device.get("brand_name", ""),
            "company_name": reference_device.get("company_name", ""),
            "gmdn_code": reference_device.get("primary_gmdn_code", ""),
            "gmdn_name": reference_device.get("primary_gmdn_name", ""),
            "device_class": reference_device.get("device_class", ""),
            "product_code": reference_device.get("primary_product_code", ""),
        },
        "candidates": [
            {
                "rank": idx + 1,
                "di": c.di,
                "brand_name": c.brand_name,
                "company_name": c.company_name,
                "catalog_number": c.catalog_number,
                "gmdn_pt_name": c.gmdn_pt_name,
                "product_code": c.product_code,
                "device_class": c.device_class,
                "device_class_match": c.device_class_match,
                "product_code_match": c.product_code_match,
                "single_use_match": c.single_use_match,
                "sterile_match": c.sterile_match,
                "mri_safety_status": c.mri_safety_status,
                "active_recalls": c.active_recalls,
                "recall_classes": c.recall_classes,
                "maude_recent_count": c.maude_recent_count,
                "equivalence_score": round(c.equivalence_score, 1),
                "commercial_distribution_status": c.commercial_distribution_status,
            }
            for idx, c in enumerate(candidates[:20])  # top 20
        ],
        "total_candidates_found": len(candidates),
        "generated_at": datetime.utcnow().isoformat() + "Z",
        "algorithm_version": "1.0",
        "notes": [
            "Score is a relative regulatory/safety equivalence indicator (0–100). It is NOT a clinical equivalence determination.",
            "Candidates with active Class I recalls are ranked last regardless of other scores.",
            "GMDN equivalence indicates substantially similar generic device type. Clinical evaluation required before any substitution.",
            "MAUDE event volume is a passive surveillance signal; normalize by market presence before drawing safety conclusions.",
        ],
    }
```

### 5.3 GMDN Index Limitations and Workarounds

The ACCESSGUDID v2 API does not support reverse GMDN lookup (i.e., "give me all devices with GMDN code X"). The API only supports forward lookup (DI → GMDN). The local GMDN index built by `build_gmdn_index()` is the workaround.

**Operational notes:**

| Issue | Workaround |
|---|---|
| GMDN code not present in v2 API response | Use `gmdnPTName` (text field) and query OpenFDA UDI endpoint as fallback |
| Bulk download ZIP is large (~1.5 GB) | Run `build_gmdn_index()` monthly on cron; index is ~200 MB SQLite |
| Manufacturer GMDN term assignment is voluntary — may choose different terms for similar devices | Search by both GMDN code and product code; Claude synthesis flags discrepancies |
| GMDN terms become obsolete but labelers don't always update | `build_gmdn_index()` tags `gmdn_code_status`; filter out `Obsolete` in scoring |
| 20.3% of records have no device description | Equivalence scoring uses structural fields only; narrative generation flags data gaps |
| Catalog number is Optional in GUDID (~15–25% missing) | Report missing catalog numbers as data gaps; do not block substitution analysis |

---

## Section 6: Docker Deployment on Thought Reliquary

### 6.1 Directory Structure

```
medops-os/
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── .env.example
├── medops/
│   ├── __init__.py
│   ├── config.py
│   ├── accessgudid.py
│   ├── openfda.py
│   ├── pubmed.py
│   ├── synthesizer.py
│   ├── formatter.py
│   ├── knowledge_base.py
│   ├── alerts.py
│   ├── pipeline.py
│   ├── substitution.py
│   ├── digest.py
│   ├── notion_sync.py
│   └── cli.py
├── data/
│   ├── medops.db          # Main knowledge base (SQLite)
│   ├── gmdn_index.db      # GMDN bulk index (SQLite)
│   └── exports/           # PDF/Markdown output staging
├── config/
│   ├── category_watches.yaml
│   └── hermes_tasks.yaml
└── logs/
    └── medops.log
```

### 6.2 Dockerfile

```dockerfile
FROM python:3.12-slim

# System dependencies
RUN apt-get update && apt-get install -y \
    curl \
    wget \
    unzip \
    sqlite3 \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Application code
COPY medops/ ./medops/
COPY config/ ./config/

# Data directory (mounted as volume at runtime)
RUN mkdir -p /app/data/exports /app/logs

# Non-root user for security
RUN useradd -m -u 1001 medops && chown -R medops:medops /app
USER medops

# Healthcheck: verify DB is accessible
HEALTHCHECK --interval=60s --timeout=10s --start-period=30s --retries=3 \
    CMD python -c "from medops.knowledge_base import get_db_connection; get_db_connection().close(); print('ok')" || exit 1

CMD ["python", "medops/pipeline.py", "--mode", "daemon"]
```

### 6.3 docker-compose.yml

```yaml
version: '3.8'

services:
  medops:
    build: .
    container_name: medops-core
    volumes:
      - ./data:/app/data
      - ./logs:/app/logs
      - ./config:/app/config:ro
    environment:
      - OPENFDA_API_KEY=${OPENFDA_API_KEY}
      - ANTHROPIC_API_KEY=${ANTHROPIC_API_KEY}
      - PUBMED_API_KEY=${PUBMED_API_KEY}
      - NOTION_API_TOKEN=${NOTION_API_TOKEN}
      - NOTION_DEVICE_REGISTRY_DB=${NOTION_DEVICE_REGISTRY_DB}
      - NOTION_EVAL_QUEUE_DB=${NOTION_EVAL_QUEUE_DB}
      - NOTION_MATRICES_DB=${NOTION_MATRICES_DB}
      - NOTION_ALERTS_LOG_DB=${NOTION_ALERTS_LOG_DB}
      - SMTP_HOST=${SMTP_HOST}
      - SMTP_PORT=${SMTP_PORT}
      - SMTP_USER=${SMTP_USER}
      - SMTP_PASSWORD=${SMTP_PASSWORD}
      - ALERT_EMAIL_TO=${ALERT_EMAIL_TO}
      - LOG_LEVEL=${LOG_LEVEL:-INFO}
      - DATA_DIR=/app/data
      - CLAUDE_MODEL=${CLAUDE_MODEL:-claude-sonnet-4-5}
    restart: unless-stopped
    networks:
      - medops-net
    logging:
      driver: json-file
      options:
        max-size: "10m"
        max-file: "5"

  # Lightweight web UI for querying the knowledge base
  medops-ui:
    image: python:3.12-slim
    container_name: medops-ui
    working_dir: /app
    volumes:
      - ./data:/app/data:ro
      - ./medops:/app/medops:ro
    environment:
      - DATA_DIR=/app/data
    ports:
      - "7860:7860"      # Gradio default
    command: >
      sh -c "pip install gradio --quiet && python medops/ui.py"
    depends_on:
      - medops
    restart: unless-stopped
    networks:
      - medops-net

networks:
  medops-net:
    driver: bridge

volumes:
  medops-data:
    driver: local
```

### 6.4 requirements.txt

```
# HTTP clients
requests==2.32.3
httpx==0.27.2
aiohttp==3.10.5

# Rate limiting
ratelimit==2.2.1

# Data processing
pandas==2.2.2
numpy==2.0.1
pydantic==2.8.2

# Claude / Anthropic API
anthropic==0.34.2

# LangChain (optional, for RAG extension)
langchain==0.3.1
langchain-anthropic==0.2.1

# Local database
# sqlite3 is built-in Python — no install needed

# Notion API
notion-client==2.2.1

# Email
# smtplib is built-in Python

# YAML configuration
pyyaml==6.0.2

# Progress tracking
tqdm==4.66.5

# Scheduling (daemon mode)
schedule==1.2.2

# CLI
# argparse is built-in Python

# XML parsing (GUDID bulk download)
# xml.etree is built-in Python

# Markdown/PDF output
markdown==3.7
weasyprint==62.3

# Optional: Gradio web UI
gradio==4.44.0

# Logging
# logging is built-in Python

# Date handling
python-dateutil==2.9.0.post0

# Caching
cachetools==5.5.0

# Testing
pytest==8.3.3
pytest-asyncio==0.24.0
responses==0.25.3    # mock HTTP for tests
```

### 6.5 .env.example

```bash
# OpenFDA API (free key from https://open.fda.gov/apis/authentication/)
OPENFDA_API_KEY=your_openfda_key_here

# Anthropic Claude API
ANTHROPIC_API_KEY=sk-ant-your-key-here
CLAUDE_MODEL=claude-sonnet-4-5

# PubMed E-utilities (free; higher rate limit with key)
PUBMED_API_KEY=your_pubmed_key_here

# Notion Integration
NOTION_API_TOKEN=secret_your_notion_token_here
NOTION_DEVICE_REGISTRY_DB=your_device_registry_db_id
NOTION_EVAL_QUEUE_DB=your_eval_queue_db_id
NOTION_MATRICES_DB=your_matrices_db_id
NOTION_ALERTS_LOG_DB=your_alerts_log_db_id

# Email alerts (SMTP)
SMTP_HOST=smtp.gmail.com
SMTP_PORT=587
SMTP_USER=your_email@gmail.com
SMTP_PASSWORD=your_app_password
ALERT_EMAIL_TO=john.burroughs@uihc.edu

# Runtime
LOG_LEVEL=INFO
DATA_DIR=/app/data
```

### 6.6 Hermes Cron Configuration

Save as `config/hermes_tasks.yaml`. Hermes reads this file at startup and registers cron tasks accordingly.

```yaml
# MedOps Hermes Task Definitions
# Thought Reliquary — 192.168.4.100
# Last updated: 2026-06-27

hermes_module: medops
version: "1.0"

cron_tasks:

  # ─── Daily Monitoring ────────────────────────────────────────────────────────

  - name: medops_maude_monitor
    description: "Daily MAUDE adverse event spike check for all formulary devices"
    schedule: "0 9 * * *"          # Every day at 9:00 AM
    command: >
      docker exec medops-core
      python medops/pipeline.py --mode maude_monitor
    timeout_seconds: 300
    on_failure: notify_hermes
    notify_on_completion: false

  # ─── Weekly Intelligence ─────────────────────────────────────────────────────

  - name: medops_recall_check
    description: "Weekly recall check for all formulary devices"
    schedule: "0 7 * * 1"          # Monday 7:00 AM
    command: >
      docker exec medops-core
      python medops/pipeline.py --mode recall_check
    timeout_seconds: 600
    on_failure: notify_hermes
    notify_on_completion: true

  - name: medops_weekly_digest
    description: "Weekly category intelligence digest — generates and delivers Monday briefing"
    schedule: "0 8 * * 1"          # Monday 8:00 AM (after recall_check)
    command: >
      docker exec medops-core
      python medops/pipeline.py --mode digest
    timeout_seconds: 900
    on_failure: notify_hermes
    notify_on_completion: true
    depends_on: medops_recall_check

  # ─── Monthly Maintenance ─────────────────────────────────────────────────────

  - name: medops_gmdn_index_refresh
    description: "Monthly rebuild of GMDN substitution index from ACCESSGUDID full release"
    schedule: "0 2 3 * *"          # 3rd of each month at 2:00 AM
    command: >
      docker exec medops-core
      python medops/cli.py db --gmdn-build
    timeout_seconds: 7200          # 2 hours; bulk download is large
    on_failure: notify_hermes
    notify_on_completion: true

  - name: medops_notion_sync
    description: "Weekly sync of active formulary to Notion Device Registry"
    schedule: "0 10 * * 1"         # Monday 10:00 AM
    command: >
      docker exec medops-core
      python medops/pipeline.py --mode notion_sync
    timeout_seconds: 300
    on_failure: notify_hermes
    notify_on_completion: false

on_demand_tasks:

  - name: device_brief
    description: "Generate full device brief for a given DI, UDI, or catalog number"
    trigger: manual
    inputs:
      - identifier: string        # DI, UDI, or catalog number
    command: >
      docker exec medops-core
      python medops/pipeline.py --mode brief --identifier "{identifier}"
    timeout_seconds: 180
    output: case_id

  - name: competitive_matrix
    description: "Generate competitive matrix for a device category"
    trigger: manual
    inputs:
      - category: string          # e.g., "hemostatics"
      - devices: list[string]     # optional; overrides default category watch list
    command: >
      docker exec medops-core
      python medops/pipeline.py --mode matrix --category "{category}"
    timeout_seconds: 300
    output: matrix_id

  - name: substitution_analysis
    description: "Run full substitution analysis for a given device"
    trigger: manual
    inputs:
      - di: string                # Device Identifier of the reference device
    command: >
      docker exec medops-core
      python medops/pipeline.py --mode substitution --di "{di}"
    timeout_seconds: 240
    output: substitution_report_id
```

### 6.7 Build and Deploy Commands

```bash
# On Thought Reliquary (192.168.4.100)

# Clone or copy repo
cd /opt/medops-os

# Create .env from template
cp .env.example .env
nano .env     # Fill in API keys

# Build and start
docker compose up -d --build

# Verify containers running
docker compose ps

# Initialize the knowledge base schema
docker exec medops-core python medops/cli.py db --init

# Build the initial GMDN index (runs in background; takes 30–90 min on first run)
docker exec medops-core python medops/cli.py db --gmdn-build &

# Run first on-demand brief to test the pipeline
docker exec medops-core python medops/cli.py brief --di "00843197107103"

# Watch logs
docker compose logs -f medops

# Access the web UI
# http://192.168.4.100:7860
```

---

## Section 7: The Notion Integration

### 7.1 Notion Database Schemas

The MedOps OS maintains four Notion databases. All are created once manually in Notion; IDs are stored in `.env`. The Python integration syncs data bidirectionally (read formulary status, write briefs/alerts).

---

#### Database 1: Device Registry

**Purpose:** Master list of all devices in the active UIHC formulary. Single source of truth for what is currently contracted, under evaluation, or retired.

**Notion Properties:**

| Property | Type | Description |
|---|---|---|
| Device Name | Title | Brand name (from GUDID) |
| DI | Text | Primary Device Identifier |
| Catalog Number | Text | Manufacturer catalog number |
| Vendor | Select | Company name |
| Category | Select | Hemostatics, Sutures, Spine Implants, etc. |
| Device Class | Select | Class I / Class II / Class III |
| Product Code | Text | FDA 3-letter product code |
| GMDN Term | Text | GMDN Preferred Term Name |
| 510(k) Number | Text | Clearance number (or PMA) |
| Regulatory Pathway | Select | 510(k) / PMA / HCT/P / Exempt |
| Formulary Status | Select | Active / Under Evaluation / Retired / Flagged |
| GPO Contract | Checkbox | Is this on a current GPO contract? |
| GPO Tier | Select | Tier 1 / Tier 2 / Tier 3 / Off-Contract |
| Last Review Date | Date | Date of most recent VAC or brief review |
| Brief ID | Text | Links to Knowledge Base case ID |
| Recall Status | Select | Clear / Active Recall / Monitor |
| MAUDE Risk | Select | Low / Medium / High |
| Notes | Text | Free text notes |
| Added By | Person | Who added this to the formulary |
| Added Date | Created time | Auto |

---

#### Database 2: Evaluation Queue

**Purpose:** Devices currently under active evaluation (pending VAC decision).

| Property | Type | Description |
|---|---|---|
| Device Name | Title | Brand name |
| DI | Text | Device Identifier |
| Vendor | Select | Company name |
| Category | Select | Device category |
| Evaluation Type | Select | New Product / Substitution / Competitive Review |
| Request Date | Date | When evaluation was requested |
| Requestor | Person | Who requested it |
| VAC Target Date | Date | Target VAC presentation date |
| Brief Status | Select | Pending / In Progress / Complete / Delivered |
| Brief ID | Text | Knowledge Base case ID |
| Substitution For | Relation | Links to Device Registry (what it replaces) |
| Clinical Champion | Person | Surgeon or clinician requesting |
| Priority | Select | Routine / Urgent / Critical |
| Notes | Text | Free text |
| Status | Select | Active / Approved / Rejected / Deferred |

---

#### Database 3: Competitive Matrices

**Purpose:** Category-level competitive analyses. Each entry is a full competitive matrix for a device category.

| Property | Type | Description |
|---|---|---|
| Matrix Title | Title | e.g., "Hemostatics Competitive Matrix — Q3 2026" |
| Category | Select | Device category |
| Devices Compared | Text | Comma-separated brand names |
| Vendors | Multi-select | All vendors included |
| Matrix ID | Text | Knowledge Base matrix ID |
| Generated Date | Date | When the matrix was generated |
| Recommendation | Select | No Change / Switch / Standardize / Further Eval |
| Summary | Text | One-sentence summary of key finding |
| VAC Presented | Checkbox | Has this been presented at VAC? |
| VAC Date | Date | Date presented to VAC |
| VAC Outcome | Select | Pending / Approved / Rejected / Tabled |
| Notion Page | URL | Link to the full matrix Notion page |
| Next Review Date | Date | Scheduled next category review |

---

#### Database 4: Alerts Log

**Purpose:** Audit trail of all recall and MAUDE spike alerts, including response actions.

| Property | Type | Description |
|---|---|---|
| Alert Title | Title | e.g., "Class II Recall — FLOSEAL 50mL — 2026-06-15" |
| Alert Type | Select | Recall / MAUDE Spike / Distribution End |
| Severity | Select | Critical (Class I) / High (Class II) / Medium (Class III) / Low |
| Device Name | Relation | Links to Device Registry |
| DI | Text | Device Identifier |
| Vendor | Select | Manufacturer |
| Alert Date | Date | When alert was detected |
| FDA Recall Number | Text | Recall number if applicable |
| Description | Text | Description of recall or spike |
| Action Required | Text | Immediate action needed |
| Response Status | Select | Open / In Progress / Resolved / Closed |
| Response Actions | Text | What was done (audit log) |
| Resolved Date | Date | When resolved |
| Assigned To | Person | Who owns the response |
| Notified Clinicians | Text | Who was notified |

---

### 7.2 Notion API Integration Module

**File: `medops/notion_sync.py`**

```python
"""
medops/notion_sync.py

Notion API integration for MedOps OS.
Syncs formulary data and writes device briefs, alerts, and matrices to Notion.

Requires notion-client v2.2.1+.
"""

import logging
import os
from datetime import datetime
from typing import Optional

from notion_client import Client

from medops.config import (
    NOTION_API_TOKEN,
    NOTION_DEVICE_REGISTRY_DB,
    NOTION_EVAL_QUEUE_DB,
    NOTION_MATRICES_DB,
    NOTION_ALERTS_LOG_DB,
)
from medops.knowledge_base import (
    get_formulary_devices,
    get_brief_by_id,
)
from medops.alerts import Alert

logger = logging.getLogger(__name__)

_notion_client: Optional[Client] = None


def _get_client() -> Client:
    global _notion_client
    if _notion_client is None:
        if not NOTION_API_TOKEN:
            raise EnvironmentError("NOTION_API_TOKEN not set")
        _notion_client = Client(auth=NOTION_API_TOKEN)
    return _notion_client


# ─── Formulary Sync ──────────────────────────────────────────────────────────

def sync_formulary_to_notion() -> dict:
    """
    Sync all formulary devices from the local SQLite knowledge base to the
    Notion Device Registry database.

    - Creates new pages for devices not yet in Notion.
    - Updates existing pages where DI matches.
    - Does NOT delete pages (Notion deletion requires manual confirmation).

    Returns:
        {"created": int, "updated": int, "errors": int}
    """
    client = _get_client()
    devices = get_formulary_devices()
    stats = {"created": 0, "updated": 0, "errors": 0}

    for device in devices:
        try:
            existing = _find_registry_page_by_di(client, device["di"])
            props = _build_registry_properties(device)

            if existing:
                client.pages.update(
                    page_id=existing["id"],
                    properties=props,
                )
                stats["updated"] += 1
                logger.debug(f"Updated Notion page for DI {device['di']}")
            else:
                client.pages.create(
                    parent={"database_id": NOTION_DEVICE_REGISTRY_DB},
                    properties=props,
                )
                stats["created"] += 1
                logger.info(f"Created Notion page for DI {device['di']} — {device.get('brand_name', '')}")

        except Exception as exc:
            stats["errors"] += 1
            logger.error(f"Notion sync error for DI {device['di']}: {exc}")

    logger.info(f"Formulary sync complete: {stats}")
    return stats


def _find_registry_page_by_di(client: Client, di: str) -> Optional[dict]:
    """Query the Device Registry database for a page with matching DI."""
    results = client.databases.query(
        database_id=NOTION_DEVICE_REGISTRY_DB,
        filter={
            "property": "DI",
            "rich_text": {"equals": di},
        },
    )
    pages = results.get("results", [])
    return pages[0] if pages else None


def _build_registry_properties(device: dict) -> dict:
    """Build Notion properties dict from a formulary device record."""
    props = {
        "Device Name": {"title": [{"text": {"content": device.get("brand_name", "")}}]},
        "DI": {"rich_text": [{"text": {"content": device.get("di", "")}}]},
        "Vendor": {"select": {"name": device.get("company_name", "Unknown")[:100]}},
        "Category": {"select": {"name": device.get("category", "Uncategorized")[:100]}},
        "Formulary Status": {"select": {"name": device.get("formulary_status", "Active")}},
    }
    if device.get("catalog_number"):
        props["Catalog Number"] = {"rich_text": [{"text": {"content": device["catalog_number"]}}]}
    if device.get("product_code"):
        props["Product Code"] = {"rich_text": [{"text": {"content": device["product_code"]}}]}
    if device.get("device_class"):
        class_map = {"1": "Class I", "2": "Class II", "3": "Class III"}
        cls = class_map.get(str(device["device_class"]), device["device_class"])
        props["Device Class"] = {"select": {"name": cls}}
    if device.get("gmdn_name"):
        props["GMDN Term"] = {"rich_text": [{"text": {"content": device["gmdn_name"][:200]}}]}
    if device.get("clearance_number"):
        props["510(k) Number"] = {"rich_text": [{"text": {"content": device["clearance_number"]}}]}
    if device.get("brief_id"):
        props["Brief ID"] = {"rich_text": [{"text": {"content": device["brief_id"]}}]}
    if device.get("last_review_date"):
        props["Last Review Date"] = {"date": {"start": device["last_review_date"]}}
    return props


# ─── Device Brief Pages ──────────────────────────────────────────────────────

def create_evaluation_page(brief_data: dict) -> str:
    """
    Create a formatted Notion page for a device evaluation brief.

    The page is created in the Evaluation Queue database and linked to the
    Device Registry if a matching DI page exists.

    Returns:
        Notion page URL
    """
    client = _get_client()

    device = brief_data.get("device", {})
    di = device.get("di", "")
    brand_name = device.get("brand_name", "")
    generated_at = brief_data.get("generated_at", datetime.utcnow().isoformat())

    # Create page in Evaluation Queue
    page_title = f"{brand_name} — Device Brief — {generated_at[:10]}"

    properties = {
        "Device Name": {"title": [{"text": {"content": page_title}}]},
        "DI": {"rich_text": [{"text": {"content": di}}]},
        "Vendor": {"select": {"name": device.get("company_name", "Unknown")[:100]}},
        "Category": {"select": {"name": brief_data.get("category", "Uncategorized")[:100]}},
        "Evaluation Type": {"select": {"name": "New Product"}},
        "Brief Status": {"select": {"name": "Complete"}},
        "Request Date": {"date": {"start": generated_at[:10]}},
    }
    if brief_data.get("case_id"):
        properties["Brief ID"] = {"rich_text": [{"text": {"content": brief_data["case_id"]}}]}

    # Build page content blocks from the brief sections
    blocks = _build_brief_blocks(brief_data)

    page = client.pages.create(
        parent={"database_id": NOTION_EVAL_QUEUE_DB},
        properties=properties,
        children=blocks,
    )
    page_url = page.get("url", "")
    logger.info(f"Created Notion evaluation page for {brand_name}: {page_url}")
    return page_url


def _build_brief_blocks(brief_data: dict) -> list:
    """
    Convert a structured brief dict into Notion block objects.
    Produces a clean, well-organized Notion page matching the MS-0001 Device Brief format.
    """
    blocks = []
    device = brief_data.get("device", {})
    narrative = brief_data.get("narrative", "")
    sections = brief_data.get("sections", {})

    def heading2(text):
        return {"object": "block", "type": "heading_2",
                "heading_2": {"rich_text": [{"type": "text", "text": {"content": text}}]}}

    def heading3(text):
        return {"object": "block", "type": "heading_3",
                "heading_3": {"rich_text": [{"type": "text", "text": {"content": text}}]}}

    def para(text):
        return {"object": "block", "type": "paragraph",
                "paragraph": {"rich_text": [{"type": "text", "text": {"content": text[:2000]}}]}}

    def divider():
        return {"object": "block", "type": "divider", "divider": {}}

    def callout(text, emoji="⚠️"):
        return {
            "object": "block", "type": "callout",
            "callout": {
                "rich_text": [{"type": "text", "text": {"content": text[:2000]}}],
                "icon": {"type": "emoji", "emoji": emoji},
            }
        }

    def bullet(text):
        return {
            "object": "block", "type": "bulleted_list_item",
            "bulleted_list_item": {"rich_text": [{"type": "text", "text": {"content": text[:2000]}}]}
        }

    def code_block(text, language="plain text"):
        return {
            "object": "block", "type": "code",
            "code": {
                "rich_text": [{"type": "text", "text": {"content": text[:2000]}}],
                "language": language,
            }
        }

    # ── Header callout with key identifiers
    header_text = (
        f"DI: {device.get('di', 'N/A')}  |  "
        f"Brand: {device.get('brand_name', 'N/A')}  |  "
        f"Vendor: {device.get('company_name', 'N/A')}  |  "
        f"Product Code: {device.get('primary_product_code', 'N/A')}  |  "
        f"Device Class: {device.get('device_class', 'N/A')}  |  "
        f"GMDN: {device.get('primary_gmdn_name', 'N/A')}"
    )
    blocks.append(callout(header_text, "🔬"))
    blocks.append(divider())

    # ── Section 1: Device Identity
    blocks.append(heading2("1. Device Identity"))
    identity_lines = [
        f"Brand Name: {device.get('brand_name', 'N/A')}",
        f"Version/Model: {device.get('version_model_number', 'N/A')}",
        f"Catalog Number: {device.get('catalog_number', 'N/A')}",
        f"Primary DI: {device.get('di', 'N/A')}",
        f"Company: {device.get('company_name', 'N/A')}",
        f"GMDN Term: {device.get('primary_gmdn_name', 'N/A')}",
        f"Product Code: {device.get('primary_product_code', 'N/A')}",
        f"Single Use: {device.get('single_use', 'N/A')}",
        f"Sterile: {device.get('device_sterile', 'N/A')}",
        f"MRI Safety: {device.get('mri_safety_status', 'N/A')}",
        f"Distribution Status: {device.get('commercial_distribution_status', 'N/A')}",
    ]
    for line in identity_lines:
        blocks.append(bullet(line))
    blocks.append(divider())

    # ── Section 2: Regulatory Status
    blocks.append(heading2("2. Regulatory Status"))
    reg = sections.get("regulatory_status", {})
    if reg:
        reg_lines = [
            f"Device Class: {reg.get('device_class', 'N/A')}",
            f"Regulatory Pathway: {reg.get('pathway', 'N/A')}",
            f"Clearance Number: {reg.get('clearance_number', 'N/A')}",
            f"Clearance Date: {reg.get('clearance_date', 'N/A')}",
            f"Applicant: {reg.get('applicant', 'N/A')}",
            f"Regulation Number: {reg.get('regulation_number', 'N/A')}",
            f"Life Sustaining: {reg.get('life_sustaining', 'N/A')}",
            f"Implant Flag: {reg.get('implant_flag', 'N/A')}",
        ]
        for line in reg_lines:
            blocks.append(bullet(line))
    elif narrative:
        blocks.append(para("See narrative brief below for regulatory details."))
    blocks.append(divider())

    # ── Section 3: Safety Record
    blocks.append(heading2("3. Safety Record"))
    safety = sections.get("safety_record", {})
    if safety.get("active_recalls"):
        blocks.append(callout(f"ACTIVE RECALL — {safety['active_recalls']}", "🚨"))
    maude_summary = safety.get("maude_summary", "No MAUDE data retrieved.")
    blocks.append(para(f"Adverse Events (MAUDE): {maude_summary}"))
    blocks.append(divider())

    # ── Section 4: Clinical Evidence
    blocks.append(heading2("4. Clinical Evidence"))
    literature = sections.get("literature", [])
    if literature:
        for pub in literature[:5]:
            blocks.append(bullet(f"{pub.get('title', '')} ({pub.get('journal', '')} {pub.get('pub_date', '')} — PMID {pub.get('pmid', 'N/A')})"))
    else:
        blocks.append(para("No PubMed literature retrieved for this device."))
    blocks.append(divider())

    # ── Section 5: AI-Generated Narrative Brief
    if narrative:
        blocks.append(heading2("5. AI-Synthesized Brief"))
        # Split narrative into ~1800-char chunks (Notion block limit is 2000 chars)
        chunk_size = 1800
        for i in range(0, len(narrative), chunk_size):
            chunk = narrative[i:i + chunk_size]
            blocks.append(para(chunk))
    blocks.append(divider())

    # ── Section 6: Substitution Candidates
    subs = sections.get("substitution_candidates", [])
    if subs:
        blocks.append(heading2("6. Substitution Candidates (Top 5)"))
        for idx, sub in enumerate(subs[:5]):
            blocks.append(bullet(
                f"#{idx + 1}: {sub.get('brand_name', 'N/A')} ({sub.get('company_name', 'N/A')}) — "
                f"DI: {sub.get('di', 'N/A')} — Score: {sub.get('equivalence_score', 'N/A')}"
            ))
        blocks.append(divider())

    # ── Footer
    blocks.append(para(f"Generated by MedOps OS on {brief_data.get('generated_at', 'N/A')} | Case ID: {brief_data.get('case_id', 'N/A')}"))

    return blocks


# ─── Alert Log ───────────────────────────────────────────────────────────────

def update_alert_log(alert: Alert) -> str:
    """
    Log a recall or MAUDE spike alert to the Notion Alerts Log database.

    Returns:
        Notion page URL for the created alert entry.
    """
    client = _get_client()

    severity_map = {
        "critical": "Critical (Class I)",
        "high": "High (Class II)",
        "medium": "Medium (Class III)",
        "low": "Low",
    }

    alert_title = f"{alert.alert_type} — {alert.brand_name} — {alert.detected_date}"
    props = {
        "Alert Title": {"title": [{"text": {"content": alert_title}}]},
        "Alert Type": {"select": {"name": alert.alert_type}},
        "Severity": {"select": {"name": severity_map.get(alert.severity.lower(), alert.severity)}},
        "DI": {"rich_text": [{"text": {"content": alert.device_di}}]},
        "Vendor": {"select": {"name": alert.manufacturer[:100] if alert.manufacturer else "Unknown"}},
        "Alert Date": {"date": {"start": alert.detected_date}},
        "Description": {"rich_text": [{"text": {"content": alert.description[:2000]}}]},
        "Action Required": {"rich_text": [{"text": {"content": alert.action_required[:2000]}}]},
        "Response Status": {"select": {"name": "Open"}},
    }
    if alert.recall_number:
        props["FDA Recall Number"] = {"rich_text": [{"text": {"content": alert.recall_number}}]}

    page = client.pages.create(
        parent={"database_id": NOTION_ALERTS_LOG_DB},
        properties=props,
    )
    page_url = page.get("url", "")
    logger.info(f"Created Notion alert log entry: {alert_title} — {page_url}")
    return page_url


# ─── Competitive Matrix Pages ─────────────────────────────────────────────────

def create_matrix_page(matrix_data: dict) -> str:
    """
    Create a formatted Notion page for a competitive matrix analysis.

    Returns:
        Notion page URL
    """
    client = _get_client()

    category = matrix_data.get("category", "Unknown Category")
    generated_at = matrix_data.get("generated_at", datetime.utcnow().isoformat())
    matrix_id = matrix_data.get("matrix_id", "")
    devices = matrix_data.get("devices", [])
    vendor_names = list({d.get("company_name", "") for d in devices if d.get("company_name")})

    title = f"{category.title()} Competitive Matrix — {generated_at[:10]}"

    properties = {
        "Matrix Title": {"title": [{"text": {"content": title}}]},
        "Category": {"select": {"name": category[:100]}},
        "Devices Compared": {"rich_text": [{"text": {"content": ", ".join(d.get("brand_name", "") for d in devices[:10])}}]},
        "Generated Date": {"date": {"start": generated_at[:10]}},
        "VAC Presented": {"checkbox": False},
    }
    if matrix_id:
        properties["Matrix ID"] = {"rich_text": [{"text": {"content": matrix_id}}]}
    if vendor_names:
        properties["Vendors"] = {"multi_select": [{"name": v[:100]} for v in vendor_names[:10]]}

    blocks = _build_matrix_blocks(matrix_data)

    page = client.pages.create(
        parent={"database_id": NOTION_MATRICES_DB},
        properties=properties,
        children=blocks,
    )
    page_url = page.get("url", "")
    logger.info(f"Created Notion matrix page: {title} — {page_url}")
    return page_url


def _build_matrix_blocks(matrix_data: dict) -> list:
    """Build Notion blocks for a competitive matrix page."""
    blocks = []
    devices = matrix_data.get("devices", [])
    narrative = matrix_data.get("narrative", "")
    category = matrix_data.get("category", "")

    def heading2(text):
        return {"object": "block", "type": "heading_2",
                "heading_2": {"rich_text": [{"type": "text", "text": {"content": text}}]}}

    def para(text):
        return {"object": "block", "type": "paragraph",
                "paragraph": {"rich_text": [{"type": "text", "text": {"content": text[:2000]}}]}}

    def bullet(text):
        return {
            "object": "block", "type": "bulleted_list_item",
            "bulleted_list_item": {"rich_text": [{"type": "text", "text": {"content": text[:2000]}}]}
        }

    def divider():
        return {"object": "block", "type": "divider", "divider": {}}

    blocks.append(heading2(f"Category: {category.title()} — {len(devices)} Devices Compared"))
    blocks.append(divider())

    # Device summary rows
    blocks.append(heading2("Device Inventory"))
    for d in devices:
        line = (
            f"{d.get('brand_name', 'N/A')} ({d.get('company_name', 'N/A')}) — "
            f"DI: {d.get('di', 'N/A')} | "
            f"Product Code: {d.get('primary_product_code', 'N/A')} | "
            f"Class: {d.get('device_class', 'N/A')} | "
            f"Recalls: {d.get('active_recalls', 'N/A')} | "
            f"MAUDE (90d): {d.get('maude_recent_count', 'N/A')}"
        )
        blocks.append(bullet(line))
    blocks.append(divider())

    # AI Narrative
    if narrative:
        blocks.append(heading2("AI-Synthesized Analysis"))
        chunk_size = 1800
        for i in range(0, len(narrative), chunk_size):
            blocks.append(para(narrative[i:i + chunk_size]))
    blocks.append(divider())

    blocks.append(para(f"Generated by MedOps OS | Matrix ID: {matrix_data.get('matrix_id', 'N/A')} | {matrix_data.get('generated_at', 'N/A')}"))
    return blocks
```

---

### 7.3 The Notion Device Brief Page — Design

A device brief in Notion is structured as a rich-content page with a callout header, sectioned content, and a footer. The design mirrors the MS-0001 Document Type A format but optimized for Notion's block model.

**Page layout (visual structure):**

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  🔬  DI: 00843197107103  |  Brand: FLOSEAL 50mL  |  Class II  |  FTL       │
│       Vendor: Baxter  |  GMDN: Absorbable haemostatic gelatin               │
└─────────────────────────────────────────────────────────────────────────────┘

── 1. Device Identity ──────────────────────────────────────────────────────────
  • Brand Name: FLOSEAL Hemostatic Matrix 50mL
  • Version/Model: 7FLOSLV050
  • Catalog Number: 1012879
  • Primary DI: 00843197107103
  • Company: Baxter Healthcare Corporation
  • GMDN Term: Absorbable haemostatic gelatin sponge
  • Product Code: FTL
  • Single Use: Yes | Sterile: Yes | MRI Safety: MR Safe
  • Distribution Status: In Commercial Distribution

── 2. Regulatory Status ────────────────────────────────────────────────────────
  • Device Class: Class II
  • Regulatory Pathway: 510(k)
  • Clearance Number: K001522
  • Clearance Date: 2000-08-14
  • Regulation Number: 21 CFR 878.4490

── 3. Safety Record ────────────────────────────────────────────────────────────
  • Adverse Events (MAUDE, last 90 days): 7 reports — product code FTL
  • Historical MAUDE total: 284 events on file
  ⚠️  No active Class I or II recalls found as of 2026-06-27

── 4. Clinical Evidence ────────────────────────────────────────────────────────
  • Renkens et al. (2001) — Intraoperative use in spinal surgery PMID 11284788
  • Oz et al. (2003) — Cardiac surgery hemostasis PMID 12965421
  [...]

── 5. AI-Synthesized Brief ─────────────────────────────────────────────────────
  [Full narrative text from Claude — multiple paragraphs]

── 6. Substitution Candidates (Top 5) ─────────────────────────────────────────
  #1: SURGIFLO (Ethicon) — DI: ... — Score: 85.0
  #2: Arista AH (BD) — DI: ... — Score: 72.0
  [...]

Generated by MedOps OS on 2026-06-27T08:14:33Z | Case ID: BRIEF-2026-0042
```

---

### 7.4 Full Pipeline with Notion Delivery

The `pipeline.py` `run_device_brief()` function calls `notion_sync.create_evaluation_page()` at the end of its execution if `NOTION_API_TOKEN` is set and the brief was successfully generated. The Notion page URL is stored alongside the case ID in the local knowledge base.

```python
# In pipeline.py, at the end of run_device_brief():
if config.NOTION_API_TOKEN:
    try:
        from medops.notion_sync import create_evaluation_page
        notion_url = create_evaluation_page(brief_record)
        kb.update_brief_notion_url(case_id, notion_url)
        logger.info(f"Brief synced to Notion: {notion_url}")
    except Exception as exc:
        logger.warning(f"Notion sync failed (non-fatal): {exc}")
```

The same pattern applies for alert events — `run_recall_alert_check()` calls `update_alert_log()` for every new alert that is not already logged, and `run_competitive_matrix()` calls `create_matrix_page()` after the matrix is generated.

---

## Appendix A: Category Watch Configuration — All 11 Categories

**File: `config/category_watches.yaml`**

```yaml
# MedOps Category Watch Configuration
# Edit this file to add/remove categories, vendors, and thresholds.
# Hermes reads this on startup; changes take effect at next scheduled run.

category_watches:

  - category: hemostatics
    display_name: "Biosurgery / Hemostatics"
    vendors: [Integra, Baxter, Ethicon, BD, Becton Dickinson]
    product_codes: [FTL, FTM, OZO, GZA, FYN]
    fda_panel: SU
    alert_threshold_maude: 5       # Alert if >5 MAUDE events in 30 days
    alert_threshold_recall: Class II
    watch_510k: true
    notes: "FLOSEAL, SURGIFLO, SURGICEL family, Arista AH"

  - category: endo_mechanicals
    display_name: "Endo Mechanicals / Laparoscopic"
    vendors: [Medtronic, Ethicon, Applied Medical, B. Braun, Aesculap]
    product_codes: [KZE, MQP, LUG, FND]
    fda_panel: SU
    alert_threshold_maude: 10
    alert_threshold_recall: Class II
    watch_510k: true
    notes: "Staplers, trocars, laparoscopic instruments"

  - category: sutures
    display_name: "Sutures"
    vendors: [Ethicon, Medtronic, Covidien, B. Braun, Teleflex]
    product_codes: [GAK, GAL, GAW, GAX]
    fda_panel: SU
    alert_threshold_maude: 3
    alert_threshold_recall: Class III
    watch_510k: false              # Sutures rarely have new 510(k) activity
    notes: "Absorbable and nonabsorbable; barbed; antibiotic-coated"

  - category: orthopedic_total_joints
    display_name: "Orthopedic Implants — Total Joints"
    vendors: [Zimmer Biomet, Stryker, DePuy Synthes, Smith+Nephew]
    product_codes: [HRS, KWQ, KYD, LNH]
    fda_panel: OR
    alert_threshold_maude: 5
    alert_threshold_recall: Class II
    watch_510k: true
    notes: "TKA, THA, unicompartmental knee. Robotic platform lock-in risk."

  - category: spine_implants
    display_name: "Orthopedic Implants — Spine"
    vendors: [Medtronic, Stryker, DePuy Synthes, NuVasive, Globus Medical]
    product_codes: [KWQ, KWR, KYD, MUY, LLQ]
    fda_panel: OR
    alert_threshold_maude: 3
    alert_threshold_recall: Class II
    watch_510k: true
    notes: "Globus + NuVasive merger 2023 — monitor contract redundancy"

  - category: burn_wound_care
    display_name: "Burn Tissue / Advanced Wound Care"
    vendors: [Integra LifeSciences, MiMedx, Organogenesis, Avita Medical, Smith+Nephew]
    product_codes: [FRO, KGZ, OZA, OZB]
    fda_panel: SU
    alert_threshold_maude: 2
    alert_threshold_recall: Class II
    watch_510k: true
    notes: "PMA pathway for Integra DRT, RECELL. HCT/P pathway for amniotic. Separate AATB compliance track."

  - category: biologic_allografts
    display_name: "Biologic Tissues / Allografts"
    vendors: [MiMedx, Artivion, Organogenesis, Osiris Therapeutics, Wright Medical]
    product_codes: []              # HCT/P products not in OpenFDA device endpoints
    fda_panel: ""
    alert_threshold_maude: 2
    alert_threshold_recall: Class II
    watch_510k: false
    notes: "Regulated under 21 CFR 1271 (HCT/P), not device. Track FDA tissue establishment recalls separately. Verify AATB accreditation."
    hctp_only: true

  - category: synthetic_tissues
    display_name: "Synthetic Human Tissues / Xenografts"
    vendors: [Integra LifeSciences, LifeNet Health, RTI Surgical, Enovis]
    product_codes: [FTB, KGX, OZC]
    fda_panel: SU
    alert_threshold_maude: 2
    alert_threshold_recall: Class II
    watch_510k: true
    notes: "SurgiMend, PriMatrix, AlloPatch. 510(k) pathway (not HCT/P)."

  - category: plastic_surgery_implants
    display_name: "Plastic Surgery Implants"
    vendors: [Allergan, AbbVie, Mentor, Johnson & Johnson, Sientra, GC Aesthetics]
    product_codes: [QDD, QMD, FTR]
    fda_panel: SU
    alert_threshold_maude: 3
    alert_threshold_recall: Class I   # All Class III devices; Class I only for threshold
    watch_510k: false              # All PMA pathway; 510(k) not applicable
    notes: "All silicone gel breast implants are Class III PMA. Boxed Warning 2021. Track BIA-ALCL FDA safety communications."

  - category: ophthalmology
    display_name: "Ophthalmology Devices"
    vendors: [Alcon, Johnson & Johnson Vision, Bausch + Lomb, Carl Zeiss Meditec, Glaukos]
    product_codes: [HQL, HQM, OZP, FMF, KZP]
    fda_panel: OP
    alert_threshold_maude: 5
    alert_threshold_recall: Class II
    watch_510k: true
    notes: "IOLs, phaco systems, MIGS glaucoma devices. Capital equipment TCO tracking separate."

  - category: surgical_robotics
    display_name: "Surgical Robotics"
    vendors: [Intuitive Surgical, Stryker, Zimmer Biomet, DePuy Synthes, Globus Medical, Medtronic]
    product_codes: [LMF, LQH, OZQ, NUY]
    fda_panel: OR
    alert_threshold_maude: 3
    alert_threshold_recall: Class I
    watch_510k: true
    notes: "Robotic platform selection drives implant vendor lock-in for 7-10yr. Track capital procurement, not just consumables. Monitor Intuitive da Vinci 5 market entry."
```

---

## Appendix B: Full `pipeline.py`

**File: `medops/pipeline.py`**

```python
"""
medops/pipeline.py

Main orchestration module for the MedOps Intelligence OS.
Called by Hermes for all trigger types (on-demand, scheduled, alert).

Usage (CLI / Hermes command):
    python medops/pipeline.py --mode brief --identifier "00843197107103"
    python medops/pipeline.py --mode matrix --category "hemostatics"
    python medops/pipeline.py --mode substitution --di "00843197107103"
    python medops/pipeline.py --mode digest
    python medops/pipeline.py --mode recall_check
    python medops/pipeline.py --mode maude_monitor
    python medops/pipeline.py --mode notion_sync
    python medops/pipeline.py --mode daemon
"""

import argparse
import logging
import os
import sys
import time
from datetime import datetime

import schedule

from medops import config
from medops.accessgudid import get_device_by_di, resolve_identifier
from medops.openfda import (
    get_510k_for_di,
    get_recalls_by_firm,
    get_maude_events,
    get_device_classification,
    get_recalls_by_product_code,
)
from medops.pubmed import search_device_literature
from medops.synthesizer import (
    generate_device_brief,
    generate_competitive_matrix,
    generate_substitution_recommendation,
    flag_anomalies,
)
from medops.knowledge_base import (
    save_brief,
    save_matrix,
    get_formulary_devices,
    add_to_formulary,
    search_briefs,
    get_brief_by_id,
)
from medops.alerts import (
    check_recalls_for_formulary,
    check_maude_spikes,
    send_alert,
)
from medops.digest import generate_weekly_digest, deliver_digest
from medops.substitution import find_substitutes, format_substitution_report

logger = logging.getLogger(__name__)


# ─── On-Demand: Device Brief ─────────────────────────────────────────────────

def run_device_brief(identifier: str) -> str:
    """
    Full pipeline for a single device brief.

    Args:
        identifier: DI, UDI, or catalog number

    Returns:
        case_id: str — knowledge base case ID for the generated brief
    """
    logger.info(f"run_device_brief: identifier={identifier}")

    # Step 1: Resolve identifier to DI and fetch ACCESSGUDID data
    di, gudid_data = resolve_identifier(identifier)
    if not gudid_data:
        raise ValueError(f"No ACCESSGUDID record found for identifier: {identifier}")

    brand_name = gudid_data.get("brand_name", "")
    product_code = gudid_data.get("primary_product_code", "")
    company_name = gudid_data.get("company_name", "")
    gmdn_name = gudid_data.get("primary_gmdn_name", "")

    # Step 2: 510(k)/PMA clearance data
    clearance_data = get_510k_for_di(di, product_code)

    # Step 3: MAUDE adverse events
    maude_data = get_maude_events(brand_name=brand_name, years_back=3)

    # Step 4: Active recalls
    recall_data = get_recalls_by_firm(firm_name=company_name, years_back=5)
    # Filter recalls by product code
    if product_code:
        pc_recalls = get_recalls_by_product_code(product_code, years_back=5)
        # Merge, dedup by recall ID
        seen_ids = {r.get("id", "") for r in recall_data}
        for r in pc_recalls:
            if r.get("id", "") not in seen_ids:
                recall_data.append(r)

    # Step 5: Classification details
    classification = get_device_classification(product_code) if product_code else {}

    # Step 6: PubMed literature
    category = _guess_category_from_product_code(product_code)
    pubmed_results = search_device_literature(
        device_name=brand_name,
        category=category,
        max_results=15,
    )

    # Step 7: Claude synthesis
    narrative = generate_device_brief(
        accessgudid_data=gudid_data,
        fda_data={
            "clearance": clearance_data,
            "classification": classification,
        },
        maude_data=maude_data,
        recall_data=recall_data,
        pubmed_abstracts=pubmed_results,
    )

    # Step 8: Flag anomalies
    anomalies = flag_anomalies({
        "gudid": gudid_data,
        "recalls": recall_data,
        "maude": maude_data,
    })

    # Step 9: Assemble brief record and save
    brief_record = {
        "di": di,
        "identifier_used": identifier,
        "device": gudid_data,
        "clearance": clearance_data,
        "classification": classification,
        "maude": maude_data,
        "recalls": recall_data,
        "literature": pubmed_results,
        "narrative": narrative,
        "anomalies": anomalies,
        "category": category,
        "generated_at": datetime.utcnow().isoformat() + "Z",
        "sections": {
            "regulatory_status": {
                "device_class": classification.get("device_class", gudid_data.get("device_class", "")),
                "pathway": clearance_data.get("pathway", "Unknown"),
                "clearance_number": clearance_data.get("k_number", ""),
                "clearance_date": clearance_data.get("decision_date", ""),
                "applicant": clearance_data.get("applicant", ""),
                "regulation_number": classification.get("regulation_number", ""),
                "life_sustaining": classification.get("life_sustain_support_flag", ""),
                "implant_flag": classification.get("implant_flag", ""),
            },
            "safety_record": {
                "active_recalls": _format_active_recalls(recall_data),
                "maude_summary": f"{len(maude_data)} events retrieved (last 3 years)",
            },
            "literature": pubmed_results,
        },
    }

    case_id = save_brief(brief_record)
    brief_record["case_id"] = case_id
    logger.info(f"Brief saved: case_id={case_id}")

    # Step 10: Notion sync (non-blocking)
    if config.NOTION_API_TOKEN:
        try:
            from medops.notion_sync import create_evaluation_page
            from medops.knowledge_base import update_brief_notion_url
            notion_url = create_evaluation_page(brief_record)
            update_brief_notion_url(case_id, notion_url)
        except Exception as exc:
            logger.warning(f"Notion sync failed (non-fatal): {exc}")

    return case_id


# ─── On-Demand: Competitive Matrix ───────────────────────────────────────────

def run_competitive_matrix(category: str, device_list: list = None) -> str:
    """
    Full pipeline for a competitive matrix for a device category.

    Args:
        category: Category name (matches category_watches.yaml)
        device_list: Optional list of DIs to compare. If None, uses formulary devices + category watch.

    Returns:
        matrix_id: str
    """
    logger.info(f"run_competitive_matrix: category={category}")

    if device_list is None:
        # Use formulary devices in this category + top 3 vendors from watch list
        formulary = get_formulary_devices()
        device_list = [d["di"] for d in formulary if d.get("category") == category]
        if not device_list:
            logger.warning(f"No formulary devices in category '{category}' — matrix will be sparse")

    devices_data = []
    for di in device_list:
        try:
            gudid = get_device_by_di(di)
            if not gudid:
                continue
            pc = gudid.get("primary_product_code", "")
            recalls = get_recalls_by_firm(gudid.get("company_name", ""), years_back=3)
            maude = get_maude_events(gudid.get("brand_name", ""), years_back=2)
            devices_data.append({
                "di": di,
                **gudid,
                "recalls": recalls,
                "active_recalls": len([r for r in recalls if r.get("status") == "Ongoing"]),
                "maude_recent_count": len(maude),
            })
        except Exception as exc:
            logger.warning(f"Failed to fetch data for DI {di}: {exc}")

    if not devices_data:
        raise ValueError(f"No device data retrieved for matrix in category '{category}'")

    matrix_narrative = generate_competitive_matrix(devices_data)

    matrix_record = {
        "category": category,
        "devices": devices_data,
        "narrative": matrix_narrative,
        "generated_at": datetime.utcnow().isoformat() + "Z",
    }
    matrix_id = save_matrix(matrix_record)
    matrix_record["matrix_id"] = matrix_id

    if config.NOTION_API_TOKEN:
        try:
            from medops.notion_sync import create_matrix_page
            create_matrix_page(matrix_record)
        except Exception as exc:
            logger.warning(f"Notion matrix sync failed (non-fatal): {exc}")

    logger.info(f"Matrix saved: matrix_id={matrix_id}")
    return matrix_id


# ─── On-Demand: Substitution Analysis ────────────────────────────────────────

def run_substitution_analysis(di: str) -> str:
    """
    Full substitution analysis for a given device.

    Args:
        di: Device Identifier of the reference device

    Returns:
        substitution_report_id: str (saved in knowledge base)
    """
    from medops.knowledge_base import save_substitution_report
    from medops.synthesizer import generate_substitution_recommendation

    logger.info(f"run_substitution_analysis: di={di}")

    reference_device = get_device_by_di(di)
    if not reference_device:
        raise ValueError(f"Reference device not found: {di}")

    candidates = find_substitutes(di)
    report = format_substitution_report(di, reference_device, candidates)

    # Claude narrative for top 5 candidates
    if candidates:
        top_candidates_data = [
            {
                "di": c.di, "brand_name": c.brand_name, "company_name": c.company_name,
                "gmdn_pt_name": c.gmdn_pt_name, "product_code": c.product_code,
                "device_class": c.device_class, "active_recalls": c.active_recalls,
                "maude_recent_count": c.maude_recent_count, "equivalence_score": c.equivalence_score,
            }
            for c in candidates[:5]
        ]
        narrative = generate_substitution_recommendation(
            device_a_data=reference_device,
            device_b_data=top_candidates_data[0] if top_candidates_data else {},
            comparison_data={"candidates": top_candidates_data, "report": report},
        )
        report["narrative"] = narrative

    report["generated_at"] = datetime.utcnow().isoformat() + "Z"
    sub_id = save_substitution_report(report)
    logger.info(f"Substitution report saved: {sub_id}")
    return sub_id


# ─── Scheduled: Weekly Digest ─────────────────────────────────────────────────

def run_scheduled_digest(categories: list = None):
    """
    Generate and deliver the weekly Monday intelligence digest.
    Called by Hermes cron: "0 8 * * 1"
    """
    logger.info("run_scheduled_digest: starting weekly digest generation")

    # Load category watch list
    import yaml
    watch_file = config.BASE_DIR / "config" / "category_watches.yaml"
    if watch_file.exists():
        with open(watch_file) as f:
            watch_config = yaml.safe_load(f)
        all_categories = [c["category"] for c in watch_config.get("category_watches", [])]
    else:
        all_categories = categories or []

    if categories:
        active_categories = [c for c in all_categories if c in categories]
    else:
        active_categories = all_categories

    digest_content = generate_weekly_digest(active_categories)
    deliver_digest(digest_content)
    logger.info("Weekly digest generated and delivered")


# ─── Scheduled: Recall Alert Check ───────────────────────────────────────────

def run_recall_alert_check():
    """
    Check all formulary devices for new recalls.
    Called by Hermes cron: "0 7 * * 1"
    """
    logger.info("run_recall_alert_check: checking formulary for new recalls")
    new_alerts = check_recalls_for_formulary()

    for alert in new_alerts:
        send_alert(alert, channel="email")
        if config.NOTION_API_TOKEN:
            try:
                from medops.notion_sync import update_alert_log
                update_alert_log(alert)
            except Exception as exc:
                logger.warning(f"Notion alert log failed: {exc}")

    logger.info(f"Recall check complete: {len(new_alerts)} new alerts")
    return new_alerts


# ─── Scheduled: MAUDE Monitor ─────────────────────────────────────────────────

def run_maude_monitor():
    """
    Daily MAUDE event spike detection for active formulary devices.
    Called by Hermes cron: "0 9 * * *"
    """
    logger.info("run_maude_monitor: checking MAUDE event volumes")
    spike_alerts = check_maude_spikes(days_lookback=30)

    for alert in spike_alerts:
        send_alert(alert, channel="email")
        if config.NOTION_API_TOKEN:
            try:
                from medops.notion_sync import update_alert_log
                update_alert_log(alert)
            except Exception as exc:
                logger.warning(f"Notion MAUDE alert log failed: {exc}")

    logger.info(f"MAUDE monitor complete: {len(spike_alerts)} spike alerts")
    return spike_alerts


# ─── Daemon Mode ──────────────────────────────────────────────────────────────

def run_daemon():
    """
    Daemon mode: register all scheduled tasks and run indefinitely.
    Called by Docker CMD: python medops/pipeline.py --mode daemon
    """
    logger.info("MedOps daemon starting — registering scheduled tasks")

    schedule.every().monday.at("07:00").do(run_recall_alert_check)
    schedule.every().monday.at("08:00").do(run_scheduled_digest)
    schedule.every().day.at("09:00").do(run_maude_monitor)

    logger.info("Scheduled tasks registered. Running.")
    while True:
        schedule.run_pending()
        time.sleep(60)


# ─── Utilities ────────────────────────────────────────────────────────────────

def _guess_category_from_product_code(product_code: str) -> str:
    """Map FDA product code to a MedOps category string."""
    PC_CATEGORY_MAP = {
        "FTL": "hemostatics", "FTM": "hemostatics", "OZO": "hemostatics",
        "KZE": "endo_mechanicals", "MQP": "endo_mechanicals",
        "GAK": "sutures", "GAL": "sutures",
        "HRS": "orthopedic_total_joints", "KWQ": "orthopedic_total_joints",
        "MUY": "spine_implants", "KWR": "spine_implants",
        "QDD": "plastic_surgery_implants", "QMD": "plastic_surgery_implants",
        "HQL": "ophthalmology", "HQM": "ophthalmology",
    }
    return PC_CATEGORY_MAP.get(product_code, "general")


def _format_active_recalls(recall_data: list) -> str:
    active = [r for r in recall_data if r.get("status") == "Ongoing"]
    if not active:
        return "No active recalls found."
    return f"{len(active)} active recall(s): " + "; ".join(
        f"Class {r.get('classification', '?')} — {r.get('reason_for_recall', 'N/A')[:80]}"
        for r in active[:3]
    )


# ─── CLI Entrypoint ───────────────────────────────────────────────────────────

def main():
    logging.basicConfig(
        level=getattr(logging, config.LOG_LEVEL, logging.INFO),
        format="%(asctime)s %(name)s %(levelname)s %(message)s",
        handlers=[
            logging.StreamHandler(sys.stdout),
            logging.FileHandler(config.BASE_DIR / "logs" / "medops.log"),
        ],
    )

    parser = argparse.ArgumentParser(description="MedOps Intelligence OS — Pipeline Runner")
    parser.add_argument("--mode", required=True,
        choices=["brief", "matrix", "substitution", "digest", "recall_check",
                 "maude_monitor", "notion_sync", "daemon"],
        help="Execution mode")
    parser.add_argument("--identifier", help="DI, UDI, or catalog number (for --mode brief)")
    parser.add_argument("--di", help="Device Identifier (for --mode substitution)")
    parser.add_argument("--category", help="Device category (for --mode matrix)")
    parser.add_argument("--devices", nargs="*", help="List of DIs for matrix (optional)")
    args = parser.parse_args()

    if args.mode == "brief":
        if not args.identifier:
            parser.error("--identifier required for --mode brief")
        case_id = run_device_brief(args.identifier)
        print(f"Brief generated. Case ID: {case_id}")

    elif args.mode == "matrix":
        if not args.category:
            parser.error("--category required for --mode matrix")
        matrix_id = run_competitive_matrix(args.category, args.devices)
        print(f"Matrix generated. Matrix ID: {matrix_id}")

    elif args.mode == "substitution":
        if not args.di:
            parser.error("--di required for --mode substitution")
        sub_id = run_substitution_analysis(args.di)
        print(f"Substitution report generated. ID: {sub_id}")

    elif args.mode == "digest":
        run_scheduled_digest()
        print("Weekly digest generated and delivered.")

    elif args.mode == "recall_check":
        alerts = run_recall_alert_check()
        print(f"Recall check complete. {len(alerts)} new alerts.")

    elif args.mode == "maude_monitor":
        alerts = run_maude_monitor()
        print(f"MAUDE monitor complete. {len(alerts)} spike alerts.")

    elif args.mode == "notion_sync":
        from medops.notion_sync import sync_formulary_to_notion
        stats = sync_formulary_to_notion()
        print(f"Notion sync complete: {stats}")

    elif args.mode == "daemon":
        run_daemon()


if __name__ == "__main__":
    main()
```

---

## Appendix C: Quick Reference

### API Endpoints Used by MedOps OS

| Service | Endpoint | Auth |
|---|---|---|
| ACCESSGUDID DI Lookup | `https://accessgudid.nlm.nih.gov/api/v2/devices/lookup.json?di={DI}` | None |
| ACCESSGUDID Bulk Download | `https://accessgudid.nlm.nih.gov/download` | None |
| OpenFDA MAUDE | `https://api.fda.gov/device/event.json` | Optional API key |
| OpenFDA 510(k) | `https://api.fda.gov/device/510k.json` | Optional API key |
| OpenFDA Recalls | `https://api.fda.gov/device/recall.json` | Optional API key |
| OpenFDA Classification | `https://api.fda.gov/device/classification.json` | Optional API key |
| OpenFDA UDI | `https://api.fda.gov/device/udi.json` | Optional API key |
| PubMed ESearch | `https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi` | Optional API key |
| PubMed EFetch | `https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi` | Optional API key |
| Anthropic Claude | `https://api.anthropic.com/v1/messages` | API key required |
| Notion API | `https://api.notion.com/v1/` | Integration token |

### Rate Limits

| Service | Limit | With Key |
|---|---|---|
| OpenFDA | 40/min, 1,000/day (anon) | 240/min, 120,000/day |
| ACCESSGUDID | Not published; be conservative at 1/sec | — |
| PubMed | 3/sec (anon) | 10/sec with key |
| Anthropic Claude | Tier-dependent; Sonnet default 2,000 RPM | — |
| Notion | 3 requests/sec | — |

### Common Commands

```bash
# Generate a device brief
docker exec medops-core python medops/cli.py brief --di "00843197107103"

# Generate a competitive matrix
docker exec medops-core python medops/cli.py matrix --category hemostatics

# Run substitution analysis
docker exec medops-core python medops/cli.py substitution --di "00843197107103"

# View active alerts
docker exec medops-core python medops/cli.py alerts --active

# Full-text search
docker exec medops-core python medops/cli.py search "biologic tissue spine"

# Add device to formulary
docker exec medops-core python medops/cli.py formulary --add --di "00843197107103" --category hemostatics

# Rebuild GMDN index
docker exec medops-core python medops/cli.py db --gmdn-build

# Initialize empty knowledge base
docker exec medops-core python medops/cli.py db --init

# Force weekly digest delivery
docker exec medops-core python medops/pipeline.py --mode digest

# Check containers
docker compose ps
docker compose logs -f medops
```

---

*Document ID: MS-0002*  
*Companion document: MS-0001 — Data Architecture & Output Formats*  
*System: MedOps Intelligence OS, Thought Reliquary (Ubuntu 24.04, 192.168.4.100)*  
*All API endpoints verified against public documentation as of June 2026.*
