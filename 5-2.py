def H5Opdr2():
    def pretty_print(filepath):
        prettyText = []
        contents = open(filepath, "r")
        for line in contents:
            contents = line.split(",")
            prettyText.append(f"{contents[1]} heeft kaartnummer: {contents[0]}")
        contents.close()
        return prettyText