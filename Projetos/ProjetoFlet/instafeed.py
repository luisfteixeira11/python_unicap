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
        border_radius=ft.border_radius.all(12),
        shadow=ft.BoxShadow(blur_radius=40, color=ft.colors.BLUE_GREY_700),
        content=ft.Column(
            spacing=0,
            controls=[
                ft.Container(
                    padding=ft.padding.symmetric(horizontal=16, vertical=12),
                    content=ft.Row(
                        [
                            ft.Container(
                                width=48,
                                height=48,
                                bgcolor=ft.colors.BLUE_300,
                                border_radius=24,
                                alignment=ft.alignment.center,
                                content=ft.Text(
                                    "L", 
                                    color=ft.colors.GREY_900, 
                                    size=28, 
                                    weight=ft.FontWeight.BOLD
                                ),
                            ),
                            ft.Column(
                                [
                                    ft.Text(
                                        "luisfteixeira11",
                                        color=ft.colors.BLACK,
                                        weight=ft.FontWeight.BOLD,
                                        size=18,
                                    ),
                                    ft.Text(
                                        "Desenvolvedor Python | Recife-PE",
                                        color=ft.colors.GREY_700,
                                        size=13,
                                    ),
                                ],
                                spacing=2,
                                alignment=ft.MainAxisAlignment.CENTER,
                            ),
                            ft.Container(expand=True),
                            ft.Icon(name=ft.icons.MORE_HORIZ, color=ft.colors.BLACK),
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                    ),
                ),
                ft.Container(
                    height=220,
                    bgcolor=ft.colors.BLUE_GREY_100,
                    alignment=ft.alignment.center,
                    content=ft.Text(
                        value="Print('HelloWorld')",
                        color=ft.colors.BLUE_GREY_400,
                        size=18,
                        italic=True,
                    ),
                ),
                ft.Container(
                    padding=ft.padding.all(16),
                    content=ft.Column(
                        controls=[
                            ft.Row(
                                [
                                    ft.IconButton(
                                        icon=ft.icons.FAVORITE_BORDER,
                                        selected_icon=ft.icons.FAVORITE,
                                        selected=False,
                                        on_click=clicked,
                                        icon_color=ft.colors.BLACK,
                                        selected_icon_color=ft.colors.RED,
                                        tooltip="Curtir",
                                    ),
                                    ft.Icon(
                                        name=ft.icons.CHAT_BUBBLE_OUTLINE,
                                        color=ft.colors.BLACK,
                                    ),
                                    ft.Icon(
                                        name=ft.icons.SEND,
                                        color=ft.colors.BLACK,
                                    ),
                                    ft.Container(expand=True),
                                    ft.IconButton(
                                        icon=ft.icons.BOOKMARK_BORDER,
                                        selected_icon=ft.icons.BOOKMARK_ROUNDED,
                                        selected=False,
                                        on_click=clicked,
                                        icon_color=ft.colors.BLACK,
                                        selected_icon_color=ft.colors.BLACK,
                                        tooltip="Salvar",
                                    ),
                                ],
                                alignment=ft.MainAxisAlignment.START,
                            ),
                            ft.Text(
                                spans=[
                                    ft.TextSpan(text='Curtido por ', style=ft.TextStyle(color=ft.colors.BLACK, size=16)),
                                    ft.TextSpan(text='pythonistas_', style=ft.TextStyle(color=ft.colors.BLACK, size=16, weight=ft.FontWeight.BOLD)),
                                    ft.TextSpan(text=' e ', style=ft.TextStyle(color=ft.colors.BLACK, size=16)),
                                    ft.TextSpan(text='149 outros', style=ft.TextStyle(color=ft.colors.BLACK, size=16, weight=ft.FontWeight.BOLD)),
                                ]
                            ),
                            ft.Text(
                                value='Compartilhando conhecimento e projetos open source!',
                                color=ft.colors.BLACK,
                                size=16,
                            ),
                            ft.Text(
                                value='há 1 hora',
                                color=ft.colors.GREY,
                                size=14,
                                offset=ft.Offset(0, -0.5),
                            ),
                            # Comentários fictícios
                            ft.Text(
                                spans=[
                                    ft.TextSpan(text='luisfteixeira11 ', style=ft.TextStyle(color=ft.colors.BLACK, size=16, weight=ft.FontWeight.BOLD)),
                                    ft.TextSpan(text='Check meu novo repositório no GitHub! 🚀', style=ft.TextStyle(color=ft.colors.BLACK, size=16)),
                                ]
                            ),
                            ft.Text(
                                spans=[
                                    ft.TextSpan(text='dev_amigo ', style=ft.TextStyle(color=ft.colors.BLACK, size=16, weight=ft.FontWeight.BOLD)),
                                    ft.TextSpan(text='Muito bom, parabéns pelo projeto!', style=ft.TextStyle(color=ft.colors.BLACK, size=16)),
                                ]
                            ),
                            ft.Text(
                                spans=[
                                    ft.TextSpan(text='python_brasil ', style=ft.TextStyle(color=ft.colors.BLACK, size=16, weight=ft.FontWeight.BOLD)),
                                    ft.TextSpan(text='Orgulho de ver devs de Recife mandando bem!', style=ft.TextStyle(color=ft.colors.BLACK, size=16)),
                                ]
                            ),
                            ft.Text(
                                value='ver todos os 128 comentários',
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