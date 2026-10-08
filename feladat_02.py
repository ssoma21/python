ev = int(input("adj egy evszamot oscipok."))
honap = int(input("adj egy honapot oscipok."))
nap = int(input("adj egy napot oscipok."))

if ev>2026:
    print("az ev hibas kirk")
if honap>12 :
    print("hiabas a honap")
if honap == 1 or honap == 3 or honap == 5 or honap == 7 or honap == 8 or honap == 10 or honap == 12 : 
        if nap>31:
            print ("a nap hibas")
        else:
             print ("koszonom!!!")
elif honap == 4 or honap == 6 or honap == 9 or honap == 11 : 
        if nap>30:
            print ("a nap hibas")
        else:
             print ("koszonom!!!")
elif honap == 2 :
    if nap>28 :
          print ("a nap hibas")
    else :
         print("koszi G")


    
    



