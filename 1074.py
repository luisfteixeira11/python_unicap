n = int(input())
for i in range (n):
    p = int (input())
    if p == 0:
        print ("NULL")
    if p%2 == 0:
        if p >0:
            print ("EVEN POSITIVE")
        elif p <0:
            print ("EVEN NEGATIVE")
    else:
        if p >0:
            print ("ODD POSITIVE")
        elif p <0:
            print ("ODD NEGATIVE")

