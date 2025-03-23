import gradio as gr
import subprocess
import os
import uuid
from PIL import Image

INPUT_DIR = "/data/input"
OUTPUT_DIR = "/data/output"

os.makedirs(INPUT_DIR, exist_ok=True)
os.makedirs(OUTPUT_DIR, exist_ok=True)

def optimize_image(image):
    image_id = str(uuid.uuid4())
    input_path = f"{INPUT_DIR}/{image_id}.png"
    output_path = f"{OUTPUT_DIR}/{image_id}_out.png"

    # Convert numpy.ndarray to PIL Image
    pil_image = Image.fromarray(image)
    pil_image.save(input_path)

    # Placeholder for AI pipeline
    subprocess.run(["echo", "Running inference on", input_path])

    # Simulate output for testing purposes
    pil_image.save(output_path)

    return output_path

with gr.Blocks() as demo:
    gr.Markdown("## 🖼️ AI Image Optimizer (Real-ESRGAN + GFPGAN)")
    with gr.Row():
        with gr.Column():
            input_image = gr.Image(label="Upload Image")
            submit_btn = gr.Button("Optimize Image")
        with gr.Column():
            output_image = gr.Image(label="Optimized Image")
            download_btn = gr.File(label="Download Optimized Image")

    submit_btn.click(fn=optimize_image, inputs=input_image, outputs=[output_image, download_btn])

demo.launch(server_name="0.0.0.0", server_port=7860)
