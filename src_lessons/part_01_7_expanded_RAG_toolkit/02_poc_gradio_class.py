import logging as log
import os

import gradio as gr

logger = log.getLogger(__name__)
log.basicConfig(level=log.INFO)
log.getLogger("httpx").setLevel(log.WARNING)

class UI:
  def onTemperatureChanged(self, slider):
    log.info(f'onTemperatureChanged:{slider}')

  def launch(self):
    history = [
        {"role": "assistant", "content": "I am happy to provide you that report and plot."},
        {"role": "assistant", "content": "Abcde"}
    ]
    with gr.Blocks( fill_height=True, title="Gradio POC", analytics_enabled=True,) as ui:
      with gr.Tab("Documents"):
        gr.Chatbot(history, type="messages")
      with gr.Tab("Settings"):
        with gr.Row():
          with gr.Column(scale=1):
            gr.Label("temperature")
            gr.Label("Other setting")
          with gr.Column(scale=3):
            self.tempSlider= gr.Slider()
            self.tempSlider.input( fn=self.onTemperatureChanged, inputs= self.tempSlider)

      #
      ui.launch()


log.info("Info message")





if __name__ == "__main__":
  ui= UI()
  ui.launch()