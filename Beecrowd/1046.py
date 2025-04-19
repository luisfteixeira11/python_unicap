hi, hf = map (int, input().split())

if hi == hf:
    print ("O JOGO DUROU 24 HORA(S)")
elif hi < hf:
    print (f"O JOGO DUROU {hf-hi} HORA(S)")
else:
    hora = hf+24-hi
    print (f"O JOGO DUROU {hora} HORA(S)")
