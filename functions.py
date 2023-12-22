from time import sleep
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT) #Flipper pin
GPIO.setup(13, GPIO.OUT) #Spinner pin
GPIO.setup(15, GPIO.OUT) #Pit pin

def flipper():
    GPIO.output(11, 1)
    sleep(1)
    GPIO.output(11, 0)

def spinner(state):
    if state == True:
        GPIO.output(13, 1)
    else:
        GPIO.output(13, 0)

def pit():
    GPIO.output(15, 1)
    sleep(1)
    GPIO.output(15, 0)

def matchtimer():
    flipper()
    sleep(10)
    pit()
    sleep(10)
    spinner(True)
    sleep(10)
    spinner(False)
