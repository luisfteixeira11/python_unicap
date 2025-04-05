linhas, ate = map (int, input().split())
for i in range (1, ate+1):
    if i%linhas == 0:
        print (f"{i}")
    else:
        print (i, end=" ")

