numlist = []
while True:
    num = int(input("Geef een getal: "))

    if num == 0:
        break
    else:
        numlist.append(num)
    
print (f"Er zijn {len(numlist)} getallen ingevoerd, de som is: {sum(numlist)}")
