import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(2, GPIO.OUT)

GPIO.output(2,GPIO.HIGH)
time.sleep(10)

GPIO.cleanup()

