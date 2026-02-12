import time
import RPi.GPIO as GPIO # RPI.GPIO is only accessible on Raspberry Pi
import smtplib
from email.message import EmailMessage
import os
import datetime

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
        print(e)

while True:
    print ("Input username for Gmail")
    user = input()
    print ("Input Password (app password only)")
    password = input()
    try:
        smtp = smtplib.SMTP('smtp.gmail.com', 587)
        smtp.starttls()
        smtp.login(user, password)
        smtp.quit()
        print("Login Successful")
        break
    except:
        print("Email credentials incorrect")

#setup of pins
answer = False
GPIO.setmode(GPIO.BCM)
print("Supported Pins:\nGPI0 4, GPIO 17, GPI0 27, GPIO 22\nGPI0 23, GPIO 24, GPI0 25, GPIO 5\nGPI0 6, GPIO 12, GPI0 13, GPIO 26\nGPI0 16") #GPIO pins from pinout.xyz
while True:
    print("Input the PIR sensor's GPIO pin")
    motionsensor = int(input())
    for _ in range(20):
        time.sleep(1)
        GPIO.setup(motionsensor, GPIO.IN)
        if GPIO.input(motionsensor) == 1:
            print("PIR sensor working")
            answer = True
            break
    if answer == True:
        break
    else:
        print ("Please try again") 

while True:
    print("Input the alarms GPIO pin")
    alarm = int(input())
    GPIO.setup(alarm, GPIO.OUT)
    GPIO.output(alarm, GPIO.HIGH)

    answer = input("Is the alarm on? (y/n): ")
    if answer == "y":
        GPIO.output(alarm, GPIO.LOW)
        break
    else:
        GPIO.output(alarm, GPIO.LOW)

while True:
    print("Input the PIR LEDs GPIO pin")
    LED = int(input())
    GPIO.setup(LED, GPIO.OUT)
    GPIO.output(LED, GPIO.HIGH)

    answer = input("Is the LED on? (y/n): ")
    if answer == "y" or "yes":
        GPIO.output(LED, GPIO.LOW)
        break
    else:
        GPIO.output(LED, GPIO.LOW)

clear = lambda: os.system('clear')
print ("Sensor Starting Now")
time.sleep(3)
try:
    while True:
        for _ in range(100):
            if GPIO.input(motionsensor) == 1:
                print ("Motion detected")
                GPIO.output(alarm, GPIO.HIGH)
                GPIO.output(LED, GPIO.HIGH)
                time.sleep(2)
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
