

egeszszam = int(input("adj meg egy szamot"))
if egeszszam % 2 ==0:
        print("paros")
else:
        print("paratlan")




#dasdwasdwa sdwasdwa dwasd wasdwa sdw

kor = int(input("hany eves vagy"))
if kor == 18:
    print("bejelentkezhetsz")
else:
    print("fiatal vagy")

#AASDAASDADADSDADDDDDDDDDDDDDDDDDDASSSSSSSS


fizetendo = int(input("adja meg a fizetendo osszeget"))
if fizetendo > 20000:
      fizetendo = fizetendo*0.9
      print("kapsz kedvezmenyt ")
print(f"fizetendo: {fizetendo}")





kor = int(input("hany eves vagy"))
if kor >=0:
    if kor >=0 and kor <=2:
        print("kisgyermek")
    elif kor <= 12:
        print("gyermek")
    elif kor <= 17:
        print("tini")
    elif kor <= 64:
        print("felnott")
    elif kor >= 65:
        print("nyugdíjas")
else:
     print("nem lehets minuszba")



a = float(input("add meg az elso szamot"))
b = float(input("add meg a masodik szamot"))
c = float(input("add meg a harmadik szamot"))


if a>b and a>c:
     print(f"{a} a legnagyobb")
if b>a and b>c:
     print(f"{b} a legnagyobb")
else:
     print(f"{c} a legnagyobb")







felhasznalojo = "admin" 
jelszojo = "1234"

felhasznalo = str(input("add meg a felhasznal nevet"))
if felhasznalojo == felhasznalo:
     jelszo = str(input("add meg a jelszot"))
if jelszojo == jelszo:
     print(" sikeres bejelentkezes")
else:
     print("helytelen a jelszo")
            



suly = float(input("add meg a csomag sulyat"))    
celallomas = str(input("add meg a celallomast"))
if celallomas == "belfold":
        if suly <5:
          print("szallitasi dij 1500ft")
        else:
            print("szallitasi dij 2500ft")
elif celallomas == "kulfold":
     eu = str(input("a csomag eu-n belul kerul igen v nem"))
     if eu == "igen" and suly <5:
          print("szallitasi dij 5000ft")
     elif eu == " igen" and suly >5:
          print("a szallitasi dij 8000ft")
     elif eu == "nem" and suly <5:
          print("szallitasi dij 10000ft")
     elif eu == "nem" and suly >=5:
          print("a szallitasi dij 15000ft")
     else:
          print("belfoldi vagy kulfoldi kellett volna")
    


    #6767676767676767676767676767676767676767676767676767676676767676766767



szam = float(input("adj meg egy szamot"))
while szam != 0:
     print(f"{szam}\{szam*2}")
     szam = float(input("add meg a kovetkezo szamot"))



szam = int(input("adj egy szamot"))
while szam % 2 !=0:
     szam = int(input("adj egy paros szamot havercsipsz"))

import random
szam = random.randint(1,2)

fej = 1 
iras = 2

while szam != 1:
     print("iras")
     szam = random.randint(1,2)
print("fej")
     




     
     