diai = str (input())
horarioi = str (input())
diaf = str (input())
horariof = str (input())
hf = int(horariof[0:2])
hi = int(horarioi[0:2])

dias = int(diaf[4:6]) - int(diai[4:6])
if dias < 0:
    dias +=30
horas = hf - hi
if horas <0:
    dias -=1
    horas +=24
minutos = int(horariof[5:7]) - int(horarioi[5:7])
if minutos <0:
    horas -=1
    minutos +=60
segundos = int(horariof[10:12]) - int(horarioi[10:12])
if segundos <0:
    minutos -=1
    segundos+=60
if horas <0:
    dias -=1
    horas+=24
if minutos <0:
    horas-=1
    minutos +=60
print(f"{dias} dia(s)")
print(f"{horas} hora(s)")
print(f"{minutos} minuto(s)")
print(f"{segundos} segundo(s)")
