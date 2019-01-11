#13-as szorzotabla elso 50 eleme


szorzando = int(13)

for i in range(1,51):
    szorzo = i
    eredmeny = szorzo*szorzando
    eredmenyKiir = str("")
    if(eredmeny%7 == 0):
        eredmenyKiir = (eredmeny, '*')
    else:
        eredmenyKiir = (eredmeny)

    print(eredmenyKiir)
