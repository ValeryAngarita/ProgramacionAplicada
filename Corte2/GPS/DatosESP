from machine import UART
import time

gps = UART(2, baudrate=9600, tx=17, rx=16)

while True:
    if gps.any():
        try:
            line = gps.readline()
            print(line)
        except:
            pass
    time.sleep(0.1)
