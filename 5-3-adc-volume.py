import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

dac = [8,11,7,1,0,5,12,6]
leds = [2,3,4,17,27,22,10,9]
comp = 14
troyka = 13

GPIO.setup(dac, GPIO.OUT)
GPIO.setup(troyka, GPIO.OUT, initial = GPIO.HIGH)
GPIO.setup(comp, GPIO.IN)
GPIO.setup(leds, GPIO.OUT)

def dec2bin(n):
    return [int(i) for i in bin(n)[2:].zfill(8)]

def adc1():
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

def adc2():
    for i in range(0, 255+1):
        value = dec2bin(i)
        GPIO.output(dac, value)
        time.sleep(0.001)
        comp_value = GPIO.input(comp)
        if comp_value:
            return i
    return 256

def voltage_to_leds(num):
    values = ("1"*int(8*num/256)).zfill(8)
    GPIO.output(leds, list(map(int, values)))


try:
    while True:
        num = adc1()
        print(f"ADC value = {num} -> {3.3*num/256}")
        voltage_to_leds(num)

finally:
    GPIO.output(dac, 0)
    GPIO.output(troyka, 0)
    GPIO.cleanup()