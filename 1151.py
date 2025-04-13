n = int(input())

def fib(n):
    if n <= 1:
        return n
    a = 0
    b = 1
    for i in range(2, n + 1):
        temp = a
        a = b
        b = temp + b
    return b

for i in range(n):
    if i == n - 1:
        print(fib(i), end="")
    else:
        print(fib(i), end=" ")
print()
