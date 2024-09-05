def H3Opdr2():
    leeftijd = int(input("Geef je leeftijd: "))
    if type(leeftijd) != int:
        print("Voer een geldige leeftijd in")
        return
    paspoort = input("Heb je een Nederlands paspoort: ")
    if paspoort != "ja" and paspoort != "nee":
        print("Voer een geldig antwoord in")
        return
    if leeftijd >= 18 and paspoort == "ja":
        print("Gefeliciteerd, je mag stemmen!")
    else:
        print("Helaas, je mag niet stemmen")
    
H3Opdr2()