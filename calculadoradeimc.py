import tkinter as tk
from tkinter import Frame, Label, Entry, Button
def calcula_IMC ():
    imc = float(peso.get())/float(altura.get())**2
    resultado ['text'] = f"O seu IMC é {imc}"

janela = tk.Tk()
janela.title("Calculadora de IMC")

frame = Frame(janela, padx=40, pady=40).grid(column=1, row=1)

Label (frame, text="Digite os valores pedidos abaixo", pady=20).grid(column=1, row=1, columnspan=2)


Label (frame, text="Qual o seu peso(kg)?").grid(column=1, row=2)
peso = Entry(frame) ##input
peso.grid(column=2, row=2)


Label (frame, text="Qual a sua altura(metros)?").grid(column=1, row=3)
altura = Entry(frame) ##input
altura.grid(column=2, row=3)


Button (frame, text="Calcular", command=calcula_IMC).grid(column=2, row=4) ##botao
resultado = Label (frame)
resultado.grid(column=1, row=5, columnspan=2) ##da o resultado


janela.mainloop()