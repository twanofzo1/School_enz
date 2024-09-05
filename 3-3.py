def H3Opdr3():
    maandnummer = int(input("Voer een maandnummer in (1-12): "))

    if maandnummer < 1 or maandnummer > 12:
        print("ongeldig")
    elif 3 <= maandnummer <= 5:
        print("lente")
    elif 6 <= maandnummer <= 8:
        print("zomer")
    elif 9 <= maandnummer <= 11:
        print("herfst")
    else:
        print("winter")

H3Opdr3()