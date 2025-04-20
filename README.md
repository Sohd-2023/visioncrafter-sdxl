# VisionCrafter-SDXL 🚀🖼️

[![Python](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Model: SDXL](https://img.shields.io/badge/Model-SDXL-purple.svg)](https://deepinfra.com)
[![DeepInfra API](https://img.shields.io/badge/API-DeepInfra-blue)](https://deepinfra.com)

>This model generates stunning high-quality images from natural language prompts using the `stability-ai/sdxl` model via the DeepInfra API.
  This is a fully open-source, customizable, and lightweight model.

---

## ✨ Features

- 🧠 Powered by Stability AI’s SDXL for high-quality image synthesis
- 🌐 Uses DeepInfra API for fast inference without local heavy models
- 🧰 Configurable inference steps and guidance scale
- 💾 Save outputs as `.png` or `.jpg`
- 🪄 Simple CLI interface

---

## Installation

This model uses the `stability-ai/sdxl` model via the DeepInfra API to convert text prompts into high-quality images.

Install dependencies:

```bash
pip install -r requirements.txt
```

## Usage
```bash
python tti_model.py --prompt "a futuristic city skyline at sunset" --output output.png
```

## Configuration
Modify `config_tti.json` to adjust:
- Model version
- Guidance scale
- Number of inference steps


Edit config_tti.json to customize:

model: Model identifier on DeepInfra

guidance_scale: Higher = more faithful to prompt

num_inference_steps: More steps = higher quality (slower)

🔑 Notes
Replace <YOUR_API_KEY> in tti_model.py with your actual DeepInfra API key.


---
