x = int(input())
for i in range(x):
    n = int(input())
    count = 0
    fib0, fib1 = 0, 1
    fibn = 0
    while (count<n-1):
        count +=1
        fibn = fib0+fib1
        fib0 = fib1
        fib1 = fibn
    if n == 1:
        fibn = 1
    print (f"Fib({n}) = {fibn}")