# tti_model.py

import argparse
import json
import requests
from PIL import Image
from io import BytesIO

# Load configuration from JSON
with open("config_tti.json") as f:
    config = json.load(f)

API_URL = "https://api.deepinfra.com/v1/inference"
HEADERS = {"Authorization": "Bearer <YOUR_API_KEY>"}  # Replace with actual key

def generate_image(prompt: str, output_path: str):
    payload = {
        "model": config["model"],
        "inputs": {
            "prompt": prompt,
            "guidance_scale": config["guidance_scale"],
            "num_inference_steps": config["num_inference_steps"]
        }
    }

    response = requests.post(API_URL, headers=HEADERS, json=payload)
    if response.status_code == 200:
        image = Image.open(BytesIO(response.content))
        image.save(output_path)
        print(f"Image saved to {output_path}")
    else:
        print(f"Error: {response.status_code} - {response.text}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate an image from a text prompt.")
    parser.add_argument("--prompt", type=str, required=True, help="Text prompt")
    parser.add_argument("--output", type=str, default="output.png", help="Output image filename")
    args = parser.parse_args()
    generate_image(args.prompt, args.output)
