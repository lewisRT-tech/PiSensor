import time
import RPi.GPIO as GPIO # RPI.GPIO is only accessible on Raspberry Pi
import smtplib
import os
import datetime
from email.message import EmailMessage

cleartime = 500

def sendemail(username, userpassword):

    msg = EmailMessage()
    msg.set_content(f"Motion detected at {datetime.datetime.now()}")
    msg["Subject"] = "Motion Alert"
    msg["From"] = username
    msg["To"] = username

    try:
        smtp = smtplib.SMTP('smtp.gmail.com', 587)
        smtp.starttls()
        smtp.login(username, userpassword)

        print("Sending email...")
        smtp.send_message(msg)

        smtp.quit()
        print("Email sent successfully")

    except Exception as e:
        print("Email failed:")
        print(e)

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
