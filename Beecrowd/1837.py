a, b = map(int, input().split())
if b<0:
    b = b+abs(2*b)
    r = a%b
    q = a//b
    q = q-(2*q)
else:
    q = a//b
    r = a%b
print (q, r)
