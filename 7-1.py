Dict = {'a': 1.0, 'b': 2.0, 'c': 9.0}

def hoogvliegers(dict_studenten_cijfers):
    hoogvliegers = {}
    for student , cijfer in dict_studenten_cijfers.items():
        if cijfer >= 9.0:
            hoogvliegers[student] = cijfer
    return hoogvliegers

print(hoogvliegers(Dict))