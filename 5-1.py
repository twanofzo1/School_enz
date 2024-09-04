def H5Opdr1():
    def gemiddelde():
        getallen = []
        zin = input("Voer een willekeurige zin in: ")
        for zin in zin.split(" "):
            getallen.append(len(zin))
        return sum(getallen) / len(getallen)