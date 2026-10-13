honap = int(input"Add meg a hónap számát")
if honap >= 1 and honap <= 12:
    if honap >= 3 and honap <= 5:
        print("Tavasz")
    elif honap >= 6 and honap <= 8:
        print("Nyár")
    elif honap >= 9 and honap <= 11:
        print("Ősz")
    else:
        print("Tél")
else:
    print(f"Hibás érték! {honap}")