from machine import ADC, PWM, Pin
from time import sleep

led = PWM(Pin(22))
led.freq(1000)

adc = ADC(Pin(28))


def led_brightness(value):
    """
        Zet de led intensiteit.
        Waarde tussen de 0 en 65535
    """

    led.duty_u16(65535-value)


while True:
    adc_value = adc.read_u16()
    led_brightness(adc_value)
    sleep(0.01)

