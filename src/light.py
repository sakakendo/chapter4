import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(2, GPIO.out)

GPIO.output(25,GPIO.HIGH)
time.sleep(10)

GPIO.cleanup()

