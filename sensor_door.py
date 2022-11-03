# Intended for use with a Raspberry Pi

import RPi.GPIO as R
from time import sleep

R.setmode(R.BOARD)
R.setup(12, R.IN) # 12 refers to the pin on the rapberry pi, occupied by the breakbeam sensor
R.setup(31, R.OUT) # 31 is the pin for the servomotor

door = R.PWM(31, 50) # Set pulse rate to 50 into the servomotor

door.start(0)

try:
    while 1:
        if R.input(12):
            door.ChangeDutyCycle(12.0)
            sleep(0.9)
            door.ChangeDutyCycle(0)
            sleep(10)
        else:
            door.ChangeDutyCycle(7.0)
            sleep(0.9)
            door.ChangeDutyCycle(0)
finally:
    door.stop
    R.cleanup()