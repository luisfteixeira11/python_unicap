a, b, c, d = map (int, input ().split())
if a==c and b==d:
    print ("O JOGO DUROU 24 HORA(S) E 0 MINUTO(S)")
else:
    h = c-a
    m = d-b
    if m <0:
        h-=1
        m+=60
    elif m>60:
        h+=1
        m-=60
    print (f"O JOGO DUROU {h} HORA(S) E {m} MINUTOS(S)")
