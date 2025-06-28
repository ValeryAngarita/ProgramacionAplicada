from machine import Pin, PWM, time_pulse_us
from time import sleep, sleep_us

trig = Pin(2, Pin.OUT)
echo = Pin(15, Pin.IN)
servo = PWM(Pin(13), freq=50)

def move_servo(angle):
    duty = int((angle / 180) * 102 + 26)
    servo.duty(duty)

def calculate_distance():
    trig.value(0)
    sleep_us(2)
    trig.value(1)
    sleep_us(10)
    trig.value(0)
    duration = time_pulse_us(echo, 1, 30000)
    if duration < 0:
        return 0
    distance = (duration * 0.0343) / 2
    if distance >= 400 or distance <= 3:
        return 0
    return distance

while True:
    for angle in range(0, 181, 2):
        move_servo(angle)
        sleep(0.03)
        dist = calculate_distance()
        print("{},{:.2f}".format(angle, dist))
    for angle in range(180, -1, -2):
        move_servo(angle)
        sleep(0.03)
        dist = calculate_distance()
        print("{},{:.2f}".format(angle, dist))
