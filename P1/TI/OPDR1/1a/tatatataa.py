from machine import Pin # type: ignore
from time import sleep

led_pin = Pin(22, Pin.OUT)


def pulse(pin, high_time, low_time):
    """
    Geef een puls op de pin:
    Maak de pin pin_nr hoog, wacht high_time,
    maak de pin laag, en wacht nog low_time
    """
    pin.value(1)
    sleep(high_time)
    pin.value(0)
    sleep(low_time)

    # implementeer deze functie


while True:
    pulse(led_pin, 0.2, 0.2)
    pulse(led_pin, 0.2, 0.2)
    pulse(led_pin, 0.2, 0.2)
    pulse(led_pin, 0.6, 0.2)

