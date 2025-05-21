vetor = []
for i in range (11):
    x = int(input())
    vetor.append(x)
    if vetor[i] <=0:
        vetor[i]=1
    print (f"X[{i}] = {vetor[i]}")
