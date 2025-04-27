import logging as log
import os

import gradio as gr

logger = log.getLogger(__name__)
log.basicConfig(level=log.INFO)
log.getLogger("httpx").setLevel(log.WARNING)

log.info("Info message")

history = [
    {"role": "assistant", "content": "I am happy to provide you that report and plot."},
    {"role": "assistant", "content": "Abcde"}
]

def launch_ui():
    with gr.Blocks( fill_height=True, title="Gradio POC", analytics_enabled=True,) as page:
      with gr.Tab("Documents"):
        gr.Chatbot(history, type="messages")
      with gr.Tab("Settings"):
        with gr.Column():
          with gr.Row():
            gr.Label("temperature")
            gr.Slider()

          with gr.Row():
            gr.Label("Other setting")
      page.launch()


if __name__ == "__main__":
  launch_ui()