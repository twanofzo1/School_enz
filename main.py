def PROG1_NS_Functies():

    def standaardprijs(afstandKM):      # creert een functie met 1 parameter (een herhaalbaar stuk code met een variabele)
        if afstandKM < 0:               # als de afstand kleiner is dan 0
            return 0                    # betaal je niks
        if afstandKM > 50:              # als de afstand groter is dan 50
            return 15 + afstandKM * 0.60# betaal je 15 euro + 60 cent per kilometer
        return afstandKM * 0.80         # anders betaal je 80 cent per kilometer
    
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

