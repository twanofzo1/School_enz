def H5Opdr4():
    import datetime 
    import os
    vandaag = datetime.datetime.today() 
    s = vandaag.strftime("%a %d %b %Y") 
    t = vandaag.strftime("%H:%M:%S")

    if not os.path.exists("hardlopers.txt"):
        file = open("hardlopers.txt", "a")
    else:
        file = open("hardlopers.txt", "w")

    while True:
        Input = input("Voer naam in (stop met 'stop'): ")
        if Input == "stop":
            break


        file.write(f"{s}, {t}, {Input}\n")

    file.close()


H5Opdr4()