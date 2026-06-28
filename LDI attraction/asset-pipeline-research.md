# Agentic AI Asset Generation Pipeline — Technical Research
**For: LDI Creative Media Operator | Platform: HP Victus (Windows, GPU) + Thought Reliquary (Ubuntu)**
**Date: June 2026**

---

## TABLE OF CONTENTS

1. [ComfyUI Agentic / Headless Operation](#1-comfyui-agentic--headless-operation)
2. [Style Extraction — Point-at-Webpage and Learn It](#2-style-extraction--point-at-webpage-and-learn-it)
3. [Video Effects — After Effects Equivalent in the AI Stack](#3-video-effects--after-effects-equivalent-in-the-ai-stack)
4. [Hugging Face API in the Pipeline](#4-hugging-face-api-in-the-pipeline)
5. [Gemini Vision + GPT-4V in the Asset Pipeline](#5-gemini-vision--gpt-4v-in-the-asset-pipeline)
6. [Thumbnail Generation Pipeline](#6-thumbnail-generation-pipeline)
7. [Site Asset Generation — CSS/SVG/WebGL Effects](#7-site-asset-generation--csssvgwebgl-effects)
8. [The Vision-Guided Style Clone Workflow](#8-the-vision-guided-style-clone-workflow)

---

## 1. COMFYUI AGENTIC / HEADLESS OPERATION

### 1.1 Running ComfyUI Headless

ComfyUI runs as an HTTP server on port `8188` by default. You interact with it purely through REST endpoints and WebSockets — no browser required.

**Key startup flags:**
```bash
# Headless (no browser opens)
python main.py --disable-auto-launch

# Custom port
python main.py --port 8288

# Listen on all network interfaces (required for cross-machine access)
python main.py --listen 0.0.0.0

# Combined: headless, LAN-accessible, GPU-optimized
.\python_embeded\python.exe -s ComfyUI\main.py --windows-standalone-build --normalvram --listen 0.0.0.0 --disable-auto-launch
```

For the Victus, edit `run_nvidia_gpu.bat` and add `--listen 0.0.0.0 --disable-auto-launch` to the command line.

**Source:** [ComfyUI Official Docs — Server Overview](https://docs.comfy.org/development/comfyui-server/comms_overview)

---

### 1.2 REST API Endpoints — Complete Reference

All endpoints also accessible with `/api/` prefix (e.g., `/api/prompt`).

| Verb | Endpoint | Purpose |
|------|----------|---------|
| `POST` | `/prompt` | Submit a workflow JSON for execution. Returns `prompt_id`. |
| `GET` | `/prompt` | Current queue status and execution info. |
| `GET` | `/queue` | Running and pending queue items. |
| `POST` | `/queue` | Delete items or clear queue: `{"clear": true}` or `{"delete": ["id1"]}` |
| `GET` | `/history` | Full execution history. |
| `GET` | `/history/{prompt_id}` | Results and output filenames for a specific run. |
| `POST` | `/history` | Clear history. |
| `GET` | `/view` | Fetch image bytes: `?filename=foo.png&subfolder=&type=output` |
| `POST` | `/upload/image` | Upload an image for use as input. Multipart form data. |
| `POST` | `/interrupt` | Cancel the currently executing workflow. |
| `POST` | `/free` | Free VRAM / system memory. |
| `GET` | `/system_stats` | GPU VRAM, Python version, device info. |
| `GET` | `/object_info` | All available node types with parameters. |
| `GET` | `/object_info/{node_class}` | Details on one node type. |
| `WS` | `/ws?clientId={uuid}` | Real-time execution status, node progress, previews. |

**Source:** [DeepWiki ComfyUI API Reference](https://deepwiki.com/Comfy-Org/ComfyUI/7-api-and-programmatic-usage), [Runflow Complete Guide](https://www.runflow.io/blog/comfyui-api-developer-guide)

---

### 1.3 Workflow Submission — The Core Pattern

**Step 1: Export workflow in API format**
In ComfyUI UI: Settings → Enable Dev Mode → Save (API Format). This produces a flat JSON where each key is a node ID.

**Step 2: The canonical Python client pattern**

```python
import json
import uuid
import urllib.request
import urllib.parse
import websocket  # pip install websocket-client

SERVER_ADDRESS = "192.168.1.100:8188"  # Victus IP
CLIENT_ID = str(uuid.uuid4())

def queue_prompt(prompt: dict) -> dict:
    payload = {"prompt": prompt, "client_id": CLIENT_ID}
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(f"http://{SERVER_ADDRESS}/prompt", data=data)
    return json.loads(urllib.request.urlopen(req).read())

def get_history(prompt_id: str) -> dict:
    url = f"http://{SERVER_ADDRESS}/history/{prompt_id}"
    with urllib.request.urlopen(url) as r:
        return json.loads(r.read())

def get_image(filename: str, subfolder: str, folder_type: str) -> bytes:
    params = urllib.parse.urlencode({
        "filename": filename, "subfolder": subfolder, "type": folder_type
    })
    url = f"http://{SERVER_ADDRESS}/view?{params}"
    with urllib.request.urlopen(url) as r:
        return r.read()

def run_workflow(workflow_path: str, overrides: dict = None) -> list[bytes]:
    """Run a workflow and return list of output image bytes."""
    with open(workflow_path) as f:
        workflow = json.load(f)
    
    # Apply parameter overrides (modify node inputs)
    if overrides:
        for node_id, inputs in overrides.items():
            for key, val in inputs.items():
                workflow[node_id]["inputs"][key] = val
    
    # Connect WebSocket for real-time tracking
    ws = websocket.WebSocket()
    ws.connect(f"ws://{SERVER_ADDRESS}/ws?clientId={CLIENT_ID}")
    
    prompt_id = queue_prompt(workflow)["prompt_id"]
    
    # Wait for completion signal
    while True:
        msg = ws.recv()
        if isinstance(msg, str):
            data = json.loads(msg)
            if (data["type"] == "executing" and
                data["data"]["node"] is None and
                data["data"]["prompt_id"] == prompt_id):
                break
    
    ws.close()
    
    # Retrieve outputs
    history = get_history(prompt_id)[prompt_id]
    images = []
    for node_output in history["outputs"].values():
        for img in node_output.get("images", []):
            images.append(get_image(img["filename"], img["subfolder"], img["type"]))
    
    return images

# Usage example:
images = run_workflow(
    "workflows/thumbnail_gen.json",
    overrides={
        "6": {"text": "Ancient Egyptian artifacts discovered beneath London"},
        "3": {"seed": 42}
    }
)
with open("output.png", "wb") as f:
    f.write(images[0])
```

**Available Python client libraries:**

| Library | Install | Notes |
|---------|---------|-------|
| `ComfyUI-PyClient` | `pip install ComfyUI-PyClient` | HTTP + WebSocket, sync/async |
| `comfyui-api-client` | `pip install comfyui-api-client` | WebSocket-based |
| `Comfyui_api_client` | `pip install Comfyui-api-client` | Sync + async versions |
| `websocket-client` | `pip install websocket-client` | Raw WebSocket (official examples use this) |

**Source:** [ComfyUI PyClient on Libraries.io](https://libraries.io/pypi/ComfyUI-PyClient), [Official script examples on HuggingFace](https://huggingface.co/spaces/Freak-ppa/ioatol/blob/382640ab6767fe3f702308c5ff7b8370319b68c1/ComfyUI/script_examples/websockets_api_example.py)

---

### 1.4 Workflow Templates for Common Tasks

**Thumbnail Generation (FLUX/SDXL text-to-image):**
- Nodes: `CheckpointLoaderSimple` → `CLIPTextEncode` (positive/negative) → `EmptyLatentImage` → `KSampler` → `VAEDecode` → `SaveImage`
- Key parameters to override: node `6` text (positive prompt), node `3` seed, node `5` width/height

**Style Transfer (img2img):**
- Nodes: `LoadImage` → `VAEEncode` → `KSampler` (with denoising_strength ~0.6-0.75) → `VAEDecode` → `SaveImage`

**Inpainting:**
- Nodes: `LoadImage` + `LoadImageMask` → `VAEEncodeForInpaint` → `KSampler` → `VAEDecode` → `SaveImage`

**Upscaling:**
- Nodes: `LoadImage` → `UpscaleModelLoader` (Real-ESRGAN x4) → `ImageUpscaleWithModel` → `SaveImage`

**IP-Adapter Style Transfer:**
- Custom nodes: `IPAdapterModelLoader` + `CLIPVisionLoader` + `IPAdapterAdvanced` → feeds into `KSampler`
- Install: ComfyUI Manager → search "ComfyUI_IPAdapter_plus"

---

### 1.5 ComfyUI Manager and Custom Node Ecosystem

ComfyUI Manager is the package manager for custom nodes. Install it once, then use it to add any node pack.

```bash
# Install ComfyUI Manager
cd ComfyUI/custom_nodes
git clone https://github.com/ltdrdata/ComfyUI-Manager
# Restart ComfyUI — Manager tab appears in UI
```

**Key custom nodes for automation pipelines:**

| Node Pack | Purpose | Install via Manager |
|-----------|---------|---------------------|
| `ComfyUI_IPAdapter_plus` | IP-Adapter style transfer | Yes |
| `ComfyUI-Advanced-ControlNet` | ControlNet with advanced scheduling | Yes |
| `ComfyUI-VideoHelperSuite` | Video loading/saving/combining | Yes |
| `ComfyUI-AnimateDiff-Evolved` | AnimateDiff motion modules | Yes |
| `ComfyUI-FluxTrainer` | LoRA training inside ComfyUI | Yes |
| `comfyui-tooling-nodes` | LAN image send/receive, scripting helpers | Yes |
| `FizzNodes` | Prompt scheduling/animation curves | Yes |
| `ComfyUI-REMBG` | Background removal via rembg | Yes |
| `ComfyUI_UltimateSDUpscale` | Tiled upscaling for large images | Yes |

**Source:** [ComfyUI Manager GitHub](https://github.com/comfy-org/ComfyUI-Manager)

---

### 1.6 LoRA Training for Style Consistency

Train a LoRA on LDI's specific visual aesthetic (e.g., rain-slicked neon, paranormal dark atmosphere) to get consistent outputs without extensive prompting.

**Method 1: ComfyUI-FluxTrainer (recommended, no extra software)**
```bash
# In ComfyUI Manager, install: ComfyUI-FluxTrainer (by kijai)
# Download FLUX dev model to models/diffusion_models/
# Download workflow: github.com/kijai/ComfyUI-FluxTrainer
# Dataset: 15-30 images of desired style, cropped to 1024x1024
# Training parameters:
#   - steps: 1000-2000
#   - learning_rate: 1e-4
#   - network_dim: 16-32
#   - trigger_word: "ldi_aesthetic"
```

**Method 2: Kohya_ss (more control)**
```bash
pip install kohya_ss
# Configure dataset in JSON format
# Train with: accelerate launch train_network.py --config_file=train_config.json
```

**Source:** [ComfyUI LoRA Training Guide](https://www.youtube.com/watch?v=8AZmT8gS7TI)

---

### 1.7 Running ComfyUI as a Windows Service (Auto-Start)

Use **NSSM** (Non-Sucking Service Manager) to run ComfyUI as a Windows background service that auto-starts on boot.

```powershell
# Install NSSM
winget install nssm

# Install ComfyUI as a service (run as Administrator)
nssm install ComfyUI

# In the NSSM GUI:
# Path: C:\ComfyUI\python_embeded\python.exe
# Startup directory: C:\ComfyUI\ComfyUI
# Arguments: -s main.py --windows-standalone-build --normalvram --listen 0.0.0.0 --disable-auto-launch

# Start/stop service manually:
nssm start ComfyUI
nssm stop ComfyUI

# Or use Windows Services (services.msc) — ComfyUI will appear in the list
```

**Alternatively: Task Scheduler** (simpler, no extra software)
- Create a task that triggers "At startup"
- Action: Run `run_nvidia_gpu.bat` with `--listen 0.0.0.0 --disable-auto-launch`
- Set "Run whether user is logged in or not"

**Source:** [NSSM Windows Service tutorial](https://www.youtube.com/watch?v=Clvsxu56zqs)

---

### 1.8 Cross-Machine Access: Thought Reliquary (Ubuntu) → Victus (Windows)

```bash
# On Victus (Windows): edit run_nvidia_gpu.bat
.\python_embeded\python.exe -s ComfyUI\main.py --windows-standalone-build --normalvram --listen 0.0.0.0

# Windows Firewall: Allow inbound on port 8188
# Control Panel → Windows Defender Firewall → Advanced Settings → 
# Inbound Rules → New Rule → Port → TCP 8188 → Allow

# Find Victus local IP
ipconfig  # Look for IPv4 Address under active adapter, e.g., 192.168.1.100

# On Thought Reliquary (Ubuntu): access ComfyUI
curl http://192.168.1.100:8188/system_stats
```

**Python client from Ubuntu to Victus:**
```python
SERVER_ADDRESS = "192.168.1.100:8188"  # Victus static LAN IP
# All other code identical — the API is network-transparent
```

**Tip:** Set a static LAN IP on the Victus via router DHCP reservation using its MAC address, so the IP never changes.

**Source:** [ComfyUI LAN Access Guide](https://comfyui-wiki.com/en/faq/how-to-access-comfyui-on-lan), [LAN access discussion](https://www.reddit.com/r/StableDiffusion/comments/14zto2t/access_comfyui_from_local_network/)

---

## 2. STYLE EXTRACTION — POINT-AT-WEBPAGE AND LEARN IT

### 2.1 Screenshot Capture Pipeline

**Playwright (recommended — Python native, more reliable than Puppeteer):**
```bash
pip install playwright
playwright install chromium
```

```python
from playwright.sync_api import sync_playwright
import base64

def capture_webpage(url: str, output_path: str = "screenshot.png") -> str:
    """Capture full-page screenshot of any URL."""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page(viewport={"width": 1440, "height": 900})
        page.goto(url, wait_until="networkidle")
        page.screenshot(path=output_path, full_page=True)
        browser.close()
    return output_path

def extract_css_styles(url: str) -> dict:
    """Extract computed CSS values from a live page."""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(url, wait_until="networkidle")
        
        styles = page.evaluate("""() => {
            const body = document.body;
            const computed = window.getComputedStyle(body);
            const h1 = document.querySelector('h1');
            const h1Computed = h1 ? window.getComputedStyle(h1) : null;
            
            // Get all CSS custom properties (design tokens)
            const rootStyles = window.getComputedStyle(document.documentElement);
            const cssVars = {};
            for (const prop of rootStyles) {
                if (prop.startsWith('--')) {
                    cssVars[prop] = rootStyles.getPropertyValue(prop).trim();
                }
            }
            
            return {
                backgroundColor: computed.backgroundColor,
                color: computed.color,
                fontFamily: computed.fontFamily,
                fontSize: computed.fontSize,
                bodyBackground: computed.backgroundImage,
                h1Font: h1Computed ? h1Computed.fontFamily : null,
                h1Weight: h1Computed ? h1Computed.fontWeight : null,
                cssVariables: cssVars,
                linkColor: window.getComputedStyle(document.querySelector('a') || body).color
            };
        }""")
        
        browser.close()
    return styles
```

**Puppeteer (Node.js alternative):**
```bash
npm install puppeteer
```

```javascript
const puppeteer = require('puppeteer');

async function captureAndExtract(url) {
    const browser = await puppeteer.launch({ headless: 'new' });
    const page = await browser.newPage();
    await page.setViewport({ width: 1440, height: 900 });
    await page.goto(url, { waitUntil: 'networkidle0' });
    await page.screenshot({ path: 'screenshot.png', fullPage: true });
    
    const styles = await page.evaluate(() => ({
        bgColor: getComputedStyle(document.body).backgroundColor,
        fontFamily: getComputedStyle(document.body).fontFamily,
        primaryColor: getComputedStyle(document.querySelector('a')).color
    }));
    
    await browser.close();
    return styles;
}
```

---

### 2.2 Color Palette Extraction (Python)

```bash
pip install colorthief Pillow scikit-learn
```

```python
from colorthief import ColorThief
from PIL import Image
import numpy as np
from sklearn.cluster import KMeans

def extract_palette(image_path: str, n_colors: int = 6) -> list[str]:
    """Extract dominant colors as hex codes."""
    # Method 1: ColorThief (fast)
    ct = ColorThief(image_path)
    palette = ct.get_palette(color_count=n_colors)
    return [f"#{r:02x}{g:02x}{b:02x}" for r, g, b in palette]

def extract_palette_kmeans(image_path: str, n_colors: int = 6) -> list[str]:
    """K-Means clustering for more accurate palette."""
    img = Image.open(image_path).convert("RGB")
    img = img.resize((200, 200))  # Downsample for speed
    pixels = np.array(img).reshape(-1, 3)
    
    kmeans = KMeans(n_clusters=n_colors, random_state=42, n_init=10)
    kmeans.fit(pixels)
    
    colors = kmeans.cluster_centers_.astype(int)
    return [f"#{r:02x}{g:02x}{b:02x}" for r, g, b in colors]
```

---

### 2.3 Vision LLM Style Analysis

**The structured style extraction prompt (works with any vision model):**

```python
STYLE_EXTRACTION_PROMPT = """
Analyze this screenshot of a website and produce a structured style brief in JSON format:

{
  "color_palette": {
    "primary_bg": "#hex",
    "secondary_bg": "#hex", 
    "primary_text": "#hex",
    "accent_1": "#hex",
    "accent_2": "#hex",
    "border_color": "#hex"
  },
  "typography": {
    "heading_font": "font name or description",
    "body_font": "font name or description",
    "font_weight_headings": "bold/semibold/light",
    "text_transform": "uppercase/lowercase/none",
    "letter_spacing": "tight/normal/wide"
  },
  "visual_mood": {
    "adjectives": ["dark", "cinematic", "mysterious"],
    "aesthetic_references": ["noir", "1980s synthwave", "occult manuscript"],
    "contrast_level": "high/medium/low",
    "lighting_feel": "neon glow / candlelight / harsh spotlight / diffused"
  },
  "layout_patterns": {
    "grid_type": "asymmetric/symmetric/editorial",
    "border_style": "description of borders or decorative elements",
    "spacing_density": "tight/comfortable/airy"
  },
  "image_generation_prompt": "A single image generation prompt that would produce an asset matching this site's aesthetic, describing style, color, mood, and atmosphere in 100 words."
}

Be specific about colors — use hex codes where you can infer them from the screenshot.
"""
```

---

### 2.4 IP-Adapter in ComfyUI for Style Transfer

IP-Adapter extracts the visual "essence" of a reference image and injects it as conditioning into the image generation process — without relying on prompts alone.

**Install:**
- ComfyUI Manager → Install "ComfyUI_IPAdapter_plus" (by cubiq)
- Download models: `ip-adapter_sdxl.safetensors`, `ip-adapter-plus_sdxl_vit-h.safetensors` → `ComfyUI/models/ipadapter/`
- Download CLIP Vision: `clip_vision_g.safetensors` → `ComfyUI/models/clip_vision/`

**Workflow node sequence:**
```
LoadImage (reference_style.png)
    ↓
IPAdapterModelLoader (ip-adapter-plus_sdxl_vit-h)
CLIPVisionLoader (clip_vision_g)
    ↓
IPAdapterAdvanced
    weight: 0.5-0.8 (higher = stronger style imprint)
    weight_type: "style transfer" | "strong style transfer"
    ↓
KSampler
    ↓
VAEDecode → SaveImage
```

**Weight types:**
- `style transfer` — transfers aesthetic without copying structure
- `strong style transfer` — more aggressive, may copy some compositional elements
- `composition` — preserves structure from reference

**Source:** [ComfyUI style transfer with IP-Adapter tutorial](https://comfyui.org/en/image-style-transfer-controlnet-ipadapter-workflow)

---

### 2.5 ControlNet for Structure Preservation

ControlNet preserves the structure (depth, edges, pose) of a source image while allowing style to change.

```
LoadImage (source.png)
    ↓
ControlNetPreprocessor (Canny/Depth/OpenPose)
    ↓
ControlNetLoader (control_sd15_canny.pth)
    ↓
ControlNetApply (strength: 0.8)
    ↓
CLIPTextEncode (style prompt)
    ↓
KSampler → VAEDecode → SaveImage
```

**Key ControlNet models for LDI use cases:**
- `Canny` — preserve hard edges and outlines
- `Depth` — preserve 3D depth structure 
- `Lineart` — preserve drawing/illustration lines
- `Segmentation` — preserve semantic regions

---

## 3. VIDEO EFFECTS — AFTER EFFECTS EQUIVALENT IN THE AI STACK

### 3.1 Remotion — Programmatic Video Composition

Remotion lets you write video compositions in React/TypeScript. It renders frames using a headless browser, producing broadcast-quality MP4s.

```bash
npx create-video@latest --yes --blank my-ldi-video
cd my-ldi-video
npm install
npm run dev  # Opens preview at localhost:3000
```

**Key capabilities:**
- Any React component = a video frame
- CSS animations, GSAP, SVG = all composited into video
- `useCurrentFrame()` and `interpolate()` for timeline control
- `Audio`, `Video`, `Img`, `Sequence` components built-in
- Renders via `npx remotion render` → MP4/WebM/GIF

```typescript
// Example: Lower third title card
import { useCurrentFrame, interpolate, AbsoluteFill } from 'remotion';

export const LDILowerThird = ({ title, subtitle }) => {
  const frame = useCurrentFrame();
  const opacity = interpolate(frame, [0, 20], [0, 1], { extrapolateRight: 'clamp' });
  const translateY = interpolate(frame, [0, 20], [30, 0], { extrapolateRight: 'clamp' });
  
  return (
    <AbsoluteFill style={{ justifyContent: 'flex-end', padding: 40 }}>
      <div style={{
        opacity,
        transform: `translateY(${translateY}px)`,
        background: 'rgba(0,0,0,0.8)',
        borderLeft: '4px solid #00ff88',
        padding: '12px 20px'
      }}>
        <div style={{ color: '#00ff88', fontFamily: 'Courier New', fontSize: 14 }}>{subtitle}</div>
        <div style={{ color: 'white', fontFamily: 'Impact', fontSize: 28 }}>{title}</div>
      </div>
    </AbsoluteFill>
  );
};
```

**Render programmatically:**
```typescript
import { renderMedia, selectComposition } from '@remotion/renderer';

const comp = await selectComposition({ serveUrl, id: 'LDILowerThird', inputProps: { title: 'THE WARDEN' } });
await renderMedia({
  composition: comp,
  serveUrl,
  codec: 'h264',
  outputLocation: 'output.mp4',
});
```

**Source:** [Remotion documentation](https://www.remotion.dev/docs)

---

### 3.2 Motion Canvas — TypeScript Code-First Animation

Motion Canvas uses TypeScript generator functions to define animations procedurally. Output: rendered video frames via FFmpeg.

```bash
npm init @motion-canvas@latest my-animation
cd my-animation
npm install
npm start  # Editor at localhost:9000
```

```typescript
// Lower third animation example
import { makeScene2D } from '@motion-canvas/2d/lib/scenes';
import { Rect, Txt } from '@motion-canvas/2d/lib/components';
import { createRef } from '@motion-canvas/core/lib/utils';
import { all, waitFor } from '@motion-canvas/core/lib/flow';

export default makeScene2D(function* (view) {
  const bar = createRef<Rect>();
  const titleText = createRef<Txt>();
  
  view.add(
    <Rect ref={bar} width={600} height={80} fill={'#0a0a0a'} 
          opacity={0} x={-200} y={300}
          stroke={'#ff3333'} lineWidth={2}>
      <Txt ref={titleText} text={'EPISODE 7: THE SIGNAL'} 
           fontFamily={'Courier New'} fontSize={24} fill={'white'} />
    </Rect>
  );
  
  yield* all(
    bar().opacity(1, 0.4),
    bar().x(0, 0.6)  // Slide in from left
  );
  yield* waitFor(3);
  yield* bar().opacity(0, 0.4);  // Fade out
});
```

**Best for:** Technical explainers, title cards, data visualizations, lower thirds with precise timing.
**Limitation:** More setup than Remotion, less CSS ecosystem integration.

**Source:** [Motion Canvas docs](https://motion-canvas-docs.vercel.app), [LavX News overview](https://news.lavx.hu/article/motion-canvas-animating-with-code-not-keyframes-using-typescript-generators)

---

### 3.3 FFmpeg + Python for Programmatic Video Effects

```bash
pip install ffmpeg-python  # Python wrapper
# Or use subprocess with ffmpeg binary directly
```

**Common effects for LDI aesthetic:**

```python
import subprocess

def apply_crt_filter(input_path: str, output_path: str):
    """CRT scanline + slight vignette + color shift."""
    cmd = [
        "ffmpeg", "-i", input_path,
        "-vf", (
            "curves=vintage,"  # Vintage color grade
            "vignette=PI/4,"   # Vignette corners
            "hue=s=0.8,"       # Slightly desaturated
            "noise=alls=5:allf=t+u"  # Film grain noise
        ),
        "-c:v", "libx264", "-crf", "18",
        output_path, "-y"
    ]
    subprocess.run(cmd, check=True)

def apply_glitch_effect(input_path: str, output_path: str):
    """Digital glitch / signal corruption effect."""
    cmd = [
        "ffmpeg", "-i", input_path,
        "-vf", (
            "rgbashift=rh=-3:bh=3,"  # Chromatic aberration
            "noise=c0s=30:c0f=t,"    # Luminance noise
            "vibrance=intensity=0.3"
        ),
        output_path, "-y"
    ]
    subprocess.run(cmd, check=True)

def create_animated_overlay(base_video: str, overlay_image: str, 
                             output: str, x: int = 50, y: int = 50):
    """Composite a PNG overlay (logo, border, element) on video."""
    cmd = [
        "ffmpeg", "-i", base_video, "-i", overlay_image,
        "-filter_complex", f"[1:v]scale=200:-1[ovr];[0:v][ovr]overlay={x}:{y}",
        "-c:v", "libx264",
        output, "-y"
    ]
    subprocess.run(cmd, check=True)

def fade_in_out(input_path: str, output_path: str, fade_duration: float = 0.5):
    """Add fade-in and fade-out to a clip."""
    # Get duration via ffprobe
    result = subprocess.run([
        "ffprobe", "-v", "error", "-show_entries", "format=duration",
        "-of", "default=noprint_wrappers=1:nokey=1", input_path
    ], capture_output=True, text=True)
    duration = float(result.stdout.strip())
    fade_out_start = duration - fade_duration
    
    cmd = [
        "ffmpeg", "-i", input_path,
        "-vf", f"fade=t=in:st=0:d={fade_duration},fade=t=out:st={fade_out_start}:d={fade_duration}",
        output_path, "-y"
    ]
    subprocess.run(cmd, check=True)
```

---

### 3.4 Runway ML Gen4/4.5 API

Runway provides the most capable commercial video generation API. Image-to-video, text-to-video, and video-to-video (transform existing footage).

```bash
pip install runwayml
```

```python
import os
from runwayml import RunwayML

client = RunwayML(api_key=os.environ["RUNWAYML_API_SECRET"])

# Image-to-video (Gen4 Turbo)
task = client.image_to_video.create(
    model="gen4_turbo",
    prompt_image="https://example.com/thumbnail.png",
    ratio="1280:720",
    prompt_text="Slow camera push into the ancient door, fog swirling, atmospheric",
    duration=5  # 5 or 10 seconds
)

# Poll for completion
import time
while True:
    result = client.tasks.retrieve(task.id)
    if result.status == "SUCCEEDED":
        print("Video URL:", result.output[0])
        break
    elif result.status == "FAILED":
        raise RuntimeError(f"Task failed: {result.failure}")
    time.sleep(5)
```

**Available models (2026):**
- `gen4_turbo` — fast, 5 credits/sec (25 credits for 5s)
- `gen4` — highest quality, 12 credits/sec (60 credits for 5s)
- `gen4_5` — improved quality + control
- `aleph2` — video-to-video with text prompt editing
- `seedance2_fast` — image/text/video input, 4-15 sec output

**Source:** [Runway API docs](https://docs.dev.runwayml.com), [RunwayML Python SDK](https://github.com/runwayml/sdk-python)

---

### 3.5 AnimateDiff in ComfyUI

AnimateDiff turns still-image checkpoints into video generators by adding a motion module.

**Setup:**
```
ComfyUI Manager → Install "ComfyUI-AnimateDiff-Evolved"
ComfyUI Manager → Install "ComfyUI-VideoHelperSuite"

# Download motion modules:
# mm_sd_v15_v2.ckpt → ComfyUI/custom_nodes/ComfyUI-AnimateDiff-Evolved/models/
# From: huggingface.co/guoyww/animatediff
```

**Workflow pattern:**
```
CheckpointLoaderSimple (SD 1.5 based checkpoint)
    ↓
AnimateDiffLoaderWithContext (motion module)
    ↓
CLIPTextEncode (positive/negative prompts)
    ↓
KSampler (batch_size=16 for 16 frames at ~2fps = ~8s clip)
    ↓
VAEDecode
    ↓
VHS_VideoCombine (creates MP4/GIF)
```

**Key parameters:**
- `context_length`: 16 frames typical
- `motion_scale`: 0.8-1.2 (higher = more motion)
- Add `IPAdapter` nodes before sampler for reference-image-guided animation

**Source:** [AnimateDiff ComfyUI guide](https://www.reddit.com/r/StableDiffusion/comments/16w4zcc/guide_comfyui_animatediff_guideworkflows/)

---

### 3.6 Stable Video Diffusion (SVD) in ComfyUI

SVD generates 14-25 frames from a single image, with natural camera motion.

```
ComfyUI Manager → Install "ComfyUI-Stable-Video-Diffusion" (by thecooltechguy)

# Download models to ComfyUI/models/svd/:
# svd_xt.safetensors (25 frames, better quality)
# From: stabilityai/stable-video-diffusion-img2vid-xt on HuggingFace
```

**Workflow:**
```
LoadImage (source.png)
    ↓
SVDModelLoader (svd_xt.safetensors)
    ↓
SVDSampler
    motion_bucket_id: 127 (higher = more motion)
    fps: 6
    augmentation_level: 0.0-0.02
    ↓
SVDDecoder
    ↓
VHS_VideoCombine → output.mp4
```

**Simplified with SVDSimpleImg2Vid node** (combines all three steps).

**Source:** [ComfyUI-Stable-Video-Diffusion GitHub](https://github.com/thecooltechguy/ComfyUI-Stable-Video-Diffusion)

---

### 3.7 Minimax Hailuo API (image-to-video, text-to-video)

Best-in-class for realistic motion, camera control, and longer clips. Native API access.

```python
import os, time, requests

api_key = os.environ["MINIMAX_API_KEY"]
headers = {"Authorization": f"Bearer {api_key}"}

def generate_video_from_image(image_url: str, prompt: str, 
                               duration: int = 6, resolution: str = "1080P") -> str:
    """Generate video from image. Returns local path to saved MP4."""
    # Step 1: Submit task
    response = requests.post(
        "https://api.minimax.io/v1/video_generation",
        headers=headers,
        json={
            "prompt": prompt,
            "first_frame_image": image_url,
            "model": "MiniMax-Hailuo-2.3",
            "duration": duration,
            "resolution": resolution
        }
    )
    task_id = response.json()["task_id"]
    
    # Step 2: Poll for completion
    while True:
        time.sleep(10)
        status_resp = requests.get(
            "https://api.minimax.io/v1/query/video_generation",
            headers=headers,
            params={"task_id": task_id}
        )
        data = status_resp.json()
        if data["status"] == "success":
            file_id = data["file_id"]
            break
        elif data["status"] == "failed":
            raise RuntimeError("Video generation failed")
    
    # Step 3: Retrieve download URL
    file_resp = requests.get(
        "https://api.minimax.io/v1/files/retrieve",
        headers=headers,
        params={"file_id": file_id}
    )
    download_url = file_resp.json()["file"]["download_url"]
    
    # Step 4: Download
    video_data = requests.get(download_url).content
    with open("output.mp4", "wb") as f:
        f.write(video_data)
    return "output.mp4"
```

**Camera movement control** (in prompt):
- `[Truck left]`, `[Pan right]`, `[Push in]`, `[Pull out]`, `[Tilt up]`, `[Zoom in]`
- Example: `"[Push in] Ancient stone corridor, torchlight flickering, fog at floor level"`

**Source:** [MiniMax API docs](https://platform.minimax.io/docs/guides/video-generation)

---

### 3.8 Kling API (image-to-video alternative)

```python
# Using klingapi.com (third-party proxy)
import requests, time

def kling_image_to_video(image_url: str, prompt: str, api_key: str) -> str:
    headers = {"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"}
    
    response = requests.post(
        "https://api.klingai.com/v1/videos/image2video",
        headers=headers,
        json={"image": image_url, "prompt": prompt, "duration": "5"}
    )
    task_id = response.json()["task_id"]
    
    while True:
        time.sleep(5)
        status = requests.get(f"https://api.klingai.com/v1/videos/{task_id}", 
                              headers=headers).json()
        if status.get("status") == "completed":
            return status["video_url"]
```

**Source:** [Kling AI API documentation](https://klingapi.com/docs)

---

### 3.9 Deforum in ComfyUI

Deforum enables video with temporal consistency — each frame influences the next via img2img chains, creating a "traveling through" effect.

**Install:** ComfyUI Manager → Install "comfyui-deforum"

**Key parameters:**
- `translation_x/y/z`: Camera pan/dolly per frame
- `rotation_x/y/z`: Camera tilt/roll/yaw
- `strength_schedule`: How much each frame deviates from the last (0.5-0.7 typical)
- `prompt_schedule`: Different prompts at different frame numbers

Best for: psychedelic transitions, dream sequences, morphing environments, the paranormal visual vibe.

---

## 4. HUGGING FACE API IN THE PIPELINE

### 4.1 Inference API — Serverless GPU (Quick Access)

```bash
pip install huggingface_hub
```

```python
from huggingface_hub import InferenceClient
import os

client = InferenceClient(api_key=os.environ["HF_TOKEN"])

# Text-to-image (FLUX.1-dev)
image = client.text_to_image(
    prompt="Dark paranormal landscape, rain-slicked streets, neon reflections, cinematic",
    model="black-forest-labs/FLUX.1-dev"
)
image.save("output.png")

# Image-to-image
with open("input.png", "rb") as f:
    result = client.image_to_image(
        image=f.read(),
        prompt="Transform to watercolor painting style",
        model="timbrooks/instruct-pix2pix"
    )
result.save("output.png")
```

**Key models available via Inference API:**

| Model | HF Path | Use Case |
|-------|---------|---------|
| FLUX.1-dev | `black-forest-labs/FLUX.1-dev` | Highest quality text-to-image |
| FLUX.1-schnell | `black-forest-labs/FLUX.1-schnell` | Fast text-to-image (Apache-2.0) |
| SDXL Base | `stabilityai/stable-diffusion-xl-base-1.0` | General generation |
| SD 3.5 Large | `stabilityai/stable-diffusion-3.5-large` | High quality generation |

**Rate limits:** Free tier is heavily rate-limited for GPU models. For production, use Inference Endpoints (see §4.3) or HF Spaces.

**Source:** [HF Inference Providers docs](https://huggingface.co/docs/hub/en/models-inference)

---

### 4.2 Gradio Client — Call Any HF Space Programmatically

Any Gradio app on HuggingFace Spaces can be called as an API. This includes community-built tools like REMBG, upscalers, and style transfer spaces.

```bash
pip install gradio_client
```

```python
from gradio_client import Client

# Connect to any public Space
client = Client("not-lain/background-removal")  # REMBG space
result = client.predict("image.png", api_name="/predict")

# Connect to private Space (requires HF token)
client = Client("myusername/my-private-space", hf_token="hf_...")

# Discover available API endpoints
client.view_api()  # Prints all available endpoints and their parameters

# Submit async job (non-blocking)
job = client.submit("prompt text", api_name="/generate")
result = job.result()  # Block until done

# Duplicate a Space to avoid rate limits
client = Client.duplicate("stabilityai/stable-diffusion", hf_token="hf_...")
```

**Useful Spaces for the pipeline:**

| Space | Use Case | ID |
|-------|---------|-----|
| Background removal | Remove BG from thumbnails | `not-lain/background-removal` |
| GFPGAN face restore | Fix faces in AI images | `avans06/Image_Face_Upscale_Restoration-GFPGAN` |
| CLIP Interrogator | Image → text prompt | `pharmapsychotic/CLIP-Interrogator` |
| Real-ESRGAN | 4x upscaling | `nightfury/Real-ESRGAN` |

**Source:** [Gradio Client PyPI](https://pypi.org/project/gradio-client/), [Gradio Python Client docs](https://www.gradio.app/main/docs/python-client/client)

---

### 4.3 HF Inference Endpoints — Dedicated Production GPU

For consistent, production-grade throughput: spin up a dedicated GPU instance on HF infrastructure.

```python
from huggingface_hub import InferenceClient

# After deploying an endpoint via huggingface.co/inference-endpoints
client = InferenceClient(
    model="https://your-endpoint-id.us-east-1.aws.endpoints.huggingface.cloud",
    token=os.environ["HF_TOKEN"]
)
image = client.text_to_image("Dark atmospheric thumbnail background")
```

**Pricing reference:**
- AWS A10G (24GB VRAM): ~$1/hr
- AWS T4 (16GB VRAM): ~$0.50/hr
- GCP L4 (24GB VRAM): ~$0.80/hr

Deploy via CLI:
```bash
pip install huggingface_hub
hf endpoints deploy my-flux-endpoint --repo black-forest-labs/FLUX.1-schnell \
  --framework pytorch --accelerator gpu --vendor aws --region us-east-1 \
  --instance-size x1 --instance-type nvidia-a10g --task text-to-image
```

**Source:** [HF Inference Endpoints pricing](https://huggingface.co/docs/inference-endpoints/en/pricing), [Enterprise endpoints cookbook](https://huggingface.co/learn/cookbook/en/enterprise_dedicated_endpoints)

---

### 4.4 Specific HF-Accessible Tools for LDI Pipeline

**Background Removal (rembg — local):**
```bash
pip install "rembg[gpu]"  # GPU version
# OR: pip install rembg   # CPU
```

```python
from rembg import remove
from PIL import Image

input_img = Image.open("thumbnail_with_bg.png")
output_img = remove(input_img)  # Returns RGBA PNG with transparent BG
output_img.save("thumbnail_no_bg.png")
```

**Face Restoration (GFPGAN — local):**
```bash
pip install gfpgan realesrgan basicsr facexlib
wget https://github.com/TencentARC/GFPGAN/releases/download/v1.3.0/GFPGANv1.4.pth
```

```python
from gfpgan import GFPGANer
import cv2

restorer = GFPGANer(
    model_path="GFPGANv1.4.pth", upscale=2, arch="clean", channel_multiplier=2
)
img = cv2.imread("ai_face_photo.jpg")
_, _, restored = restorer.enhance(img, has_aligned=False, only_center_face=False, paste_back=True)
cv2.imwrite("restored.jpg", restored)
```

**Image Upscaling (Real-ESRGAN — via ModelsLab API):**
```python
import requests

response = requests.post(
    "https://modelslab.com/api/v6/image_editing/super_resolution",
    json={
        "key": "YOUR_API_KEY",
        "url": "https://example.com/low-res.jpg",
        "scale": 4,
        "model_id": "RealESRGAN_x4plus",
        "face_enhance": False
    }
)
upscaled_url = response.json()["output"][0]
```

**Source:** [GFPGAN GitHub](https://github.com/tencentarc/gfpgan), [rembg GitHub](https://github.com/danielgatis/rembg), [Real-ESRGAN API](https://modelslab.com/real-esrgan)

---

### 4.5 HF vs. Local ComfyUI Decision Matrix

| Scenario | Use HF API | Use Local ComfyUI |
|----------|-----------|------------------|
| Quick iteration / prototyping | ✓ | |
| Need FLUX.1-dev or SDXL baseline | ✓ | ✓ |
| Need custom LoRA | | ✓ |
| Need IP-Adapter or ControlNet | | ✓ |
| Need AnimateDiff / SVD | | ✓ |
| High volume batch processing | ✓ (Endpoints) | ✓ |
| Need inpainting workflows | | ✓ |
| No local GPU available | ✓ | |

---

## 5. GEMINI VISION + GPT-4V IN THE ASSET PIPELINE

### 5.1 Gemini Vision API (Google)

Gemini 2.0 Flash and 2.5 Pro accept image inputs and produce structured JSON outputs — ideal for design analysis.

```bash
pip install google-genai
```

```python
import base64
import json
from google import genai

client = genai.Client()  # Uses GOOGLE_API_KEY env var

def analyze_screenshot_style(image_path: str) -> dict:
    """Analyze a webpage screenshot and extract design style."""
    with open(image_path, "rb") as f:
        image_bytes = f.read()
    
    interaction = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=[
            {
                "role": "user",
                "parts": [
                    {"text": STYLE_EXTRACTION_PROMPT},  # From Section 2.3
                    {
                        "inline_data": {
                            "mime_type": "image/png",
                            "data": base64.b64encode(image_bytes).decode("utf-8")
                        }
                    }
                ]
            }
        ]
    )
    
    # Parse JSON from response
    text = interaction.text
    json_start = text.find("{")
    json_end = text.rfind("}") + 1
    return json.loads(text[json_start:json_end])

def analyze_competitor_thumbnail(image_path: str) -> dict:
    """Analyze what makes a YouTube thumbnail work visually."""
    prompt = """
    Analyze this YouTube thumbnail and provide:
    1. PRIMARY HOOK: What is the main visual that draws the eye first?
    2. COLOR PSYCHOLOGY: How do the colors create emotion?
    3. COMPOSITION: Rule of thirds, focal points, negative space
    4. TEXT TREATMENT: Font weight, size, position, contrast
    5. FACE/EXPRESSION: If present, what emotion and why it works
    6. GENRE SIGNALS: What visual cues signal the content type?
    7. CTR PREDICTION: Rate 1-10 and explain why
    8. REPLICATION PROMPT: Write a 150-word prompt to create a similar thumbnail in ComfyUI
    
    Return as JSON.
    """
    # Same API call pattern as above with different prompt
    ...
```

**Gemini models for vision tasks:**

| Model | Context | Best For |
|-------|---------|---------|
| `gemini-2.0-flash` | 1M tokens | Fast analysis, cost-effective |
| `gemini-2.5-pro` | 2M tokens | Complex reasoning, highest accuracy |
| `gemini-2.5-flash` | 1M tokens | Balance of speed and quality |

**Source:** [Gemini API Vision docs](https://ai.google.dev/gemini-api/docs/vision)

---

### 5.2 GPT-4o Vision (OpenAI)

```bash
pip install openai
```

```python
import base64, json
from openai import OpenAI

client = OpenAI()  # Uses OPENAI_API_KEY env var

def analyze_image_gpt4o(image_path: str, prompt: str) -> str:
    with open(image_path, "rb") as f:
        image_data = base64.b64encode(f.read()).decode("utf-8")
    
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": prompt},
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/png;base64,{image_data}",
                            "detail": "high"  # "low" = 85 tokens, "high" = up to 4096 tokens
                        }
                    }
                ]
            }
        ],
        max_tokens=2000
    )
    return response.choices[0].message.content
```

---

### 5.3 Reference Image → Generation Prompt Pipeline

The core vision-to-generation loop:

```python
async def vision_to_comfyui_pipeline(
    reference_image_path: str,
    target_subject: str,
    comfyui_workflow_path: str
) -> bytes:
    """
    Complete pipeline: reference image → vision analysis → ComfyUI generation
    """
    
    # Step 1: Analyze reference image with Gemini
    style_data = analyze_screenshot_style(reference_image_path)
    
    # Step 2: Build ComfyUI prompt from extracted style
    color_desc = ", ".join(style_data["color_palette"].values())
    mood = " ".join(style_data["visual_mood"]["adjectives"])
    
    generation_prompt = (
        f"{target_subject}, "
        f"{mood} aesthetic, "
        f"color palette: {color_desc}, "
        f"{style_data['visual_mood']['lighting_feel']}, "
        f"cinematic composition, ultra detailed, 8k"
    )
    
    # Step 3: Run ComfyUI with generated prompt
    images = run_workflow(
        comfyui_workflow_path,
        overrides={"6": {"text": generation_prompt}}
    )
    
    return images[0]
```

---

### 5.4 Automated Prompt Refinement Loop

```python
def refinement_loop(
    initial_prompt: str,
    workflow_path: str,
    target_description: str,
    iterations: int = 3
) -> bytes:
    """Generate → Analyze → Critique → Regenerate."""
    
    current_prompt = initial_prompt
    
    for i in range(iterations):
        # Generate image
        images = run_workflow(workflow_path, overrides={"6": {"text": current_prompt}})
        
        # Save temp output
        temp_path = f"iteration_{i}.png"
        with open(temp_path, "wb") as f:
            f.write(images[0])
        
        # Analyze with vision model
        critique_prompt = f"""
        I'm trying to generate: "{target_description}"
        
        Current generation prompt was: "{current_prompt}"
        
        Looking at the generated image:
        1. What is working well?
        2. What is missing or wrong?
        3. Provide an improved prompt (keep under 200 words) that will better match the target.
        
        Return JSON: {{"working": "...", "missing": "...", "improved_prompt": "..."}}
        """
        
        result = json.loads(analyze_image_gpt4o(temp_path, critique_prompt))
        current_prompt = result["improved_prompt"]
        print(f"Iteration {i+1}: {result['missing']}")
    
    return images[0]
```

**Source:** [Microsoft Foundry GPT-4V prompt engineering](https://learn.microsoft.com/en-us/azure/foundry/openai/concepts/gpt-4-v-prompt-engineering)

---

## 6. THUMBNAIL GENERATION PIPELINE

### 6.1 Visual Psychology for Paranormal/Mystery YouTube

What works in this niche (based on thumbnail performance research):

| Element | Best Practice | LDI Application |
|---------|--------------|-----------------|
| **Background** | Deep black/navy with atmospheric fog | Dark voids, smoky environments |
| **Accent colors** | Electric teal, blood red, amber-gold | Map to Warden/Ghost/Root channel palettes |
| **Typography** | Heavy condensed caps (Impact, Bebas Neue) | White with 2px black stroke for contrast |
| **Image type** | Dramatic face OR mysterious object (NOT both) | Key artifact/subject centered |
| **Contrast** | Extremely high — thumbnail must read at 80px | Brightest element is the subject |
| **Border elements** | Subtle grain texture, glow edges | LDI signature border marks |
| **Number/question** | Digits and ? marks boost CTR | "7 CURSED SITES" outperforms "CURSED SITES" |

---

### 6.2 Full Automated Thumbnail Pipeline (Python)

```bash
pip install Pillow requests openai google-genai
```

```python
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageEnhance
import requests
import io

class LDIThumbnailGenerator:
    def __init__(self, width=1280, height=720):
        self.width = width
        self.height = height
    
    def generate_base_image(self, prompt: str, api: str = "flux") -> Image.Image:
        """Generate the base background/scene image."""
        if api == "dalle":
            from openai import OpenAI
            client = OpenAI()
            response = client.images.generate(
                model="dall-e-3",
                prompt=f"{prompt}, YouTube thumbnail, cinematic, dramatic lighting, 16:9 aspect ratio",
                size="1792x1024",
                quality="hd"
            )
            img_data = requests.get(response.data[0].url).content
            return Image.open(io.BytesIO(img_data)).resize((self.width, self.height))
        
        elif api == "comfyui":
            # Use ComfyUI workflow
            images = run_workflow("workflows/thumbnail.json", {"6": {"text": prompt}})
            return Image.open(io.BytesIO(images[0]))
    
    def add_text_overlay(
        self, 
        base: Image.Image, 
        title: str, 
        subtitle: str = None,
        title_color: tuple = (255, 255, 255),
        accent_color: tuple = (0, 255, 128)
    ) -> Image.Image:
        """Add styled text with shadow and outline."""
        img = base.copy()
        draw = ImageDraw.Draw(img)
        
        # Load fonts (download Bebas Neue, Impact, or use system fonts)
        try:
            title_font = ImageFont.truetype("BebasNeue-Regular.ttf", 100)
            sub_font = ImageFont.truetype("BebasNeue-Regular.ttf", 45)
        except:
            title_font = ImageFont.load_default(size=80)
            sub_font = ImageFont.load_default(size=40)
        
        # Position: bottom-left third
        margin = 50
        text_y = self.height - 220
        
        # Draw text shadow
        shadow_offset = 4
        draw.text((margin + shadow_offset, text_y + shadow_offset), 
                  title.upper(), font=title_font, fill=(0, 0, 0, 180))
        
        # Draw outline (stroke effect)
        for dx in [-2, -1, 0, 1, 2]:
            for dy in [-2, -1, 0, 1, 2]:
                if dx != 0 or dy != 0:
                    draw.text((margin + dx, text_y + dy), 
                              title.upper(), font=title_font, fill=(0, 0, 0))
        
        # Draw main text
        draw.text((margin, text_y), title.upper(), font=title_font, fill=title_color)
        
        # Subtitle / episode number
        if subtitle:
            draw.text((margin, text_y + 110), subtitle.upper(), 
                      font=sub_font, fill=accent_color)
        
        return img
    
    def apply_ldi_treatment(self, img: Image.Image) -> Image.Image:
        """Apply LDI-specific visual treatments."""
        # Boost contrast
        enhancer = ImageEnhance.Contrast(img)
        img = enhancer.enhance(1.3)
        
        # Slight color shift (cooler shadows, warmer highlights)
        # Add subtle vignette
        vignette = Image.new("RGBA", img.size, (0, 0, 0, 0))
        draw = ImageDraw.Draw(vignette)
        for i in range(100):
            opacity = int(i * 1.5)
            draw.ellipse(
                [i*3, i*2, self.width - i*3, self.height - i*2],
                outline=(0, 0, 0, opacity)
            )
        img = img.convert("RGBA")
        img = Image.alpha_composite(img, vignette)
        return img.convert("RGB")
    
    def add_border_elements(self, img: Image.Image, style: str = "warden") -> Image.Image:
        """Add LDI signature border marks and corner elements."""
        draw = ImageDraw.Draw(img)
        
        if style == "warden":
            accent = (0, 255, 128)  # Teal
        elif style == "ghost":
            accent = (100, 150, 255)  # Blue
        elif style == "root":
            accent = (255, 120, 0)  # Amber
        else:
            accent = (255, 255, 255)
        
        # Corner marks
        corner_size = 20
        line_width = 3
        corners = [(15, 15), (self.width-15, 15), 
                   (15, self.height-15), (self.width-15, self.height-15)]
        for cx, cy in corners:
            # L-shaped corner marks
            draw.line([(cx-corner_size, cy), (cx, cy)], fill=accent, width=line_width)
            draw.line([(cx, cy-corner_size), (cx, cy)], fill=accent, width=line_width)
        
        return img
    
    def generate(self, title: str, prompt: str, subtitle: str = None, 
                 channel: str = "warden", output_path: str = "thumbnail.png") -> str:
        """Full pipeline: prompt → base image → text → treatment → save."""
        base = self.generate_base_image(prompt)
        with_text = self.add_text_overlay(base, title, subtitle)
        with_treatment = self.apply_ldi_treatment(with_text)
        final = self.add_border_elements(with_treatment, style=channel)
        final.save(output_path, "PNG", quality=95)
        return output_path

# Usage
gen = LDIThumbnailGenerator()
gen.generate(
    title="The Vanished Lighthouse",
    subtitle="Episode 12",
    prompt="Abandoned lighthouse on rocky coast, storm approaching, lightning, dark moody atmosphere",
    channel="warden",
    output_path="ep12_thumbnail.png"
)
```

---

### 6.3 Figma API for Template-Based Generation

For template-based thumbnails with consistent branding (alternative to PIL):

```bash
npm install figma-api
```

```javascript
const Figma = require('figma-api');
const api = new Figma.Api({ personalAccessToken: process.env.FIGMA_TOKEN });

// Update text in a template frame
async function updateThumbnailTemplate(fileKey, nodeId, titleText) {
    // Note: Figma API is read-only for most operations
    // For programmatic generation, use the Figma REST API + Figma plugin or
    // export the template then manipulate with sharp/PIL
    
    const file = await api.getFileNodes(fileKey, [nodeId]);
    // Export the node as PNG with variable substitution via Figma plugin
}

// Better approach: Export frames via Figma REST API
async function exportFrame(fileKey, nodeId) {
    const response = await api.getImage(fileKey, {
        ids: nodeId,
        scale: 2,
        format: 'png'
    });
    return response.images[nodeId];  // URL to export
}
```

**Practical note:** For dynamic text, use PIL/Pillow over Figma API — Figma's API is primarily read-only. Consider **Figmatic** (`figmatic.dev`) for template automation.

---

### 6.4 YouTube A/B Testing via YouTube Data API

```python
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build

def update_thumbnail(video_id: str, thumbnail_path: str, credentials):
    youtube = build("youtube", "v3", credentials=credentials)
    youtube.thumbnails().set(
        videoId=video_id,
        media_body=thumbnail_path,
        media_mime_type="image/png"
    ).execute()

# A/B test: Upload variant thumbnail, track CTR via YouTube Analytics API
def get_video_ctr(video_id: str, credentials) -> float:
    analytics = build("youtubeAnalytics", "v2", credentials=credentials)
    response = analytics.reports().query(
        ids=f"channel==MINE",
        startDate="2026-01-01",
        endDate="2026-12-31",
        metrics="clickThroughRate,impressions",
        dimensions="video",
        filters=f"video=={video_id}"
    ).execute()
    return response["rows"][0][1]  # CTR
```

---

## 7. SITE ASSET GENERATION — CSS/SVG/WEBGL EFFECTS

### 7.1 CSS Glitch and Dark-Atmosphere Effects

**Glitch text effect (pure CSS):**
```css
.glitch-text {
  position: relative;
  color: #fff;
  animation: glitch 3s infinite;
}

.glitch-text::before,
.glitch-text::after {
  content: attr(data-text);
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
}

.glitch-text::before {
  color: #ff0033;
  clip-path: polygon(0 45%, 100% 45%, 100% 55%, 0 55%);
  transform: translate(-3px, 0);
  animation: glitch-slice-1 3s infinite;
}

.glitch-text::after {
  color: #00ffff;
  clip-path: polygon(0 70%, 100% 70%, 100% 80%, 0 80%);
  transform: translate(3px, 0);
  animation: glitch-slice-2 3s infinite;
}

@keyframes glitch-slice-1 {
  0%, 90%, 100% { transform: translate(-3px, 0); }
  92% { transform: translate(3px, -2px); clip-path: polygon(0 20%, 100% 20%, 100% 30%, 0 30%); }
  94% { transform: translate(-1px, 1px); clip-path: polygon(0 60%, 100% 60%, 100% 70%, 0 70%); }
}

@keyframes glitch-slice-2 {
  0%, 88%, 100% { transform: translate(3px, 0); }
  90% { transform: translate(-3px, 2px); clip-path: polygon(0 80%, 100% 80%, 100% 90%, 0 90%); }
  92% { transform: translate(1px, -1px); }
}
```

**CRT scanline overlay (pure CSS — add to `body::after`):**
```css
body {
  position: relative;
}

body::after {
  content: '';
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  pointer-events: none;
  z-index: 9999;
  background: repeating-linear-gradient(
    0deg,
    transparent,
    transparent 2px,
    rgba(0, 0, 0, 0.08) 2px,
    rgba(0, 0, 0, 0.08) 4px
  );
  animation: flicker 0.15s infinite;
}

@keyframes flicker {
  0%, 100% { opacity: 1; }
  50% { opacity: 0.95; }
}
```

**Signal noise / grain texture:**
```css
/* Using SVG filter for grain */
.grain-overlay {
  position: fixed;
  top: -50%;
  left: -50%;
  width: 200%;
  height: 200%;
  pointer-events: none;
  z-index: 9998;
  opacity: 0.05;
  animation: grain 0.5s steps(1) infinite;
  background-image: url("data:image/svg+xml,%3Csvg viewBox='0 0 256 256' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='noise'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.9' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23noise)'/%3E%3C/svg%3E");
}

@keyframes grain {
  0% { transform: translate(0, 0); }
  20% { transform: translate(-5%, -10%); }
  40% { transform: translate(-15%, 5%); }
  60% { transform: translate(7%, -15%); }
  80% { transform: translate(-5%, 15%); }
  100% { transform: translate(10%, 5%); }
}
```

**Neon glow border:**
```css
.neon-border {
  border: 1px solid #00ff88;
  box-shadow: 
    0 0 5px #00ff88,
    0 0 15px #00ff88,
    0 0 30px #00ff8840,
    inset 0 0 10px #00ff8810;
  animation: neon-pulse 2s ease-in-out infinite alternate;
}

@keyframes neon-pulse {
  from { box-shadow: 0 0 5px #00ff88, 0 0 15px #00ff88, 0 0 30px #00ff8840; }
  to   { box-shadow: 0 0 10px #00ff88, 0 0 25px #00ff88, 0 0 50px #00ff8860; }
}
```

**VISCSS framework** — ready-made dark aesthetic CSS with CRT, noise, and neon classes:
```html
<link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/viskem/viscss@v0.1.0/vis.css">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/viskem/viscss@v0.1.0/vis-effects.css">
<!-- Classes: .vfx-crt .vfx-noise .vfx-glow .vfx-preset-cyberpunk .vfx-preset-retro-terminal -->
```

**Source:** [Building Glitch Effects with Pure CSS](https://deloughry.co.uk/posts/building-glitch-effects-with-css/), [VISCSS framework](https://www.viscss.com)

---

### 7.2 SVG Animation for Signature Elements

**Signal waveform SVG animation:**
```html
<svg viewBox="0 0 400 100" xmlns="http://www.w3.org/2000/svg">
  <path id="signal" fill="none" stroke="#00ff88" stroke-width="2"/>
  <script>
    function generateSignalPath() {
      let d = "M 0 50";
      for (let x = 0; x <= 400; x += 2) {
        const y = 50 + Math.sin(x * 0.05 + Date.now() * 0.003) * 20 
                    + Math.sin(x * 0.13) * 8 
                    + (Math.random() > 0.97 ? (Math.random() - 0.5) * 40 : 0); // Glitch spikes
        d += ` L ${x} ${y}`;
      }
      document.getElementById("signal").setAttribute("d", d);
      requestAnimationFrame(generateSignalPath);
    }
    generateSignalPath();
  </script>
</svg>
```

**Root system growth (Warden aesthetic):**
```javascript
// Canvas-based procedural root growth
function drawRoots(canvas, color = '#00ff88') {
  const ctx = canvas.getContext('2d');
  const branches = [];
  
  function Branch(x, y, angle, length, depth) {
    this.x = x; this.y = y; this.angle = angle;
    this.length = length; this.depth = depth;
    this.progress = 0;
  }
  
  branches.push(new Branch(canvas.width/2, canvas.height, -Math.PI/2, 100, 0));
  
  function animate() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    branches.forEach(b => {
      b.progress = Math.min(b.progress + 0.02, 1);
      const endX = b.x + Math.cos(b.angle) * b.length * b.progress;
      const endY = b.y + Math.sin(b.angle) * b.length * b.progress;
      ctx.beginPath();
      ctx.moveTo(b.x, b.y);
      ctx.lineTo(endX, endY);
      ctx.strokeStyle = color;
      ctx.lineWidth = Math.max(0.5, 3 - b.depth * 0.5);
      ctx.globalAlpha = 0.7 - b.depth * 0.1;
      ctx.stroke();
      
      if (b.progress === 1 && b.depth < 6 && Math.random() > 0.7) {
        branches.push(new Branch(endX, endY, 
          b.angle + (Math.random() - 0.5) * 1.2, 
          b.length * 0.7, b.depth + 1));
      }
    });
    requestAnimationFrame(animate);
  }
  animate();
}
```

---

### 7.3 GSAP for Entrance Animations and Scroll Reveals

```bash
npm install gsap
# OR CDN:
# <script src="https://cdn.jsdelivr.net/npm/gsap@3.12.5/dist/gsap.min.js"></script>
# <script src="https://cdn.jsdelivr.net/npm/gsap@3.12.5/dist/ScrollTrigger.min.js"></script>
```

```javascript
import gsap from 'gsap';
import ScrollTrigger from 'gsap/ScrollTrigger';
gsap.registerPlugin(ScrollTrigger);

// Entrance animation: elements appear with glitch-in effect
gsap.from('.section-title', {
  duration: 0.8,
  opacity: 0,
  y: 30,
  skewX: -5,
  ease: 'power3.out',
  stagger: 0.1
});

// Scroll-triggered reveal
gsap.from('.artifact-card', {
  scrollTrigger: {
    trigger: '.artifacts-grid',
    start: 'top 80%',
    toggleActions: 'play none none reverse'
  },
  opacity: 0,
  y: 50,
  duration: 0.6,
  stagger: 0.15,
  ease: 'power2.out'
});

// Parallax depth layers
gsap.to('.bg-layer-1', {
  scrollTrigger: {
    trigger: 'body',
    start: 'top top',
    end: 'bottom bottom',
    scrub: 1
  },
  y: '-20%',
  ease: 'none'
});

// Neon border pulse on hover
document.querySelectorAll('.neon-card').forEach(card => {
  card.addEventListener('mouseenter', () => {
    gsap.to(card, { boxShadow: '0 0 30px #00ff88', duration: 0.3 });
  });
  card.addEventListener('mouseleave', () => {
    gsap.to(card, { boxShadow: '0 0 10px #00ff8860', duration: 0.5 });
  });
});
```

**Source:** [GSAP ScrollTrigger tutorial](https://www.youtube.com/watch?v=sND4EO6L4vA)

---

### 7.4 Three.js / WebGL for Particle Systems and Shader Effects

```bash
npm install three
```

```javascript
import * as THREE from 'three';

// Signal static / void shimmer shader
const staticFragShader = `
  uniform float uTime;
  uniform vec2 uResolution;
  varying vec2 vUv;
  
  float random(vec2 st) {
    return fract(sin(dot(st, vec2(12.9898, 78.233))) * 43758.5453123);
  }
  
  void main() {
    vec2 uv = vUv;
    
    // Scanlines
    float scanline = step(0.5, fract(uv.y * 50.0));
    
    // Static noise (time-varying)
    float noise = random(uv + vec2(uTime * 0.1, 0.0));
    float noise2 = random(uv * 2.0 + vec2(0.0, uTime * 0.07));
    
    // Chromatic aberration
    float r = random(uv + vec2(0.003, 0.0) + uTime * 0.001);
    float b = random(uv - vec2(0.003, 0.0) + uTime * 0.001);
    
    vec3 color = vec3(r * 0.8, noise2 * 0.7, b * 0.8);
    color *= 0.3 + scanline * 0.1;
    
    gl_FragColor = vec4(color, 0.15);
  }
`;

function createStaticOverlay(container) {
  const renderer = new THREE.WebGLRenderer({ alpha: true });
  renderer.setSize(window.innerWidth, window.innerHeight);
  container.appendChild(renderer.domElement);
  
  const scene = new THREE.Scene();
  const camera = new THREE.OrthographicCamera(-1, 1, 1, -1, 0, 1);
  
  const material = new THREE.ShaderMaterial({
    fragmentShader: staticFragShader,
    vertexShader: `varying vec2 vUv; void main() { vUv = uv; gl_Position = vec4(position, 1.0); }`,
    uniforms: {
      uTime: { value: 0 },
      uResolution: { value: new THREE.Vector2(window.innerWidth, window.innerHeight) }
    },
    transparent: true
  });
  
  const plane = new THREE.Mesh(new THREE.PlaneGeometry(2, 2), material);
  scene.add(plane);
  
  function animate(t) {
    material.uniforms.uTime.value = t * 0.001;
    renderer.render(scene, camera);
    requestAnimationFrame(animate);
  }
  requestAnimationFrame(animate);
}
```

**Source:** [Three.js digital static noise shader](https://gist.github.com/zouloux/dddd0c48f632077a20dc), [Three.js + GSAP particle system](https://github.com/isladjan/particles-playground)

---

### 7.5 Lottie Animations — After Effects to Web

Lottie lets you export After Effects animations as JSON and play them natively in browsers, React, iOS, and Android.

**Workflow:**
1. Create animation in After Effects
2. Install Bodymovin plugin (Window → Extensions → Bodymovin)
3. Enable scripting: Edit → Preferences → Scripting → Allow Scripts to Write Files
4. Export: Select composition → Render → saves `animation.json`

**Web implementation:**
```bash
npm install lottie-web
```

```javascript
import lottie from 'lottie-web';

const animation = lottie.loadAnimation({
  container: document.getElementById('lottie-container'),
  renderer: 'svg',  // 'svg' | 'canvas' | 'html'
  loop: true,
  autoplay: true,
  path: '/animations/ldi-logo-reveal.json'
});

// Control programmatically
animation.play();
animation.pause();
animation.setSpeed(1.5);
animation.goToAndPlay(30, true);  // Go to frame 30 and play
```

**React:**
```bash
npm install @lottiefiles/react-lottie-player
```

```jsx
import { Player } from '@lottiefiles/react-lottie-player';

<Player
  autoplay
  loop
  src="/animations/glitch-logo.json"
  style={{ height: '150px', width: '150px' }}
/>
```

**Lottie limitations (design for export):**
- ❌ No effects (glow, blur) — they won't export
- ❌ No 3D layers, expressions, or time remapping
- ✅ Shapes, masks, text, solid layers, transforms

**Source:** [Lottie Airbnb GitHub](https://github.com/airbnb/lottie-web), [Bodymovin After Effects export guide](https://www.linkedin.com/posts/sviatoslav-motion_how-to-export-lottie-from-after-effects-activity-7364249162567061506-7_MF)

---

## 8. THE VISION-GUIDED STYLE CLONE WORKFLOW

**Complete end-to-end pipeline: point a tool at a webpage → learn its visual language → generate assets in that style.**

---

### STAGE 1: Screenshot Capture

```python
# install: pip install playwright && playwright install chromium
from playwright.sync_api import sync_playwright

def capture_site(url: str, output_dir: str = "site_analysis") -> dict:
    """Capture full-page screenshot + extract CSS computed values."""
    import os; os.makedirs(output_dir, exist_ok=True)
    
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page(viewport={"width": 1440, "height": 900})
        page.goto(url, wait_until="networkidle", timeout=30000)
        
        # Full-page screenshot
        screenshot_path = f"{output_dir}/screenshot.png"
        page.screenshot(path=screenshot_path, full_page=False)  # Above-fold first
        
        # Extract computed styles
        css_data = page.evaluate("""() => {
            const computed = window.getComputedStyle(document.body);
            const root = window.getComputedStyle(document.documentElement);
            const cssVars = {};
            for (const p of root) {
                if (p.startsWith('--')) cssVars[p] = root.getPropertyValue(p).trim();
            }
            const firstH1 = document.querySelector('h1, h2, .title, [class*="heading"]');
            const firstAccent = document.querySelector('a, button, .btn, [class*="accent"]');
            return {
                bg: computed.backgroundColor,
                text: computed.color,
                fontFamily: computed.fontFamily,
                h1Font: firstH1 ? getComputedStyle(firstH1).fontFamily : null,
                accentColor: firstAccent ? getComputedStyle(firstAccent).color : null,
                cssVars
            };
        }""")
        
        browser.close()
    
    css_data["screenshot_path"] = screenshot_path
    css_data["url"] = url
    return css_data
```

---

### STAGE 2: Vision Model Analysis

```python
import base64, json
from google import genai

def analyze_visual_language(screenshot_path: str, css_data: dict) -> dict:
    """Use Gemini to analyze the visual design language."""
    client = genai.Client()
    
    with open(screenshot_path, "rb") as f:
        img_b64 = base64.b64encode(f.read()).decode("utf-8")
    
    # Include CSS data to give the model ground truth values
    css_context = f"""
    Measured CSS values from the live page:
    - Background: {css_data.get('bg')}
    - Text: {css_data.get('text')}
    - Font: {css_data.get('fontFamily')}
    - H1 Font: {css_data.get('h1Font')}
    - Accent: {css_data.get('accentColor')}
    - CSS Variables: {json.dumps(css_data.get('cssVars', {}), indent=2)[:500]}
    """
    
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=[{
            "role": "user",
            "parts": [
                {"text": f"""
                Analyze this website screenshot along with the provided CSS measurements.
                
                {css_context}
                
                Produce a complete style brief as JSON:
                {{
                  "color_palette": {{
                    "primary_bg": "#000000",
                    "secondary_bg": "#111111", 
                    "primary_text": "#ffffff",
                    "accent_1": "#00ff88",
                    "accent_2": "#ff3333",
                    "muted": "#666666"
                  }},
                  "typography": {{
                    "heading_font": "exact font name",
                    "body_font": "exact font name",
                    "weight": "regular/medium/bold",
                    "tracking": "tight/normal/wide",
                    "case": "uppercase/mixed"
                  }},
                  "visual_mood": {{
                    "primary_adjectives": ["dark", "atmospheric", "mysterious"],
                    "genre_aesthetic": "paranormal documentary / noir / occult",
                    "contrast": "high/medium/low",
                    "saturation": "desaturated/muted/vibrant",
                    "lighting": "neon glow / candlelight / harsh spotlight"
                  }},
                  "component_patterns": {{
                    "card_style": "description",
                    "border_style": "description",
                    "spacing": "tight/comfortable/airy",
                    "image_treatment": "description"
                  }},
                  "sdxl_prompt": "150-word image generation prompt that would produce an asset matching this aesthetic",
                  "negative_prompt": "50-word negative prompt"
                }}
                
                Use the measured CSS values to populate color_palette accurately.
                """},
                {
                    "inline_data": {
                        "mime_type": "image/png",
                        "data": img_b64
                    }
                }
            ]
        }]
    )
    
    text = response.text
    start = text.find("{")
    end = text.rfind("}") + 1
    return json.loads(text[start:end])
```

---

### STAGE 3: CSS Extraction (Actual Values)

```python
def extract_complete_styles(url: str) -> dict:
    """Deep CSS extraction: fonts, colors, spacing, all computed values."""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(url, wait_until="networkidle")
        
        deep_styles = page.evaluate("""() => {
            // Sample key elements
            const selectors = ['body', 'h1', 'h2', 'h3', 'p', 'a', 'button', 
                               'header', 'nav', '.hero', '.card', 'footer'];
            const result = {};
            
            selectors.forEach(sel => {
                const el = document.querySelector(sel);
                if (!el) return;
                const s = getComputedStyle(el);
                result[sel] = {
                    color: s.color,
                    backgroundColor: s.backgroundColor,
                    fontFamily: s.fontFamily,
                    fontSize: s.fontSize,
                    fontWeight: s.fontWeight,
                    letterSpacing: s.letterSpacing,
                    textTransform: s.textTransform,
                    borderColor: s.borderColor,
                    borderWidth: s.borderWidth,
                    boxShadow: s.boxShadow,
                    padding: s.padding,
                    margin: s.margin
                };
            });
            
            // Extract all used colors from visible elements
            const allColors = new Set();
            document.querySelectorAll('*').forEach(el => {
                const s = getComputedStyle(el);
                ['color', 'backgroundColor', 'borderColor', 'outlineColor'].forEach(prop => {
                    const val = s[prop];
                    if (val && val !== 'rgba(0, 0, 0, 0)' && val !== 'transparent') {
                        allColors.add(val);
                    }
                });
            });
            
            return { elements: result, allColors: [...allColors].slice(0, 50) };
        }""")
        
        browser.close()
    return deep_styles
```

---

### STAGE 4: Style Description Synthesis (Claude API)

```python
import anthropic

def synthesize_style_brief(css_data: dict, visual_analysis: dict) -> str:
    """Use Claude to synthesize CSS values + visual analysis into actionable design brief."""
    client = anthropic.Anthropic()
    
    message = client.messages.create(
        model="claude-opus-4-5",
        max_tokens=2000,
        messages=[{
            "role": "user",
            "content": f"""
            I have extracted the following data from a website:
            
            RAW CSS VALUES:
            {json.dumps(css_data, indent=2)[:2000]}
            
            VISUAL ANALYSIS:
            {json.dumps(visual_analysis, indent=2)}
            
            Synthesize this into a comprehensive creative brief with:
            
            1. DESIGN SYSTEM (colors, fonts, spacing rules)
            2. VISUAL VOICE (3 sentences describing the aesthetic personality)
            3. ASSET GENERATION RULES (what makes every asset feel native to this brand)
            4. DO/DON'T LIST (5 of each)
            5. COMFYUI WORKFLOW RECOMMENDATIONS (which workflows to use for this aesthetic)
            6. CSS SNIPPET (20 lines of CSS that captures the core atmosphere)
            
            Be specific and actionable. This brief will be used by an AI asset generation pipeline.
            """
        }]
    )
    return message.content[0].text
```

---

### STAGE 5: Image Generation with Extracted Style

```python
def generate_style_matched_assets(
    style_brief: dict,
    asset_type: str,  # "thumbnail_bg", "border_element", "icon", "hero_image"
    subject: str,
    comfyui_server: str = "192.168.1.100:8188"
) -> list[bytes]:
    """Generate assets conditioned on extracted style data."""
    
    # Build ComfyUI prompt from style analysis
    color_palette = style_brief.get("color_palette", {})
    mood = style_brief.get("visual_mood", {})
    
    base_prompt = style_brief.get("sdxl_prompt", "")
    
    # Asset-type specific additions
    type_modifiers = {
        "thumbnail_bg": "dramatic composition, space for text overlay, vignette",
        "border_element": "decorative border element, transparent background, isolated",
        "icon": "icon design, flat design, minimal, isolated on black",
        "hero_image": "wide format, cinematic aspect ratio, atmospheric"
    }
    
    full_prompt = f"{subject}, {base_prompt}, {type_modifiers.get(asset_type, '')}"
    
    # For IP-Adapter: use screenshot as style reference if workflow supports it
    # For text2img: use the generated prompt directly
    
    images = run_workflow(
        f"workflows/{asset_type}.json",
        overrides={
            "6": {"text": full_prompt},
            "7": {"text": style_brief.get("negative_prompt", "low quality, blurry")}
        }
    )
    
    return images
```

---

### STAGE 6: Complete Pipeline Runner

```python
class StyleClonePipeline:
    """Full pipeline: URL → style analysis → asset generation."""
    
    def __init__(self, comfyui_server: str = "192.168.1.100:8188"):
        self.comfyui_server = comfyui_server
        self.output_dir = "pipeline_output"
        os.makedirs(self.output_dir, exist_ok=True)
    
    def run(self, url: str, assets_to_generate: list[dict]) -> dict:
        """
        assets_to_generate example:
        [
            {"type": "thumbnail_bg", "subject": "ancient ritual chamber"},
            {"type": "border_element", "subject": "circuit trace decorative border"},
            {"type": "hero_image", "subject": "abandoned research facility"},
        ]
        """
        results = {}
        
        print(f"[1/6] Capturing screenshot of {url}...")
        site_data = capture_site(url)
        
        print("[2/6] Analyzing visual language with Gemini...")
        visual_analysis = analyze_visual_language(
            site_data["screenshot_path"], site_data
        )
        
        print("[3/6] Extracting deep CSS styles...")
        css_styles = extract_complete_styles(url)
        
        print("[4/6] Synthesizing style brief with Claude...")
        style_brief_text = synthesize_style_brief(css_styles, visual_analysis)
        
        # Merge visual analysis with synthesized brief
        full_brief = {**visual_analysis, "synthesis": style_brief_text}
        
        # Save brief
        brief_path = f"{self.output_dir}/style_brief.json"
        with open(brief_path, "w") as f:
            json.dump(full_brief, f, indent=2)
        print(f"   Style brief saved to {brief_path}")
        
        print("[5/6] Generating assets with ComfyUI...")
        for asset in assets_to_generate:
            print(f"   Generating: {asset['type']} — {asset['subject']}")
            images = generate_style_matched_assets(
                full_brief, asset["type"], asset["subject"]
            )
            
            for i, img_data in enumerate(images):
                out_path = f"{self.output_dir}/{asset['type']}_{i:02d}.png"
                with open(out_path, "wb") as f:
                    f.write(img_data)
                results[f"{asset['type']}_{i}"] = out_path
        
        print("[6/6] Pipeline complete.")
        return {"brief": brief_path, "assets": results}

# ─── USAGE ───────────────────────────────────────────────────────────────────
pipeline = StyleClonePipeline(comfyui_server="192.168.1.100:8188")

results = pipeline.run(
    url="https://competitor-paranormal-channel.com",
    assets_to_generate=[
        {"type": "thumbnail_bg", "subject": "haunted lighthouse at night"},
        {"type": "border_element", "subject": "signal interference decorative frame"},
        {"type": "hero_image", "subject": "ancient map with glowing markers"},
    ]
)

print("Generated assets:", results["assets"])
```

---

### Tool-by-Tool Reference for Each Stage

| Stage | Tool | Install | Notes |
|-------|------|---------|-------|
| Screenshot | `playwright` | `pip install playwright && playwright install chromium` | Best cross-platform headless browser |
| Screenshot | `puppeteer` | `npm install puppeteer` | Node.js alternative |
| CSS extraction | Playwright `evaluate()` | (same install) | `window.getComputedStyle()` on all elements |
| Color extraction | `colorthief` | `pip install colorthief` | Fast dominant color extraction |
| Color extraction | `scikit-learn` KMeans | `pip install scikit-learn` | More accurate palette clustering |
| Vision analysis | `google-genai` | `pip install google-genai` | Gemini 2.0 Flash vision |
| Vision analysis | `openai` | `pip install openai` | GPT-4o with `detail: "high"` |
| Style synthesis | `anthropic` | `pip install anthropic` | Claude for creative brief writing |
| Image generation | ComfyUI API | Local (HTTP+WebSocket) | Full workflow control |
| Image generation | `huggingface_hub` | `pip install huggingface_hub` | `InferenceClient` for quick results |
| Image generation | `runwayml` | `pip install runwayml` | For video assets |
| Style transfer | IP-Adapter (ComfyUI) | ComfyUI Manager | Screenshot as reference image |
| Background removal | `rembg` | `pip install "rembg[gpu]"` | Post-process assets |
| Upscaling | Real-ESRGAN | ComfyUI Manager | Upscale final outputs |

---

## APPENDIX: QUICK REFERENCE — KEY API ENDPOINTS

| Service | Endpoint | Auth | Notes |
|---------|----------|------|-------|
| ComfyUI submit | `POST http://VICTUS:8188/prompt` | None (LAN) | Send workflow JSON |
| ComfyUI status | `WS ws://VICTUS:8188/ws?clientId=UUID` | None | Real-time progress |
| ComfyUI result | `GET http://VICTUS:8188/history/{id}` | None | After completion |
| ComfyUI image | `GET http://VICTUS:8188/view?filename=X` | None | Retrieve output |
| Gemini | `POST https://generativelanguage.googleapis.com/v1beta/interactions` | `x-goog-api-key` | Vision + text |
| OpenAI | `POST https://api.openai.com/v1/chat/completions` | Bearer token | GPT-4o vision |
| HF Inference | `POST https://router.huggingface.co/v1` | Bearer token | Routes to providers |
| Runway | `POST https://api.runwayml.com/v1/image_to_video` | Bearer token | Gen4 Turbo |
| MiniMax | `POST https://api.minimax.io/v1/video_generation` | Bearer token | Hailuo-2.3 |
| Kling | `POST https://api.klingai.com/v1/videos/image2video` | Bearer token | |

---

*Research compiled June 2026. APIs and model versions subject to change — verify against official documentation before production deployment.*
