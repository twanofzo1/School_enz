
def standaardprijs(afstandKM):          # creert een functie met 1 parameter (een herhaalbaar stuk code met een variabele)
    if afstandKM <= 0:                  # als de afstand kleiner is dan 0
        return 0                        # betaal je niks
    if afstandKM > 50:                  # als de afstand groter is dan 50
        return 15 + afstandKM * 0.60    # betaal je 15 euro + 60 cent per kilometer
    return afstandKM * 0.80             # anders betaal je 80 cent per kilometer

def ritprijs(leeftijd, weekendrit, afstandKM):  # creert een functie met 3 parameters
    prijs = standaardprijs(afstandKM)           # berekent de standaardprijs in de net beschreven functie
    if leeftijd < 12 or leeftijd >= 65:         # als de leeftijd kleiner is dan 12 of groter of gelijk aan 65
        if weekendrit:                          # als het een weekendrit is
            return prijs * 0.65                 # betaal je 65% van de prijs
        return prijs * 0.70                     # anders betaal je 70% van de prijs
    if weekendrit:                              # als het een weekendrit is
        return prijs * 0.60                     # betaal je 60% van de prijs
    return prijs                                # anders betaal je de volledige prijs

#nogmaals onderzoekend vermogen vind ik raar aangezien ik hier geen hulp of bron bij nodig had maar nogmaals hier is een python cursus https://www.youtube.com/watch?v=ix9cRaBkVe0

#Test:


def equals(a, b):
    if a == b:
        print("\u001b[32mTest succeeded\u001b[0m")
    else:
        print(f"\u001b[31mTest failed given:{a} != {b}\u001b[0m")


equals(ritprijs(leeftijd=11, weekendrit=True, afstandKM=60) , 33.15 )
equals(ritprijs(leeftijd=11, weekendrit=False, afstandKM=60), 35.7 ) # FLOATING POINT INPRECISION  AAAAAAAAAAAAAAAAAGGGGHHHHHHHH
equals(ritprijs(leeftijd=11, weekendrit=True, afstandKM=20) , 10.4 )
equals(ritprijs(leeftijd=11, weekendrit=False, afstandKM=20), 11.2 )

equals(ritprijs(leeftijd=20, weekendrit=True, afstandKM=60) , 30.6 ) # FLOATING POINT INPRECISION  AAAAAAAAAAAAAAAAAGGGGHHHHHHHH
equals(ritprijs(leeftijd=20, weekendrit=False, afstandKM=60), 51 )
equals(ritprijs(leeftijd=20, weekendrit=True, afstandKM=20) , 9.6 ) 
equals(ritprijs(leeftijd=20, weekendrit=False, afstandKM=20), 16 )




