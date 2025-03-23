import gradio as gr
import subprocess
import os
import uuid
from PIL import Image
import numpy as np

INPUT_DIR = "/data/input"
OUTPUT_DIR = "/data/output"

os.makedirs(INPUT_DIR, exist_ok=True)
os.makedirs(OUTPUT_DIR, exist_ok=True)

def optimize_image(image: np.ndarray):
    image_id = str(uuid.uuid4())
    input_path = f"{INPUT_DIR}/{image_id}.png"
    output_path = f"{OUTPUT_DIR}/{image_id}_out.png"

    pil_image = Image.fromarray(image)
    pil_image.save(input_path)

    # Dummy inference placeholder (replace with real pipeline)
    subprocess.run(["echo", f"Processing {input_path} -> {output_path}"])

    pil_image.save(output_path)

    return output_path

demo = gr.Interface(
    fn=optimize_image,
    inputs=gr.Image(type="numpy", label="Upload Image"),
    outputs=gr.Image(label="Optimized Image"),
    live=False,
    title="🖼️ AI Image Optimizer (Gradio Only)"
)

demo.launch(server_name="0.0.0.0", server_port=7860)
