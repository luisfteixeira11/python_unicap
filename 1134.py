n = 0
gas = 0
alc = 0
die = 0
while (n!=4):
    n = int(input())
    while (n<=0 or n>4):
        n = int(input())
    if n ==1:
        alc +=1
    elif n == 2:
        gas +=1
    elif n == 3:
        die +=1
print ("MUITO OBRIGADO")
print (f"Alcool: {alc}")
print (f"Gasolina: {gas}")
print (f"Diesel: {die}")
