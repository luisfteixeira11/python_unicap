import tkinter as tk
import datetime
import time
import os
from tkinter import Label, Frame, Button

def tocar_som():
    caminho_som = 'alarm_clockwav-14477.mp3'
    if os.name == 'nt':
        os.system(f'start {caminho_som}')

def alarme():
    horarioalarme = f"{hora.get()}:{minuto.get()}:{segundo.get()}"
    horarioatual = datetime.datetime.now().strftime('%H:%M:%S')
    horario ['text'] = f"Horaio Atual: {horarioatual}\nAlarme definido: {horarioalarme}" 
        
    if horarioalarme == horarioatual:
        tocar_som()
    else:
        janela.after(1000, alarme)

janela = tk.Tk()
janela.geometry("400x250")
janela.title ("Alarme de Relogio")
Label (janela, text="Alarme de Relogio em Python", font="Helvetica 20 bold").pack(pady=10)
Label (janela, text="Definir Alarme").pack(pady=5)

Frame = tk.Frame(janela)
Frame.pack()

def options (value):
    opt = tk.StringVar(janela)
    opcoes = [str(i).zfill(2) for i in range(value)]
    opt.set (opcoes[0])
    tk.OptionMenu (Frame, opt, *opcoes).pack(side=tk.LEFT)
    return opt

hora = options(24)
minuto = options(60)
segundo = options(60)

Button (janela, text="Definir alarme", font=("Helvetica 10"), command=alarme).pack(pady=20)

horario = Label (janela, font="Helvetica 10", text="Horário atual: --:--:--\nAlarme definido: --:--:--")
horario.pack(pady=10)

tk.mainloop()