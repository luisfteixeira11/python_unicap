lista = []
indice = []
for i in range (100):
    x = int(input())
    lista.append(x)
    indice.append(i+1)

for i in range (len(lista)):
    for j in range (len(lista)-1):
        if lista [j] < lista [j+1]:
            t = lista [j]
            lista [j] = lista [j+1]
            lista [j+1] = t
            te = indice [j]
            indice [j] = indice [j+1]
            indice [j+1] = te
print (lista[0])
print (indice[0])
