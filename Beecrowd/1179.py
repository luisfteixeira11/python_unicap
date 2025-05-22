par = []
impar = []
contador = 0
iniciador = -5
key1 = True
key2 = True
for i in range(15):
    n = int(input())
    if n % 2 == 0:
        par.append(n)
    else:
        impar.append(n)
while True:
    contador += 5
    iniciador +=5
    contador1 = 0
    if not key1:
        break
    if contador >= len(impar):
        contador += len(impar) - contador
        key1 = False
    for i in range(iniciador ,contador):
        print(f"impar[{contador1}] = {impar[i]}")
        contador1 += 1
    contador1 = 0
    if not key2:
        break
    if contador >= len(par):
        contador = len(impar) - contador
        key2 = False
    for i in range(iniciador, contador):
        print(f"par[{contador1}] = {par[i]}")
        contador1 += 1
    if not key1 and not key2:
        break

