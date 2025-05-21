v = [int(input()) for i in range (20)]
contador = 19
for i in range (10):
    temp = v[i]
    v[i] = v[contador]
    v[contador] = temp
    contador -=1
for i in range(20):
    print(f"N[{i}] = {v[i]}")