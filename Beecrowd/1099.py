n = int(input())
for i in range (n):
    x, y = map (int, input().split())
    soma = 0
    if x>y:
        x-=1
    if x<y:
        x+=1
    while (x!=y):
        if x%2==1 and x<y:
            soma +=x
            x+=1
        elif x%2==1 and x>y:
            soma +=x
            x-=1
        elif x%2==0 and x<y:
            x+=1
        elif x%2==0 and x>y:
            x-=1

    print (soma)
