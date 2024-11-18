from machine import ADC, PWM, Pin
from time import sleep

led = Pin(22, Pin.OUT)
adc = ADC(Pin(28))

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
    adc_value = adc.read_u16()
    pulse(led,adc_value/65535 , adc_value/65535)
    sleep(0.01)
