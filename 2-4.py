import random                                                       # importeer de random module

def H2Opdr4():
    bedrag = int(input("Voer een bedrag in euro centen in: "))      # vraag om een bedrag in euro's

    prijs = random.randrange(10, 150)                               # random getal tussen 10 en 150
    if prijs > bedrag:                                              # als de prijs hoger is dan het bedrag
        print("Helaas, je hebt niet genoeg geld") 
        return bedrag                                               # stop de functie en return het bedrag
    
    orignalprijs = prijs                                            # onthoud de originele prijs

    munten = [50, 20, 10, 5, 2, 1]                                  # lijst met munten
    for munt in munten:                                             # gaat over elke munt heen
        aantal = prijs // munt                                      # floor division (aantal keer dat de munt in het bedrag past afgerond naar beneden)
        print(f"{aantal} x €{munt}")                                # print het aantal keer dat de munt in het bedrag past
        prijs = prijs % munt                                        # zet het bedrag naar de modulo (de overblijfsel in helen van de deling)
        if prijs == 0:                                              # als de prijs 0 is
            break                                                   # stop de loop 
    
    return bedrag - orignalprijs                                    # return het verschil tussen het bedrag en de prijs (overige geld)

bedrag = H2Opdr4()

print(f"\nJe hebt nog {bedrag} cent over")                          # print het overige geld