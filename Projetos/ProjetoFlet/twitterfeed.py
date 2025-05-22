import flet as ft

def main(page: ft.Page):
    page.bgcolor = ft.colors.BLACK
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    user_info = ft.Column(
        [
            ft.Text(
                "Luis Teixeira",
                style=ft.TextStyle(color=ft.colors.WHITE, weight=ft.FontWeight.BOLD),
                size=18,
            ),
            ft.Text(
                "@luisfteixeira11",
                style=ft.TextStyle(color=ft.colors.GREY_400),
                size=14,
            ),
        ],
        spacing=2,
        alignment=ft.MainAxisAlignment.START,
    )

    post_text = ft.Text(
        value="vou me matar.",
        color=ft.colors.WHITE,
        size=16,
    )
    card = ft.Card(
        content=ft.Container(
            bgcolor=ft.colors.BLUE_GREY_900,
            border_radius=15,
            padding=20,
            width=420,
            content=ft.Column(
                [
                    ft.Row(
                        [user_info],
                        spacing=15,
                        alignment=ft.MainAxisAlignment.START,
                    ),
                    ft.Divider(height=15, color=ft.colors.GREY_800),
                    post_text,
                    ft.Divider(height=10, color=ft.colors.GREY_800),
                    ft.Row(
                        [
                            ft.Icon(name=ft.icons.CHAT, color=ft.colors.GREY_400),
                            ft.Icon(name=ft.icons.SHARE, color=ft.colors.GREY_400),
                            ft.Icon(name=ft.icons.FAVORITE_BORDER, color=ft.colors.GREY_400),
                            ft.Icon(name=ft.icons.ANALYTICS, color=ft.colors.GREY_400),
                        ],
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    ),
                ],
                spacing=10,
            ),
        )
    )

    page.add(card)

ft.app(target=main)