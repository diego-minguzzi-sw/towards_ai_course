import flet as ft

# Run using the following command:
# flet run  -w main_04_routing.py
def main(page: ft.Page):
    textRoute= ft.Text(f"Initial route: {page.route}")
    page.add(textRoute)

    def route_change(e: ft.RouteChangeEvent):
        textRoute.value= f'New route: {e.route}'
        textRoute.update()

        buttSettings.disabled = True if e.route == '/settings' else False
        buttSettings.update()

        buttGoStore.disabled = True if e.route == '/store' else False
        buttGoStore.update()

    def onButtGoStore( e):
        pass
        page.route= '/store'
        page.update()

    def onButtGoSettings( e):
        pass
        page.route= '/settings'
        page.update()

    buttGoStore = ft.ElevatedButton("Go to store", on_click=onButtGoStore, width=100)
    buttSettings = ft.ElevatedButton("Settings", on_click=onButtGoSettings, width=100)

    page.add(buttSettings)
    page.add(buttGoStore)

    page.on_route_change = route_change

ft.app(main, view=ft.AppView.WEB_BROWSER)