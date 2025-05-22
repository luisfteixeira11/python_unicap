import tkinter as tk
import datetime
import os
from tkinter import Label, Frame, Button

def tocar_som():
    caminho_som = 'alarm_clockwav-14477.mp3'
    if os.name == 'nt':
        os.system(f'start {caminho_som}')

def alarme():
    horarioalarme = f"{hora.get()}:{minuto.get()}:{segundo.get()}"
    horarioatual = datetime.datetime.now().strftime('%H:%M:%S')
    horario['text'] = f"Horário Atual: {horarioatual}\nAlarme definido: {horarioalarme}"
    if horarioalarme == horarioatual:
        tocar_som()
    else:
        janela.after(1000, alarme)

janela = tk.Tk()
janela.geometry("420x320")
janela.title("Alarme de Relógio")
janela.configure(bg="#f0f4f7")

Label(
    janela,
    text="Alarme de Relógio em Python",
    font="Helvetica 20 bold",
    bg="#f0f4f7",
    fg="#2d415a"
).pack(pady=15)

Label(
    janela,
    text="Defina o horário do alarme:",
    font="Helvetica 12",
    bg="#f0f4f7",
    fg="#2d415a"
).pack(pady=5)

frame = Frame(janela, bg="#f0f4f7")
frame.pack(pady=10)

def options(value, label):
    container = tk.Frame(frame, bg="#f0f4f7")
    container.pack(side=tk.LEFT, padx=5)
    tk.Label(container, text=label, font="Helvetica 11", bg="#f0f4f7", fg="#2d415a").pack()
    opt = tk.StringVar(janela)
    opcoes = [str(i).zfill(2) for i in range(value)]
    opt.set(opcoes[0])
    tk.OptionMenu(container, opt, *opcoes).pack()
    return opt

hora = options(24, "Hora")
minuto = options(60, "Minuto")
segundo = options(60, "Segundo")

Button(
    janela,
    text="Definir Alarme",
    font="Helvetica 12 bold",
    bg="#2d415a",
    fg="white",
    activebackground="#3e5c76",
    activeforeground="white",
    relief=tk.RAISED,
    bd=3,
    command=alarme
).pack(pady=25)

horario = Label(
    janela,
    font="Helvetica 13",
    text="Horário atual: --:--:--\nAlarme definido: --:--:--",
    bg="#f0f4f7",
    fg="#2d415a"
)
horario.pack(pady=10)

tk.mainloop()