novoclassico = 1
vi = 0
vg = 0
e = 0
grenais = 0
while (novoclassico == 1):
    i, g = map(int, input().split())
    if i > g:
        vi +=1
    elif g > i:
        vg +=1
    elif g == i:
        e +=1
    grenais +=1
    novoclassico = int(input("Novo grenal (1-sim 2-nao)\n"))
print (f"{grenais} grenais")
print (f"Inter:{vi}")
print (f"Gremio:{vg}")
print (f"Empates:{e}")
if vi > vg:
    print("Inter venceu mais")
elif vg > vi:
    print("Gremio venceu mais")
else:
    print("Nao houve vencedor")
