i = 0
j = 1
while (i<=2):
    for l in range (3):
        print(f"I={i} J={j}")
        j+=1
    j-=3
    i+=0.2
    j+=0.2
    if i == 0 or (i>0.9 and i<=1) or (i>1.9 and i<=2):
        i = round(i)
    else:
        i = round (i, 1)
    if (j>0.9 and j<=1) or (j>1.9 and j<=2) or (j>2.9 and j<=3) or (j>3.9 and j<=4) or (j>4.9 and j<=5):
        j = round(j)
    else:
        j = round (j, 1)
