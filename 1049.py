o = str (input())
e = str (input())
c = str (input())
if o == "vertebrado":
    if e == "mamifero":
        if c == "onivoro":
            print ("homem")
        elif c == "herbivoro":
            print ("vaca")
    elif e == "ave":
        if c == "onivoro":
            print ("pomba")
        elif c == "carnivoro":
            print ("aguia")
elif o == "invertebrado":
    if e == "inseto":
        if c == "hematofago":
            print ("pulga")
        elif c == "herbivoro":
            print ("lagarta")
    elif e == "anelideo":
        if c == "hematofago":
            print ("sanguessuga")
        elif c == "onivoro":
            print ("minhoca")


