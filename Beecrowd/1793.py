lista =[]
n = 3456789
while n!=0:
    n = int(input())
    if n == 0:
        break
    tempo = list(map(int, input().split()))
    soma = 0
    for i in range(n):
        if tempo [i]+10 > tempo [i+1]:
            soma += tempo [i]+10 -tempo [i+1]
        soma +=10
    print (soma)
