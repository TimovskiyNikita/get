import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

dac = [8,11,7,1,0,5,12,6]
number = [0,0,0,0,0,0,0,0]

GPIO.setup(dac, GPIO.OUT)
GPIO.output(dac, number)
time.sleep(15)

GPIO.output(dac, 0)
GPIO.cleanup()