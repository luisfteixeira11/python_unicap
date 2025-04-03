while True:
    try:
        entrada = int(input())
        resultado = (entrada*(entrada+1)//2)**2
        print(resultado)
    except EOFError:
        break
