lijst = ['a', 'b', 'c']

def wijzig(lst):
    global lijst
    lijst = ['d', 'e', 'f']
    
print(lijst)
wijzig(lijst)
print(lijst)

#Waarom kun je in de functie niet de opdracht lijst = ['d', 'e', 'f'] geven?
#kan je wel
#Werkt jouw functie ook met een string-parameter? Probeer dit! Waarom werkt het wel/niet?
#i guess dat je alles kan invullen
#Welke rol speelt (im)mutabiliteit in deze vraag?
#geen