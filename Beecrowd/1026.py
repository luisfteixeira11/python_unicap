while(True):

    try:
        a, b = map(int, input().split())
        print(a^b) #ou exclusivo entre 1 e 0


    except EOFError:
        break