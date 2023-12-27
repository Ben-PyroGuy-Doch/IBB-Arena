from time import sleep
import RPi.GPIO as GPIO
import logging

logging.basicConfig(filename='/var/log/arenaweb.log', encoding='utf-8', level=logging.DEBUG, format='%(asctime)s %(levelname)-2s %(message)s',  datefmt='%Y-%m-%d %H:%M:%S')
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT) #Flipper pin
GPIO.setup(13, GPIO.OUT) #Spinner pin
GPIO.setup(15, GPIO.OUT) #Pit pin

def flipper():
    GPIO.output(11, 1)
    logging.info('spinner triggered')
    sleep(1)
    GPIO.output(11, 0)

def spinner(state):
    if state == True:
        logging.info('spinner turned on')
        GPIO.output(13, 1)
    else:
        logging.info('spinner turned off')

        GPIO.output(13, 0)

def pit():
    logging.info('pit triggered')
    GPIO.output(15, 1)
    sleep(1)
    GPIO.output(15, 0)

def matchtimer():
    logging.info('match started')
    flipper()
    sleep(10)
    pit()
    sleep(10)
    spinner(True)
    sleep(10)
    spinner(False)
    logging.info('match ended')
