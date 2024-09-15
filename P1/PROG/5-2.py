def pretty_print(filepath):
    prettyText = []
    with open(filepath, "r") as file:
        for line in file:
            parts = line.strip().split(",")
            prettyText.append(f"{parts[1]} heeft kaartnummer: {parts[0]}")
    
    return "\n".join(prettyText)

print(pretty_print("kaartnummers.txt"))