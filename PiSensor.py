import time
import RPi.GPIO as GPIO # RPI.GPIO is only accessible on Raspberry Pi
import smtplib
import os
import datetime

cleartime = 500

def sendemail(username, userpassword):
    send = smtplib.SMTP('smtp.gmail.com', 587)
    # start TLS for security
    send.starttls()
    # Authentication
    send.login(username, userpassword)
    # message to be sent
    message = "Motion detected at " + str(datetime.datetime.now())
    # sending the mail
    send.sendmail(username, username, message)
    # terminating the session
    send.quit()


print ("Input name")
user = input()
print ("input password")
password = input()

print("Supported Pins:\nGPI0 4, GPIO 17, GPI0 27, GPIO 22\nGPI0 23, GPIO 24, GPI0 25, GPIO 5\nGPI0 6, GPIO 12, GPI0 13, GPIO 26\nGPI0 16")
print("Input the PIR sensor's GPIO pin")
motionsensor = int(input())
print("Input the alarms GPIO pin")
alarm = int(input())
print("Input the PIR LEDs GPIO pin")
LED = int(input())

#GPIO pins from pinout.xyz

#setup of pins
GPIO.setmode(GPIO.BCM)
GPIO.setup(motionsensor, GPIO.IN)
GPIO.setup(alarm, GPIO.OUT)
GPIO.setup(LED, GPIO.OUT)

print ("Sensor Starting Now")
time.sleep(3)
try:
    while True:
        for _ in range(cleartime):
            if GPIO.input(motionsensor) == 1:
                print ("Motion detected")
                GPIO.output(alarm, GPIO.HIGH)
                GPIO.output(LED, GPIO.HIGH)
                time.sleep(1)
                GPIO.output(alarm, GPIO.LOW)
                sendemail(user, password)
                time.sleep(10)
                GPIO.output(LED, GPIO.LOW)
            else:
                print ("No motion detected")
                time.sleep(1)
        clear = lambda: os.system('clear')
        clear()
except KeyboardInterrupt:
    GPIO.cleanup()