uurloon = float(input("Wat verdien je per uur: "))

if type(uurloon) != float or type(uurloon) != int:
    print("Voer een geldig uurloon in")
    exit()

uren = int(input("\nHoeveel uur heb je gewerkt: "))

if type(uren) != int or type(uren) != float:
    print("Voer een geldig aantal uren in")
    exit()

print(f"{uren} uur werken levert: {uurloon * uren} op")