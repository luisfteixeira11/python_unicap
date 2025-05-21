n = float(input())
v = [n]
print (f"N[0] = {v[0]:.4f}")
for i in range(1, 100):
    n/=2
    v.append(n)
    print (f"N[{i}] = {v[i]:.4f}")