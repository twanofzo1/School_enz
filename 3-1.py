def H3Opdr1():
    score = input("Geef je score: ")
    if type(score) != int:
        print("Voer een geldige score in")
        return
    if score > 15:
        print(f"Gefeliciteerd!\nMet een score van {score} ben je geslaagd!")
    else:
        print(f"Helaas,\nje bent niet geslaagd. Je score was: {score}")