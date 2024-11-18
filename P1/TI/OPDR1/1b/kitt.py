from machine import Pin
import time

#1 + 2 + 0 + 8 + 0 + 32 + 0 + 128 = 171

led_pins = [
    Pin(0, Pin.OUT),
    Pin(1, Pin.OUT),
    Pin(2, Pin.OUT),
    Pin(3, Pin.OUT),
    Pin(4, Pin.OUT)
]


def leds(value, delay_time):
    for led_pin in led_pins:
        if value % 2 == 1:
            led_pin.on()
        else:
            led_pin.off()
        value = value // 2
    time.sleep(delay_time)


delay = 0.1
reverse = False
ledNr = 1
while True:
    if reverse == False:
        ledNr *=2
    else:
        ledNr *=0.5
    
    if ledNr == 1 or ledNr == 8:
        reverse = not reverse
    leds(ledNr, delay)


