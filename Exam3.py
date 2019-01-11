#Szia xyz! Te x éves vagy!

import datetime

aktualisDatum = datetime.datetime.now()
nev = str(input("Add meg a teljes neved! (pl: Rácz István)\n"))
szulValue = input("Születési dátumod '-' elválasztva! (pl: 1993-12-09)\n")

szulEv = int(szulValue.split("-")[0])
szulHo = int(szulValue.split("-")[1])
szulNap = int(szulValue.split("-")[2])

aktualisEv = aktualisDatum.year
aktualisHo = aktualisDatum.month
aktualisNap = aktualisDatum.day

evek = aktualisEv-szulEv
kNev1 = str(nev.split(" ")[0])
kNev2 = str(nev.split(" ")[1])
keresztNev = ""
if(kNev2 != ""):
    keresztNev = kNev1+" "+kNev2
else:
    keresztNev = kNev1

if(aktualisHo == szulHo):
    if(aktualisNap == szulNap):
        print("Kedves ",keresztNev,"!","Boldog Születésnapot! Ma:",evek,"Éves vagy!")

    elif(aktualisNap > szulNap):
        print("Kedves ",keresztNev,"!","Jelenleg",evek,"Éves Vagy")

    elif(aktualisNap < szulNap):
        print("Kedves ",keresztNev,"!","A hónap végére",evek,"Éves leszel")

elif(aktualisHo > szulHo):
    print("Kedves ",keresztNev,"!","Jelenleg: ",evek,"Éves vagy!")

elif(aktualisHo < szulHo):
    print("Kedves ",keresztNev,"!","Jelenleg: ",evek-1,"Éves vagy!")

else:
    print("Hiba történt kérlek futtatsd újra a programot!")