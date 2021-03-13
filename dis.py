'''Ultrasonic sensor and distance calculation and beep buzzer'''
'''Description:
    This program uses an ultrasonic sensor, buzzer, and GPIO pins for calculating 
        the distance of undefined objects and beep to the user'''

'''Import packages'''
import RPi.GPIO as GPIO
import time
from time import sleep
'''variables declared forvariables declared for store GPIO PIN to it
    The echo pin is used for ultrasonic input 
    The Trig pin used for ultrasonic output
    Buzzer is used input for the beep.     '''
TRIG=21
ECHO=20
buzzer=16 

'''#Disable warnings (optional)
    Select GPIO mode
    Set buzzer - pin 16 as output'''
GPIO.setwarnings(False)   
GPIO.setmode(GPIO.BCM)      
GPIO.setup(buzzer,GPIO.OUT)
'''Run forever loop'''
while True:
    print("distance measurement in progress")
    '''Set echo pin as output and Trig pin as input '''
    GPIO.setup(21,GPIO.OUT)
    GPIO.setup(20,GPIO.IN)
    GPIO.output(21,False)
    print("waiting for sensor to settle")
    '''#Delay in seconds and set TRIG as Hige'''
    time.sleep(0.2)
    GPIO.output(21,True)
    time.sleep(0.00001)
    GPIO.output(21,False)
    '''#while the Echo is low record time if it high record a time that high'''
    while GPIO.input(20)==0:
        pulse_start=time.time()
    while GPIO.input(20)==1:
        pulse_end=time.time()
    '''Time taken by the pulse is actually for to and from the travel of ultrasonic signals, 
        while we need only half of this. Therefore time is taken as time/2.'''
    pulse_duration=pulse_end-pulse_start
    distance=pulse_duration*17150
    distance=round(distance,2)
    '''If the distance is less than 50cm the beep the Buzer'''
    if distance <50:
        GPIO.output(buzzer,GPIO.HIGH)
    else :
        GPIO.output(buzzer,GPIO.LOW)
    print("distance:",distance,"cm")
    time.sleep(2)        