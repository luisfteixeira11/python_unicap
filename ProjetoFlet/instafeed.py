import flet as ft

def main(page: ft.Page):
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.bgcolor = ft.colors.BLACK 
    
    def clicked(e):
        e.control.selected = not e.control.selected
        e.control.update()
    
    layout = ft.Container(
        bgcolor=ft.colors.WHITE,
        width=500,
        #height=700,
        border_radius=ft.border_radius.all(10),
        shadow=ft.BoxShadow(blur_radius=50, color=ft.colors.TEAL),
        content=ft.Column(
            spacing=0,
            controls=[
                ft.ListTile(
                    title=ft.Text(value='NASA', color=ft.colors.BLACK, weight=ft.FontWeight.BOLD),
                    subtitle=ft.Text(value='A lua!', color=ft.colors.BLACK),
                    leading=ft.Image(
                        src='https://www.google.com/imgres?q=nasa%20foto&imgurl=https%3A%2F%2Flookaside.fbsbx.com%2Flookaside%2Fcrawler%2Fmedia%2F%3Fmedia_id%3D100069033495847&imgrefurl=https%3A%2F%2Fwww.facebook.com%2FNASAHistoryOffice%2F&docid=s1Sq4jgnfRpdiM&tbnid=8ieIBg4zHV1oTM&vet=12ahUKEwjW3qTqneiMAxWJKLkGHZ6FI0UQM3oFCIgBEAA..i&w=958&h=1004&hcb=2&ved=2ahUKEwjW3qTqneiMAxWJKLkGHZ6FI0UQM3oFCIgBEAA',
                        fit=ft.ImageFit.CONTAIN,
                    ),
                    trailing=ft.Icon(name=ft.icons.MORE_HORIZ, color=ft.colors.BLACK),
                ),
                ft.Image(
                    src='https://www.google.com/imgres?q=lua&imgurl=https%3A%2F%2Fwww.correiobraziliense.com.br%2Fcbradar%2Fwp-content%2Fuploads%2F2025%2F04%2Fmoon-pink_1744438274959.jpg&imgrefurl=https%3A%2F%2Fwww.correiobraziliense.com.br%2Fcbradar%2Fnao-se-assuste-ao-ver-uma-lua-rosa-no-ceu-neste-domingo-13%2F&docid=pX308lSO88_3zM&tbnid=woL6hQ4FusuNyM&vet=12ahUKEwjn0LXPnuiMAxXwK7kGHQAdJSkQM3oECBYQAA..i&w=1280&h=720&hcb=2&ved=2ahUKEwjn0LXPnuiMAxXwK7kGHQAdJSkQM3oECBYQAA',
                    fit=ft.ImageFit.CONTAIN,
                ),
                ft.Container(
                    padding=ft.padding.all(15),
                    content=ft.Column(
                        controls=[
                            ft.ResponsiveRow(
                                columns=12,
                                controls=[
                                    ft.IconButton(
                                        col=1,
                                        icon=ft.icons.FAVORITE_BORDER,
                                        selected_icon=ft.icons.FAVORITE,
                                        selected=False,
                                        on_click=clicked,
                                        icon_color=ft.colors.BLACK,
                                        selected_icon_color=ft.colors.RED,
                                        tooltip="Curtir",
                                    ),
                                    ft.Icon(
                                        col=1,
                                        name=ft.icons.CHAT_BUBBLE_OUTLINE,
                                        color=ft.colors.BLACK,
                                    ),
                                    ft.Icon(
                                        col=1,
                                        name=ft.icons.SEND,
                                        color=ft.colors.BLACK,
                                    ),
                                    ft.Container(col=8),
                                    ft.IconButton(
                                        col=1,
                                        icon=ft.icons.BOOKMARK_BORDER,
                                        selected_icon=ft.icons.BOOKMARK_ROUNDED,
                                        selected=False,
                                        on_click=clicked,
                                        icon_color=ft.colors.BLACK,
                                        selected_icon_color=ft.colors.BLACK,
                                        tooltip="Salvar",
                                    ),
                                ]
                            ),
                            ft.Text(
                                spans=[
                                    ft.TextSpan(text='Curtido por ', style=ft.TextStyle(color=ft.colors.BLACK, size=16)),
                                    ft.TextSpan(text='luisfteixeira_', style=ft.TextStyle(color=ft.colors.BLACK, size=16, weight=ft.FontWeight.BOLD)),
                                    ft.TextSpan(text=' e ', style=ft.TextStyle(color=ft.colors.BLACK, size=16)),
                                    ft.TextSpan(text='1969 outros', style=ft.TextStyle(color=ft.colors.BLACK, size=16, weight=ft.FontWeight.BOLD)),
                                ]
                            ),
                            ft.Text(
                                value='Um pequeno passo para o homem, um grande passo para a humanidade!',
                                color=ft.colors.BLACK,
                                size=16,
                            ),
                            ft.Text(
                                value='56 ANOS ATRÁS',
                                color=ft.colors.GREY,
                                size=14,
                                offset=ft.Offset(0, -0.5),
                            ),
                            ft.Text(
                                spans=[
                                    ft.TextSpan(text='Elon Musk ', style=ft.TextStyle(color=ft.colors.BLACK, size=16, weight=ft.FontWeight.BOLD)),
                                    ft.TextSpan(text='Agora bora para Marte! #SpaceX', style=ft.TextStyle(color=ft.colors.BLACK, size=16)),
                                ]
                            ),
                            ft.Text(
                                value='ver todos os 2.025 comentários',
                                color=ft.colors.GREY,
                                size=16,
                            ),
                            ft.TextField(
                                hint_text='Adicionar um comentário...',
                                hint_style=ft.TextStyle(color=ft.colors.GREY, size=16),
                                border=ft.InputBorder.UNDERLINE,
                                border_color=ft.colors.GREY,
                                border_width=1,
                                color=ft.colors.BLACK,
                            )
                        ]
                )
                )
            ]
        )
    )
    
    page.add(layout)
    
if __name__ == "__main__":
    ft.app(target=main)