from time import sleep

import machine
import neopixel

np = neopixel.NeoPixel(machine.Pin(21), 8)

i = 0
r = 255
g = 0
b = 0

while True:

    np[i] = (r, g, b)
    
    np.write()  

    i += 1
    if i == 8:
        for j in range(8):
            np[j] = (0,0,0)
        i = 0
        if b == 255:
            r = 255
            b = 0
        elif g == 255:
            b = 255
            g = 0
        else:
            g = 255
            r = 0
        sleep(1)
        np.write()
        
        

    sleep(1)