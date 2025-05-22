while True:
    n = int(input())
    if n==0:
        break
    soma = 0
    for i in range(1, n+1):
        soma += i*i
        
    print(soma) ##pegando o quadrado e contando quantos quadrados de numero x numero possui de um ate n vai achar uma progressao dos quadrados de x
