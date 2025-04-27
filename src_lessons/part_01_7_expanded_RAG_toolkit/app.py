import gradio as gr

with gr.Blocks() as demo:
    textbox = gr.Textbox()

demo.launch()