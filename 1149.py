lista = list (map (int, input().split()))
a = lista [0]
soma=0
lista.remove (a)
for i in range (len (lista)):
    if lista [i] >0:
        n = lista [i]
for i in range (n):
    soma = soma+a+i
print (soma)
