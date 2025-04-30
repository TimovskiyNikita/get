import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

dac = [8,11,7,1,0,5,12,6]
comp = 14
troyka = 13

GPIO.setup(dac, GPIO.OUT)
GPIO.setup(troyka, GPIO.OUT, initial = GPIO.HIGH)
GPIO.setup(comp, GPIO.IN)

def dec2bin(n):
    return [int(i) for i in bin(n)[2:].zfill(8)]

def adc():
    for i in range(0, 255+1):
        value = dec2bin(i)
        GPIO.output(dac, value)
        time.sleep(0.001)
        comp_value = GPIO.input(comp)
        if comp_value:
            return i
    return 256

try:
    while True:
        num = adc()
        print(f"ADC value = {num} -> {3.3*num/256}")

finally:
    GPIO.output(dac, 0)
    GPIO.output(troyka, 0)
    GPIO.cleanup()                                                                                            