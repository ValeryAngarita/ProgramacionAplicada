from machine import Pin
import time

ledR = 23
ledVe = 22
ledAz = 21
ledAm = 19
ledN = 16
ledB = 0
ledM = 2
ledVi = 15

leds = [Pin (i, Pin.OUT) for i in (ledR, ledVe, ledAz, ledAm, ledN, ledB, ledM, ledVi) ]

while True:
  for led in leds:
    led.value(1)
    time.sleep(0.4)