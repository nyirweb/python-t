# Masodpercek atszamitasa evek honapok napok percek

def seconds(x):
    y = x//31104000
    mon = (x%31104000)//2592000
    d = (x%2592000)//86400
    h = (x%86400)//3600
    min = (x%3600)//60
    sec = (x%60)
    print("A megadott másodperc: \n",
          y,"Év",mon,"Hónap",
          d,"Nap",min,"Perc",sec,"Másodperc")

s = int(input("Add meg a másodperceket (egész számok)\n"))

seconds(s)