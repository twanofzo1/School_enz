def analyzer(lijst):
    if not type(lijst) == str:
        print("Ongelidige invoer")
        return
    lijst = lijst.split("-")
    for i in range(len(lijst)):
        lijst[i] = int(lijst[i])
    

    return (f"Gesorteerde list van ints: {lijst.sort()}", f"Groostste getal: {max(lijst)} , Kleinste getal: {min(lijst)}", f"Aantal getallen: {len(lijst)}", f"Som van de getallen: {sum(lijst)}", f"Gemiddelde: {sum(lijst)/len(lijst)}\n")

    
#print(str(analyzer("5-9-7-1-7-8-3-2-4-8-7-9")).replace("(","").replace(")","").replace(",","").replace("'",""))
for i in analyzer("5-9-7-1-7-8-3-2-4-8-7-9"):
    print(i)