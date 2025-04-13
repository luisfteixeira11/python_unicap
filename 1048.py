sal = float (input())
if sal >=0 and sal <=400:
    print (f"Novo salario: {sal+sal*15/100:.2f}")
    print (f"Reajuste ganho: {sal*15/100:.2f}")
    print ("Em percentual: 15%")
elif sal <=800:
    print (f"Novo salario: {sal+sal*12/100:.2f}")
    print (f"Reajuste ganho: {sal*12/100:.2f}")
    print ("Em percentual: 12%")
elif sal <=1200:
    print (f"Novo salario: {sal+sal*10/100:.2f}")
    print (f"Reajuste ganho: {sal*10/100:.2f}")
    print ("Em percentual: 10%")
elif sal <=2000:
    print (f"Novo salario: {sal+sal*7/100:.2f}")
    print (f"Reajuste ganho: {sal*7/100:.2f}")
    print ("Em percentual: 7%")
else:
    print (f"Novo salario: {sal+sal*4/100:.2f}")
    print (f"Reajuste ganho: {sal*4/100:.2f}")
    print ("Em percentual: 4%")

