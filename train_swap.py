n = int(input())
for i in range (n):
    length = int(input())
    car = input().split()
    ordn = []
    swaps = 0
    for j in range (length):
        ordn.append (int (car [j]))

    for j in range (length):
        for k in range (length-1):
            if ordn [k] > ordn [k+1]:
                temp = ordn [k]
                ordn[k] = ordn [k+1]
                ordn [k+1] = temp
                swaps +=1
    print (f"Optimal train swapping takes {swaps} swaps")
