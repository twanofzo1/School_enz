a = 6
b = 7
c = (a + b) / 2

voornaam = "Twan"
tussenvoegsel = ""
achternaam = "Roodenburg"
mijnnaam = voornaam + " " + tussenvoegsel + " " + achternaam

#----------------------------------------------------#
opdr1 = 6.75 > a < b
opdr2 = len(mijnnaam) == len(voornaam + " " + tussenvoegsel + " " + achternaam)
opdr3 = len(mijnnaam) == c * 5
opdr4 = tussenvoegsel in mijnnaam

print(f"6.75 > a < b: {opdr1}")
print(f"De lengte van mijnnaam is gelijk aan de lengte van voornaam + tussenvoegsel + achternaam: {opdr2}")
print(f"De lengte van mijnnaam is gelijk aan c * 5: {opdr3}")
print(f"Komt het tussenvoegsel voor in mijnnaam?: {opdr4}")
