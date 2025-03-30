n = int(input())
lista = []
for i in range (n):
    n = int (input())
    lista.append(n)
out = len(lista)
inl = 0
for i in range (len(lista)):
    if lista [i] >=10 and lista[i] <= 20:
        out -=1
        inl +=1
print (f"{inl} in")
print (f"{out} out")
