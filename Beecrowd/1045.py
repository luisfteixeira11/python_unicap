a,b,c = map (float, input().split())
if a>=b+c:
    print ("NAO FORMA TRIANGULO")
elif a*a==(b*b+c*c):
    print ("TRIANGULO RETANGULO")
elif a*a>(b*b+c*c):
    print ("TRIANGULO OTUSANGULO")
    if a==b and b==c:
        print ("TRIANGULO EQUILÁTERO")
    elif a==b or b==c or a==c:
        print ("TRIANGULO ISOSCELES")
elif a*a<(b*b+c*c):
    print ("TRIANGULO ACUTANGULO")
    if a==b and b==c:
        print ("TRIANGULO EQUILÁTERO")
    elif a==b or b==c or a==c:
        print ("TRIANGULO ISOSCELES")

