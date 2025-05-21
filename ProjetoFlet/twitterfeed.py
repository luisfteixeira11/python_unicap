import flet as ft

def main(page: ft.Page):
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.bgcolor = ft.colors.BLACK

    avatar = ft.CircleAvatar(
        col=2,
        height=70,
        width=80,
    )
    user = ft.Text(
        spans=[
            ft.TextSpan(
                text="Elon Musk",
                style=ft.TextStyle(color=ft.colors.BLACK, weight=ft.FontWeight.BOLD),
            ),
            ft.TextSpan(
                text=" @elonmusk", style=ft.TextStyle(color=ft.colors.GREY)
            ),
        ],
        size=16,
    )
    description = ft.Text(
        value="Alexandre de Morais.",
        color=ft.colors.BLACK,
    )
    media = ft.Container(
        border_radius=ft.border_radius.all(20),
        border=ft.border.all(width=1, color=ft.colors.GREY_300),
        height=200,
        margin=ft.margin.symmetric(vertical=10),
        content=ft.Column(
            spacing=0,
            controls=[
                ft.Container(
                    height=100,
                    bgcolor=ft.colors.GREY_200, 
                ),
                ft.Container(
                    padding=ft.padding.all(20),
                    content=ft.Column(
                        spacing=0,
                        controls=[
                            user,
                            ft.Text(
                                value="alexandre de morais.",
                                max_lines=1,
                                overflow=ft.TextOverflow.ELLIPSIS,
                                color=ft.colors.BLACK,
                            ),
                        ],
                    ),
                ),
            ],
        ),
    )
    actions = ft.ResponsiveRow(
        controls=[
            ft.Icon(name=ft.icons.CHAT, col=1, color=ft.colors.BLACK),
            ft.Icon(name=ft.icons.SHARE, col=1, color=ft.colors.BLACK),
            ft.Icon(name=ft.icons.FAVORITE_BORDER, col=1, color=ft.colors.BLACK),
            ft.Icon(name=ft.icons.ANALYTICS, col=1, color=ft.colors.BLACK),
        ],
        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
    )

    layout = ft.Container(
        width=500,
        bgcolor=ft.colors.WHITE,
        border_radius=ft.border_radius.all(10),
        padding=ft.padding.all(20),
        shadow=ft.BoxShadow(color=ft.colors.LIGHT_BLUE_ACCENT, blur_radius=300),
        content=ft.ResponsiveRow(
            columns=12,
            controls=[
                avatar,
                ft.Column(
                    col=10,
                    controls=[
                        user,
                        description,
                        media,
                        actions,
                    ],
                ),
            ],
        ),
    )

    page.add(layout)

ft.app(target=main , view=ft.WEB_BROWSER)
