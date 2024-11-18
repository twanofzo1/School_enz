import os

filePath = "kluizen.txt"
aantalKluizen = 12

def beschikbare_kluizen():
    kluizen = []
    with open(filePath, "r") as f:
        for line in f:
            if ";" in line:
                kluizen.append(int(line.split(";")[0]))
    return kluizen

def aantal_kluizen_vrij() -> int:
    return aantalKluizen - len(beschikbare_kluizen())

def nieuwe_kluis() -> int:
    if aantal_kluizen_vrij() > 0:
        code = input("voer een code in zonder ';' : ")
        if ";" in code:
            return -1
        with open(filePath, "a") as f:
            kluisnummer = min(set(range(1, aantalKluizen + 1)) - set(beschikbare_kluizen()))
            f.write(f"{kluisnummer};{code}\n")
        return kluisnummer
    else:
        return -2

def kluis_openen() -> bool:
    kluisnummer = input("voer een kluisnummer in : ")
    code = input("voer een code in : ")

    with open(filePath, "r") as f:
        for line in f:
            stored_kluisnummer, stored_code = line.strip().split(";")
            if kluisnummer == stored_kluisnummer and code == stored_code:
                return True
    return False

def kluis_teruggeven() -> bool:
    kluisnummer = input("voer een kluisnummer in : ")
    code = input("voer een code in : ")

    lines = []
    with open(filePath, "r") as f:
        lines = f.readlines()

    with open(filePath, "w") as f:
        for line in lines:
            stored_kluisnummer, stored_code = line.strip().split(";")
            if not (kluisnummer == stored_kluisnummer and code == stored_code):
                f.write(line)
            else:
                return True
    return False

usrInput = input("""
1: Ik wil weten hoeveel kluizen nog vrij zijn. 
2: Ik wil een nieuwe kluis.
3: Ik wil even iets uit mijn kluis halen.
4: Ik geef mijn kluis terug.
""")

while True:
    try:
        usrInput = int(usrInput)
        if 1 <= usrInput <= 4:
            break
        else:
            print("Voer een getal tussen 1 en 4 in")
    except ValueError:
        print("Voer een geldig getal in")
    usrInput = input()

if not os.path.exists(filePath):
    with open(filePath, "w") as f:
        for i in range(aantalKluizen):  # Initialize with 12 empty lines
            f.write("\n")

if usrInput == 1:
    print(f"Er zijn nog {aantal_kluizen_vrij()} kluizen vrij")
elif usrInput == 2:
    result = nieuwe_kluis()
    if result == -1:
        print("Ongeldige code. Gebruik geen ';'.")
    elif result == -2:
        print("Geen kluizen beschikbaar.")
    else:
        print(f"Uw kluisnummer is: {result}")
elif usrInput == 3:
    if kluis_openen():
        print("Kluis geopend.")
    else:
        print("Onjuiste combinatie van kluisnummer en code.")
elif usrInput == 4:
    if kluis_teruggeven():
        print("Kluis teruggegeven.")
    else:
        print("Onjuiste combinatie van kluisnummer en code.")
else:
    print("Er is iets fout gegaan")