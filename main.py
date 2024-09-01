def H1Opdr1():
    #1.1
    # 5 - 5 - int
    # 5.0 - 5.0 - float
    # 5 % 2 - 1 - int
    # 5 > 1 - True - bool
    # '5' - '5' - str
    # 5 * 2 - 10 - int
    return

#1.2
def H1Opdr2():
    opdr1 = len("Supercalifragilisticexpialidocious")

    opdr2 = "ice" in "Supercalifragilisticexpialidocious"

    opdr3 = len("Antidisestablishmentarianism") > len("Honorificabilitudinitatibus")

    componisten = ['Berlioz', 'Borodin', 'Brian', 'Bartok', 'Bellini', 'Buxtehude', 'Bernstein']
    opdr4 = min(componisten)

    opdr5 = max(componisten)

    print(f"Aantal letters in 'Supercalifragilisticexpialidocious': {opdr1}")
    print(f"Komt 'ice' voor in 'Supercalifragilisticexpialidocious'?: {opdr2}")
    print(f"Is 'Antidisestablishmentarianism' langer dan 'Honorificabilitudinitatibus'?: {opdr3}")
    print(f"Componist die alfabetisch het eerst komt: {opdr4}")
    print(f"Componist die alfabetisch het laatst komt: {opdr5}")

def H1Opdr3():
    a = 6
    b = 7
    c = (a + b) / 2

    voornaam = "Twan"
    tussenvoegsel = ""
    achternaam = "Roodenburg"
    mijnnaam = voornaam + " " + tussenvoegsel + " " + achternaam
    H1opdr4(a , b , c , voornaam , tussenvoegsel , achternaam , mijnnaam)

    


def H1opdr4(a , b , c , voornaam , tussenvoegsel , achternaam , mijnnaam):
    opdr1 = 6.75 > a < b
    opdr2 = len(mijnnaam) == len(voornaam + " " + tussenvoegsel + " " + achternaam)
    opdr3 = len(mijnnaam) == c * 5
    opdr4 = tussenvoegsel in mijnnaam

    print(f"6.75 > a < b: {opdr1}")
    print(f"De lengte van mijnnaam is gelijk aan de lengte van voornaam + tussenvoegsel + achternaam: {opdr2}")
    print(f"De lengte van mijnnaam is gelijk aan c * 5: {opdr3}")
    print(f"Komt het tussenvoegsel voor in mijnnaam?: {opdr4}")


def H1Opdr5():
    favorieten = ['artiest1']
    print(favorieten)
    favorieten.append('artiest2')
    print(favorieten)
    favorieten[1] = 'artiest3'
    print(favorieten)

def H1Opdr6():
    getallen = [3, 7, -2, 12]
    diff = max(getallen) - min(getallen)
    print(diff)


def H1Opdr7():
    letters = ('A', 'C', 'B', 'B', 'C', 'A', 'C', 'C', 'B')
    for letter in set(letters):
        print(f"{letter} komt {letters.count(letter)} keer voor")



def H2Opdr1():
    cijferPROJA = 7.5
    cijferPROG = 9.0
    cijferMOD = 6.0

    gemiddelde = (cijferPROJA + cijferPROG + cijferMOD) / 3
    beloning = gemiddelde * 30
    overzicht = f"Mijn cijfers (gemiddeld een {gemiddelde}) leveren een beloning van € {beloning} op!"
    print(overzicht)


def H2Opdr2():
    print (0 == (1 == 2))
    print ((2 + (3 == 4) + 5) == 7)
    print ((1 < -1) == (3 > 4))


def H2Opdr3():
    uurloon = float(input("Wat verdien je per uur: "))

    if type(uurloon) != float or type(uurloon) != int:
        print("Voer een geldig uurloon in")
        return
    
    uren = int(input("\nHoeveel uur heb je gewerkt: "))

    if type(uren) != int or type(uren) != float:
        print("Voer een geldig aantal uren in")
        return
    
    print(f"{uren} uur werken levert: {uurloon * uren} op")


import random
def H2Opdr4(): # 
    bedrag = input("Voer een bedrag in euro centen in: ")   # vraag om een bedrag in euro's
    if type(bedrag) != int:                                 # als het bedrag geen integer is
        print("Voer een geldig bedrag in") 
        return                                              # stop de functie

    prijs = random.randrange(10, 150)                       # random getal tussen 10 en het 150
    if prijs > bedrag:                                      # als de prijs hoger is dan het bedrag
        print("Helaas, je hebt niet genoeg geld") 
        return                                              # stop de functie
    
    munten = [50 , 20 ,10 , 5 , 2 , 1]                      # lijst met munten
    for munt in munten:                                     # gaat over elke munt heen
        aantal = prijs // munt                              # floor division (aantal keer dat de munt in het bedrag past afgerond naar beneden)
        print(f"{aantal} x €{munt}")                        # print het aantal keer dat de munt in het bedrag past
        prijs = prijs % munt                                # zet het bedrag naar de modulo (de overblijfsel in helen van de deling)
        if bedrag == 0:                                     # als het bedrag 0 is
            break                                           # stop de loop 
    
    return bedrag - prijs                                  # return het verschil tussen het bedrag en de prijs (overige geld)

    # Onderzoekend vermogen is raar aangezien veel leerlingen het niet uit zichzelf kunnen bedenken de wat ervarener studenten wel 
    # dus die moeten gaan acteren alsof ze het niet kunnen en moeten opzoeken op internet of aan de docent vragen
    # beetje raar als je het mij vraagt
    # maar goed heb hier een link naar een python cursus https://www.youtube.com/watch?v=ix9cRaBkVe0 van een betrouwbare bron


def H3Opdr1():
    score = input("Geef je score: ")
    if type(score) != int:
        print("Voer een geldige score in")
        return
    if score > 15:
        print(f"Gefeliciteerd!\nMet een score van "{score} " ben je geslaagd!")
    else:
        print(f"Helaas,\nje bent niet geslaagd. Je score was: {score}")

def H3Opdr2():
    leeftijd = int(input("Geef je leeftijd: "))
    paspoort = input("Heb je een Nederlands paspoort: ")
    if leeftijd >= 18 and paspoort == "ja":
        print("Gefeliciteerd, je mag stemmen!")
    else:
        print("Helaas, je mag niet stemmen")

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


def H3Opdr4():
    dagen = ["maandag", "dinsdag", "woensdag"]
    for dag in dagen:
        print(dag[:2])

def H3Opdr5(length):
    for i in range(0, length, 2):
        print(i)

def H3Opdr6():
    s = "Guido van Rossum heeft programmeertaal Python bedacht."
    for letter in s:
        if letter in "aeiou":
            print(letter)

def H4Opdr1():
    def som(getal1, getal2, getal3):
        return getal1 + getal2 + getal3
    
def H4Opdr2():
    def som(getallen):
        return sum(getallen)

def H4Opdr3():
    def lang_genoeg(lengte):
        if lengte >= 120:
            return "Je bent lang genoeg voor de attractie!"
        else:
            return "Sorry, je bent te klein!"

def H4Opdr4():
    def new_password(oldpassword, newpassword):
        if oldpassword != newpassword and len(newpassword) >= 6 and ("0123456789" in newpassword):
            return True
        else:
            return False

def H4Opdr5():
    def kwadraten_som(grondgetallen):
        kwadraten = []
        for getal in grondgetallen:
            if getal > 0:
                kwadraten.append(getal ** 2)
        return sum(kwadraten)


def PROG1_NS_Functies():
    def standaardprijs(afstandKM):
        if afstandKM < 0:
            return 0
        if afstandKM > 50:
            return 15 + afstandKM * 0.60
        return afstandKM * 0.80
    ritprijs(leeftijd, weekendrit, afstandKM)