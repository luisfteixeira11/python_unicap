cod, qnt = map (int, input().split())
if cod == 1:
    pag = qnt * 4
elif cod == 2:
    pag = qnt * 4.5
elif cod == 3:
    pag = qnt * 5
elif cod == 4:
    pag = qnt * 2
elif cod == 5:
    pag = qnt * 1.5
print (f"Total: R$ {pag:.2f}")
