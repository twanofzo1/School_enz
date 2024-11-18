from time import sleep

import machine
import neopixel

np = neopixel.NeoPixel(machine.Pin(21), 8)

i = 0
while True:
    np[i] = (255, 0, 0)
    
    np.write()  

    i += 1
    if i == 8:
        for j in range(8):
            np[j] = (0,0,0)
        i = 0
        sleep(1)
        

    sleep(1)