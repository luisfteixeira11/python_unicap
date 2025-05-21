while True:
    x = int(input())
    if x == 0:
        break
    jogo = str(input())
    possivel = 0
    ganhavel = False
    for i in range(1, x-1):
        if 'X' not in jogo:
            if x%3==0 and x!=3:
                break
            else:
                ganhavel == True
                break
    if ganhavel == True:
        print ("S")
    else:
        print ("N")    