#Jövőérték számítása
# C=10.000 p=8% --> r= 0.08/

r = float(8/100)/12
m = 12
C = float(10000)

print("Kalkulátor\n 10.000 Forint névértékű betét jövőbeni értéke évi 8%-os kamatozással\n","Kamatok tőkésítése: Havonta\n",
      "Kamat (havonta): ", r,"\n")

t = float(input("A számításhoz add meg a megtakarítani szánt évek számát!\n"))

FV = float(C)*(1+r/m)**(m*t)


print("A betét várható értéke (Kamatadó és szocho. nélkül): \n","~",round(FV),"Forint")