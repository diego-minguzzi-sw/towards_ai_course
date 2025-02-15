import flet as ft
import time

def main(page: ft.Page):
    def onButtAddClicked( e):
        pass
        page.add( ft.Checkbox(label= newTaskTextField.value) )
        buttNew.disabled= False
        buttNew.update()
        newTaskTextField.value= ''
        newTaskTextField.focus()
        newTaskTextField.update()

    page.adaptive = True
    page.title = "Flet counter example"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    newTaskTextField= ft.TextField(hint_text='What needs to be done?', width=300)
    buttAdd = ft.ElevatedButton("Add", on_click=onButtAddClicked)
    buttNew = ft.ElevatedButton("New", disabled=True)
    buttOther = ft.ElevatedButton("Other", disabled=True)
    page.add( ft.Row(controls=[ buttNew, buttOther]) )
    page.add( ft.Row(controls=[ newTaskTextField, buttAdd]) )

    page.add( ft.Row(controls=[ ft.IconButton(ft.Icons.ADD),
                                ft.IconButton(ft.Icons.REMOVE),
                                ft.IconButton(ft.Icons.ADD_CIRCLE) ] ) )
    dropOptions= ft.Dropdown( width=100,
                              options=[
                                ft.dropdown.Option('Red'),
                                ft.dropdown.Option('Green'),
                                ft.dropdown.Option('Blue')
                              ],
                              value='Green' )
    page.add( dropOptions)

ft.app(main)
