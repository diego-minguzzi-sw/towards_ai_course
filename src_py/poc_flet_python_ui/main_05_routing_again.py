import flet as ft

RootPath='/'
SettingsPath='/settings'

# Run using the following command:
# flet run  -w main_05_routing_again.py
def main(page: ft.Page):
    page.title = "Routes Example"

    robotButtonsHeight=50
    robotButtons= [
        ft.ElevatedButton("Start", icon=ft.Icons.NOT_STARTED, col={"md": 1}, height=robotButtonsHeight),
        ft.ElevatedButton("Stop", icon=ft.Icons.STOP_CIRCLE, col={"md": 1}, height=robotButtonsHeight),
        ft.ElevatedButton("Clear Errors", icon=ft.Icons.AUTO_FIX_HIGH, col={"md": 1}, height=robotButtonsHeight),
        ft.ElevatedButton("Zero torque", icon=ft.Icons.FORKLIFT, col={"md": 1}, height=robotButtonsHeight),
        ft.ElevatedButton("Servo torque", icon=ft.Icons.FORKLIFT, col={"md": 1}, height=robotButtonsHeight)
    ]

    images = ft.GridView(
        expand=1,
        runs_count=12,
        child_aspect_ratio=0.3,
        spacing=5,
        run_spacing=5,
        auto_scroll=True,
        horizontal=True,
        max_extent=100
    )

    images.controls= [
        ft.ElevatedButton("Acquire location", icon=ft.Icons.PLACE),
        ft.ElevatedButton("Acquire Marker", icon=ft.Icons.QR_CODE_SCANNER),
        ft.ElevatedButton("Pick", icon=ft.Icons.BACKPACK),
        ft.ElevatedButton("Place", icon=ft.Icons.NO_BACKPACK)  ]

    def route_change(route):
        page.views.clear()
        page.views.append(
            ft.View(
                RootPath,
                [
                    ft.AppBar(leading=ft.Icon(ft.Icons.MEDICAL_SERVICES),
                              title=ft.Text("Flet app"),
                              bgcolor=ft.Colors.PRIMARY_CONTAINER,
                              actions=[
                                ft.IconButton(ft.Icons.SETTINGS_REMOTE_OUTLINED,
                                              on_click=lambda _: page.go(SettingsPath))
                              ])
                ],
            )
        )
        if page.route == SettingsPath:
            page.views.append(
                ft.View(
                    SettingsPath,
                    [
                        ft.AppBar(leading=ft.Icon(ft.Icons.MEDICAL_SERVICES_OUTLINED),
                                  title=ft.Text("Settings"),
                                  bgcolor=ft.Colors.PRIMARY_CONTAINER,
                                  actions=[
                                    ft.IconButton(ft.Icons.HOME_OUTLINED,
                                                  on_click=lambda _: page.go(RootPath))
                                  ]),

                        ft.Container(
                            content=ft.ResponsiveRow( robotButtons,
                                          alignment=ft.MainAxisAlignment.SPACE_EVENLY,
                                          run_spacing={"xs": 10},
                                          columns=len(robotButtons)),
                            border_radius=10,
                            padding=10,
                            bgcolor=ft.Colors.SECONDARY_CONTAINER),
                        images
                    ],
                )
            )
        page.update()

    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)


ft.app(main, view=ft.AppView.WEB_BROWSER)