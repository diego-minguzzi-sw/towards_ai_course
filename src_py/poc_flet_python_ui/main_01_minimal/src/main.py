import flet as ft
import time

def main(page: ft.Page):
    text= ft.Text( value="Hello, Flet!", color="green")
    page.add( ft.Row( controls=[ft.Text( value="A", color="red"),
                                ft.Text( value="B", color="green"),
                                ft.Text( value="C", color="blue") ]))
    page.add( ft.Row( controls=[ft.Text( value="Your name:", color="blue"),
                                ft.TextField(label='Your name'),
                                ft.ElevatedButton(text='Say your name') ] ) )
    page.add(text)
    page.update()

    for i in range(10):
      text.value= f'Hello, flet! #{i}'
      time.sleep(1)
      page.update()

ft.app(main)
