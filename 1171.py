n = int(input())
def verfreq(lista, num):
    iguais = 0
    for elemento in lista:
        if elemento == num:
            iguais += 1
    return iguais

lista = []
for _ in range(n):
    lista.append(int(input()))
lista.sort()
processados = set()
for num in lista:
    if num not in processados:
        x = verfreq(lista, num)
        print(f"{num} aparece {x} vez(es)")
        processados.add(num)