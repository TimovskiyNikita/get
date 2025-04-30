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
    num = 128
    GPIO.output(dac, dec2bin(num))
    time.sleep(0.0005)
    if GPIO.input(comp):
        num -= 128
    num += 64
    GPIO.output(dac, dec2bin(num))
    time.sleep(0.0005)
    if GPIO.input(comp):
        num -= 64
    num += 32
    GPIO.output(dac, dec2bin(num))
    time.sleep(0.0005)
    if GPIO.input(comp):
        num -= 32
    num += 16
    GPIO.output(dac, dec2bin(num))
    time.sleep(0.0005)
    if GPIO.input(comp):
        num -= 16
    num += 8
    GPIO.output(dac, dec2bin(num))
    time.sleep(0.0005)
    if GPIO.input(comp):
        num -= 8
    num += 4
    GPIO.output(dac, dec2bin(num))
    time.sleep(0.0005)
    if GPIO.input(comp):
        num -= 4
    num += 2
    GPIO.output(dac, dec2bin(num))
    time.sleep(0.0005)
    if GPIO.input(comp):
        num -= 2
    num += 1
    GPIO.output(dac, dec2bin(num))
    time.sleep(0.0005)
    if GPIO.input(comp):
        num -= 1
    return num


try:
    while True:
        num = adc()
        print(f"ADC value = {num} -> {3.3*num/256}")

finally:
    GPIO.output(dac, 0)
    GPIO.output(troyka, 0)
    GPIO.cleanup()