import time

try:
    import RPI.GPIO as GPIO # RPI.GPIO is only accessable on Rasberry PI
except:
    raise ("RPI GPIO does not exist as a library due to an issue")

try:
    GPIO.setmode(GPIO.BCM)
except:
    raise ("GPIO.setmode(GPIO.BCM) is unable to execute")

try:
    print ("PIR Module Test (CTRL+C to exit)")
    time.sleep(3)
    while True:
        if GPIO.input(PIR_PIN):
            print ("Motion detected")
            time.sleep(1)
        else:
            print ("No motion detected")
except:
    raise ("Error, program cannot accept PIR_PIN input")

