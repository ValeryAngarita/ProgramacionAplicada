pinLed = 18
pinPulsador = 35

from machine import Pin
import time 

led = Pin(pinLed, Pin.OUT)
pulsador = Pin (pinPulsador, Pin.IN)

while True:
    logic_state = pulsador.value()
    if logic_state == True:
        led.value(1)
        logic_state = pulsador.value()
    else:
        led.value(0)
        logic_state = pulsador.value()