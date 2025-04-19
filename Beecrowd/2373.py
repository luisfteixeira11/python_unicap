bandejas = int(input())
quebrados = 0
for b in range (bandejas):
    l, c = map(int, input().split())
    if l > c:
        quebrados += c
print(quebrados)
