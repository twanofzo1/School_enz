from machine import Pin # type: ignore
from time import sleep

led_pin = Pin(22, Pin.OUT)
button_pin_on = Pin(27, Pin.IN, pull=Pin.PULL_DOWN)
button_pin_off = Pin(26, Pin.IN, pull=Pin.PULL_DOWN)

while True:
    if button_pin_on.value():
        led_pin.value(1)
        sleep(0.2) # for consistency
    elif button_pin_off.value():
        led_pin.value(0)
        sleep(0.2) # for consistency





