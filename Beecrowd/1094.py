n = int(input())
t = 0
tc = 0
tr = 0 
ts = 0
for i in range (n):
    x = input().split()
    t += int (x[0])
    if x[1] == "C":
        tc +=int (x[0])
    elif x[1] == "R":
        tr +=int (x[0])
    elif x[1] == "S":
        ts +=int (x[0])

print(f"Total: {t} cobaias")
print(f"Total de coelhos: {tc}")
print(f"Total de ratos: {tr}")
print(f"Total de sapos: {ts}")
print(f"Percentual de coelhos: {tc/t*100:.2f} %")
print(f"Percentual de ratos: {tr/t*100:.2f} %")
print(f"Percentual de sapos: {ts/t*100:.2f} %")
