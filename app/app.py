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

with gr.Blocks() as demo:
    gr.Markdown("## 🖼️ AI Image Optimizer (Gradio 3.x)")
    with gr.Row():
        with gr.Column():
            input_image = gr.Image(label="Upload Image")
            submit_btn = gr.Button("Optimize Image")
        with gr.Column():
            output_image = gr.Image(label="Optimized Image")

    submit_btn.click(fn=optimize_image, inputs=input_image, outputs=output_image)

demo.queue().launch(server_name="0.0.0.0", server_port=7860)
