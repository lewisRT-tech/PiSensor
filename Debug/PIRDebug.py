import time
import RPi.GPIO as GPIO # RPI.GPIO is only accessable on Rasberry PI

MotionSensor = 17

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.IN)


print ("PIR Module Test (CTRL+C to exit)")
time.sleep(3)
try:
    while True:
        if GPIO.input(MotionSensor) == 1:
            print ("Motion detected")
            time.sleep(1)
        else:
            print ("No motion detected")
            time.sleep(1)
except KeyboardInterrupt:
    GPIO.cleanup()
