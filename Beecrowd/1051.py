x = float(input())
imp = 0
if x<=2000:
    print ("Isento")
elif x>2000:
    if x<3000:
        imp += (x-2000)*8/100
    elif x>3000 and x<=4500:
        imp += (1000)*8/100
        imp += (x-3000)*18/100
    elif x>4500:
        imp += (1000)*8/100
        imp += (1500)*18/100
        imp += (x-4500)*28/100
    print(f"R$ {imp:.2f}")
