def code(invoerstring):
    string = ""
    for i in invoerstring:
        if ord(i) < ord("x"):
            string += chr(ord(i) + 3)
        else:
            string += chr(ord(i)-(122-97-3))
        
    return string

print(code("RutteAlkmaarDen Helder"))
