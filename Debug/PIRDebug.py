import time
import RPi.GPIO as GPIO # RPI.GPIO is only accessable on Rasberry PI

MotionSensor = 17
Alarm = 4

GPIO.setmode(GPIO.BCM)
GPIO.setup(MotionSensor, GPIO.IN)
GPIO.setup(Alarm, GPIO.OUT)


print ("PIR Module Test (CTRL+C to exit)")
time.sleep(3)
try:
    while True:
        if GPIO.input(MotionSensor) == 1:
            print ("Motion detected")
            GPIO.output(Alarm, GPIO.HIGH)
            time.sleep(1)
            GPIO.output(Alarm, GPIO.LOW)
            time.sleep(3)
        else:
            print ("No motion detected")
            time.sleep(1)
except KeyboardInterrupt:
    GPIO.cleanup()
