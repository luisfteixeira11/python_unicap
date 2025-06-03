def intersec (x, y, u, v, x1, y1, u1, v1):
    if x1>x:
        x = x1
    if y1<y:
        y = y1
    if u1<u:
        u = u1
    if v1>v:
        v = v1
    return x, y, u, v

contador = 1
while True:
    n = int(input())
    if n == 0:
        break
    

    x = -10000
    y = 10000
    u = 10000
    v = -10000
    
    for i in range(n):
        x1, y1, u1, v1 = map(int, input().split())
        x, y, u, v = intersec (x, y, u, v, x1, y1, u1, v1)
    print (f"Teste {contador}")
    contador +=1
    if x<u and y>v:
        print (f"{x} {y} {u} {v}")
    else:
        print("nenhum")
    
    print()
