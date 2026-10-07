#kerj a felhasznalotol egy evszamot, dontsd el, hogy szoko ev e.
#csak pozitiv egesz szam legyen. legyen kissebb 2050nel

ev = int(input("adj egy evszamot oscipok"))
if ev<0 or ev>2050:
    print("ez az evszam nem jo bakancs")
elif ev%4 == 0:
    print("ez z ev szokoev")   

