x = int(input())
y = int(input())
soma = 0
if x > y: #vai ta sempre crescente
    t = x
    x = y
    y = t
while (x<=y):
    if x%13 != 0:
        soma +=x
    x+=1
print (soma)
