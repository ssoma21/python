
attempt = 1 

jelszo = "okos2026"

elszo = str(input("adja meg a jelszavad "))

while elszo != jelszo and attempt<3 :
    print("hibas jelszo")
    elszo = str(input("adj egy masik jelszot"))
    attempt = attempt+1
if elszo == jelszo :
    print("koszi te bum")
else:
    print("tul sok probalkozas")
