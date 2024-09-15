opdr1 = len("Supercalifragilisticexpialidocious")

opdr2 = "ice" in "Supercalifragilisticexpialidocious"

opdr3 = len("Antidisestablishmentarianism") > len("Honorificabilitudinitatibus")

componisten = ['Berlioz', 'Borodin', 'Brian', 'Bartok', 'Bellini', 'Buxtehude', 'Bernstein']
opdr4 = min(componisten)

opdr5 = max(componisten)

print(f"Aantal letters in 'Supercalifragilisticexpialidocious': {opdr1}")
print(f"Komt 'ice' voor in 'Supercalifragilisticexpialidocious'?: {opdr2}")
print(f"Is 'Antidisestablishmentarianism' langer dan 'Honorificabilitudinitatibus'?: {opdr3}")
print(f"Componist die alfabetisch het eerst komt: {opdr4}")
print(f"Componist die alfabetisch het laatst komt: {opdr5}")