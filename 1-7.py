letters = ('A', 'C', 'B', 'B', 'C', 'A', 'C', 'C', 'B')
for letter in set(letters):
    print(f"{letter} komt {letters.count(letter)} keer voor")