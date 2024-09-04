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

bedrag = H2Opdr4()