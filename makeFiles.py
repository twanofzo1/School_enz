prim = 9
sec = 4

for i in range(1, sec-1):
    with open(f"{prim}-{i}.py", "w") as f:
        f.close()