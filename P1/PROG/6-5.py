while True:
    inp = input("Geef een string van 4 letters: ")
    if len(inp) != 4:
        print(f"{inp} heeft {len(inp)} letters")
    else:
        break
print(f"Inlezen van correcte string: {inp} is geslaagd")