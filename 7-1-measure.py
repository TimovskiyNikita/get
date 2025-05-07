import RPi.GPIO as GPIO
import time
import matplotlib.pyplot as plt

GPIO.setmode(GPIO.BCM)

dac = [8,11,7,1,0,5,12,6]
leds = [2, 3, 4, 17, 27, 22, 10, 9]
comp = 14
troyka = 13

GPIO.setup(dac, GPIO.OUT)
GPIO.setup(leds, GPIO.OUT)
GPIO.setup(troyka, GPIO.OUT)
GPIO.setup(comp, GPIO.IN)

voltage = 0

def dec2bin(n):
    return [int(i) for i in bin(n)[2:].zfill(8)]

def adc():
    t = 0.005
    num = 128
    GPIO.output(dac, dec2bin(num))
    time.sleep(t)
    if GPIO.input(comp):
        num -= 128
    num += 64
    GPIO.output(dac, dec2bin(num))
    time.sleep(t)
    if GPIO.input(comp):
        num -= 64
    num += 32
    GPIO.output(dac, dec2bin(num))
    time.sleep(t)
    if GPIO.input(comp):
        num -= 32
    num += 16
    GPIO.output(dac, dec2bin(num))
    time.sleep(t)
    if GPIO.input(comp):
        num -= 16
    num += 8
    GPIO.output(dac, dec2bin(num))
    time.sleep(t)
    if GPIO.input(comp):
        num -= 8
    num += 4
    GPIO.output(dac, dec2bin(num))
    time.sleep(t)
    if GPIO.input(comp):
        num -= 4
    num += 2
    GPIO.output(dac, dec2bin(num))
    time.sleep(t)
    if GPIO.input(comp):
        num -= 2
    num += 1
    GPIO.output(dac, dec2bin(num))
    time.sleep(t)
    if GPIO.input(comp):
        num -= 1
    return num

def voltage_to_leds(num):
    values = ("1"*int(8*num/256)).zfill(8)
    GPIO.output(leds, list(map(int, values)))

def visualization(values):
    plt.plot([i+1 for i in range(len(values))], values)
    plt.xlabel("N")
    plt.ylabel("V, в В")
    plt.grid(True)
    plt.show()

try:
    values = []
    time1 = time.time()

    GPIO.output(troyka, 1)
    while voltage<(192):
        voltage = adc()
        values.append(voltage)
        # voltage_to_leds(voltage)


    GPIO.output(troyka, 0)
    while voltage>(128):
        voltage = adc()
        values.append(voltage)
       # voltage_to_leds(voltage)

    time2 = time.time()
    time = time2-time1

    visualization(values)

    with open("data.txt", "w") as f:
        f.write("\n".join([str(value) for value in values]))

    with open("settings.txt", "w") as f:
        f.write(f"{time}, {round(time/len(values),3)}, {round((224/256)*3.3/256,3)}")
    print(f"время эксперимента: {time}, средняя частота дискретизации: {round(time/len(values),3)}, шаг квантования АЦП: {round((224/256)*3.3/256,3)}")

finally:
    GPIO.output(dac, 0)
    GPIO.output(leds, 0)
    GPIO.cleanup()