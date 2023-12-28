from time import sleep
import RPi.GPIO as GPIO
import logging

logging.basicConfig(filename='/var/log/arenaweb.log', encoding='utf-8', level=logging.DEBUG, format='%(asctime)s %(levelname)-2s %(message)s',  datefmt='%Y-%m-%d %H:%M:%S')
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT) #Flipper pin
GPIO.setup(13, GPIO.OUT) #Spinner pin
GPIO.setup(15, GPIO.OUT) #Pit pin
GPIO.setup(19, GPIO.OUT) #LED mid pin
GPIO.setup(21, GPIO.OUT) #LED start pin
GPIO.setup(23, GPIO.OUT) #LED end pin

def flipper():
    GPIO.output(11, 1)
    logging.info('flipper triggered')
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

def lightstart():
    GPIO.output(19, 1)
    logging.info('light start')
    sleep(1)
    GPIO.output(19, 0)

def lightmid():
    GPIO.output(21, 1)
    logging.info('light mid started')
    sleep(1)
    GPIO.output(21, 0)

def lightend():
    GPIO.output(23, 1)
    logging.info('light end started')
    sleep(1)
    GPIO.output(23, 0)

def matchtimer():
    logging.info('match started')
    lightstart()
    flipper()
    sleep(10)
    lightmid()
    pit()
    sleep(10)
    spinner(True)
    sleep(10)
    spinner(False)
    lightend()
    logging.info('match ended')
