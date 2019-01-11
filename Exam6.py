#7-es szorzotabla elso husz szama *-al jelölve a 3-al oszthatoak

szorzo = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,17,19,20,21]

szorzando = int(7)

for i in range(0,20):
    eredmeny = szorzo[i]*szorzando
    eredmenyKiir = str("")
    if(eredmeny%3 == 0):
        eredmenyKiir = (eredmeny, '*')
    else:
        eredmenyKiir = (eredmeny)

    print(eredmenyKiir)
