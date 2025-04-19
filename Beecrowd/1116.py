n = int(input())
for i in range(n):
    x, y = map(int, input().split())
    if y == 0:
        print ("divisao impossivel")
    elif y<0 and x>0:
        x = x-(2*x)
        y = y+abs(2*y)
        q = x/y
        print(q)
    else:
        q=x/y
        print(q)
