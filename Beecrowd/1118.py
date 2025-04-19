n = 0
novocalculo = 1
while (novocalculo == 1):
    media = 0
    n = float(input())
    if n<0 or n>10:
        while n<0 or n>10:
            n = float(input("nota invalida\n"))
    media +=n
    n = float(input())
    if n<0 or n>10:
        while n<0 or n>10:
            n = float(input("nota invalida\n"))
    media +=n
    media /= 2
    print(f"media = {media:.2f}")
    novocalculo = int(input("novo calculo (1-sim 2-nao)\n"))
    while novocalculo <1 or novocalculo >2:
         novocalculo = int(input("novo calculo (1-sim 2-nao)\n"))

