def H5Opdr3():
    def getFileData(filepath):
        contents = open(filepath, "r")
        aantalLines = 0
        nummers = []
        for line in contents:
            line = line.split(",")
            aantalLines +=1
            nummers.append(line[0])
        contents.close()
        return f"Deze file telt {aantalLines} regels\nHet grootste kaartnummer is: {max(nummers)} en dat staat op regel {nummers.index(max(nummers)) + 1}"