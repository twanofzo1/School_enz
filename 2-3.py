uurloon = float(input("Wat verdien je per uur: "))

if type(uurloon) != float:
    print("Voer een geldig uurloon in")
    exit()

uren = float(input("\nHoeveel uur heb je gewerkt: "))

if type(uren) != float:
    print("Voer een geldig aantal uren in")
    exit()

print(f"{uren} uur werken levert: {uurloon * uren} op")