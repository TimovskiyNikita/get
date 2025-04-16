import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

dac = [8,11,7,1,0,5,12,6]
GPIO.setup(dac, GPIO.OUT)

def dec2bin(n):
    return [int(i) for i in bin(n)[2:].zfill(8)]

period = 10

try:
    while True:
        print("Введите период треугольного сигнала:")
        try:
            period = float(input())
        except ValueError:
            print("Не числовое значение")
        else:
            for i in range(0,255+1):
                GPIO.output(dac, dec2bin(i))
                time.sleep(period/512)
            for i in range(254, 0, -1):
                GPIO.output(dac, dec2bin(i))
                time.sleep(period/512)
        
finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()