import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(24, GPIO.OUT)

duty_cycle = 0
pwm = GPIO.PWM(24, 1000)
pwm.start(duty_cycle)

try:
    while True:
        print("Введите коэффициент заполнения:")
        duty_cycle = float(input())
        print(f"Предполагаемое напряжение на выходе RC-цепи: {round(3.3*duty_cycle/100, 3)}В")
        pwm.start(duty_cycle)

finally:
    pwm.stop()
    GPIO.cleanup()karCyn-6tomnu-casjyr