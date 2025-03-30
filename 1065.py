x1 = int(input())
x2 = int(input())
x3 = int(input())
x4 = int(input())
x5 = int(input())
p = 0

if x1%2==0:
    p +=1
if x2%2==0:
    p +=1
if x3%2==0:
    p +=1
if x4%2==0:
    p +=1
if x5%2==0:
    p +=1
print(f"{p} valores pares")
