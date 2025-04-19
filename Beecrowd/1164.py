def somadivisores (n):
    soma = 0
    for i in range(1, n):
        if n%i==0:
            soma +=i
    return soma

n = int(input())
for i in range(n):
    x = int(input())
    if somadivisores(x) == x:
        print(f"{x} eh perfeito")
    else:
        print(f"{x} nao eh perfeito")
