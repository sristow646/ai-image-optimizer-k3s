
import gradio as gr
import subprocess
import os
import uuid

INPUT_DIR = "/data/input"
OUTPUT_DIR = "/data/output"

os.makedirs(INPUT_DIR, exist_ok=True)
os.makedirs(OUTPUT_DIR, exist_ok=True)

def optimize_image(image):
    image_id = str(uuid.uuid4())
    input_path = f"{INPUT_DIR}/{image_id}.png"
    output_path = f"{OUTPUT_DIR}/{image_id}_out.png"
    
    image.save(input_path)
    
    # Combine GFPGAN + Real-ESRGAN pipeline
    subprocess.run(["python3", "inference_gfpgan_realesrgan.py", "--input", input_path, "--output", output_path])
    
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
