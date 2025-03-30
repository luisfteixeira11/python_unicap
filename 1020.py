dade = int (input ())
meses = idade//30
dias = idade%365
anos = idade//365
if meses >= 12:
    meses = meses%12
if dias >= 30:
    dias = dias%30
    meses +=1
print (anos, "ano(s)")
print (meses, "mes(es)")
print (dias, "dia(s)"

