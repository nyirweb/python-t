#Hanyast szeretnél programozásból?

jegy = int(input("Hanyast szeretnél programozásból?\n"))

if(jegy == 1):
    print("1 - Elégtelen - Azért ezt gondold át! Kettes hátha megvan!?")
elif(jegy == 2):
    print("2 - Elégséges - Biztosan csak elégésgest érdemelsz?")
elif(jegy == 3):
    print("3 - Közepes - Hátha még belehúzol és évvégén 4 lesz!")
elif(jegy == 4):
    print("4 - Jó - Ami jó az jó, de lehetne jeles is!")
elif(jegy == 5):
    print("5 - Jeles - Tehát úgy érzed kiváló munkát végeztél!?")
else:
    print("Helytelen számot adtál meg! Futtatsd újra a szoftvert és 1 és 5 között válassz!")