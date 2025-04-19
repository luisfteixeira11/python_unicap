x1 = float (input())
x2 = float (input())
x3 = float (input())
x4 = float (input())
x5 = float (input())
x6 = float (input())
soma = 0
p = 0
if x1 > 0:
    p+=1
    soma+=x1
if x2 > 0:
    p+=1
    soma+=x2
if x3 > 0:
    p+=1
    soma+=x3
if x4 > 0:
    p+=1
    soma+=x4
if x5 > 0:
    p+=1
    soma+=x5
if x6 > 0:
    p+=1
    soma+=x6
print (f"{p} valores positivos")
print (f"{soma/6}")
