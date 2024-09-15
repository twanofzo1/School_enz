import json

bestand = 'oefening_7_5_inloggers.json'

def isString(string):
    if type(string) != str or string == "":
        print("Dit is geen geldige input")
        exit()
    return string

while True:
    naam = isString(input("Wat is je achternaam? "))
    voorl = isString(input("Wat zijn je voorletters? "))
    gbdatum = isString(input("Wat is je geboortedatum? "))
    email = isString(input("Wat is je e-mail adres? "))

    data = {
        'naam': naam,
        'voorletters': voorl,
        'gebb_datum': gbdatum,
        'e-mail': email
    }

    personen = []
    personen.append(data)
    if input("wil je nog een persoon toevoegen? (ja/nee) ") == "nee":
        break

with open(bestand, 'w') as f:
    json.dump(personen, f)
    f.close()

    # Maak een dictionary van de gegevens van deze gebruiker. Zie ook het voorbeeldbestand onderaan de pagina.
    # wanneer de volgende persoon inlogt is onbekend, dus schrijf meteen naar file.


