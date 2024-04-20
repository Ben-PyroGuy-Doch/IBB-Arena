from time import sleep      # get a time source 
import RPi.GPIO as GPIO     # import GPIO
import sys                  # import sys 
import logging              # import loggng for output logging 

logging.basicConfig(filename='/var/log/arenaapi.log', encoding='utf-8', level=logging.DEBUG, format='%(asctime)s %(levelname)-2s %(message)s',  datefmt='%Y-%m-%d %H:%M:%S')
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)    # Flipper pin
GPIO.setup(13, GPIO.OUT)    # Spinner 1C pin
GPIO.setup(16, GPIO.OUT)    # Spinner 1A pin added pns for relays 
GPIO.setup(18, GPIO.OUT)    # Spinner 2C pin added pns for relays 
GPIO.setup(22, GPIO.OUT)    # Spinner 2A pin added pns for relays 
GPIO.setup(24, GPIO.OUT)    # Spinner 3C pin added pns for relays
GPIO.setup(26, GPIO.OUT)    # Spinner 3A pin added pns for relays
GPIO.setup(15, GPIO.OUT)    # Pit pin # now a PWM for the Servo 
p = GPIO.PWM(15, 50)        # Sets up pin 15 at PWM pin 
p.start(0)                  # Starts running PWM on the pin and sets it to 0
GPIO.setup(19, GPIO.OUT)    # LED mid pin
GPIO.setup(21, GPIO.OUT)    # LED start pin
GPIO.setup(23, GPIO.OUT)    # LED end pin


active_flag = 'active_flag.txt' # File where weapon active flag is stored, 1=weapons active 0=weapons inactive, this is also used to break the match loop

def flipper():
    flagcheck()
    GPIO.output(11, 1)
    logging.info('flipper triggered')
    sleep(1)
    GPIO.output(11, 0)

def spinner1c():  
    flagcheck()
    logging.info('Spinner 1 clockwise')
    GPIO.output(16, 0)
    sleep(1)
    GPIO.output(13, 1)

def spinner1a():  
    flagcheck()
    logging.info('Spinner 1 anti-clockwise')
    GPIO.output(13, 0)
    sleep(1)
    GPIO.output(16, 1)

def spinner1off(): 
    flagcheck()
    logging.info('Spinner 1 off')
    GPIO.output(13, 0)
    GPIO.output(16, 0)

def spinner2c(): 
    flagcheck()
    logging.info('Spinner 2 clockwise')
    GPIO.output(22, 0)
    sleep(1)
    GPIO.output(18, 1)

def spinner2a(): 
    flagcheck()
    logging.info('Spinner 2 anti-clockwise')
    GPIO.output(18, 0)
    sleep(1)
    GPIO.output(22, 1)

def spinner2off():  
    flagcheck()
    logging.info('Spinner 2 off')
    GPIO.output(18, 0)
    GPIO.output(22, 0)

def spinner3c(state): 
    flagcheck()
    logging.info('Spinner 3 clockwise')
    GPIO.output(26, 0)
    sleep(1)
    GPIO.output(24, 1)

def spinner3a(state): 
    flagcheck()
    logging.info('Spinner 3 anti-clockwise')
    GPIO.output(24, 0)
    sleep(1)
    GPIO.output(26, 1)

def spinner3off(state):  
    flagcheck()
    logging.info('Spinner 3 off')
    GPIO.output(24, 0)
    GPIO.output(26, 0)

def pitdown():
    flagcheck()
    logging.info('pit down')
    p.ChangeDutyCycle(3)

def pitup():
    flagcheck()
    logging.info('pit up')
    p.ChangeDutyCycle(12)

def lightstart():
    flagcheck()
    GPIO.output(19, 1)
    logging.info('light start')
    GPIO.output(19, 0)

def lightmid():
    flagcheck()
    GPIO.output(21, 1)
    logging.info('light mid started')
    GPIO.output(21, 0)

def lightend():
    flagcheck()
    GPIO.output(23, 1)
    logging.info('light end started')
    GPIO.output(23, 0)

def stopmatch():
    with open(active_flag, 'w') as file:
    # Write '0' to the file
        file.write('0')

def flagcheck():
    with open(active_flag, 'r') as file:
        # Read the content of the file
        content = file.read()

        # Check if the content is '0' or '1'
        if content == '0':
            logging.info("match end flag is set ending loop")
            sys.exit()
        elif content == '1':
            return
        

def matchtimer120():
    logging.info('match started')
    with open(active_flag, 'w') as file:
        file.write('1')
    lightstart()
    sleep(30) #timer till pit opens and spinner turns on
    #middle of match, weapons activate
    lightmid()
    spinner1c(True)
    spinner2c(True)
    spinner3c(True)
    pitdown()
    sleep(90) #timer till the end of the match
    #end of the match
    lightend()
    spinner1c(False)
    spinner1a(False)
    spinner2c(False)
    spinner2a(False)
    spinner3c(False)
    spinner3a(False)
    stopmatch()
    logging.info('match ended')

def matchtimer180():
    logging.info('match started')
    with open(active_flag, 'w') as file:
        file.write('1')
    lightstart()
    sleep(60) #timer till pit opens and spinner turns on
    #middle of match, weapons activate
    lightmid()
    spinner1c(True)
    spinner2c(True)
    spinner3c(True)
    pitdown()
    sleep(120) #timer till the end of the match
    #end of the match
    lightend()
    spinner1c(False)
    spinner1a(False)
    spinner2c(False)
    spinner2a(False)
    spinner3c(False)
    spinner3a(False)
    stopmatch()
    logging.info('match ended')

def matchtimerDuck():
    logging.info('match started')
    with open(active_flag, 'w') as file:
        file.write('1')
    lightstart()
    sleep(15) #timer till pit opens and spinner turns on
    #middle of match, weapons activate
    lightmid()
    spinner1c(True)
    spinner2c(True)
    spinner3c(True)
    pitdown()
    sleep(60) #timer till the end of the match
    #end of the match
    lightend()
    spinner1c(False)
    spinner1a(False)
    spinner2c(False)
    spinner2a(False)
    spinner3c(False)
    spinner3a(False)
    stopmatch()
    logging.info('match ended')