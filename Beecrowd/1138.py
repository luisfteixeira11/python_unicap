a = 3411431
b = 1244531
while (a!=0 and b!=0):
    contagem = [0]*10
    a, b = map(int, input().split())
    if a==0 and b == 0:
        break
    for i in range(a, b+1):
        for digito in str(i):
            contagem [int(digito)] +=1
            
    print(f"{contagem[0]} {contagem[1]} {contagem[2]} {contagem[3]} {contagem[4]} {contagem[5]} {contagem[6]} {contagem[7]} {contagem[8]} {contagem[9]}")
