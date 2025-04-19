def isPrime (n):
    for i in range(2, n):
        if n%i == 0:
            return False
    return True
n = int(input())
for i in range(n):
    x = int(input())
    if isPrime(x) == True:
        print(f"{x} eh primo")
    else:
        print(f"{x} nao eh primo")

