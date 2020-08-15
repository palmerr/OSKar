import RPi.GPIO as GPIO
from operator import add
import os, sys, time

class clsGpio(object):

    def __init__(self, gpiopin):

        self.gpiopin = gpiopin
        
       
    def setGpioPin(self, gpiopin):
        self.gpiopin = gpiopin

    def setGpioAn(self):
        pin = self.gpiopin
        GPIO.setmode(GPIO.BOARD)
        GPIO.setwarnings(False)
        GPIO.setup(pin, GPIO.OUT)
        GPIO.output(pin, GPIO.LOW)
               

    def setGpioAus(self):
        pin = self.gpiopin
        GPIO.setmode(GPIO.BOARD)
        GPIO.setwarnings(False)
        GPIO.setup(pin, GPIO.OUT)
        GPIO.output(pin,GPIO.HIGH)
    
    def setGpioClear(self):
        GPIO.cleanup()

    def getGpioAn(self):
        return "Pin ist an"
        
    def getGpioAus(self):
        return "Pin ist aus"
        
    def getGpioClear(self):
        return "Pin wird gelöscht"
        
#Zum Testen
#pin = clsGpio(gpiopin = 11)
#pin.setGpioAn()
#print(pin.getGpioAn())
#time.sleep(5.0)
#pin.setGpioAus()
#print(pin.getGpioAus())
#pin.setGpioClear()
#print(pin.getGpioClear())