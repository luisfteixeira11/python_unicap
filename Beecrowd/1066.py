x1 = int (input())
x2 = int (input())
x3 = int (input())
x4 = int (input())
x5 = int (input())

par = 0
impar = 0
pos = 0
neg = 0
lista = [x1,x2,x3,x4,x5]
for i in range (len(lista)):
    if lista [i]>0:
        pos+=1
    elif lista[i]<0:
        neg +=1
    if lista[i]%2 == 0:
        par+=1
    else:
        impar+=1
print (f"{par} valor(es) par(es)")
print (f"{impar} valor(es) impar(es)")
print (f"{pos} valor(es) positivo(s)")
print (f"{neg} valor(es) negativo(s)")
