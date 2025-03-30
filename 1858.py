n = int(input())
x = input().split()
for i in range (n):
    x[i] = int(x[i])
menor = min(x)
res = x.index(menor) + 1
print (res)
