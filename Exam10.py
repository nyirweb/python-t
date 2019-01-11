# Óra számolás 51 óra van hátra feladat

egyNap = int(24)

idoAktualis = int(14)
ebresztesigHatra = int(51)

print("--------------------------------------------------------------------")
# Óra számolás

egyNap = int(24)

e = int(ebresztesigHatra-idoAktualis)

maradekOra = int(0)
napok = int(0)

if(ebresztesigHatra >= 24):
    maradekOra = ebresztesigHatra
    while(maradekOra >= 24):
        napok += 1
        maradekOra = int(ebresztesigHatra)-(int(napok)*int(24))+int(idoAktualis)

print("Az ébresztés ideje: ",napok,"nap múlva",maradekOra,"Órakkor")


