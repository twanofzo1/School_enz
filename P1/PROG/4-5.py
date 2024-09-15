def kwadratenSom(grondGetallen):
    som = 0
    for num in grondGetallen:
        if num > 0:
            som += num**2
    return som

print(f"De kwadraten som van [4, 3, -5] is: {kwadratenSom([4, 3, -5])}")