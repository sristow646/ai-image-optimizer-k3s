import gradio as gr
import subprocess
import os
import uuid
from PIL import Image
import numpy as np
from diffusers import StableDiffusionPipeline
import torch

INPUT_DIR = "/data/input"
OUTPUT_DIR = "/data/output"

os.makedirs(INPUT_DIR, exist_ok=True)
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Load Stable Diffusion
pipe = StableDiffusionPipeline.from_pretrained("runwayml/stable-diffusion-v1-5")
pipe.to("cuda" if torch.cuda.is_available() else "cpu")

def optimize_image(image: np.ndarray):
    image_id = str(uuid.uuid4())
    input_path = f"{INPUT_DIR}/{image_id}.png"
    output_path = f"{OUTPUT_DIR}/{image_id}_out.png"

    pil_image = Image.fromarray(image)
    pil_image.save(input_path)

    subprocess.run(["echo", f"Optimizing {input_path} -> {output_path}"])

    pil_image.save(output_path)

    return output_path

def generate_image_from_text(prompt):
    image = pipe(prompt, num_inference_steps=30).images[0]
    image_id = str(uuid.uuid4())
    output_path = f"{OUTPUT_DIR}/{image_id}_generated.png"
    image.save(output_path)
    return output_path

with gr.Blocks() as demo:
    gr.Markdown("## 🖼️ AI Toolbox: Optimizer & Text-to-Image Generator")

    with gr.Tabs():
        with gr.TabItem("Image Optimizer"):
            with gr.Row():
                with gr.Column():
                    input_image = gr.Image(label="Upload Image")
                    submit_btn = gr.Button("Optimize Image")
                with gr.Column():
                    output_image = gr.Image(label="Optimized Image")
            submit_btn.click(fn=optimize_image, inputs=input_image, outputs=output_image)

        with gr.TabItem("Text-to-Image Generator"):
            with gr.Row():
                with gr.Column():
                    text_input = gr.Textbox(label="Enter your prompt")
                    generate_btn = gr.Button("Generate Image")
                with gr.Column():
                    generated_image = gr.Image(label="Generated Image")
            generate_btn.click(fn=generate_image_from_text, inputs=text_input, outputs=generated_image)

demo.queue().launch(server_name="0.0.0.0", server_port=7860)
