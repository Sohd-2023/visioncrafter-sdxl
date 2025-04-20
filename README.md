# VisionCrafter-SDXL 🚀🖼️

[![Python](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Model: SDXL](https://img.shields.io/badge/Model-SDXL-purple.svg)](https://deepinfra.com)
[![DeepInfra API](https://img.shields.io/badge/API-DeepInfra-blue)](https://deepinfra.com)

> This model generates stunning high-quality images from text prompts using the `stability-ai/sdxl` model via the DeepInfra API.
  This is a fully open-source, customizable, and lightweight model.

---

## ✨ Features

- 🧠 Powered by Stability AI’s SDXL for high-quality image synthesis
- 🌐 Uses DeepInfra API for fast inference without local heavy models
- 🧰 Configurable inference steps and guidance scale
- 💾 Save outputs as `.png` or `.jpg`
- 🪄 Simple CLI interface

---

## 🖥️ Demo

## Installation
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

