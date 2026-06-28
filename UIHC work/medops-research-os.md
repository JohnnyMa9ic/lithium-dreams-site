# UIHC MedOps Research OS — Core Framework
## Medical Device Intelligence System for Perioperative Supply Chain

---

```
DOCUMENT ID:     MS-0001
VERSION:         1.0
DATE:            June 2026
AUTHOR:          J. Burroughs, Supply Chain / Perioperative Services
INSTITUTION:     University of Iowa Hospitals & Clinics (UIHC)
CLASSIFICATION:  Internal — Operational Use
STATUS:          ACTIVE
```

---

## TABLE OF CONTENTS

1. [System Architecture](#section-1-the-system-architecture)
2. [Data Sources & API Architecture](#section-2-data-sources--api-architecture)
3. [The Device Brief (Output Format 1)](#section-3-the-device-brief-output-format-1)
4. [The Competitive Matrix (Output Format 2)](#section-4-the-competitive-matrix-output-format-2)
5. [The Substitution Recommendation (Output Format 3)](#section-5-the-substitution-recommendation-output-format-3)
6. [Device Category Modules](#section-6-the-device-category-modules)
7. [Emerging Technology Brief Format](#section-7-the-emerging-technology-brief-format)

---

---

# SECTION 1: THE SYSTEM ARCHITECTURE

## 1.1 What This System Is

The **UIHC MedOps Research OS** is a personal AI-orchestrated research and synthesis engine for medical device supply chain intelligence. It ingests structured data from public regulatory databases, synthesizes competitive intelligence via LLM, and produces formatted evaluation outputs for procurement decision support.

It is built on the same architecture as the LDI content production engine — Hermes orchestration, Claude API, Python, Ollama local inference, running on the Thought Reliquary (Ubuntu 24.04). The pipeline logic is identical. The domain is different.

**What it is:**
- A personal research synthesis engine for perioperative supply chain work
- An AI-orchestrated pipeline: device data in → competitive intelligence out → structured brief published
- A repeatable, auditable workflow for new product evaluation, category review, and substitution analysis
- Built on 100% public regulatory data (FDA, NLM) with no proprietary data requirements to function

**What it is not:**
- A replacement for clinical judgment — synthesis supports, not supplants, clinical and procurement decision-making
- A commercial product — this is a personal professional intelligence OS; no PHI is processed
- A real-time pricing feed — GPO contract pricing cannot be stored; price tiers (Entry/Mid/Premium) are used instead of specific dollar values
- A compliance system — outputs are decision support documents, not regulatory submissions

---

## 1.2 The Pipeline

The pipeline mirrors the LDI episode production workflow directly:

| LDI Content Engine | MedOps Research OS |
|---|---|
| TRIGGER: New topic, listener request, editorial cycle | TRIGGER: New device rep, category review, recall, contract renewal |
| DATA: Research brief, source documents, archives | DATA: ACCESSGUDID + OpenFDA + PubMed + vendor data |
| SYNTHESIS: Claude writes script, episode dossier | SYNTHESIS: Claude classifies, compares, flags, scores |
| OUTPUT: Video script / Podcast / Dossier | OUTPUT: Device Brief / Competitive Matrix / Substitution Rec |
| ARCHIVE: Thought Reliquary knowledge base | ARCHIVE: Searchable device intelligence library |

```
╔══════════════════════════════════════════════════════════════════════════╗
║                    UIHC MedOps Research OS — Pipeline                    ║
╚══════════════════════════════════════════════════════════════════════════╝

  TRIGGER
  ┌──────────────────────────────────────────────────────────────────┐
  │  New device evaluation  │  Category review  │  Substitution need │
  │  Recall alert           │  Contract renewal │  Emerging tech scan │
  └──────────────────────────────────┬───────────────────────────────┘
                                     │
                                     ▼
  DATA COLLECTION
  ┌──────────────────────────────────────────────────────────────────┐
  │                                                                    │
  │  ┌─────────────────┐   ┌──────────────────┐   ┌───────────────┐  │
  │  │  ACCESSGUDID    │   │    OpenFDA       │   │   PubMed /    │  │
  │  │  (NLM API v2)   │   │  (5 endpoints)   │   │  ClinTrials   │  │
  │  │                 │   │                  │   │               │  │
  │  │  DI → Device    │   │  510(k)/PMA      │   │  Literature   │  │
  │  │  record, GMDN,  │   │  MAUDE events    │   │  synthesis    │  │
  │  │  MRI safety,    │   │  Recalls         │   │  via E-utils  │  │
  │  │  sterility,     │   │  Classification  │   │               │  │
  │  │  device class   │   │  Registry/List   │   └───────────────┘  │
  │  └────────┬────────┘   └────────┬─────────┘                      │
  │           │                     │            ┌───────────────┐    │
  │           └─────────────────────┘            │  Vendor data  │    │
  │                     │                        │  (manual)     │    │
  │                     └────────────────────────┤  GPO portal   │    │
  │                                              │  SEC EDGAR    │    │
  │                                              └───────────────┘    │
  └──────────────────────────────────┬───────────────────────────────┘
                                     │
                                     ▼
  SYNTHESIS (Claude API + Hermes Orchestration)
  ┌──────────────────────────────────────────────────────────────────┐
  │                                                                    │
  │   CLASSIFY      COMPARE       FLAG           SCORE                │
  │   Device class  GMDN peers    Recalls        10-dimension         │
  │   Product code  Spec matrix   MAUDE spikes   scoring rubric      │
  │   Regulatory    Clinical ev.  Data gaps      VAC-ready output    │
  │   pathway       Cost tier     Safety delta                        │
  │                                                                    │
  └──────────────────────────────────┬───────────────────────────────┘
                                     │
                                     ▼
  OUTPUT (3 Formats)
  ┌─────────────────┬────────────────────────┬────────────────────────┐
  │  DEVICE BRIEF   │  COMPETITIVE MATRIX    │  SUBSTITUTION REC      │
  │                 │                        │                        │
  │  Single device  │  Multi-device category │  A → B recommendation  │
  │  full profile   │  comparison table      │  clinical + supply     │
  │  (Sec. 3)       │  (Sec. 4)              │  chain rationale       │
  │                 │                        │  (Sec. 5)              │
  └────────┬────────┴──────────┬─────────────┴────────────┬───────────┘
           │                   │                           │
           └───────────────────┼───────────────────────────┘
                               │
                               ▼
  ARCHIVE
  ┌──────────────────────────────────────────────────────────────────┐
  │  Thought Reliquary — Local knowledge base                         │
  │  ┌────────────────────────────────────────────────────────────┐   │
  │  │  /medops/briefs/       — all Device Briefs (UIHC-DEV-*)    │   │
  │  │  /medops/matrices/     — Competitive Matrices              │   │
  │  │  /medops/substitutions/— Substitution Recommendations      │   │
  │  │  /medops/emerging/     — Emerging Tech Briefs (EMT-*)      │   │
  │  │  /medops/categories/   — Category Intelligence Modules     │   │
  │  │  /medops/archive/gudid/— Local GUDID SQLite database       │   │
  │  └────────────────────────────────────────────────────────────┘   │
  └──────────────────────────────────────────────────────────────────┘
```

---

## 1.3 The Three Output Formats

These map directly to the three LDI output formats. Same architecture. Different domain.

| Output Format | LDI Equivalent | Trigger | Primary Audience |
|---|---|---|---|
| **Device Brief** | Episode dossier | New product rep visit, product intro | VAC, Department Chair, self |
| **Competitive Matrix** | 3-theory comparison table | Category review, contract renewal | VAC, GPO negotiation team |
| **Substitution Recommendation** | Deep-dive episode | Recall, backorder, cost initiative | VAC chair, CMO/CNO, Director of Supply Chain |

---

---

# SECTION 2: DATA SOURCES & API ARCHITECTURE

## 2.1 Primary Data Source: ACCESSGUDID (NLM API v2)

AccessGUDID is the FDA's Global Unique Device Identification Database, operated by the National Library of Medicine. It is the authoritative public repository of device identification data for all medical devices distributed in the US. As of mid-2026, it contains over **5 million device records** from approximately **11,779 distinct labelers**.

```
Base URL:      https://accessgudid.nlm.nih.gov/api/v2/
Authentication: None required — fully public
Rate Limits:   Not explicitly documented by NLM; implement conservative 1-second delays
```

### Key Endpoints

| Endpoint | Method | Required Parameter | Description |
|---|---|---|---|
| `/devices/lookup.json` | GET | `di=[DI]` | Lookup by Device Identifier |
| `/devices/lookup.json` | GET | `udi=[UDI]` | Lookup by full UDI string (percent-encoded) |
| `/devices/lookup.json` | GET | `record_key=[UUID]` | Lookup by Public Device Record Key |
| `/api/v2/parse_udi` | GET | Full UDI string | Parse UDI into DI + PI components |
| `/api/v2/devices/snomed.json` | GET | — | SNOMED mapping (requires UMLS ticket) |

> **Note:** Use v2 only. v1 is deprecated.

### Key Fields to Extract Per Device Record

| Field | JSON Path | Required? | Notes |
|---|---|---|---|
| Device Identifier (DI) | `gudid.device.identifiers.identifier.deviceId` | Yes | Core identifier |
| Brand Name | `gudid.device.brandName` | Yes | |
| Version/Model Number | `gudid.device.versionModelNumber` | Yes | |
| Catalog Number | `gudid.device.catalogNumber` | **Optional** | Frequently missing — critical gap |
| Company Name | `gudid.device.companyName` | Yes | |
| Device Description | `gudid.device.deviceDescription` | Optional | 20.3% of records missing |
| GMDN Preferred Term Name | `gudid.device.gmdnTerms.gmdn.gmdnPTName` | Yes | Primary substitution grouping key |
| GMDN Definition | `gudid.device.gmdnTerms.gmdn.gmdnPTDefinition` | Auto | |
| GMDN Term Code | (5-digit numeric) | Yes (v3) | Key for programmatic grouping |
| FDA Product Code | `gudid.device.productCodes.fdaProductCode.productCode` | Yes | 3-letter code |
| Device Class | `productCodes.productCode.deviceClass` | Yes | 1 / 2 / 3 |
| Sterile | `gudid.device.sterilization.deviceSterile` | Yes | Boolean |
| MRI Safety Status | `gudid.device.MRISafetyStatus` | Yes | MR Safe / MR Conditional / MR Unsafe |
| Single Use | `gudid.device.singleUse` | Yes | Boolean |
| Lot Batch Tracking | `gudid.device.lotBatch` | Yes | PI flag |
| Expiration Date Tracking | `gudid.device.expirationDate` | Yes | PI flag |
| Labeler DUNS Number | `gudid.device.dunsNumber` | Yes | Manufacturer financial lookup key |
| Commercial Distribution Status | `gudid.device.deviceCommDistributionStatus` | Yes | "In Commercial Distribution" = active |

### Bulk Download (for Local Database)

| Download Type | Frequency | RSS Feed |
|---|---|---|
| Latest Full Release | Monthly (1st) | `https://accessgudid.nlm.nih.gov/download.rss?files=full` |
| Daily Updates | Daily | `https://accessgudid.nlm.nih.gov/download.rss?files=daily` |
| Weekly Updates | Weekly | `https://accessgudid.nlm.nih.gov/download.rss?files=weekly` |

Full release includes pipe-delimited CSV files suitable for SQLite import. See Section 2.7 (Bulk Download Python) for implementation.

### ACCESSGUDID Limitations (The Five Critical Gaps)

| Gap | Impact | Mitigation |
|---|---|---|
| **1. Catalog number is optional** | Cannot reliably match to hospital item master by catalog # alone | Use DI + brand name + version as primary keys; manually verify catalog # with vendor |
| **2. Device description missing in 20.3% of records** | Substitution analysis loses narrative context for many records | Cross-reference FDA product code description; request IFU from vendor |
| **3. No pricing data** | Cannot assess cost equivalence from GUDID alone | Use GPO tier reference + published benchmarks (Curvo); store as tier (Entry/Mid/Premium) only |
| **4. No clinical outcomes data** | GUDID confirms device type, not clinical performance | Chain to PubMed E-utilities; cross-reference AJRR for implants |
| **5. No direct recall linkage** | GUDID DI does not automatically link to recall records | Chain to OpenFDA `/device/recall.json` by product code + company name |

---

### ACCESSGUDID Python Functions

```python
import requests
import time
from typing import Optional

GUDID_BASE = "https://accessgudid.nlm.nih.gov/api/v2"

def lookup_device_by_di(di: str) -> dict:
    """
    Look up a device record from ACCESSGUDID by Device Identifier (DI).
    
    Args:
        di: The Device Identifier (static barcode portion of the UDI)
    
    Returns:
        Full device record as dict, or raises on error
    """
    url = f"{GUDID_BASE}/devices/lookup.json"
    params = {"di": di}
    
    try:
        response = requests.get(url, params=params, timeout=15)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as e:
        if response.status_code == 404:
            return {"error": "DI not found in ACCESSGUDID", "di": di}
        raise RuntimeError(f"ACCESSGUDID lookup failed for DI {di}: {e}")
    except requests.exceptions.Timeout:
        raise RuntimeError(f"ACCESSGUDID request timed out for DI {di}")


def lookup_device_by_udi(udi: str) -> dict:
    """
    Look up a device record from ACCESSGUDID by full UDI string.
    Also returns parsed Production Identifier components (lot, serial, expiration).
    
    Args:
        udi: Full UDI string from device label (will be percent-encoded automatically)
    
    Returns:
        Device record + parsed UDI header fields
    """
    url = f"{GUDID_BASE}/devices/lookup.json"
    params = {"udi": udi}
    
    try:
        response = requests.get(url, params=params, timeout=15)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as e:
        if response.status_code == 404:
            return {"error": "UDI not found in ACCESSGUDID", "udi": udi}
        raise RuntimeError(f"ACCESSGUDID UDI lookup failed: {e}")


def extract_device_profile(gudid_record: dict) -> dict:
    """
    Extract the key fields needed for device evaluation from a raw ACCESSGUDID response.
    Returns a flattened dict suitable for Device Brief generation.
    
    Args:
        gudid_record: Raw JSON response from ACCESSGUDID lookup
    
    Returns:
        Flattened device profile dict
    """
    device = gudid_record.get("gudid", {}).get("device", {})
    
    # Extract product code (may be list or single)
    product_codes = device.get("productCodes", {}).get("fdaProductCode", {})
    if isinstance(product_codes, list):
        primary_code = product_codes[0]
    else:
        primary_code = product_codes
    
    # Extract GMDN (may be list or single)
    gmdn_terms = device.get("gmdnTerms", {}).get("gmdn", {})
    if isinstance(gmdn_terms, list):
        primary_gmdn = gmdn_terms[0]
    else:
        primary_gmdn = gmdn_terms
    
    return {
        "di": device.get("identifiers", {}).get("identifier", {}).get("deviceId"),
        "brand_name": device.get("brandName"),
        "version_model": device.get("versionModelNumber"),
        "catalog_number": device.get("catalogNumber"),  # May be None
        "company_name": device.get("companyName"),
        "device_description": device.get("deviceDescription"),  # May be None
        "labeler_duns": device.get("dunsNumber"),
        "product_code": primary_code.get("productCode"),
        "product_code_name": primary_code.get("productCodeName"),
        "device_class": primary_code.get("deviceClass"),
        "regulation_number": primary_code.get("regulationNumber"),
        "implant_flag": primary_code.get("implantFlag"),
        "gmdn_term_name": primary_gmdn.get("gmdnPTName"),
        "gmdn_definition": primary_gmdn.get("gmdnPTDefinition"),
        "mri_safety": device.get("MRISafetyStatus"),
        "single_use": device.get("singleUse"),
        "sterile": device.get("sterilization", {}).get("deviceSterile"),
        "sterilization_method": device.get("sterilization", {}).get("methodTypes"),
        "lot_batch_tracking": device.get("lotBatch"),
        "expiration_date_tracking": device.get("expirationDate"),
        "distribution_status": device.get("deviceCommDistributionStatus"),
        "distribution_end_date": device.get("deviceCommDistributionEndDate"),
        "hctp": device.get("deviceHCTP"),
        "combination_product": device.get("deviceCombinationProduct"),
        "life_sustain_support": primary_code.get("lifeSustainSupportFlag"),
    }


def data_quality_check(device_profile: dict) -> dict:
    """
    Run the 5 mandatory data quality checks on an ACCESSGUDID device record
    before using it in analysis. Returns a quality report.
    
    Args:
        device_profile: Flattened device profile from extract_device_profile()
    
    Returns:
        Quality report with pass/fail status and warnings
    """
    checks = {
        "CHECK_1_DI_PRESENT": {
            "description": "Device Identifier (DI) is present and non-empty",
            "pass": bool(device_profile.get("di")),
            "severity": "CRITICAL",
            "impact": "Cannot process without DI — abort pipeline"
        },
        "CHECK_2_DISTRIBUTION_ACTIVE": {
            "description": "Device is in active commercial distribution",
            "pass": device_profile.get("distribution_status") == "In Commercial Distribution",
            "severity": "HIGH",
            "impact": "Discontinued device — flag for substitution, do not recommend procurement"
        },
        "CHECK_3_PRODUCT_CODE_PRESENT": {
            "description": "FDA Product Code is present",
            "pass": bool(device_profile.get("product_code")),
            "severity": "HIGH",
            "impact": "Cannot chain to OpenFDA 510(k)/PMA/MAUDE/Recall without product code"
        },
        "CHECK_4_GMDN_PRESENT": {
            "description": "GMDN term name is present",
            "pass": bool(device_profile.get("gmdn_term_name")),
            "severity": "MEDIUM",
            "impact": "Cannot perform GMDN-based substitution grouping — manual category assignment required"
        },
        "CHECK_5_DESCRIPTION_PRESENT": {
            "description": "Device description is present (optional field — 20.3% missing across all records)",
            "pass": bool(device_profile.get("device_description")),
            "severity": "LOW",
            "impact": "Clinical Evidence Summary may be less accurate; cross-reference product code name as fallback"
        }
    }
    
    critical_failures = [k for k, v in checks.items() if not v["pass"] and v["severity"] == "CRITICAL"]
    high_failures = [k for k, v in checks.items() if not v["pass"] and v["severity"] == "HIGH"]
    
    return {
        "device_di": device_profile.get("di"),
        "brand_name": device_profile.get("brand_name"),
        "quality_checks": checks,
        "pipeline_clear": len(critical_failures) == 0,
        "warnings": len(high_failures) > 0,
        "critical_failures": critical_failures,
        "high_failures": high_failures
    }
```

---

## 2.2 Primary Data Source: OpenFDA Device Endpoints

```
Base URL:      https://api.fda.gov
Documentation: https://open.fda.gov/apis/
Authentication: None required (limited). Free API key increases rate limits.
API Key Setup: https://open.fda.gov/apis/authentication/
               No approval required — provide email, agree to terms, receive key immediately.
               Append to all requests: &api_key=YOUR_KEY
```

### Rate Limits

| Authentication | Requests/Minute | Requests/Day | Burst Limit |
|---|---|---|---|
| No API key | 40/min per IP | 1,000/day per IP | 4 req/sec |
| With free API key | **240/min per key** | 120,000/day per key | 4 req/sec |
| Exceeded limit | HTTP 429 | — | Back off 60 seconds |

**Pagination cap:** `skip + limit ≤ 25,000`. For datasets exceeding 25,000 records, segment queries by narrow date ranges.

**Recommended implementation:** Initialize once as `OpenFDAClient(api_key="YOUR_KEY")` and use across all endpoint calls. See Section 2.7 for the rate-limited client class.

---

### OpenFDA Python Functions

#### 1. 510(k) Clearance Lookup

```python
import requests
import time
from typing import Optional

OPENFDA_BASE = "https://api.fda.gov/device"
API_KEY = "YOUR_API_KEY"  # Register at https://open.fda.gov/apis/authentication/

def get_510k_clearances(
    product_code: Optional[str] = None,
    applicant: Optional[str] = None,
    k_number: Optional[str] = None,
    limit: int = 10
) -> dict:
    """
    Query the FDA 510(k) premarket notification database.
    
    Returns clearance records including: applicant, device name, decision date,
    product code, predicate device reference, and clearance type.
    
    Args:
        product_code: 3-letter FDA product code (e.g., "HRS" for hip implants)
        applicant:    Company name (partial match supported)
        k_number:     Specific 510(k) number (e.g., "K173929")
        limit:        Max records to return (max 1000)
    
    Returns:
        Raw OpenFDA JSON response with 'meta' and 'results' keys
    """
    if not any([product_code, applicant, k_number]):
        raise ValueError("At least one search parameter required")
    
    search_parts = []
    if product_code:
        search_parts.append(f'product_code:"{product_code}"')
    if applicant:
        search_parts.append(f'applicant:"{applicant}"')
    if k_number:
        search_parts.append(f'k_number:"{k_number}"')
    
    params = {
        "search": " AND ".join(search_parts),
        "limit": limit,
        "sort": "decision_date:desc",
        "api_key": API_KEY
    }
    
    try:
        time.sleep(0.25)  # Respect 4 req/sec burst limit
        response = requests.get(f"{OPENFDA_BASE}/510k.json", params=params, timeout=15)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as e:
        if response.status_code == 404:
            return {"meta": {"results": {"total": 0}}, "results": []}
        if response.status_code == 429:
            time.sleep(60)
            return get_510k_clearances(product_code, applicant, k_number, limit)
        raise RuntimeError(f"510(k) query failed: {e}")
```

#### 2. PMA (Premarket Approval) Lookup

```python
def get_pma_approvals(
    applicant: Optional[str] = None,
    generic_name: Optional[str] = None,
    trade_name: Optional[str] = None,
    product_code: Optional[str] = None,
    limit: int = 10
) -> dict:
    """
    Query the FDA Premarket Approval (PMA) database.
    Required for Class III devices (breast implants, some biologics/burn products,
    cardiac devices). A PMA device cannot be substituted with a 510(k)-cleared device.
    
    Key fields returned: applicant, generic_name, trade_name, approval_date,
    supplement_reason, advisory_committee.
    
    Args:
        applicant:    Company name (e.g., "Allergan", "Mentor")
        generic_name: Generic device name
        trade_name:   Brand/trade name
        product_code: 3-letter FDA product code (e.g., "QDD" for silicone gel breast implants)
        limit:        Max records to return
    
    Returns:
        Raw OpenFDA JSON response
    """
    search_parts = []
    if applicant:
        search_parts.append(f'applicant:"{applicant}"')
    if generic_name:
        search_parts.append(f'generic_name:"{generic_name}"')
    if trade_name:
        search_parts.append(f'trade_name:"{trade_name}"')
    if product_code:
        search_parts.append(f'product_code:"{product_code}"')
    
    if not search_parts:
        raise ValueError("At least one search parameter required")
    
    params = {
        "search": " AND ".join(search_parts),
        "limit": limit,
        "sort": "approval_date:desc",
        "api_key": API_KEY
    }
    
    try:
        time.sleep(0.25)
        response = requests.get(f"{OPENFDA_BASE}/pma.json", params=params, timeout=15)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as e:
        if response.status_code == 404:
            return {"meta": {"results": {"total": 0}}, "results": []}
        if response.status_code == 429:
            time.sleep(60)
            return get_pma_approvals(applicant, generic_name, trade_name, product_code, limit)
        raise RuntimeError(f"PMA query failed: {e}")
```

#### 3. Recall Record Lookup

```python
def get_device_recalls(
    product_code: Optional[str] = None,
    firm_name: Optional[str] = None,
    classification: Optional[str] = None,
    status: str = None,
    date_from: Optional[str] = None,
    limit: int = 20
) -> dict:
    """
    Query FDA device recall records.
    
    Recall classification: Class I = most serious risk; Class II = may cause harm;
    Class III = unlikely to cause harm.
    
    Args:
        product_code:   3-letter FDA product code
        firm_name:      Recalling firm name (partial match)
        classification: "Class I", "Class II", or "Class III"
        status:         "Ongoing", "Terminated", or "Completed"
        date_from:      Filter recalls initiated after this date (YYYY-MM-DD)
        limit:          Max records to return
    
    Returns:
        Raw OpenFDA JSON response. Check for 'status':'Ongoing' for active recalls.
    """
    search_parts = []
    if product_code:
        search_parts.append(f'product_code:"{product_code}"')
    if firm_name:
        search_parts.append(f'recalling_firm:"{firm_name}"')
    if classification:
        search_parts.append(f'classification:"{classification}"')
    if status:
        search_parts.append(f'status:"{status}"')
    if date_from:
        search_parts.append(f'recall_initiation_date:[{date_from} TO *]')
    
    if not search_parts:
        raise ValueError("At least one search parameter required")
    
    params = {
        "search": " AND ".join(search_parts),
        "limit": limit,
        "sort": "recall_initiation_date:desc",
        "api_key": API_KEY
    }
    
    try:
        time.sleep(0.25)
        response = requests.get(f"{OPENFDA_BASE}/recall.json", params=params, timeout=15)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as e:
        if response.status_code == 404:
            return {"meta": {"results": {"total": 0}}, "results": [],
                    "note": "No recall records found for this query"}
        if response.status_code == 429:
            time.sleep(60)
            return get_device_recalls(product_code, firm_name, classification, status, date_from, limit)
        raise RuntimeError(f"Recall query failed: {e}")


def check_active_class_one_recalls(product_code: str, firm_name: Optional[str] = None) -> dict:
    """
    Convenience function: check for any active Class I recalls for a device.
    Class I = most serious; triggers immediate action in procurement workflow.
    
    Returns:
        Dict with 'has_active_class_one' bool and recall details if any found
    """
    results = get_device_recalls(
        product_code=product_code,
        firm_name=firm_name,
        classification="Class I",
        status="Ongoing",
        limit=10
    )
    
    active_recalls = results.get("results", [])
    return {
        "has_active_class_one": len(active_recalls) > 0,
        "count": len(active_recalls),
        "recalls": active_recalls
    }
```

#### 4. MAUDE Adverse Events Query

```python
def get_maude_events(
    product_code: Optional[str] = None,
    brand_name: Optional[str] = None,
    catalog_number: Optional[str] = None,
    event_type: Optional[str] = None,
    date_from: Optional[str] = None,
    limit: int = 100,
    count_by_brand: bool = False
) -> dict:
    """
    Query the FDA MAUDE (Manufacturer and User Facility Device Experience) adverse events database.
    ~24M+ records from ~1992 to present. Updated weekly.
    
    IMPORTANT INTERPRETATION NOTE: Raw MAUDE volume is NOT a direct safety signal.
    High-volume products will have more reports. Always normalize by market share estimate.
    MAUDE is passive surveillance — all adverse events are under-reported.
    No causal relationship is established by a MAUDE report.
    
    Args:
        product_code:   3-letter FDA product code (recommended for category-level queries)
        brand_name:     Device brand name
        catalog_number: Device catalog number
        event_type:     "Death", "Injury", "Malfunction", or "Other"
        date_from:      Filter events received after this date (YYYY-MM-DD)
        limit:          Max records to return
        count_by_brand: If True, return aggregated counts by brand_name (for category comparison)
    
    Returns:
        Raw OpenFDA JSON. If count_by_brand=True, returns count aggregation.
    """
    search_parts = []
    if product_code:
        search_parts.append(f'device.product_code:"{product_code}"')
    if brand_name:
        search_parts.append(f'device.brand_name:"{brand_name}"')
    if catalog_number:
        search_parts.append(f'device.catalog_number:"{catalog_number}"')
    if event_type:
        search_parts.append(f'event_type:"{event_type}"')
    if date_from:
        search_parts.append(f'date_received:[{date_from} TO *]')
    
    if not search_parts:
        raise ValueError("At least one search parameter required")
    
    params = {
        "search": " AND ".join(search_parts),
        "api_key": API_KEY
    }
    
    if count_by_brand:
        params["count"] = "device.brand_name.exact"
    else:
        params["limit"] = limit
        params["sort"] = "date_received:desc"
    
    try:
        time.sleep(0.25)
        response = requests.get(f"{OPENFDA_BASE}/event.json", params=params, timeout=15)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as e:
        if response.status_code == 404:
            return {"meta": {"results": {"total": 0}}, "results": []}
        if response.status_code == 429:
            time.sleep(60)
            return get_maude_events(product_code, brand_name, catalog_number,
                                    event_type, date_from, limit, count_by_brand)
        raise RuntimeError(f"MAUDE query failed: {e}")


def get_maude_death_count(product_code: str, date_from: str = "2021-01-01") -> int:
    """Get count of Death event type reports for a product code in a date range."""
    result = get_maude_events(
        product_code=product_code,
        event_type="Death",
        date_from=date_from,
        limit=1
    )
    return result.get("meta", {}).get("results", {}).get("total", 0)
```

#### 5. Device Classification Lookup

```python
def get_device_classification(
    product_code: Optional[str] = None,
    device_name: Optional[str] = None,
    device_class: Optional[str] = None,
    review_panel: Optional[str] = None,
    limit: int = 20
) -> dict:
    """
    Query the FDA device classification database.
    Maps product codes to device class (I/II/III), regulation number, review panel,
    submission type, and implant/life-support flags.
    
    Use this to confirm the regulatory pathway requirement for any device:
    - device_class "1" = generally exempt (most Class I)
    - device_class "2" = 510(k) required (most surgical supplies)
    - device_class "3" = PMA required (breast implants, high-risk devices)
    
    Args:
        product_code:  3-letter FDA product code (e.g., "HRS", "GAK", "QDD")
        device_name:   Generic device name (partial match)
        device_class:  "1", "2", or "3"
        review_panel:  FDA review panel code (e.g., "SU" = General & Plastic Surgery)
        limit:         Max records to return
    
    Returns:
        Raw OpenFDA JSON with classification records
    """
    search_parts = []
    if product_code:
        search_parts.append(f'product_code:"{product_code}"')
    if device_name:
        search_parts.append(f'device_name:"{device_name}"')
    if device_class:
        search_parts.append(f'device_class:"{device_class}"')
    if review_panel:
        search_parts.append(f'review_panel:"{review_panel}"')
    
    if not search_parts:
        raise ValueError("At least one search parameter required")
    
    params = {
        "search": " AND ".join(search_parts),
        "limit": limit,
        "api_key": API_KEY
    }
    
    try:
        time.sleep(0.25)
        response = requests.get(f"{OPENFDA_BASE}/classification.json", params=params, timeout=15)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as e:
        if response.status_code == 404:
            return {"meta": {"results": {"total": 0}}, "results": []}
        if response.status_code == 429:
            time.sleep(60)
            return get_device_classification(product_code, device_name, device_class, review_panel, limit)
        raise RuntimeError(f"Classification query failed: {e}")
```

---

## 2.3 The Full Device Dossier Chain

Chain all five sources together for a complete device profile:

```python
def build_device_dossier(di: str) -> dict:
    """
    Build a complete device dossier by chaining ACCESSGUDID → OpenFDA endpoints.
    This is the core data collection function for Device Brief generation.
    
    Pipeline:
      1. ACCESSGUDID → device record, GMDN, product code, safety flags
      2. 510(k)/PMA → clearance history, predicate device
      3. Classification → device class, regulation number, implant flag
      4. MAUDE → adverse event counts by brand (normalized comparison)
      5. Recalls → active/historical recall records
    
    Args:
        di: Device Identifier (DI)
    
    Returns:
        Complete dossier dict ready for Claude API synthesis
    """
    print(f"[MedOps] Building dossier for DI: {di}")
    
    # Step 1: ACCESSGUDID — base device record
    raw_gudid = lookup_device_by_di(di)
    profile = extract_device_profile(raw_gudid)
    
    quality = data_quality_check(profile)
    if not quality["pipeline_clear"]:
        return {"error": "Data quality check failed", "quality_report": quality}
    
    product_code = profile.get("product_code")
    company_name = profile.get("company_name")
    
    # Step 2: 510(k) or PMA clearance
    clearances_510k = get_510k_clearances(product_code=product_code, limit=5)
    clearances_pma = {}
    if profile.get("device_class") == "3":
        clearances_pma = get_pma_approvals(
            applicant=company_name, product_code=product_code, limit=5
        )
    
    # Step 3: Device classification
    classification = get_device_classification(product_code=product_code, limit=1)
    
    # Step 4: MAUDE — brand-level counts for category comparison
    maude_brand_counts = get_maude_events(
        product_code=product_code,
        count_by_brand=True
    )
    # Also get recent adverse events for this specific brand
    brand_name = profile.get("brand_name")
    maude_recent = get_maude_events(
        product_code=product_code,
        brand_name=brand_name,
        date_from="2021-01-01",
        limit=20
    )
    
    # Step 5: Recalls — last 5 years
    recalls = get_device_recalls(
        product_code=product_code,
        firm_name=company_name,
        date_from="2021-01-01",
        limit=10
    )
    active_class_one = check_active_class_one_recalls(product_code, company_name)
    
    return {
        "device_profile": profile,
        "quality_report": quality,
        "clearances_510k": clearances_510k.get("results", []),
        "clearances_pma": clearances_pma.get("results", []),
        "classification": classification.get("results", []),
        "maude_brand_counts": maude_brand_counts.get("results", []),
        "maude_recent_events": maude_recent.get("results", []),
        "maude_recent_total": maude_recent.get("meta", {}).get("results", {}).get("total", 0),
        "recalls": recalls.get("results", []),
        "active_class_one_recall": active_class_one,
    }
```

---

## 2.4 Supplementary Sources (Manual / Semi-Automated)

| Source | Access Method | Use Case | API / URL |
|---|---|---|---|
| **PubMed (NCBI E-utilities)** | API (free, no auth) | Clinical literature search on device efficacy and safety | `https://eutils.ncbi.nlm.nih.gov/entrez/eutils/` |
| **ClinicalTrials.gov API v2** | API (free, no auth) | Ongoing studies involving specific devices; pipeline intelligence | `https://clinicaltrials.gov/api/v2/` |
| **SEC EDGAR** | API (free) | Public company filings; vendor financial stability assessment | `https://www.sec.gov/cgi-bin/browse-edgar` |
| **AAOS / AJRR** | Manual | Orthopaedic outcomes data; joint replacement registry survivorship | `https://www.aaos.org/registry/ajrr/` |
| **AORN** | Manual | Perioperative standards and recommended practices | `https://www.aorn.org` |
| **NASS** | Manual | Spine surgery clinical guidelines | `https://www.spine.org` |
| **SAGES** | Manual | GI / laparoscopic surgery evidence-based documents | `https://www.sages.org` |
| **ASPS** | Manual | Plastic surgery safety guidance | `https://www.plasticsurgery.org` |
| **GPO Portals (Vizient, Premier)** | Manual — proprietary | Contract status, tier pricing — cannot be stored | Login required; reference by tier only |
| **Market Scope** | Commercial | Ophthalmology market intelligence | `https://www.market-scope.com` |
| **Curvo Labs** | Commercial | ASP benchmarking at SKU level (GPO-neutral) | `https://www.gocurvo.com` |

---

## 2.5 The Rate-Limited OpenFDA Client (Production Implementation)

```python
import time
import requests
from typing import Optional


class OpenFDAClient:
    """
    Rate-limited OpenFDA client with retry logic.
    Initialize once; reuse across all endpoint calls in a pipeline run.
    
    Usage:
        client = OpenFDAClient(api_key="YOUR_KEY")
        results = client.query("device/510k.json", {"search": "product_code:HRS", "limit": 10})
        all_recalls = client.paginate("device/recall.json", "product_code:HRS", max_records=500)
    """
    
    BASE_URL = "https://api.fda.gov"
    
    def __init__(self, api_key: Optional[str] = None):
        self.api_key = api_key
        # 240 req/min with key = 4/sec; 40 req/min without = ~0.67/sec
        # Use 0.25s delay (4/sec) with key, 1.5s without
        self.delay = 0.25 if api_key else 1.5
        self.last_request_time = 0
    
    def query(self, endpoint: str, params: dict) -> dict:
        """
        Make a single rate-limited query to an OpenFDA endpoint.
        Handles HTTP 429 (rate limit exceeded) with exponential backoff.
        """
        elapsed = time.time() - self.last_request_time
        if elapsed < self.delay:
            time.sleep(self.delay - elapsed)
        
        if self.api_key:
            params = {**params, "api_key": self.api_key}
        
        url = f"{self.BASE_URL}/{endpoint}"
        
        for attempt in range(3):
            try:
                response = requests.get(url, params=params, timeout=20)
                self.last_request_time = time.time()
                
                if response.status_code == 429:
                    backoff = 60 * (attempt + 1)
                    print(f"[OpenFDA] Rate limit hit. Waiting {backoff}s...")
                    time.sleep(backoff)
                    continue
                
                if response.status_code == 404:
                    return {"meta": {"results": {"total": 0}}, "results": []}
                
                response.raise_for_status()
                return response.json()
                
            except requests.exceptions.Timeout:
                if attempt == 2:
                    raise RuntimeError(f"OpenFDA request timed out after 3 attempts: {url}")
                time.sleep(5)
        
        raise RuntimeError(f"OpenFDA query failed after 3 attempts: {url}")
    
    def paginate(
        self, endpoint: str, search: str,
        limit: int = 1000, max_records: int = 25000
    ) -> list:
        """
        Paginate through OpenFDA results up to the 25,000-record hard cap.
        For datasets > 25,000 records, use narrow date ranges to segment.
        
        Args:
            endpoint:    OpenFDA endpoint (e.g., "device/recall.json")
            search:      Search query string
            limit:       Records per page (max 1000)
            max_records: Total records to retrieve (hard cap: 25000)
        
        Returns:
            List of all result records
        """
        all_results = []
        skip = 0
        
        while skip + limit <= max_records:
            data = self.query(endpoint, {
                "search": search,
                "limit": limit,
                "skip": skip
            })
            
            batch = data.get("results", [])
            all_results.extend(batch)
            
            total = data.get("meta", {}).get("results", {}).get("total", 0)
            
            if len(batch) < limit:
                break
            if skip + limit >= min(total, max_records):
                break
            
            skip += limit
        
        return all_results
```

---

## 2.6 PubMed E-utilities (Literature Synthesis)

```python
import requests
import time
from typing import Optional

PUBMED_BASE = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils"

def search_pubmed(query: str, max_results: int = 20, date_from: Optional[str] = None) -> list:
    """
    Search PubMed for clinical literature on a device or clinical topic.
    Returns a list of PMIDs for downstream abstract retrieval.
    
    Args:
        query:       Search query (e.g., "FLOSEAL hemostasis spine randomized controlled trial")
        max_results: Maximum results to return (default 20)
        date_from:   Filter publications after this year (e.g., "2018")
    
    Returns:
        List of PMIDs
    """
    search_params = {
        "db": "pubmed",
        "term": query,
        "retmax": max_results,
        "retmode": "json",
        "sort": "relevance"
    }
    
    if date_from:
        search_params["mindate"] = date_from
        search_params["datetype"] = "pdat"
    
    time.sleep(0.34)  # NCBI recommends max 3 requests/second without API key
    response = requests.get(f"{PUBMED_BASE}/esearch.fcgi", params=search_params, timeout=15)
    response.raise_for_status()
    
    data = response.json()
    return data.get("esearchresult", {}).get("idlist", [])


def fetch_pubmed_abstracts(pmids: list) -> list:
    """
    Fetch abstracts for a list of PMIDs.
    Returns list of dicts with title, authors, journal, year, abstract text.
    
    Args:
        pmids: List of PubMed IDs (strings or ints)
    
    Returns:
        List of abstract dicts for Claude API synthesis
    """
    if not pmids:
        return []
    
    params = {
        "db": "pubmed",
        "id": ",".join(str(p) for p in pmids),
        "retmode": "xml",
        "rettype": "abstract"
    }
    
    time.sleep(0.34)
    response = requests.get(f"{PUBMED_BASE}/efetch.fcgi", params=params, timeout=30)
    response.raise_for_status()
    
    # Parse XML response — simplified extraction
    # For production: use BioPython Entrez or lxml for robust XML parsing
    import xml.etree.ElementTree as ET
    root = ET.fromstring(response.text)
    
    abstracts = []
    for article in root.findall(".//PubmedArticle"):
        pmid_el = article.find(".//PMID")
        title_el = article.find(".//ArticleTitle")
        abstract_el = article.find(".//AbstractText")
        year_el = article.find(".//PubDate/Year")
        journal_el = article.find(".//Journal/Title")
        
        abstracts.append({
            "pmid": pmid_el.text if pmid_el is not None else None,
            "title": title_el.text if title_el is not None else None,
            "abstract": abstract_el.text if abstract_el is not None else None,
            "year": year_el.text if year_el is not None else None,
            "journal": journal_el.text if journal_el is not None else None,
        })
    
    return abstracts
```

---

## 2.7 ACCESSGUDID Bulk Data Processing (Local SQLite Database)

For high-volume work and fast GMDN-based substitution lookups, maintain a local SQLite mirror of the GUDID full release. Monthly update cycle via RSS-triggered download.

```python
import zipfile
import csv
import io
import sqlite3
import requests
from pathlib import Path
import xml.etree.ElementTree as ET

GUDID_RSS_FULL = "https://accessgudid.nlm.nih.gov/download.rss?files=full"
GUDID_RSS_DAILY = "https://accessgudid.nlm.nih.gov/download.rss?files=daily"
LOCAL_DB_PATH = "/path/to/medops/archive/gudid/gudid.db"


def get_latest_release_url(rss_url: str = GUDID_RSS_FULL) -> str:
    """Parse ACCESSGUDID RSS feed and return the latest release ZIP URL."""
    response = requests.get(rss_url, timeout=30)
    response.raise_for_status()
    
    root = ET.fromstring(response.text)
    # First <enclosure> in the feed is the most recent release
    enclosure = root.find(".//enclosure")
    if enclosure is None:
        raise RuntimeError("No release found in GUDID RSS feed")
    
    return enclosure.get("url")


def download_and_load_gudid(db_path: str = LOCAL_DB_PATH) -> None:
    """
    Download GUDID full release and load pipe-delimited files into SQLite.
    Full release is ~500MB compressed; run monthly or on-demand.
    
    Tables created: device (main), device_gmdn, device_size, device_contact, etc.
    """
    print("[MedOps] Fetching latest GUDID full release URL from RSS...")
    zip_url = get_latest_release_url()
    
    print(f"[MedOps] Downloading: {zip_url}")
    response = requests.get(zip_url, stream=True, timeout=300)
    response.raise_for_status()
    
    content = b"".join(response.iter_content(chunk_size=8192))
    
    conn = sqlite3.connect(db_path)
    conn.execute("PRAGMA journal_mode=WAL")
    
    with zipfile.ZipFile(io.BytesIO(content)) as z:
        for filename in z.namelist():
            if not filename.endswith(".txt"):
                continue
            
            print(f"[MedOps] Loading: {filename}")
            with z.open(filename) as f:
                reader = csv.DictReader(
                    io.TextIOWrapper(f, encoding="utf-8", errors="replace"),
                    delimiter="|"
                )
                table_name = Path(filename).stem.lower().replace(" ", "_")
                rows = list(reader)
                
                if not rows:
                    continue
                
                columns = list(rows[0].keys())
                col_defs = ", ".join(f'"{c}" TEXT' for c in columns)
                
                conn.execute(f'DROP TABLE IF EXISTS "{table_name}"')
                conn.execute(f'CREATE TABLE "{table_name}" ({col_defs})')
                conn.executemany(
                    f'INSERT INTO "{table_name}" VALUES ({", ".join("?" for _ in columns)})',
                    [list(r.values()) for r in rows]
                )
                conn.commit()
                print(f"[MedOps]   → {len(rows):,} records loaded")
    
    # Create indexes for fast lookups
    conn.execute('CREATE INDEX IF NOT EXISTS idx_device_di ON device ("primaryDI")')
    conn.execute('CREATE INDEX IF NOT EXISTS idx_device_company ON device ("companyName")')
    conn.execute('CREATE INDEX IF NOT EXISTS idx_gmdn_code ON device_gmdn ("gmdnPTCode")')
    conn.commit()
    conn.close()
    
    print(f"[MedOps] GUDID database loaded to: {db_path}")


def find_substitutes_by_gmdn(di: str, db_path: str = LOCAL_DB_PATH) -> list:
    """
    Find all active substitute devices sharing the same GMDN term code as the input DI.
    Primary function for substitution candidate identification.
    
    Returns:
        List of substitute device dicts, sorted by company name
    """
    conn = sqlite3.connect(db_path)
    
    # Get GMDN code for target device
    cursor = conn.execute(
        'SELECT "gmdnPTCode" FROM device_gmdn WHERE "primaryDI" = ?', (di,)
    )
    row = cursor.fetchone()
    if not row:
        conn.close()
        return []
    
    gmdn_code = row[0]
    
    # Find all devices with same GMDN in active commercial distribution
    substitutes = conn.execute("""
        SELECT 
            d."primaryDI",
            d."brandName",
            d."catalogNumber",
            d."companyName",
            d."versionModelNumber",
            d."deviceCommDistributionStatus",
            d."singleUse",
            d."deviceSterile",
            d."MRISafetyStatus",
            g."gmdnPTName"
        FROM device d
        JOIN device_gmdn g ON d."primaryDI" = g."primaryDI"
        WHERE g."gmdnPTCode" = ?
          AND d."deviceCommDistributionStatus" = 'In Commercial Distribution'
          AND d."primaryDI" != ?
        ORDER BY d."companyName"
    """, (gmdn_code, di)).fetchall()
    
    conn.close()
    
    return [
        {
            "di": r[0], "brand_name": r[1], "catalog_number": r[2],
            "company_name": r[3], "version_model": r[4], "distribution_status": r[5],
            "single_use": r[6], "sterile": r[7], "mri_safety": r[8], "gmdn_term": r[9]
        }
        for r in substitutes
    ]
```

---

---

# SECTION 3: THE DEVICE BRIEF (OUTPUT FORMAT 1)

## 3.1 What It Is

The Device Brief is a complete single-device profile for new product evaluation. It is generated when a vendor rep submits a new device for consideration, when a recalled item needs an evaluated replacement, or when a new device enters the service line. It is the primary output for VAC submission and department chair review.

Equivalent to the LDI episode dossier: full treatment of a single subject, synthesized from multiple sources, formatted for the intended audience.

---

## 3.2 Device Brief Template

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
DEVICE EVALUATION BRIEF
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
CASE ID:        [auto-generated: UIHC-DEV-YYYY-####]
DATE ISSUED:    [YYYY-MM-DD]
CATEGORY:       [device category — maps to Section 6 module]
EVALUATOR:      J. Burroughs, Supply Chain / Perioperative Services
STATUS:         [UNDER REVIEW / APPROVED / DECLINED / ON HOLD]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1. DEVICE IDENTIFICATION
   ─────────────────────
   Brand Name:
   Generic Name / Device Type:
   Manufacturer:
   Catalog Number(s):           [from GUDID catalogNumber — flag if missing]
   UDI-DI:
   GMDN Term:
   Device Class:                [I / II / III]
   510(k) Number / PMA Number:
   Clearance / Approval Date:
   Labeler DUNS:                [use for SEC EDGAR lookup if public company]

2. CLINICAL PROFILE
   ─────────────────
   Indicated Use:
   Contraindications:
   Procedure Categories (CPT):  [CPT code alignment — manual or vendor-provided]

   Clinical Evidence Summary:
   [Claude-synthesized from PubMed abstract retrieval — see prompt in Section 3.3]
   Evidence Quality:            [RCT / Prospective Cohort / Case Series / Manufacturer Data Only]

   Relevant Studies:
   ┌─────────┬────────────────────────────────┬──────────────┬───────────┐
   │ PMID    │ Title (truncated)              │ Year/Journal │ Key Finding│
   ├─────────┼────────────────────────────────┼──────────────┼───────────┤
   │         │                                │              │           │
   └─────────┴────────────────────────────────┴──────────────┴───────────┘

3. REGULATORY & SAFETY RECORD
   ───────────────────────────
   Recall History (last 5 years):
   ┌────────────────┬───────────┬──────────────────────────────┬──────────┐
   │ Initiation Date│ Class     │ Reason                       │ Status   │
   ├────────────────┼───────────┼──────────────────────────────┼──────────┤
   │                │           │                              │          │
   └────────────────┴───────────┴──────────────────────────────┴──────────┘

   Adverse Event Summary (MAUDE, last 3 years):
   Total Reports (brand, this product code):
   Deaths:          [count]
   Injuries:        [count]
   Malfunctions:    [count]
   MAUDE Context:   [relative to category brand volume — see count_by_brand query]

   Current Recall Status:  [NONE / ⚠ ACTIVE RECALL: Class I / Class II / Class III]
   MRI Safety:             [MR Safe / MR Conditional / MR Unsafe — from GUDID]
   Single Use:             [Y / N]
   Sterile (as supplied):  [Y / N]

4. COMPETITIVE CONTEXT
   ────────────────────
   Current Incumbent:          [what this replaces or competes with at UIHC]
   Key Competitors (2-3):      [alternatives in same GMDN category]
   Clinical Differentiation:   [what the rep claims vs. what published evidence shows]
   Market Position:            [Premium / Mid-Tier / Entry]
   Notes on Vendor Claims:     [flag unsubstantiated claims]

5. SUPPLY CHAIN PROFILE
   ─────────────────────
   Manufacturer Stability:     [SEC filing note if public company; private = note limited visibility]
   GPO Contract Status:        [Vizient tier / Premier tier / HealthTrust / Non-contracted]
   Lead Time:                  [from vendor quote]
   Minimum Order Quantity:     [from vendor quote]
   Sterility / Shelf Life:     [from GUDID sterilization fields]
   Consignment Available:      [Y / N]
   Sterile Processing Impact:  [tray requirements, instrument reprocessing, SPD impact]

6. EVALUATION SCORE
   ──────────────────
   [10-dimension scoring table — see Section 4.2 for full rubric]

   ┌────────────────────────────────────────┬──────────┬──────────────────────────┐
   │ Dimension                              │ Score    │ Rationale (brief)         │
   │                                        │ (1–5)    │                           │
   ├────────────────────────────────────────┼──────────┼──────────────────────────┤
   │ 1. Clinical Evidence Quality           │          │                           │
   │ 2. Safety Record                       │          │                           │
   │ 3. Regulatory Status                   │          │                           │
   │ 4. Clinical Differentiation            │          │                           │
   │ 5. Cost Profile                        │          │                           │
   │ 6. Supply Chain Risk                   │          │                           │
   │ 7. Usability / Learning Curve          │          │                           │
   │ 8. Contract Position                   │          │                           │
   │ 9. Conversion Complexity               │          │                           │
   │ 10. Strategic Fit                      │          │                           │
   ├────────────────────────────────────────┼──────────┼──────────────────────────┤
   │ TOTAL (50 = max raw; normalized /100)  │    /50   │                           │
   └────────────────────────────────────────┴──────────┴──────────────────────────┘

   OVERALL SCORE (normalized):  [X / 100]
   RECOMMENDATION:              [APPROVE / DECLINE / PILOT (30-day) / REFER TO VAC]

7. FLAGS & NOTES
   ──────────────
   AUTO-GENERATED FLAGS (from data pipeline):
   □ Active Class I Recall detected
   □ Active Class II Recall detected
   □ MAUDE event volume elevated vs. category peers
   □ Death events reported (last 3 years)
   □ Missing 510(k) / PMA — regulatory pathway unconfirmed
   □ Device description missing in GUDID
   □ Catalog number absent — item master reconciliation required
   □ Not in active commercial distribution
   □ PMA device — cannot substitute with 510(k) equivalent
   □ HCTP product — requires AATB accreditation verification

   MANUAL NOTES:
   [Free text field — evaluator observations, rep meeting notes, physician input]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
BRIEF GENERATED:  [timestamp] | SOURCE: UIHC MedOps OS v1.0 / MS-0001
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## 3.3 Claude API System Prompt — Device Brief Synthesis

```python
DEVICE_BRIEF_SYSTEM_PROMPT = """You are a perioperative supply chain analyst at an academic medical center (University of Iowa Hospitals & Clinics). Your role is to synthesize regulatory data, adverse event records, and clinical literature into structured evaluation briefs for the hospital's Value Analysis Committee.

OPERATING PRINCIPLES:
- You are producing decision support for clinical and supply chain professionals. You are NOT making clinical decisions.
- Distinguish clearly between: (a) what FDA data shows, (b) what peer-reviewed literature shows, and (c) what vendor-submitted data claims.
- Flag every adverse event trend, active recall, or data gap explicitly — do not bury safety signals.
- If evidence quality is low (case series, manufacturer-funded only, no RCTs), say so plainly.
- Use hedged language for interpretations ("suggests," "consistent with," "does not demonstrate") and direct language for facts ("the FDA 510(k) was cleared on [date]").
- Output must be suitable for direct inclusion in a VAC submission document.

OUTPUT FORMAT: Structured JSON with these top-level keys:
- clinical_evidence_summary (string, 150-300 words)
- evidence_quality_tier ("RCT/Meta-Analysis" | "Prospective Cohort" | "Case Series" | "Manufacturer Data Only" | "No Published Evidence")
- key_findings (list of strings, max 5)
- safety_flags (list of strings — any concerns from recalls, MAUDE, data gaps)
- auto_flags (list of flag codes from the standard flag list)
- competitive_notes (string, 100-200 words, if competitor data provided)
- recommendation_rationale (string, 100-200 words)
- confidence_level ("HIGH" | "MEDIUM" | "LOW") with rationale"""


DEVICE_BRIEF_USER_PROMPT_TEMPLATE = """Generate a clinical evidence summary and flag analysis for the following device evaluation.

=== DEVICE DATA (ACCESSGUDID) ===
{device_profile_json}

=== 510(k) / PMA CLEARANCES ===
{clearances_json}

=== ADVERSE EVENTS (MAUDE) — LAST 3 YEARS ===
Total reports (this brand, this product code): {maude_total}
Brand-level distribution across category:
{maude_brand_counts_json}

Recent adverse event details (sample):
{maude_recent_json}

=== RECALL RECORDS (LAST 5 YEARS) ===
{recalls_json}

Active Class I Recall: {has_active_class_one}

=== CLINICAL LITERATURE (PubMed abstracts) ===
{literature_json}

=== TASK ===
1. Write a Clinical Evidence Summary (150-300 words) integrating the literature findings. Include study designs, key outcomes, and limitations. Note if evidence is primarily manufacturer-sponsored.
2. Assign an Evidence Quality Tier.
3. List up to 5 Key Findings (bullet-style).
4. List all Safety Flags (from MAUDE data, recall records, or data gaps).
5. Note which auto-flags from the standard list are triggered.
6. Provide a Recommendation Rationale (100-200 words).
7. Assign a Confidence Level with 1-sentence justification.

Return valid JSON matching the output schema in your system instructions."""


def generate_device_brief_synthesis(dossier: dict, literature: list) -> dict:
    """
    Call Claude API to generate the synthesized sections of the Device Brief.
    
    Args:
        dossier:    Output from build_device_dossier()
        literature: Output from fetch_pubmed_abstracts()
    
    Returns:
        Structured dict with all Claude-generated brief sections
    """
    import anthropic
    import json
    
    client = anthropic.Anthropic()  # Uses ANTHROPIC_API_KEY env var
    
    user_content = DEVICE_BRIEF_USER_PROMPT_TEMPLATE.format(
        device_profile_json=json.dumps(dossier["device_profile"], indent=2),
        clearances_json=json.dumps(dossier["clearances_510k"][:3], indent=2),
        maude_total=dossier["maude_recent_total"],
        maude_brand_counts_json=json.dumps(dossier["maude_brand_counts"][:15], indent=2),
        maude_recent_json=json.dumps(dossier["maude_recent_events"][:5], indent=2),
        recalls_json=json.dumps(dossier["recalls"], indent=2),
        has_active_class_one=dossier["active_class_one_recall"]["has_active_class_one"],
        literature_json=json.dumps(literature, indent=2)
    )
    
    response = client.messages.create(
        model="claude-opus-4-5",
        max_tokens=4096,
        system=DEVICE_BRIEF_SYSTEM_PROMPT,
        messages=[{"role": "user", "content": user_content}]
    )
    
    return json.loads(response.content[0].text)
```

---

---

# SECTION 4: THE COMPETITIVE MATRIX (OUTPUT FORMAT 2)

## 4.1 What It Is

The Competitive Matrix is a multi-device comparison across a category. Used for category reviews, contract renewals, and formulary standardization decisions. The output is a VAC-ready table showing all candidate devices scored across all 10 evaluation dimensions with totals and a narrative summary.

Equivalent to the LDI 3-theory comparison table: all leading options in a category laid out side-by-side with consistent criteria.

---

## 4.2 The 10-Dimension Scoring Rubric

Each dimension is scored 1–5. Total raw score is out of 50; normalized to 100 for the Device Brief.

---

### Dimension 1: Clinical Evidence Quality

| Score | Criteria |
|---|---|
| **5** | ≥2 independent RCTs or a systematic review/meta-analysis showing clinical superiority or non-inferiority. Studies not funded solely by manufacturer. |
| **4** | 1 RCT, or a strong prospective multicenter cohort study. May include some manufacturer funding but with independent endpoint adjudication. |
| **3** | Prospective single-center study or a retrospective multicenter cohort. Peer-reviewed. No RCT available for this indication. |
| **2** | Case series only, or a single retrospective single-center study. Limited generalizability. |
| **1** | Manufacturer data only (white papers, IFUs, sponsored case reports), or no published peer-reviewed evidence available. |

---

### Dimension 2: Safety Record

| Score | Criteria |
|---|---|
| **5** | No recalls in last 5 years. MAUDE event rate below category median. No Death events. Device class II or lower. |
| **4** | No active recalls. MAUDE event rate at or near category median. No Death events. Minor Class III recall >3 years ago, fully terminated. |
| **3** | No active recalls. MAUDE event rate above category median but explainable by market share. 1 terminated Class II recall >2 years ago. |
| **2** | Active Class III recall or terminated Class II recall <2 years ago. MAUDE event rate notably elevated vs. category. |
| **1** | Active Class I or Class II recall. Multiple recalls in last 3 years. Death events reported within last 2 years. |

---

### Dimension 3: Regulatory Status

| Score | Criteria |
|---|---|
| **5** | 510(k) cleared within last 8 years (current-generation technology). Device Class II. Clear predicate chain. Device class matches category standard. |
| **4** | 510(k) cleared 8–15 years ago, or recent clearance on a long-established platform. PMA device with clean post-market record. |
| **3** | 510(k) >15 years old. Predicate chain is long or convoluted. Device class mismatch vs. category peers — requires explanation. |
| **2** | Clearance date unknown or pending confirmation from vendor. Product code mismatch with intended use. 510(k) does not cover current intended use at facility. |
| **1** | Regulatory pathway unconfirmed. Vendor cannot provide 510(k)/PMA number. Device used off-label for intended procedure. |

---

### Dimension 4: Clinical Differentiation

| Score | Criteria |
|---|---|
| **5** | Independent evidence of genuine clinical differentiation (statistically significant outcome improvement vs. comparators in RCT or large prospective study). |
| **4** | Clinical differentiation supported by peer-reviewed evidence, though not head-to-head RCT. Mechanism of action difference is independently validated. |
| **3** | Differentiation claims plausible and consistent with published literature, but no direct comparative trial. Vendor clinical claims partially substantiated. |
| **2** | Differentiation claims are largely vendor-sponsored or based on surrogate endpoints without patient outcome data. |
| **1** | No clinical differentiation from existing formulary options. "New and improved" claims with no published substantiation. Clinically equivalent to current formulary item. |

---

### Dimension 5: Cost Profile

| Score | Criteria |
|---|---|
| **5** | Entry-tier pricing. GPO contract at Tier 1. Lowest cost-per-case in category. Immediate savings vs. current formulary. |
| **4** | Mid-tier pricing at or below current formulary. GPO contract available. Cost-per-case favorable when full episode considered. |
| **3** | Mid-tier pricing, comparable to current formulary. GPO contract available. No clear cost advantage or disadvantage. |
| **2** | Premium pricing above current formulary. Limited GPO contract. Justification required (clinical evidence must support premium). |
| **1** | Premium pricing with no GPO contract and no published clinical evidence justifying cost premium. Non-contracted spend, budget impact negative. |

> **Note:** Store as tier only. Do not record specific GPO contract prices in this system.

---

### Dimension 6: Supply Chain Risk

| Score | Criteria |
|---|---|
| **5** | Multi-source category. Manufacturer is financially stable (public company, strong balance sheet). Lead time <5 business days. No documented backorder history. |
| **4** | Primary source with alternatives available in GMDN category. Stable manufacturer. Lead time 5–10 business days. Minor backorder incidents only. |
| **3** | Limited alternatives in GMDN category. Manufacturer financially stable but private (limited visibility). Lead time 10–20 business days. |
| **2** | Sole-source in category or narrowly sourced. Manufacturer is private with limited financial visibility. Lead time >20 days. Prior backorder documented. |
| **1** | Sole-source with no viable GMDN alternatives. Manufacturer under financial stress (bankruptcy, acquisition instability, litigation). Lead time >30 days or unreliable. |

---

### Dimension 7: Usability / Learning Curve

| Score | Criteria |
|---|---|
| **5** | Direct drop-in replacement for current formulary item. No new training required. Sterile processing workflow unchanged. SPD tray compatibility confirmed. |
| **4** | Minor technique adjustment. 1-session orientation sufficient. No new instrument sets required. Existing sterile processing protocols apply. |
| **3** | Moderate learning curve. 3–5 case supervised orientation. New instrument trays may be required. SPD impact manageable. |
| **2** | Significant learning curve. Formal credentialing or proctoring required. New sterile processing protocol required. Multi-week transition period. |
| **1** | Major system change. Requires >10 cases proctored training. Significant SPD capital investment. O.R. staff re-education required. Program-level disruption. |

---

### Dimension 8: Contract Position

| Score | Criteria |
|---|---|
| **5** | GPO Tier 1 contract with primary GPO (Vizient or Premier). Existing facility contract in place. Compliant with IDN purchasing policy. |
| **4** | GPO Tier 2 contract. Feasible to negotiate Tier 1 with volume commitment. Contract renewal cycle aligns. |
| **3** | GPO Tier 3 or non-primary GPO. Contract available but not at best pricing. Requires contract activation. |
| **2** | No current GPO contract. Direct-vendor negotiation required. Pricing subject to list price without framework. |
| **1** | Non-contracted item. Purchasing outside GPO generates maverick spend. Requires supply chain director exception approval. |

---

### Dimension 9: Conversion Complexity

| Score | Criteria |
|---|---|
| **5** | Formulary swap with no physician preference items involved. Purely administrative conversion. No clinical trials required. No credentialing. |
| **4** | Minor physician communication required. Brief product introduction sufficient. No formal trials. 2–4 week transition timeline. |
| **3** | Physician sign-off required for PPI category. 30-day pilot recommended. 1–2 procedure types affected. Standard VAC approval pathway. |
| **2** | Significant physician preference item. Multiple specialties affected. Formal 60-day pilot with outcomes tracking. Full VAC process required. |
| **1** | Major implant system change or robotic platform switch. Multi-specialty impact. 90–180 day managed conversion. CMO/CNO sign-off required. Multi-year contract implications. |

---

### Dimension 10: Strategic Fit

| Score | Criteria |
|---|---|
| **5** | Directly enables current service line growth priorities. Aligns with robotics integration roadmap. Supports UIHC academic research agenda. |
| **4** | Supports service line direction. Compatible with strategic platform investments. Neutral on research agenda. |
| **3** | Neutral strategic impact. Not a driver or inhibitor of current strategic priorities. Adequate fit. |
| **2** | Creates new single-source dependency. Competes with existing strategic vendor relationships. Adds formulary complexity without strategic benefit. |
| **1** | Conflicts with active strategic initiatives. Creates lock-in incompatible with current or planned technology investments. No strategic justification. |

---

## 4.3 The Competitive Matrix Output Format

```markdown
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
COMPETITIVE MATRIX — [CATEGORY NAME]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
DATE:           [YYYY-MM-DD]
GMDN TERM:      [GMDN preferred term name]
PRODUCT CODE:   [FDA product code(s)]
EVALUATOR:      J. Burroughs, Supply Chain / Perioperative
MATRIX ID:      UIHC-MTX-YYYY-####
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

| Dimension                     | [Device A]  | [Device B]  | [Device C]  | [Device D]  |
|-------------------------------|-------------|-------------|-------------|-------------|
| Manufacturer                  |             |             |             |             |
| Brand Name                    |             |             |             |             |
| 510(k) / PMA Number           |             |             |             |             |
| Device Class                  |             |             |             |             |
| Clearance Date                |             |             |             |             |
| **1. Clinical Evidence**      | **[1-5]**   | **[1-5]**   | **[1-5]**   | **[1-5]**   |
| **2. Safety Record**          | **[1-5]**   | **[1-5]**   | **[1-5]**   | **[1-5]**   |
| **3. Regulatory Status**      | **[1-5]**   | **[1-5]**   | **[1-5]**   | **[1-5]**   |
| **4. Clinical Differentiation**| **[1-5]** | **[1-5]**   | **[1-5]**   | **[1-5]**   |
| **5. Cost Profile**           | **[1-5]**   | **[1-5]**   | **[1-5]**   | **[1-5]**   |
| **6. Supply Chain Risk**      | **[1-5]**   | **[1-5]**   | **[1-5]**   | **[1-5]**   |
| **7. Usability / Learning**   | **[1-5]**   | **[1-5]**   | **[1-5]**   | **[1-5]**   |
| **8. Contract Position**      | **[1-5]**   | **[1-5]**   | **[1-5]**   | **[1-5]**   |
| **9. Conversion Complexity**  | **[1-5]**   | **[1-5]**   | **[1-5]**   | **[1-5]**   |
| **10. Strategic Fit**         | **[1-5]**   | **[1-5]**   | **[1-5]**   | **[1-5]**   |
| **TOTAL (raw/50)**            | **[X/50]**  | **[X/50]**  | **[X/50]**  | **[X/50]**  |
| **SCORE (normalized/100)**    | **[X/100]** | **[X/100]** | **[X/100]** | **[X/100]** |
| **RECOMMENDATION**            |             |             |             |             |

RECOMMENDATION KEY:
  FORMULARY PRIMARY   — Add as primary formulary item
  FORMULARY SECONDARY — Add as backup / specialty use
  PILOT (30 days)     — Conditional on pilot outcomes
  NO ACTION           — Do not add to formulary
  REFER TO VAC        — Requires full committee review

NARRATIVE SUMMARY: [Claude-generated — see prompt below]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
MATRIX GENERATED: [timestamp] | SOURCE: UIHC MedOps OS v1.0 / MS-0001
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## 4.4 Claude API Prompt — Matrix Generation

```python
COMPETITIVE_MATRIX_SYSTEM_PROMPT = """You are a perioperative supply chain specialist conducting a formal competitive device evaluation for a university academic medical center.

Your task is to score multiple devices across the 10-dimension evaluation rubric and generate a narrative summary of key differentiators.

SCORING PRINCIPLES:
- Score based on available data only. If data for a dimension is absent, score 3 (neutral) and flag the gap.
- Do not inflate scores based on manufacturer reputation.
- Weight clinical evidence and safety above cost for clinical risk items. Weight cost and contract position equally for commodity categories.
- Call out when clinical differentiation claims are vendor-sourced only.

OUTPUT FORMAT: Return JSON with:
  - "scores": dict keyed by device name, each containing scores for all 10 dimensions plus total and normalized score
  - "narrative": string (300-400 words) covering: key differentiators, safety standouts, cost-value relationship, and primary recommendation with rationale
  - "data_gaps": list of dimensions and devices where data was insufficient for confident scoring
  - "primary_recommendation": the device name that scores highest with 1-sentence rationale
  - "flags": list of safety or compliance flags across all devices evaluated"""


COMPETITIVE_MATRIX_USER_PROMPT_TEMPLATE = """Conduct a competitive evaluation for the following {n} devices in the {category} category.

GMDN Term: {gmdn_term}
FDA Product Codes: {product_codes}

DEVICE DATA:
{devices_json}

Using the 10-dimension rubric:
1. Clinical Evidence Quality (1-5)
2. Safety Record (1-5)  
3. Regulatory Status (1-5)
4. Clinical Differentiation (1-5)
5. Cost Profile (1-5) [use provided tier if available; score 3 if unknown]
6. Supply Chain Risk (1-5)
7. Usability / Learning Curve (1-5)
8. Contract Position (1-5) [score 3 if GPO status not provided]
9. Conversion Complexity (1-5)
10. Strategic Fit (1-5) [consider UIHC academic medical center context]

Score each device on each dimension. Total raw score is out of 50; normalize to 100.
Return JSON per the output schema in your system instructions."""
```

---

---

# SECTION 5: THE SUBSTITUTION RECOMMENDATION (OUTPUT FORMAT 3)

## 5.1 What It Is

The Substitution Recommendation is the most operationally critical output format. It drives direct procurement decisions: replace Device A with Device B on the formulary, or add Device B to replace recalled/discontinued Device A. It is formatted for presentation to a VAC or department chair.

Equivalent to the LDI deep-dive investigation episode: takes a specific proposition, examines it systematically, and delivers a supported verdict.

---

## 5.2 The Substitution Algorithm

```
INPUT: Device A (current / incumbent) + Device B (proposed substitute)

┌─────────────────────────────────────────────────────────────────────────┐
│ STEP 1 — ACCESSGUDID EQUIVALENCE CHECK                                   │
│                                                                           │
│  Compare Device A vs. Device B:                                          │
│    • GMDN term code    → same GMDN = same generic category               │
│    • Device class      → must match (Class II → Class II)                │
│    • Single-use flag   → must match (cannot sub SUE with reusable)       │
│    • Sterility method  → must be compatible                               │
│    • MRI safety status → B must be ≥ A (cannot sub MR Safe with Unsafe) │
│    • Size/config range → B must cover all sizes currently used at UIHC   │
│                                                                           │
│  → Output: EQUIVALENT / SIMILAR (minor diff) / DIFFERENT CATEGORY        │
└─────────────────────────────────────────────────────────────────────────┘
                               │
                               ▼
┌─────────────────────────────────────────────────────────────────────────┐
│ STEP 2 — REGULATORY CHAIN ANALYSIS                                        │
│                                                                           │
│  • Look up Device B's 510(k) via OpenFDA 510(k) endpoint                 │
│  • Check: is Device A listed as predicate device for Device B?            │
│    YES → strong regulatory equivalence signal (A → B predicate chain)    │
│    NO  → document Device B's predicate chain; assess clinical similarity  │
│  • Confirm: Device B 510(k) covers the intended use at UIHC              │
│  • Flag if B is a PMA device substituting a 510(k) Class II device       │
│                                                                           │
│  → Output: STRONG REGULATORY EQUIVALENCE / PATHWAY CLEAR / REVIEW NEEDED │
└─────────────────────────────────────────────────────────────────────────┘
                               │
                               ▼
┌─────────────────────────────────────────────────────────────────────────┐
│ STEP 3 — SAFETY DELTA ANALYSIS                                            │
│                                                                           │
│  MAUDE comparison (last 3 years):                                        │
│    • Device A total adverse event count (product code, brand)             │
│    • Device B total adverse event count (product code, brand)             │
│    • Adjust for market share / relative volume                            │
│    • Compare Death and Injury event counts specifically                   │
│                                                                           │
│  Recall comparison:                                                       │
│    • Device A recalls (last 5 years) → class, status                     │
│    • Device B recalls (last 5 years) → class, status                     │
│                                                                           │
│  Newness flag:                                                            │
│    • If Device B cleared <3 years ago → flag "LIMITED POST-MARKET DATA"   │
│                                                                           │
│  → Output: SAFETY EQUIVALENT / B BETTER / A BETTER / INSUFFICIENT DATA   │
└─────────────────────────────────────────────────────────────────────────┘
                               │
                               ▼
┌─────────────────────────────────────────────────────────────────────────┐
│ STEP 4 — CLINICAL EVIDENCE DELTA                                          │
│                                                                           │
│  PubMed search: "[Device A brand] outcomes" vs. "[Device B brand] outcomes" │
│  Search template: "[device_a] OR [device_b] [procedure_type] outcomes"   │
│                                                                           │
│  Assess:                                                                  │
│    • Are there head-to-head comparative trials?                           │
│    • Are there outcome studies for each device individually?              │
│    • Quality of evidence: RCT > prospective cohort > case series          │
│    • Manufacturer funding: flag all manufacturer-sponsored studies        │
│                                                                           │
│  Note: Most supply chain substitutions (especially commodity categories)  │
│  lack head-to-head trial data. This is expected — document accordingly.  │
│                                                                           │
│  → Output: EVIDENCE SUPPORTS B / EVIDENCE SUPPORTS A / EQUIVALENT /      │
│            NO COMPARATIVE DATA (document substitution on GMDN basis)      │
└─────────────────────────────────────────────────────────────────────────┘
                               │
                               ▼
┌─────────────────────────────────────────────────────────────────────────┐
│ STEP 5 — SUPPLY CHAIN FACTORS                                             │
│                                                                           │
│  Manual lookup:                                                           │
│    • GPO contract: A vs. B (tier, pricing reference)                      │
│    • Lead time: A vs. B (from vendor quotes)                              │
│    • MOQ: A vs. B                                                         │
│    • Consignment: A vs. B                                                 │
│    • Manufacturer stability: A vs. B (SEC EDGAR if public)                │
│    • Sterile processing compatibility: tray match, SPD workflow           │
│                                                                           │
│  → Output: Net supply chain score (favors A / Neutral / favors B)        │
└─────────────────────────────────────────────────────────────────────────┘
                               │
                               ▼
┌─────────────────────────────────────────────────────────────────────────┐
│ STEP 6 — RECOMMENDATION GENERATION (Claude API)                           │
│                                                                           │
│  Input: Steps 1–5 structured outputs + Device Briefs for A and B          │
│  Output: Structured recommendation with rationale (see Section 5.4)       │
│                                                                           │
│  Final verdict:                                                           │
│    APPROVE SUBSTITUTION — Evidence supports replacing A with B            │
│    APPROVE PARALLEL — Add B alongside A (for specific indications)        │
│    APPROVE PILOT — Conditional on 30-day pilot with outcome tracking      │
│    DO NOT SUBSTITUTE — Evidence or supply chain factors favor A           │
│    REFER TO VAC — Complexity requires full committee deliberation          │
└─────────────────────────────────────────────────────────────────────────┘
```

---

## 5.3 The Substitution Recommendation Brief

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
DEVICE SUBSTITUTION RECOMMENDATION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
CASE ID:        [UIHC-SUB-YYYY-####]
DATE ISSUED:    [YYYY-MM-DD]
CATEGORY:       [device category]
EVALUATOR:      J. Burroughs, Supply Chain / Perioperative Services
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

PROPOSED SUBSTITUTION:
  CURRENT (Device A):  [Brand / Manufacturer / DI / Catalog #]
  PROPOSED (Device B): [Brand / Manufacturer / DI / Catalog #]

TRIGGER: [Recall / Backorder / Cost Initiative / New Technology / Contract Renewal]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

SECTION A: DEVICE IDENTIFICATION COMPARISON
──────────────────────────────────────────────

| Field                    | Device A (Current)    | Device B (Proposed)   |
|--------------------------|-----------------------|-----------------------|
| Brand Name               |                       |                       |
| Manufacturer             |                       |                       |
| UDI-DI                   |                       |                       |
| Catalog Number           |                       |                       |
| GMDN Term                |                       |                       |
| Device Class             |                       |                       |
| 510(k) / PMA #           |                       |                       |
| Clearance / Approval Date|                       |                       |
| Single Use               |                       |                       |
| Sterile (as supplied)    |                       |                       |
| MRI Safety               |                       |                       |
| Size Range Coverage      |                       |                       |

STEP 1 — EQUIVALENCE:   [EQUIVALENT / SIMILAR / DIFFERENT CATEGORY]
STEP 2 — REGULATORY:    [STRONG EQUIVALENCE / PATHWAY CLEAR / REVIEW NEEDED]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

SECTION B: SAFETY COMPARISON (Steps 3–4)
──────────────────────────────────────────

| Safety Metric                        | Device A         | Device B         |
|--------------------------------------|------------------|------------------|
| MAUDE events (last 3 years)          |                  |                  |
| — Deaths                             |                  |                  |
| — Injuries                           |                  |                  |
| — Malfunctions                       |                  |                  |
| Active Class I Recall                |                  |                  |
| Active Class II Recall               |                  |                  |
| Recalls (last 5 years, all classes)  |                  |                  |
| Post-market data maturity            |                  |                  |

STEP 3 — SAFETY DELTA:  [EQUIVALENT / B BETTER / A BETTER / INSUFFICIENT DATA]

Clinical Evidence:
  Device A evidence summary:    [from Device A Brief]
  Device B evidence summary:    [from Device B Brief]
  Head-to-head comparative data: [Y / N — if N, document basis for equivalence]

STEP 4 — EVIDENCE DELTA: [B SUPPORTED / A SUPPORTED / EQUIVALENT / NO COMPARATIVE DATA]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

SECTION C: SUPPLY CHAIN COMPARISON (Step 5)
─────────────────────────────────────────────

| Supply Chain Factor          | Device A         | Device B         |
|------------------------------|------------------|------------------|
| GPO Contract Status          |                  |                  |
| GPO Tier                     |                  |                  |
| Price Tier                   |                  |                  |
| Lead Time                    |                  |                  |
| Minimum Order Quantity       |                  |                  |
| Consignment Available        |                  |                  |
| Manufacturer Stability       |                  |                  |
| GMDN Alternatives Available  |                  |                  |
| SPD / Sterile Processing     |                  |                  |

STEP 5 — SUPPLY CHAIN NET: [FAVORS A / NEUTRAL / FAVORS B]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

SECTION D: RECOMMENDATION (Step 6 — Claude-generated)
────────────────────────────────────────────────────────

RECOMMENDATION:
  [APPROVE SUBSTITUTION / APPROVE PARALLEL / APPROVE PILOT /
   DO NOT SUBSTITUTE / REFER TO VAC]

RATIONALE:
  [Claude-generated narrative — 200-300 words synthesizing Steps 1-5]

IMPLEMENTATION NOTES:
  Transition Timeline:    [estimated days]
  Physician Notification: [Y / N — required for PPI categories]
  SPD Protocol Update:    [Y / N]
  Training Required:      [Y / N — estimated hours]
  Pilot Parameters:       [if applicable: case count, outcome metrics, timeline]
  VAC Approval Required:  [Y / N — Y for all Class III devices and PPI categories]

APPROVAL CHAIN:
  □ Supply Chain Evaluator:          J. Burroughs _________________ Date: _______
  □ Department Physician Liaison:    _________________ Date: _______
  □ VAC Chair (if required):         _________________ Date: _______
  □ Director of Supply Chain:        _________________ Date: _______

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
DOCUMENT GENERATED: [timestamp] | UIHC MedOps OS v1.0 / MS-0001
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## 5.4 Claude API Prompt — Substitution Recommendation Narrative

```python
SUBSTITUTION_SYSTEM_PROMPT = """You are a perioperative supply chain specialist preparing a device substitution recommendation for a university academic medical center Value Analysis Committee.

You have been provided structured outputs from a 5-step substitution analysis. Your task is to synthesize these findings into a formal recommendation narrative.

OPERATING PRINCIPLES:
- Lead with patient safety. If Step 3 (Safety Delta) is ambiguous, recommend caution.
- Acknowledge data limitations explicitly. A GMDN-based equivalence is not clinical equivalence — say so.
- Be direct. The VAC needs a clear recommendation with clear rationale.
- Flag any condition that should be placed on approval (pilot period, physician sign-off, etc.).
- Do not speculate beyond the data provided.

OUTPUT FORMAT: Return JSON with:
  - "recommendation": one of APPROVE_SUBSTITUTION / APPROVE_PARALLEL / APPROVE_PILOT / DO_NOT_SUBSTITUTE / REFER_TO_VAC
  - "recommendation_summary": 1-sentence plain-language verdict
  - "rationale_narrative": string (200-300 words) synthesizing the 5 steps
  - "conditions": list of strings (conditions on approval, if any)
  - "implementation_notes": dict with keys: transition_timeline_days, physician_notification_required, spd_update_required, training_required, pilot_parameters (if applicable)
  - "confidence_level": HIGH / MEDIUM / LOW
  - "confidence_rationale": 1-sentence explanation"""


SUBSTITUTION_USER_PROMPT_TEMPLATE = """Prepare a substitution recommendation for replacing Device A with Device B.

STEP 1 — GUDID EQUIVALENCE:
  Result: {step1_result}
  Details: {step1_details}

STEP 2 — REGULATORY CHAIN:
  Result: {step2_result}
  Device A 510(k)/PMA: {device_a_clearance}
  Device B 510(k)/PMA: {device_b_clearance}
  Is Device A predicate for Device B: {is_predicate}
  Details: {step2_details}

STEP 3 — SAFETY DELTA:
  Result: {step3_result}
  Device A MAUDE (last 3 years): Deaths={a_deaths}, Injuries={a_injuries}, Malfunctions={a_malfunctions}
  Device B MAUDE (last 3 years): Deaths={b_deaths}, Injuries={b_injuries}, Malfunctions={b_malfunctions}
  Device A active recalls: {a_active_recalls}
  Device B active recalls: {b_active_recalls}
  Device B data maturity note: {b_data_maturity}

STEP 4 — CLINICAL EVIDENCE DELTA:
  Result: {step4_result}
  Device A clinical summary: {device_a_evidence}
  Device B clinical summary: {device_b_evidence}
  Head-to-head trials exist: {head_to_head}

STEP 5 — SUPPLY CHAIN NET:
  Result: {step5_result}
  GPO contract comparison: {gpo_comparison}
  Lead time comparison: {leadtime_comparison}
  Manufacturer stability: {manufacturer_stability}
  SPD / sterile processing impact: {spd_impact}

TRIGGER FOR THIS SUBSTITUTION: {trigger}
CATEGORY: {category}
FACILITY CONTEXT: University academic medical center; academic program dependencies noted where applicable.

Generate the substitution recommendation JSON per your system instructions."""
```

---

---

# SECTION 6: THE DEVICE CATEGORY MODULES

## Module format

Each module is used to initialize the Claude API context for category-specific analysis and to anchor evaluations in category-appropriate criteria. Reference the applicable module at the start of any Device Brief, Competitive Matrix, or Substitution Recommendation generation prompt.

---

## MODULE 1: Biosurgery / Hemostatics

```
CATEGORY:          Biosurgery / Hemostatics
GMDN CODES:        Flowable hemostatic agent (37374); Absorbable hemostatic gauze (46891);
                   Topical thrombin, bovine/human (12844)
PRODUCT CODES:     FTL (Hemostat, Absorbable, Foam), FTM (Hemostat, Topical Thrombin),
                   OZO (Oxidized Cellulose), KZE (Staple, Surgical Absorbable — related)
KEY VENDORS:
  ├── Ethicon (J&J)       SURGICEL Family (Original, Nu-Knit, Fibrillar, Powder, SNoW), SURGIFLO
  ├── Baxter              FLOSEAL Hemostatic Matrix
  ├── BD                  Arista AH Hemostatic Agent (microporous polysaccharide)
  └── Integra LifeSciences INTEGRA hemostatic products; PriMatrix; SurgiMend (wound/burns)
EVALUATION CRITERIA (CATEGORY-SPECIFIC):
  • Mechanism of action: oxidized cellulose (SURGICEL) vs. gelatin matrix + thrombin
    (FLOSEAL/SURGIFLO) vs. microporous polysaccharide (Arista) — not interchangeable mechanisms
  • Time to hemostasis at 3, 5, and 10 minutes (primary RCT endpoint)
  • Application compatibility: flowable (endoscopic) vs. sheet vs. powder vs. matrix + thrombin
  • Biocompatibility with implants: product must be fully absorbed prior to closure
  • Cost-consequence analysis: FLOSEAL published $5.38M annual savings in cardiac (PMID: 24927164);
    SURGIFLO vs. FLOSEAL ~$65/case savings no significant outcome difference in spinal fusion
    (PMID: 25907200) — use these as benchmarks
  • Shelf life, storage temperature, and resupply chain risk for specialty products
PROFESSIONAL SOCIETY GUIDANCE:
  • AORN: Perioperative Standards and Recommended Practices (hemostat section)
  • Journal of the American College of Surgeons; Surgical Endoscopy (primary literature sources)
RED FLAGS:
  • Thrombin products: confirm bovine vs. human thrombin sourcing (allergy/religious considerations)
  • Application in wet field vs. dry field: match product to surgical approach
  • Biocompatibility concerns with joint implants — do not leave oxidized cellulose at implant interface
  • Shelf life <12 months: resupply chain risk for low-volume specialties
SUBSTITUTION COMPLEXITY:   MEDIUM
  (Mechanism differences limit direct substitution; parallel formulary by procedure type is common)
NOTES:
  Category is high-leverage for GPO standardization. Running 2+ hemostatic agents adds cost
  without demonstrated outcome benefit in most procedures. Target: 1 primary + 1 specialty backup.
```

---

## MODULE 2: Endo Mechanicals / Laparoscopic

```
CATEGORY:          Endo Mechanicals / Laparoscopic
GMDN CODES:        Surgical stapler, endo linear cutter (47241); Trocar (40896);
                   Surgical clip applier (13582)
PRODUCT CODES:     KZE (Staple, Surgical Absorbable), MQP (Laparoscopic Trocars),
                   IYO (Stapler, Endoscopic)
KEY VENDORS:
  ├── Ethicon (J&J)    ECHELON FLEX Powered Staplers, ENDOPATH Trocars, GST System
  ├── Medtronic        ENDO GIA Stapler (Tri-Staple Technology), Signia Stapling System
  ├── Applied Medical  Kii Access Systems, REVEAL retractors
  └── B. Braun         Aesculap laparoscopic portfolio
EVALUATION CRITERIA (CATEGORY-SPECIFIC):
  • Staple line integrity and hemostasis (primary safety endpoint; misfire rate)
  • Cartridge color system / tissue thickness compatibility — confirm color-coding matches
    across full procedure portfolio (thin, medium, thick tissue indications)
  • Powered vs. manual: GST (Ethicon) vs. Signia (Medtronic) — 75% lower hemostasis
    complications matched sleeve gastrectomy cohort (PMC: 7368239)
  • Robotic stapler compatibility: Intuitive SureForm integration if da Vinci program active
  • Trocar design: optical vs. bladed entry; bladeless options for specific procedures
  • Surgeon ergonomics: PubMed PMID 17629973 evaluation dimensions (acceptability, ergonomics,
    functionality, overall preference)
  • Cost per case: cartridge + stapler + trocar pack total
PROFESSIONAL SOCIETY GUIDANCE:
  • SAGES (Society of American Gastrointestinal and Endoscopic Surgeons): clinical guidelines
  • AORN: Recommended Practices for Endo Mechanical
RED FLAGS:
  • Cartridge incompatibility between new stapler handle and existing OR inventory
  • Stapler malfunction rate: cross-reference MAUDE product code KZE / IYO for misfire events
  • Do not mix stapler systems within a procedure — standardize by service line
  • Powered staplers require battery management; confirm OR workflow compatibility
SUBSTITUTION COMPLEXITY:   HIGH
  (Cartridge ecosystem lock-in; surgeon-specific preferences; powered vs. manual is a significant
  technique shift; robotic integration adds complexity)
NOTES:
  Stapler decisions have significant downstream impact on robotic program supply chain.
  Coordinate stapler evaluation with robotic platform team. Ethicon GST is tightly integrated
  with da Vinci SureForm; Medtronic Tri-Staple is table-side system.
```

---

## MODULE 3: Sutures

```
CATEGORY:          Sutures
GMDN CODES:        Suture, absorbable (10083); Suture, nonabsorbable synthetic (11175);
                   Suture, barbed (66474)
PRODUCT CODES:     GAK (Suture, Absorbable), GAL (Suture, Nonabsorbable)
KEY VENDORS:
  ├── Ethicon (J&J)      VICRYL, PDS II, PROLENE, MONOCRYL, STRATAFIX (barbed), PERMA-HAND silk
  ├── Medtronic (Covidien)Polysorb, Biosyn, Surgidac, Sofsilk
  ├── B. Braun            SAFIL, MONOSYN, SERAFIT, NOVAFIL
  └── Teleflex            Look Sutures portfolio
EVALUATION CRITERIA (CATEGORY-SPECIFIC):
  • Absorbable vs. nonabsorbable: match tissue holding time to healing timeline by procedure
  • Monofilament vs. braided: monofilament = lower SSI risk; braided = better handling/knot security
  • Barbed (knotless) sutures: OR time reduction in specific procedures; learning curve cost
  • Antibiotic-coated (VICRYL Plus / triclosan): SSI evidence varies — strongest in abdominal closure;
    cost premium requires procedure-specific justification
  • Size range coverage: 0 through 7-0 minimum; confirm full range available from proposed vendor
  • Packaging: strip packs vs. tray dispensing — match to OR preference
  • NOTE: Surgeon brand preference is the dominant performance variable in clinical evaluations
    even when products are clinically equivalent (PMID: 17629973) — manage preference with
    data, not accommodation
PROFESSIONAL SOCIETY GUIDANCE:
  • AORN: Suture selection guidance
  • ACSRS: wound closure recommendations by procedure
RED FLAGS:
  • Size range gaps: vendor cannot supply sizes currently used in high-volume procedures
  • Needle type mismatch: confirm trocar vs. cutting needle compatibility with procedure requirements
  • Transition from a strong-preference incumbent (Ethicon) requires surgeon communication
    strategy — plan this before beginning evaluation
SUBSTITUTION COMPLEXITY:   LOW
  (Highest-leverage standardization category; minimal patient risk; surgeon preference manageable
  with structured VAC process; 15-25% savings achievable through standardization)
NOTES:
  Sutures represent the single best formulary standardization opportunity with least clinical
  controversy. Target: 1 primary vendor across all absorbable and nonabsorbable categories.
  Run parallel formulary for 30 days max; then mandate standard with exception process.
```

---

## MODULE 4: Orthopedic — Total Joints

```
CATEGORY:          Orthopedic — Total Joints
GMDN CODES:        Total knee replacement prosthesis (36799); Total hip replacement prosthesis (36800);
                   Hip prosthesis, acetabular cup (13021); Unicompartmental knee prosthesis (47162)
PRODUCT CODES:     HRS (Hip, Femoral, Total), KWQ (Knee, Total), KYP (Hip, Acetabular Component)
KEY VENDORS:
  ├── Zimmer Biomet   Persona (knee), G7 Acetabular (hip), ROSA Knee Robot
  ├── Stryker         Triathlon (knee), Accolade II (hip), Mako SmartRobotics
  ├── DePuy Synthes   ATTUNE Knee, Pinnacle Hip, VELYS Robotic
  └── Smith+Nephew    LEGION Knee, BIRMINGHAM Hip, NAVIO Robotics
EVALUATION CRITERIA (CATEGORY-SPECIFIC):
  • AJRR survivorship data — only independent long-term outcomes source; mandatory reference
  • Bearing surface: highly cross-linked UHMWPE is standard of care; metal-on-metal is
    de facto retired (FDA communications 2011+, multiple Class I recalls)
  • Fixation: cemented vs. cementless vs. hybrid — confirm surgeon technique match
  • ROBOTIC LOCK-IN: Mako (Stryker) requires Stryker implants; ROSA (ZB) requires ZB implants;
    VELYS (DePuy) requires DePuy implants. Robot selection = implant vendor for 7-10 years.
    Model robotic TCO separately before allowing robot preference to drive implant contract.
  • Patient-matched (3D-printed) implants: 30-60% cost premium; 4-6 week lead time; limited
    to revision, deformity, or complex primary cases
  • ODEP ratings (A*, A, B) based on registry survivorship — use as independent benchmark
  • Consignment tray management: ANSI/AAMI ST79 compliance; SPD throughput impact is real
PROFESSIONAL SOCIETY GUIDANCE:
  • AJRR Annual Report: https://www.aaos.org/registry/ajrr/
  • AAOS CPGs: Total Knee Arthroplasty; Total Hip Arthroplasty
  • AOANJRR: gold-standard long-term survivorship data (Australian registry)
RED FLAGS:
  • Metal-on-metal bearing surfaces — do not approve; multiple Class I recalls
  • Vendor cannot provide AJRR survivorship data — score Clinical Evidence at 1
  • Robotic platform decision made without implant TCO modeling
  • Consignment implant trays missing size coverage — confirm full range before approval
SUBSTITUTION COMPLEXITY:   VERY HIGH
  (PPI category; multiple physician stakeholders; AJRR data required; robotic platform
  implications; 90-180 day managed conversion; mandatory VAC review)
NOTES:
  Physician preference variation accounts for 36-61% of TKA/THA implant cost variation.
  Structured VAC process supported by AJRR data consistently achieves 15-25% savings.
  This is the highest-impact cost category in perioperative supply chain.
```

---

## MODULE 5: Orthopedic — Spine

```
CATEGORY:          Orthopedic — Spine
GMDN CODES:        Intervertebral cage (15866); Pedicle screw system (46827);
                   Cervical disc replacement (47392)
PRODUCT CODES:     MUY (Spine, Intervertebral Cage), KWC (Spine, Pedicle Screw)
KEY VENDORS:
  ├── Medtronic         SOLERA (rod/screw), PRESTIGE (disc), CD Horizon; Mazor X Stealth robot
  ├── Stryker           Tritanium (TLIF/PLIF cages), Serrato, Cipriano
  ├── DePuy Synthes     CONCORDE LIFT, CONDUIT, VIPER2
  └── Globus+NuVasive   COALITION (ALIF), ExcelsiusGPS robot (Globus); XLIF approach (NuVasive)
                        NOTE: Globus + NuVasive merged 2023 — now #2 spine company globally.
                        Re-evaluate all contracts post-merger for pricing leverage.
EVALUATION CRITERIA (CATEGORY-SPECIFIC):
  • Approach compatibility: TLIF / PLIF / ALIF / XLIF (lateral) — confirm vendor covers all
    approaches used by UIHC spine surgeons before any standardization discussion
  • Cage material: PEEK vs. titanium vs. titanium-coated PEEK — osteointegration implications;
    surgeon should drive this decision with outcomes data
  • Navigation compatibility: Mazor X (Medtronic) vs. ExcelsiusGPS (Globus) — robot-agnostic
    instruments do not exist; confirm navigation system before implant selection
  • Instrumentation system complexity: number of trays, sterilization cycle requirements,
    SPD labor impact
  • Biologic adjunct ecosystem: vendor relationships for allograft / DBM / BMP supplements
  • GPO pricing: highly leverageable in high-volume spine programs; Tier 1 contracts can achieve
    30-40% below list in competitive bidding
PROFESSIONAL SOCIETY GUIDANCE:
  • NASS: evidence-based clinical guidelines (https://www.spine.org)
  • ISASS: International Society for the Advancement of Spine Surgery
  • Imaging/robotics acquisition: PMID 31032450
RED FLAGS:
  • Cage material mismatch with surgeon protocol — do not substitute without surgeon sign-off
  • Navigation system incompatibility with existing capital equipment
  • BMP (rhBMP-2) usage compliance: FDA labeling restrictions apply; document clinical
    justification for off-label use
  • Post-merger vendor instability (Globus + NuVasive): monitor for SKU rationalization,
    sales rep turnover, and pricing changes
SUBSTITUTION COMPLEXITY:   VERY HIGH
  (Surgeon-specific technique; navigation system lock-in; biologic ecosystem dependencies;
  mandatory VAC with surgeon champion involvement)
NOTES:
  Spine is the second-highest cost opportunity after total joints. CVACs targeting 2-3
  instrumentation systems maximum consistently achieve significant savings. Approach
  standardization before implant standardization — surgeons are more willing to discuss
  implant substitution within a familiar approach.
```

---

## MODULE 6: Burn Tissues / Wound Care

```
CATEGORY:          Burn Tissues / Wound Care
GMDN CODES:        Skin substitute, biological (44019); Wound dressing, non-sterile (16006);
                   Skin graft, synthetic (35874)
PRODUCT CODES:     KGX (Skin Substitute, Temporary), OZP (Wound Dressing, Biological)
KEY VENDORS:
  ├── Integra LifeSciences  Integra DRT (PMA), Omnigraft, Bilayer Matrix, Meshed Bilayer
  ├── MiMedx               EpiFix, AmnioFix (HCT/P — not a device; see below)
  ├── Organogenesis         Apligraf (BLA), Dermagraft (510(k)), NovaBay
  ├── Avita Medical         RECELL Autologous Cell Harvesting (PMA, 2018 — burns)
  └── Smith+Nephew          BIOBRANE, TransCyte
EVALUATION CRITERIA (CATEGORY-SPECIFIC):
  • REGULATORY PATHWAY DETERMINES PROCUREMENT WORKFLOW:
    PMA (Integra DRT, RECELL) → standard device procurement
    HCT/P (MiMedx EpiFix, amniotic allografts) → tissue bank procurement workflow;
      requires AATB accreditation verification; NOT subject to GUDID/UDI
    BLA (Apligraf) → biological product procurement; CBER oversight
  • Indication specificity: deep partial/full-thickness burns (Integra DRT); ≥30% TBSA
    full-thickness burns (Epicel — autologous keratinocytes); partial-thickness (Biobrane)
  • HCPCS Q-codes: each product has specific Q-codes affecting billing compliance
    (Q4105 = Integra DRT; confirm current codes annually — CMS updates)
  • Payer coverage criteria: Medicare requires wound size, ABI measurements, prior treatment
    failure documentation for advanced wound care coverage — affects formulary compliance
  • Donor site sparing: Integra's core clinical value argument vs. autograft
PROFESSIONAL SOCIETY GUIDANCE:
  • ABA (American Burn Association): burn care clinical guidelines
  • AORN: wound care and skin substitute procedures
RED FLAGS:
  • HCT/P products without AATB accreditation — do not approve; procurement block
  • RECELL: must confirm burn surgeon training completed before adding to formulary
  • Q-code mismatch: billing errors on wound care products create compliance risk
  • Refrigerated / cryopreserved products: confirm cold chain capability in OR and storage
SUBSTITUTION COMPLEXITY:   HIGH
  (Regulatory pathway differences mean A and B may not be substitutable; must confirm
  same regulatory pathway and indication coverage; physician specialty input required)
NOTES:
  Do not conflate device and HCT/P procurement workflows. Amniotic membrane products
  (MiMedx, Organogenesis) are NOT devices and do NOT appear in ACCESSGUDID. Tissue bank
  accreditation check is the mandatory first step for any amniotic product evaluation.
```

---

## MODULE 7: Biologic Tissues / Allografts

```
CATEGORY:          Biologic Tissues / Allografts
GMDN CODES:        N/A — most allografts are HCT/P, not devices; some are covered
                   under specific device GMDN codes for musculoskeletal applications
PRODUCT CODES:     N/A for HCT/P products; device classification applies only to
                   processed allografts regulated as devices (e.g., decellularized products)
KEY VENDORS:
  ├── MiMedx               AmnioFix, EpiFix, OrthoFlo (amniotic — HCT/P)
  ├── Artivion (CryoLife)   BioGlue, cardiovascular allografts
  ├── Organogenesis         NovaBay, Dermagraft
  ├── Osiris/Smith+Nephew   Grafix, Stravix (amniotic membrane)
  └── Wright Medical/Stryker GRAFTJACKET (orthopedic soft tissue — ADM)
EVALUATION CRITERIA (CATEGORY-SPECIFIC):
  • REGULATORY DISTINCTION (critical for procurement):
    HCT/P (21 CFR Part 1271): NOT subject to 510(k)/PMA; NOT in ACCESSGUDID; NOT UDI-labeled
    Decellularized ADMs (some): regulated as devices; 510(k) cleared; in ACCESSGUDID
    Confirm regulatory pathway BEFORE initiating GUDID/OpenFDA pipeline
  • AATB accreditation: mandatory verification for all tissue suppliers
  • FDA tissue establishment registration (21 CFR 1271): verify registration number
  • Donor screening: HIV, HBV, HCV, HTLV I/II, syphilis, West Nile, CMV — per product
  • Chain of custody: recovery → processing → storage → implantation documentation
  • Temperature monitoring: cryopreserved products require validated cold chain records
  • Minimal manipulation / homologous use compliance: HCT/P exemption criteria
PROFESSIONAL SOCIETY GUIDANCE:
  • AATB: American Association of Tissue Banks (accreditation standards)
  • ASPS: tissue reconstruction guidance; BIA-ALCL for implant-based reconstruction
RED FLAGS:
  • No AATB accreditation — hard stop; do not purchase
  • No FDA tissue establishment registration — hard stop
  • Donor testing documentation incomplete — escalate to infection control
  • Cryopreserved product received without temperature monitoring records — quarantine
  • HCT/P marketed with drug or device claims — may require PMA; verify with regulatory team
SUBSTITUTION COMPLEXITY:   HIGH
  (Regulatory framework entirely different from devices; physician specialist required;
  tissue bank compliance team must be involved; AATB accreditation check is step 0)
NOTES:
  Allografts represent a compliance-intensive procurement category. A single AATB
  accreditation lapse at a supplier requires immediate formulary suspension.
  Maintain a running list of accreditation expiration dates for all tissue suppliers.
```

---

## MODULE 8: Synthetic Tissues / Xenografts

```
CATEGORY:          Synthetic Tissues / Xenografts
GMDN CODES:        Mesh, surgical, resorbable (35700); Biological tissue matrix (58963);
                   Acellular dermal matrix (47401)
PRODUCT CODES:     KGN (Mesh, Absorbable), GXX (Tissue Matrix, Biological)
KEY VENDORS:
  ├── Integra LifeSciences  SurgiMend, PriMatrix, NeuraMend (fetal bovine collagen)
  ├── LifeNet Health         AlloPatch (human allograft — see Module 7 for HCT/P note)
  └── RTI Surgical (Enovis)  Conexa, BioTend (human allograft soft tissue)
EVALUATION CRITERIA (CATEGORY-SPECIFIC):
  • Source material: fetal bovine collagen (SurgiMend/PriMatrix) vs. porcine collagen vs.
    human acellular dermis — antigenicity and remodeling profile differ
  • Fetal bovine source: lower antigenicity than adult bovine; preferred for hernia repair
    and soft tissue reconstruction
  • Mechanical properties: tensile strength, suture pull-out, remodeling timeline
  • Sterilization method: EtO vs. gamma irradiation vs. e-beam — affects mechanical integrity
  • Infection resistance: relevant for contaminated fields (hernia in obese patients, etc.)
  • MSRP: $800-$2,500+ per sheet; high-leverage GPO category; confirm GPO tier
  • These are regulated as DEVICES (510(k) pathway), unlike HCT/P allografts
PROFESSIONAL SOCIETY GUIDANCE:
  • ACS (American College of Surgeons): hernia repair guidelines
  • ASPS: reconstruction guidance
RED FLAGS:
  • Source material religious/ethical objections: bovine collagen requires patient disclosure;
    confirm institutional consent protocol
  • Off-label use in contaminated fields: confirm 510(k) indication covers intended use
  • Shelf life variability by sterilization method: confirm with vendor before stocking
SUBSTITUTION COMPLEXITY:   MEDIUM
  (Device regulatory pathway makes GUDID chain applicable; however source material
  and mechanical property differences require procedure-specific evaluation)
NOTES:
  SurgiMend and PriMatrix are regularly confused with HCT/P allografts by clinical staff.
  These are medical devices (510(k) cleared). Reinforce procurement workflow distinction
  to OR and SPD teams.
```

---

## MODULE 9: Plastic Surgery Implants

```
CATEGORY:          Plastic Surgery Implants
GMDN CODES:        Breast implant, silicone gel-filled (11230); Tissue expander (46839)
PRODUCT CODES:     QDD (Breast Implant, Silicone Gel), GZN (Tissue Expander)
KEY VENDORS:
  ├── Allergan/Natrelle (AbbVie)  SoftTouch, SilkSurface, structured implants, tissue expanders (PMA)
  ├── Mentor (J&J)                MemoryGel, MemoryShape, CPG — highly structured (PMA)
  ├── Sientra                     HSC+ round and anatomic — high-strength cohesive (PMA)
  └── GC Aesthetics               Nagor, Eurosilicone brands (CE mark; PMA for US)
EVALUATION CRITERIA (CATEGORY-SPECIFIC):
  • ALL SILICONE GEL BREAST IMPLANTS ARE CLASS III / PMA — no 510(k) equivalents exist.
    This category cannot be evaluated with standard 510(k) substitution logic.
  • Shell type: smooth vs. textured — TEXTURED SURFACES CARRY BIA-ALCL RISK
    Allergan BIOCELL textured (macro-textured): Class I recall 2019 — DO NOT STOCK
    Sientra micro-textured and Mentor SILTEX: remain on market with enhanced monitoring
  • Cohesivity: standard gel / cohesive / highly cohesive (gummy bear/form-stable)
  • Shape: round vs. anatomic — anatomic requires rotational stability; impacts revision risk
  • 10-year CORE study data: FDA-required; available for all major brands; reference in evaluation
  • Patient Decision Checklist: federal mandate; must be documented in patient record
  • Tissue expander compatibility: same-vendor system strongly preferred for 2-stage reconstruction
  • FDA Boxed Warning (2021, all breast implants): covers BIA-ALCL and systemic symptoms
PROFESSIONAL SOCIETY GUIDANCE:
  • ASPS (American Society of Plastic Surgeons): BIA-ALCL guidance; Patient Safety Committee
  • FDA: https://www.fda.gov/medical-devices/breast-implants
RED FLAGS:
  • ANY textured macro-surface implant (Allergan BIOCELL) — Class I recall; immediate action
  • 10-year CORE study data not available from vendor — escalate; all major brands have this
  • Patient Decision Checklist not integrated into OR consent workflow — compliance risk
  • Implant tracking/registry enrollment: FDA mandatory post-market requirement; confirm
    institutional tracking process with plastic surgery service line
SUBSTITUTION COMPLEXITY:   VERY HIGH
  (All PMA; physician preference item; patient consent requirements; mandatory tracking;
  cannot substitute between 510(k) and PMA; full VAC review required)
NOTES:
  Breast implant procurement involves more regulatory compliance requirements than any other
  category in this portfolio. Patient Decision Checklist, implant tracking, and BIA-ALCL
  monitoring are federal requirements — not optional. Coordinate with plastic surgery
  program coordinator before any formulary change.
```

---

## MODULE 10: Ophthalmology Devices

```
CATEGORY:          Ophthalmology Devices
GMDN CODES:        Intraocular lens (IOL), monofocal (34987); IOL, multifocal (47303);
                   Phacoemulsification system (36741); Glaucoma drainage implant (45699)
PRODUCT CODES:     HQK (Intraocular Lens), HTK (Phacoemulsification System),
                   MYN (Glaucoma Drainage Device)
KEY VENDORS:
  ├── Alcon                AcrySof IOL family, CENTURION phaco system, NGENUITY visualization
  ├── J&J Vision           TECNIS IOL family (PureSee, Synergy, Multifocal), WHITESTAR phaco
  ├── Bausch + Lomb        enVista IOL, AKREOS, Stellaris phaco, Crystalens
  ├── Carl Zeiss Meditec   LUMERA microscopes, IOLMaster biometry, MEL90 excimer
  └── Glaukos              iStent inject W, Hydrus Microstent, Preserflo (MIGS)
EVALUATION CRITERIA (CATEGORY-SPECIFIC):
  • IOL SELECTION: monofocal vs. toric vs. EDOF vs. multifocal — premium IOLs are
    patient-cost-share items (not formulary); supply chain controls monofocal/toric only
  • PHACO SYSTEM LOCK-IN: each phaco platform uses proprietary IOL cartridges and handpieces.
    Alcon CENTURION ≠ J&J WHITESTAR cartridge compatibility. Switching phaco system = switching IOLs.
    Model phaco lock-in exactly as robotics lock-in in orthopedics.
  • MIGS devices (glaucoma): FDA-cleared for use concurrent with cataract surgery; iStent (510(k),
    GS1-cleared); Hydrus (510(k)); Preserflo (recent clearance) — evaluate with cataract program
  • Total cost of ownership: capital + annual maintenance + disposable pack per case + IOL cost
  • Service SLA: high-volume cataract programs require ≤4-hour on-site response time; confirm
    regional service infrastructure before capital acquisition
  • OCT and diagnostic equipment: capital equipment committee decision, not supply chain formulary
PROFESSIONAL SOCIETY GUIDANCE:
  • AAO (American Academy of Ophthalmology): preferred practice patterns
  • Market Scope: ophthalmology market intelligence: https://www.market-scope.com
RED FLAGS:
  • Phaco cartridge incompatibility — do not source IOLs from a vendor whose cartridges
    are incompatible with current phaco system
  • Service response time >8 hours — unacceptable for high-volume cataract program; escalate
  • Premium IOL being added to standard formulary — these are patient-pay items; billing error risk
  • MIGS device without ophthalmology credentialing verification
SUBSTITUTION COMPLEXITY:   HIGH
  (Phaco system lock-in; IOL/cartridge interdependency; surgeon preference strong;
  capital equipment decisions drive disposable supply chain for 5-7 years)
NOTES:
  The phaco + IOL relationship is the ophthalmology equivalent of robot + implant in orthopedics.
  Model capital acquisition costs before any formulary IOL change. A $50/case IOL savings is
  irrelevant if it requires a $400K phaco system replacement.
```

---

## MODULE 11: Surgical Robotics

```
CATEGORY:          Surgical Robotics
GMDN CODES:        Robotic surgical system (45764); Robot-assisted surgical instrument (46821)
PRODUCT CODES:     QFN (Robotic Surgical System), varies by platform
KEY VENDORS:
  ┌─ GENERAL LAPAROSCOPIC ROBOTICS ──────────────────────────────────────────┐
  │  Intuitive Surgical    da Vinci Xi, X, and 5 (latest); 60+ procedure types│
  │                        Market dominant; 12M+ procedures globally           │
  │  Capital: $500K–$2.5M+ │ Service: $100K–$180K/yr │ Disposable: $700–$2K/case│
  └───────────────────────────────────────────────────────────────────────────┘
  ┌─ TOTAL JOINT ROBOTICS ───────────────────────────────────────────────────┐
  │  Mako SmartRobotics     Stryker (Stryker implants ONLY)                   │
  │  ROSA Knee / Hip        Zimmer Biomet (ZB implants ONLY)                  │
  │  VELYS Robotic          DePuy Synthes (DePuy implants ONLY)               │
  │  NAVIO                  Smith+Nephew (S+N implants ONLY)                   │
  └───────────────────────────────────────────────────────────────────────────┘
  ┌─ SPINE ROBOTICS ────────────────────────────────────────────────────────┐
  │  Mazor X Stealth Ed.   Medtronic (fluoroscopy + O-arm)                   │
  │  ExcelsiusGPS          Globus Medical (CT-based navigation)               │
  └───────────────────────────────────────────────────────────────────────────┘
EVALUATION CRITERIA (CATEGORY-SPECIFIC):
  • IMPLANT LOCK-IN: All total joint robots require proprietary implants.
    Robot platform selection = implant vendor contract for 7-10 years.
    MANDATORY: model full TCO including robotic capital + annual service + 
    10-year procedural disposable cost BEFORE robot drives contract decision.
  • Break-even case volumes:
    da Vinci: 200-300 cases/year across all specialties
    Mako / ROSA: 150-200 robotic joint cases/year
  • Surgeon adoption: minimum 3-4 committed champions; single-surgeon program = financial risk
  • Guaranteed uptime SLA: target 98%+; confirm regional service infrastructure
    (target ≤4-8 hour on-site response)
  • Technology roadmap: is next-gen platform imminent? (da Vinci 5 vs. Xi pricing delta)
  • Decision matrix weights (Robotomated 2026 framework):
    Clinical fit 30% | Financial viability 25% | Surgeon adoption 20% |
    Vendor strength 15% | Strategic positioning 10%
PROFESSIONAL SOCIETY GUIDANCE:
  • AORN: robotic surgery standards
  • SAGES: robotic program development guidance
  • NASS: robotic spine surgery navigation guidance (PMID 31032450)
RED FLAGS:
  • Robot purchasing decision made without implant contract modeling — escalate immediately
  • <3 surgeon champions committed before capital approval — program failure risk
  • No guaranteed uptime SLA in contract — add before signing
  • Da Vinci disposable cost not included in program financial model — major budget variance risk
  • Robotic spine platform incompatible with existing navigation equipment
SUBSTITUTION COMPLEXITY:   N/A (capital equipment — not formulary substitution)
  Robot decisions are strategic capital decisions, not supply chain substitutions.
  Use this module for TCO modeling and competitive evaluation only.
NOTES:
  Robotics is the single highest-cost, highest-lock-in decision in the perioperative supply
  chain portfolio. A ROSA vs. Mako decision at UIHC determines the implant vendor for
  every total knee and hip for the next decade. Do not allow individual surgeon or
  department preference to drive this decision without full multi-specialty TCO analysis.
```

---

---

# SECTION 7: THE EMERGING TECHNOLOGY BRIEF FORMAT

## 7.1 What It Is

The Emerging Technology Brief is a forward-looking intelligence format for tracking new technology before it arrives at UIHC. It is market intelligence, not a procurement decision document. It feeds the "in the queue" pipeline — technologies that need monitoring before they require full Device Brief evaluation.

Equivalent to the LDI "episode in development" queue: track it, set a review date, prepare before it lands.

---

## 7.2 Emerging Technology Brief Template

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
EMERGING TECHNOLOGY BRIEF
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
TECH ID:          [EMT-YYYY-###]
DATE:             [YYYY-MM-DD]
CATEGORY:         [device category — maps to Section 6 module]
TECHNOLOGY:       [name / brief description]
STAGE:            [IDE Trial / 510(k) Pending / Recently Cleared (<2 yrs) / Early Adoption]
STATUS:           WATCH / MONITOR / PREPARE / DEFER

  WATCH   — Aware; no action needed; re-evaluate in 12 months
  MONITOR — Active tracking; 6-month review cycle
  PREPARE — Likely arrival at UIHC within 12-24 months; begin preparation
  DEFER   — Technology assessed; not appropriate for UIHC at this time
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

KEY VENDORS DEVELOPING:
  [List vendors with active development / cleared products in this technology space]

CLINICAL PROBLEM BEING SOLVED:
  [What unmet clinical need does this technology address? Why now?]

REGULATORY STATUS:
  [IDE / 510(k) number if filed / clearance date if cleared / PMA timeline if applicable]
  [Link to ClinicalTrials.gov identifier if IDE study ongoing]

PUBLISHED EVIDENCE (current):
  [Summary of published clinical evidence. Be explicit about evidence quality.
  Early-stage technologies often have only IDE study data or single-center series.
  PubMed search query used: ...]
  Evidence Quality: [RCT / Prospective / Case Series / Preclinical / None]

COMPETITIVE THREAT TO CURRENT UIHC PORTFOLIO:
  [Does this technology challenge an existing formulary item or capital investment?
  If yes: which item(s), and what is the timeline for potential displacement?]

ESTIMATED ARRIVAL AT UIHC:
  [Conservative timeline estimate based on regulatory stage + adoption curve]

PREPARATION NEEDED:
  [What should supply chain / perioperative team do NOW to prepare?
  Examples: budget cycle notification, surgeon awareness, SPD training, capital planning]

NEXT REVIEW DATE:  [YYYY-MM-DD]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
BRIEF GENERATED: [timestamp] | UIHC MedOps OS v1.0 / MS-0001
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## 7.3 Example Emerging Technology Briefs

---

### EMT-2026-001: AI-Guided Total Joint Robotics (Next Generation)

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
EMERGING TECHNOLOGY BRIEF
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
TECH ID:          EMT-2026-001
DATE:             2026-06-27
CATEGORY:         Surgical Robotics — Total Joints
TECHNOLOGY:       AI-Guided Autonomous Cutting and Soft Tissue Balancing in
                  Total Knee Arthroplasty (TKA) — next-generation robotic platforms
                  with intraoperative AI adjustment (beyond current semi-active systems)
STAGE:            Early Adoption / IDE Trials for next-generation autonomy features
STATUS:           MONITOR
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

KEY VENDORS DEVELOPING:
  • Stryker (Mako 2.0 / enhanced AI modules): building AI-driven soft tissue balancing
    into Mako platform; ongoing IDE studies on autonomous bone resection verification
  • Zimmer Biomet (ROSA Next Gen): AI-guided alignment verification in active development
  • Think Surgical (TSolution One): fully autonomous bone preparation; 510(k) cleared
    for TKA; limited US adoption but represents the autonomous end of the spectrum
  • Brainlab / DePuy Synthes: AI-assisted navigation modules for VELYS platform
  • Monogram Orthopedics: computer-designed, robotically manufactured patient-specific
    implants; FDA Breakthrough Device Designation received

CLINICAL PROBLEM BEING SOLVED:
  Current semi-active robotic systems (Mako, ROSA, VELYS) require surgeon-guided bone
  resection within a pre-planned safe zone. The clinical problem they do NOT solve:
  intraoperative soft tissue balancing — the primary determinant of functional outcome
  and revision risk in TKA. Next-generation platforms aim to provide real-time AI-guided
  ligament tension analysis and autonomous adjustment of resection depth to achieve
  balanced flexion/extension gaps without manual iterative technique.
  Secondary problem: implant positioning reproducibility across high and low volume surgeons.

REGULATORY STATUS:
  • Think Surgical TSolution One: 510(k) cleared (K143608 — autonomous bone prep, TKA)
  • Mako enhanced AI features: IDE studies ongoing as of 2026; not yet cleared for
    autonomous soft tissue balancing
  • Monogram Orthopedics: Breakthrough Device Designation (FDA); PMA pathway anticipated
  • ClinicalTrials.gov: search "autonomous robotic total knee arthroplasty" — multiple
    active IDE studies (NCT identifiers current as of filing date)

PUBLISHED EVIDENCE (current):
  • TSolution One: single-center case series showing improved coronal alignment vs.
    conventional TKA (PMID search: "Think Surgical TSolution autonomous TKA outcomes")
  • Semi-active robotic TKA (Mako, current generation): meta-analyses showing improved
    component positioning but mixed evidence on functional outcomes vs. conventional TKA
    (PMID: 34726378 — meta-analysis, 12 RCTs)
  • AI soft tissue balancing: preclinical and early feasibility studies only as of 2026;
    no published RCT evidence for autonomous soft tissue adjustment
  Evidence Quality: CASE SERIES (TSolution) / PRECLINICAL (AI balancing autonomy)

COMPETITIVE THREAT TO CURRENT UIHC PORTFOLIO:
  HIGH. If UIHC has or is evaluating Mako or ROSA, next-generation AI features will be
  delivered as software upgrades to existing platforms (maintaining implant lock-in).
  If UIHC has NOT yet committed to a robotic TKA platform, this technology cycle argues
  for delaying capital commitment 12-18 months until AI feature availability is clearer.
  Monogram patient-specific autonomous approach would require entirely new capital commitment.

ESTIMATED ARRIVAL AT UIHC:
  • Enhanced AI modules for existing Mako/ROSA: 18-36 months (upgrade pathway)
  • New platform with full soft tissue AI integration: 36-60 months
  • Think Surgical TSolution: available now; limited adoption due to OR workflow changes

PREPARATION NEEDED:
  1. Flag in capital budget cycle: robotic TKA capital decision should account for
     next-generation AI timeline
  2. Include AI feature roadmap questions in any robotic TKA platform RFP
  3. Alert orthopedic surgery chief and total joint program director: technology landscape
     summary prepared — schedule 30-min briefing
  4. Add ClinicalTrials.gov monitoring for IDE studies: alert if any advance to pivotal stage
  5. Do NOT commit to robotic TKA capital in current budget cycle without explicit AI
     upgrade pathway guarantee from any vendor

NEXT REVIEW DATE: 2026-12-27
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
BRIEF GENERATED: 2026-06-27 | UIHC MedOps OS v1.0 / MS-0001
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

### EMT-2026-002: Next-Generation Amniotic-Based Biologics (Dehydrated vs. Cryopreserved)

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
EMERGING TECHNOLOGY BRIEF
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
TECH ID:          EMT-2026-002
DATE:             2026-06-27
CATEGORY:         Biologic Tissues / Allografts (HCT/P)
TECHNOLOGY:       Next-Generation Amniotic-Based Products — placental tissue allografts
                  with enhanced viability preservation claims; injectable amniotic formulations;
                  and FDA-contested "same surgical procedure" exemption products
STAGE:            Active Market (some products) / Regulatory Contested Status (others)
STATUS:           PREPARE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

KEY VENDORS DEVELOPING:
  • MiMedx (market leader): EpiFix (dehydrated amniotic membrane), AmnioFix (injection),
    OrthoFlo (injectable amniotic allograft) — largest portfolio; AATB accredited
  • Organogenesis: Affinity (cryopreserved placental membrane)
  • Osiris Therapeutics / Smith+Nephew: Grafix (cryopreserved amniotic membrane), Stravix
  • StimLabs: LNBM (lyophilized bone matrix with amnion layer)
  • Amniox Medical (Tissuetech): CLARIX Flo, NEOX (injectable and sheet forms)
  • Multiple emerging small manufacturers — significant AATB accreditation variability

CLINICAL PROBLEM BEING SOLVED:
  Amniotic tissue allografts are used for wound healing augmentation, tendon repair
  protection, and intra-articular injection for osteoarthritis pain management. The
  core clinical claim is growth factor and cytokine delivery to augment natural healing.
  Injectable amniotic products are being positioned for orthopedic applications (knee
  OA injection, rotator cuff repair augmentation) as an alternative to or complement
  to PRP (platelet-rich plasma) protocols. The next generation focuses on demonstrating
  maintained growth factor viability through improved preservation methods.

REGULATORY STATUS:
  CRITICAL NOTE — Regulatory landscape for amniotic products is contested and active:
  • Most amniotic membrane products: HCT/P under 21 CFR 1271.15(b) "same surgical
    procedure" exemption or 1271.3(d) "361 HCT/P" status — NOT subject to 510(k)/PMA
  • FDA enforcement discretion period extended repeatedly (2017 → 2021 → 2023) for
    products using "minimal manipulation / homologous use" criteria
  • CONTESTED: Injectable amniotic products (OrthoFlo, AmnioFlo): FDA sent warning
    letters to several manufacturers asserting these require BLA (351 product status,
    not 361 HCT/P). Enforcement status as of June 2026: monitor FDA guidance updates.
  • ClinicalTrials.gov: NCT04313478 (MiMedx OrthoFlo knee OA — Phase III), others active
  Action: verify regulatory status of any specific product with manufacturer before
  initiating procurement. Products with pending FDA enforcement action = formulary risk.

PUBLISHED EVIDENCE (current):
  • Dehydrated amniotic membrane (EpiFix): RCT evidence for chronic diabetic foot ulcers
    (PMID: 24702145, Snyder et al., Wound Repair Regen 2016); stronger evidence base
    for wound care than for orthopedic injection applications
  • Cryopreserved amniotic membrane (Grafix): RCT for DFU (PMID: 25527055); evidence
    quality moderate; sponsor involvement in primary trials
  • Injectable amniotic for knee OA: early feasibility data only; no peer-reviewed
    RCT as of mid-2026; Phase III trials ongoing (see ClinicalTrials.gov above)
  • Head-to-head: dehydrated vs. cryopreserved — limited direct comparative trials;
    preservation method effect on growth factor viability remains disputed in literature
  Evidence Quality: RCT for wound care applications / CASE SERIES for orthopedic injection

COMPETITIVE THREAT TO CURRENT UIHC PORTFOLIO:
  MEDIUM for wound care (if EpiFix challenges current wound care formulary).
  HIGH WATCH for orthopedic injection: if Phase III trials complete with positive results,
  injectable amniotic products could enter orthopedic and sports medicine service lines
  within 24-36 months, requiring new formulary category and procurement workflow.

ESTIMATED ARRIVAL AT UIHC:
  • Sheet amniotic for wound care: may already be in use — verify current formulary
  • Injectable amniotic for orthopedics (if Phase III positive): 24-36 months
  • Full FDA regulatory clarity on contested products: 12-24 months (watch FDA guidance)

PREPARATION NEEDED:
  1. Audit current formulary: confirm which amniotic products are currently in use at UIHC
     and verify AATB accreditation currency for all suppliers (annual check required)
  2. Monitor FDA enforcement action list for amniotic product warning letters —
     any active warning letter against a current supplier = immediate procurement review
  3. Brief wound care and orthopedic surgery service lines on regulatory uncertainty
     for injectable amniotic products — do not add injectable formulations to formulary
     until FDA enforcement status is resolved
  4. Prepare tissue bank compliance checklist for next-generation amniotic supplier
     evaluation (AATB accreditation, FDA registration, donor screening documentation)
  5. Flag for budget cycle: if Phase III knee OA trial results publish positive, prepare
     for formulary addition request from sports medicine / orthopedics

NEXT REVIEW DATE: 2026-12-27
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
BRIEF GENERATED: 2026-06-27 | UIHC MedOps OS v1.0 / MS-0001
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

### EMT-2026-003: Intelligent Energy Devices — AI-Integrated Electrosurgical and Ultrasonic Platforms

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
EMERGING TECHNOLOGY BRIEF
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
TECH ID:          EMT-2026-003
DATE:             2026-06-27
CATEGORY:         Endo Mechanicals / Energy Devices
TECHNOLOGY:       Intelligent Energy — AI-integrated generator platforms that
                  automatically adjust energy delivery based on real-time tissue sensing,
                  replacing fixed-parameter electrosurgical units (ESUs) and
                  ultrasonic energy devices with adaptive tissue feedback systems
STAGE:            Recently Cleared (some features) / Early Adoption
STATUS:           MONITOR
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

KEY VENDORS DEVELOPING:
  • Medtronic: Valleylab FT10 and FX8 (adaptive energy delivery ESUs — 510(k) cleared);
    Thunderbeat (ultrasonic + bipolar combined) — next generation in development
  • Ethicon (J&J): Echelon Energy HARMONIC series with ADAPT tissue sensing;
    ENSEAL X1 with advanced tissue fusion algorithms
  • Olympus: THUNDERBEAT Open Type with dual energy delivery — cleared and in use
  • Megadyne (Medtronic subsidiary): MEGA SOFT patient return electrode with impedance
    monitoring — foundational safety feature now being extended to output adaptation
  • AtriCure: sensing-integrated energy for cardiac surgery
  • Applied Medical: limited AI integration in current portfolio; watch for next generation

CLINICAL PROBLEM BEING SOLVED:
  Standard electrosurgical units require manual adjustment of energy settings by the
  surgeon or circulator as tissue type changes during a procedure (e.g., switching
  from fat to fascia to vessel). Incorrect settings increase: thermal spread and collateral
  tissue damage, risk of inadequate hemostasis, eschar buildup on instrument tips, and
  inadvertent burns (site injuries). Adaptive/intelligent energy platforms use real-time
  impedance monitoring and machine learning models to automatically optimize energy
  delivery parameters, targeting: faster vessel sealing, less thermal spread, fewer
  incomplete seals, and reduced surgeon cognitive load.
  Secondary problem: generator-instrument interoperability — new platforms aim to create
  intelligent communication between generator and handpiece.

REGULATORY STATUS:
  • Valleylab FT10/FX8: 510(k) cleared; in commercial distribution; ACCESSGUDID present
  • HARMONIC SYNERGY+: 510(k) cleared with adaptive tissue sensing features
  • Next-generation AI optimization features (deep tissue classification, autonomous
    parameter adjustment): several devices in 510(k) review as of 2026
  • ClinicalTrials.gov: search "adaptive electrosurgical tissue sealing" — early feasibility
    studies for next-generation platforms (NCT numbers: verify current status)

PUBLISHED EVIDENCE (current):
  • Ethicon HARMONIC vs. conventional: substantial RCT evidence base for ultrasonic energy
    in general surgery, bariatric, thyroid — well-established literature
  • Adaptive/intelligent energy features specifically: primarily manufacturer-sponsored
    feasibility studies and bench validation as of 2026
  • Thermal spread reduction with intelligent energy: multiple prospective studies showing
    reduction in lateral thermal spread vs. conventional monopolar (PMID: 28742373 and others)
  • AI-assisted setting optimization: early clinical data from Valleylab FT10 showing
    reduced hemostatic failure rate in laparoscopic procedures (single-center series)
  Evidence Quality: ESTABLISHED (conventional energy) / CASE SERIES (AI features specifically)

COMPETITIVE THREAT TO CURRENT UIHC PORTFOLIO:
  MEDIUM-HIGH. If UIHC currently has Ethicon HARMONIC or Medtronic Valleylab units under
  active contract, next-generation AI features may be delivered as software upgrades
  (same hardware, firmware update) or require new generator capital commitment.
  Key question: does current generator service contract include AI feature updates, or
  will vendor position this as a new capital acquisition?

ESTIMATED ARRIVAL AT UIHC:
  • Adaptive ESU features (Valleylab FT10/FX8): AVAILABLE NOW — check if UIHC already
    has these units; if yes, activate software features; if no, include in next ESU cycle
  • Full AI tissue classification with autonomous parameter adjustment: 18-36 months
    for broadly cleared, commercially available systems with published evidence

PREPARATION NEEDED:
  1. Inventory current ESU fleet: identify generator models, age, and service contract terms
  2. Request software roadmap from current energy vendor(s): what AI features are available
     now vs. upcoming; what hardware is required
  3. Review current ESU capital replacement cycle timing: if cycle due within 2 years,
     incorporate intelligent energy capability as evaluation criterion in next RFP
  4. Brief OR leadership and surgical techs: adaptive energy devices may change OR workflow
     (less manual adjustment); include in OR in-service planning
  5. For MAUDE monitoring: set up periodic query on product codes for current ESU platform
     to track adverse event trends as new AI features roll out

NEXT REVIEW DATE: 2026-12-27
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
BRIEF GENERATED: 2026-06-27 | UIHC MedOps OS v1.0 / MS-0001
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

---

# APPENDIX A: QUICK REFERENCE — ENDPOINTS AND RESOURCES

## FDA / NLM APIs

| Resource | URL |
|---|---|
| AccessGUDID (device lookup, DI) | `https://accessgudid.nlm.nih.gov/api/v2/devices/lookup.json?di={DI}` |
| AccessGUDID (bulk download) | `https://accessgudid.nlm.nih.gov/download` |
| AccessGUDID (daily RSS) | `https://accessgudid.nlm.nih.gov/download.rss?files=daily` |
| OpenFDA — 510(k) | `https://api.fda.gov/device/510k.json` |
| OpenFDA — PMA | `https://api.fda.gov/device/pma.json` |
| OpenFDA — Recalls | `https://api.fda.gov/device/recall.json` |
| OpenFDA — MAUDE | `https://api.fda.gov/device/event.json` |
| OpenFDA — Classification | `https://api.fda.gov/device/classification.json` |
| OpenFDA — UDI (GUDID mirror) | `https://api.fda.gov/device/udi.json` |
| OpenFDA API Key Registration | `https://open.fda.gov/apis/authentication/` |
| PubMed E-utilities (search) | `https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi` |
| PubMed E-utilities (fetch) | `https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi` |
| ClinicalTrials.gov API v2 | `https://clinicaltrials.gov/api/v2/` |
| SEC EDGAR (company filings) | `https://www.sec.gov/cgi-bin/browse-edgar` |

## Professional Societies and Registries

| Organization | URL |
|---|---|
| AHRMM (supply chain) | `https://www.ahrmm.org` |
| AJRR (joint replacement registry) | `https://www.aaos.org/registry/ajrr/` |
| AAOS (orthopaedic surgery) | `https://www.aaos.org` |
| NASS (spine surgery) | `https://www.spine.org` |
| SAGES (GI / laparoscopic) | `https://www.sages.org` |
| ASPS (plastic surgery) | `https://www.plasticsurgery.org` |
| AAO (ophthalmology) | `https://www.aao.org` |
| AATB (tissue banks) | `https://www.aatb.org` |
| AORN (perioperative nursing) | `https://www.aorn.org` |

## FDA Web Databases

| Database | URL |
|---|---|
| 510(k) Search | `https://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfpmn/pmn.cfm` |
| PMA Search | `https://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfpma/pma.cfm` |
| MAUDE Search | `https://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfmaude/search.cfm` |
| Recall Database | `https://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfRes/res.cfm` |
| Product Classification | `https://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfPCD/classification.cfm` |
| FDA Breast Implant Safety | `https://www.fda.gov/medical-devices/breast-implants` |

## Commercial Intelligence Tools (Reference — not automated in this pipeline)

| Tool | URL | Primary Use |
|---|---|---|
| Curvo Labs (BroadJump) | `https://www.gocurvo.com` | ASP benchmarking, GPO-neutral pricing |
| GHX + Lumere | `https://www.ghx.com` | Clinical evidence library, VAC workflow |
| MD Buyline (symplr) | `https://www.mdbuyline.com` | Capital equipment benchmarking |
| Definitive Healthcare | `https://www.definitivehc.com` | Market share, utilization data |
| Market Scope | `https://www.market-scope.com` | Ophthalmology market intelligence |

---

# APPENDIX B: COMPLIANCE REFERENCE

## Data Classification

| Data Type | PHI? | Restrictions |
|---|---|---|
| ACCESSGUDID device records | No | None — public data |
| OpenFDA MAUDE aggregate counts | No | None — aggregated |
| Individual MAUDE MDR report narratives | Possibly | May contain patient demographics; handle with care |
| Hospital item master data | No | Internal operational data |
| GPO contract pricing (specific) | No (not PHI, but confidential) | NDA / GPO member agreement; do not store |
| GPO pricing tiers (Entry/Mid/Premium) | No | Safe to reference; do not attribute to specific contract |
| Clinical literature (PubMed) | No | None |
| EHR patient data with device records | Yes | Full HIPAA/HITECH; BAA required; do not ingest into this system |
| Curvo / MD Buyline licensed data | No | Licensed data; usage restricted per service agreement |

**Bottom line:** This system operates entirely on public regulatory data and published literature. PHI boundary is only crossed if EHR-linked patient outcome data is ingested. Current architecture does not cross that boundary.

## Pricing Data Policy

Store pricing as tier references only:
- **Entry** — below market median for category
- **Mid** — at or near market median
- **Premium** — above market median; requires clinical evidence justification

Do not record specific GPO contract prices. Reference GPO contract number and tier designation only. When cost analysis is needed, use published benchmarks from peer-reviewed literature or Curvo aggregate ASP data under applicable license terms.

## Value Analysis Governance Note

- **OIG compliance**: Anti-kickback statute governs vendor-surgeon financial relationships in implant decisions. Sole-source physician preference arrangements without documented clinical justification create OIG exposure. This system's output documents constitute clinical justification documentation.
- **Joint Commission**: Device tracking for recalls is a survey requirement. GUDID-based recall monitoring directly supports this compliance requirement.
- **AATB accreditation**: Mandatory for all tissue suppliers (allografts, amniotic products). Annual verification required. Loss of accreditation = immediate formulary suspension.

---

*Document ID: MS-0001 | UIHC MedOps Research OS v1.0*
*Compiled: June 2026 | J. Burroughs, Supply Chain / Perioperative Services*
*Data sources: AccessGUDID NLM (accessgudid.nlm.nih.gov), FDA OpenFDA API (api.fda.gov),*
*AHRMM GUDID Best Practices Guide (ahrmm.org, 2023), GHX/Lumere product documentation,*
*Curvo Labs product documentation, AJRR Annual Report (aaos.org/registry/ajrr/),*
*PubMed comparative device studies, Robotomated procurement guide (2026),*
*FDA breast implant post-market safety page (fda.gov/medical-devices/breast-implants),*
*MedDeviceGuide GUDID Quality Analysis (2026).*
