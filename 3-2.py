def H3Opdr2():
    leeftijd = int(input("Geef je leeftijd: "))
    paspoort = input("Heb je een Nederlands paspoort: ")
    if leeftijd >= 18 and paspoort == "ja":
        print("Gefeliciteerd, je mag stemmen!")
    else:
        print("Helaas, je mag niet stemmen")