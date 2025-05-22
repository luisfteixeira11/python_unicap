import tkinter as tk
from tkinter import Frame, Label, Entry, Button

def calcula_IMC():
    try:
        imc = float(peso.get()) / float(altura.get()) ** 2
        if imc < 18.5:
            status = "Abaixo do peso"
        elif imc < 25:
            status = "Peso normal"
        elif imc < 30:
            status = "Sobrepeso"
        else:
            status = "Obesidade"
        resultado['text'] = f"Seu IMC é {imc:.2f} ({status})"
    except Exception:
        resultado['text'] = "Preencha todos os campos corretamente!"

janela = tk.Tk()
janela.title("Calculadora de IMC")
janela.configure(bg="#ffffff")

frame = Frame(janela, padx=30, pady=30, bg="#ffffff", bd=2, relief=tk.RIDGE)
frame.pack(pady=30, padx=30)

Label(
    frame,
    text="Calculadora de IMC",
    font="Helvetica 18 bold",
    bg="#ffffff",
    fg="#2d415a"
).grid(column=0, row=0, columnspan=2, pady=(0, 20))

Label(
    frame,
    text="Peso (kg):",
    font="Helvetica 12",
    bg="#ffffff"
).grid(column=0, row=1, sticky="e", pady=5)
peso = Entry(frame, font="Helvetica 12", width=10, justify="center", bg="#f0f4f7")
peso.grid(column=1, row=1, pady=5)

Label(
    frame,
    text="Altura (m):",
    font="Helvetica 12",
    bg="#ffffff"
).grid(column=0, row=2, sticky="e", pady=5)
altura = Entry(frame, font="Helvetica 12", width=10, justify="center", bg="#f0f4f7")
altura.grid(column=1, row=2, pady=5)

Button(
    frame,
    text="Calcular IMC",
    font="Helvetica 12 bold",
    bg="#2d415a",
    fg="white",
    activebackground="#3e5c76",
    activeforeground="white",
    relief=tk.RAISED,
    bd=3,
    command=calcula_IMC
).grid(column=0, row=3, columnspan=2, pady=20)

resultado = Label(
    frame,
    font="Helvetica 13",
    text="",
    bg="#ffffff",
    fg="#2d415a"
)
resultado.grid(column=0, row=4, columnspan=2, pady=10)

janela.mainloop()