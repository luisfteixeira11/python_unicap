while True:
    nq = int (input ())
    if nq == 0:
        break
    for q in range (nq):
        a,b,c,d,e = list (map (int, input ().split ()))
        lista = [a, b, c, d, e]
        gab = []
        for i in range (len (lista)-1):
            if lista [0] <= 127:
                gab.append (lista[0])
        if len (gab) >1:
            print ("*")
        if len (gab) ==0:
            print ("*")
        else:
            gaba = str (gab [0])
            print (f"{gaba}")
