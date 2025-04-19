n = int (input ())
for i in range (n):
    a = str (input())
    if a [0] == a [2]:
        print (int (a[0])*int (a[2]))
    else:
        maius = a.upper()
        if a[1] == maius [1]:
            print (int (a[2]) - int (a[0]))
        else:
            print (int (a[2]) + int (a[0]))
