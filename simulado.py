nome = str (input())
x = int (nome [0])
y = int (nome [1])
z = int (nome [2])
o = nome [3]
if o.lower() == "c":
    if x>=y:
        var=x
        x=y
        y=var
    if y>=z:
        var=y
        y=z
        z=var
if o.lower() == "d":
    if y<=z:
        var=y
        y=z
        z=var
    if x<=y:
        var=x
        x=y
        y=var
print (x, y, z)
