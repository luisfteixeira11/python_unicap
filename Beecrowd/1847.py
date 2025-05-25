a, b, c = map(int, input().split())
difba = b-a
difcb = c-b
difnegba = a-b
difnegcb = b-c
if b==a:
    if c>b:
        print(":)")
    else:
        print(":(")
elif b>a:
    if b>=c:
        print(":(")
    elif difcb<difba:
        print(":(")
    else:
        print(":)")
elif b<a:
    if c>b:
        print(":)")
    elif difnegba>difnegcb:
        print(":)")
    else:
        print(":(")