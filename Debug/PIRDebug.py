import time
import RPi.GPIO as GPIO # RPI.GPIO is only accessible on Raspberry Pi

#GPIO pins from pinout.xyz
motionsensor = 4
alarm = 17
LED = 27

#setup of pins
GPIO.setmode(GPIO.BCM)
GPIO.setup(motionsensor, GPIO.IN)
GPIO.setup(alarm, GPIO.OUT)
GPIO.setup(LED, GPIO.OUT)


print ("PIR Module Test (CTRL+C to exit)")
time.sleep(3)
try:
    while True:
        if GPIO.input(motionsensor) == 1:
            print ("Motion detected")
            GPIO.output(alarm, GPIO.HIGH)
            GPIO.output(LED, GPIO.HIGH)
            time.sleep(1)
            GPIO.output(alarm, GPIO.LOW)
            time.sleep(3)
            GPIO.output(LED, GPIO.LOW)
        else:
            print ("No motion detected")
            time.sleep(1)
except KeyboardInterrupt:
    GPIO.cleanup()
