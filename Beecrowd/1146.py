n = 38791237
while n!=0:
    n = int(input())
    if n == 0:
        break
    for i in range (1, n+1):
        if i ==n:
            print (i, end="\n")
        else:
            print(i, end=" ")
