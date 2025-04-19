x = 4963127
while x!=0:
    soma = 0
    x = int(input())
    if x==0:
        break
    if x%2!=0:
        x+=1
    for i in range(5):
        soma +=x
        x+=2
    print(soma)
