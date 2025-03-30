n = int (input())
def verfreq (lista, num):
    iguais = 0
    high = len (lista)-1
    low = 0
    while (low<=high):
        mid = (low+high)//2
        if lista [mid]==num:
            iguais+=1
            mid-=1
        if lista[mid] <num:
            low = mid+1
        else:
            high = mid-1
    return iguais
lista = []
for i in range (n):
    lista.append (int (input()))
lista.sort ()
for i in range (len (lista)):
    x=verfreq(lista, lista [i])
    if lista [i-1] != lista [i]:
        print (f"{lista[i]} aparece {x} vez(es)")