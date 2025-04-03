x = 429084
y = 493814
while (x>0 and y>0):
    soma = 0
    x, y = map(int, input().split())
    if x <= 0 or y <= 0:
        break
    if x > y:
        while (x>=y):
            soma += y
            print (y, end= " ")
            y +=1
    elif x < y:
        while (x<=y):
            soma +=x
            print (x, end= " ")
            x +=1
    print (f"Sum={soma}")
