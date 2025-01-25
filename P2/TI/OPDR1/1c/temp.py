from machine import Pin, ADC
import time

led = Pin("LED", Pin.OUT)
temp_sensor = ADC(4) 

for _ in range(5):
    led(0)
    time.sleep(.1)
    led(1)
    time.sleep(.1)

def read_temperature():
    adc_value = temp_sensor.read_u16()
    voltage = adc_value * 3.3 / 65535
    temperature = 27 - (voltage - 0.706) / 0.001721
    return temperature

while True:
    data = input("\ninput: ")

    print("Received '" + data + "'.")
    if data == '0':
        print("Turning led off.")
        led(0)
    elif data == '1':
        print("Turning led on.")
        led(1)
    elif data == 'T':
        temperature = read_temperature()
        print(f"Temperature: {temperature} C")
    else:
        print("Unknown command.")