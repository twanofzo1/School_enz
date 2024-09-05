Dict = {'a': 1, 'b': 2, 'c': 9}

def hoogvliegers(dict_studenten_cijfers):
    hoogvliegers = {}
    for student in dict_studenten_cijfers:
        if dict_studenten_cijfers[student] >= 9.0:
            hoogvliegers[student] = dict_studenten_cijfers[student]
    return hoogvliegers

print(hoogvliegers(Dict))