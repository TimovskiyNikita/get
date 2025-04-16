import RPi.GPIO as GPIO
import time
import keyboard

GPIO.setmode(GPIO.BCM)

dac = [8,11,7,1,0,5,12,6]
GPIO.setup(dac, GPIO.OUT)

def dec2bin(n):
    return [int(i) for i in bin(n)[2:].zfill(8)]

try:
    while True:
        print("Введите целое число от 0 до 255: ")
        try:
            n = input()
            if n.lower()=="q":
                break
        except ValueError:
            print("Вы ввели не числовое значение")
        else:
            if int(n)!=float(n):
                print("Вы ввели не целое число") 
            elif n<0:
                print("Вы ввели отрицательное число")
            elif n>255:
                print("Вы ввели число, превышающее возможности 8-разрядного ЦАП")
            else:
                V = dec2bin(int(n))
                print(f"Предполагаемое напряжение на выходе ЦАП: {round(3.3*n/256,3)}")
                GPIO.output(dac, V)
        
            
finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()