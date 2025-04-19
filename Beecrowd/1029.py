def fib(n):
    global calls
    calls += 1
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)

n = int(input())
for i in range(n):
    calls = -1
    x = int(input())
    res = fib(x)
    print(f"fib({x}) = {calls} calls = {res}")
