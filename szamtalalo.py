import random #akkor importaljuk a randomomt ha veletlen szamot generalunk

gondoltszam = random.randint(1, 100) 

print("gondoltam egy szamot talald ki")
tipp = int(input("add meg a tipped"))
attempt = 1


while tipp != gondoltszam and attempt<6 :
    if gondoltszam<tipp:
        print("ennel kissebb")
    else:
        print("ennel nagyobb")
    tipp = int(input("Adj egy uj tippet"))
    attempt = attempt + 1
if tipp == gondoltszam:
    print("nyertel")
else:
    print(f"A gondoltzam: {gondoltszam}")





#egeszitds ki a jatekot egy pontszammal ha 1 tol veget er akkkor lehessen uj jaktekot inditani es novelje a pont szamot (pl. a maradek tippjeinek a szamaval)



