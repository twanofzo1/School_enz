def namen():
    namen = {}
    while True:
        naam = input('Volgende naam: ')
        if naam == '':
            break
        namen[naam] = namen.get(naam, 0) + 1
    return namen

namen_dict = namen()
for naam, count in namen_dict.items():
    print(f"{naam} komt {count} keer voor")