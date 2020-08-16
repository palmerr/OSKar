import RPi.GPIO as GPIO

class clsPump(object):
    

     def __init__(self):

        pass

     def set_pump_on(self, pump_on):
     
        self.pumpOn = pumpOn

     def set_pump_off(self, pump_off):
     
        self.gpiopin = gpiopin
       

     def get_pump_on(self):
     
        return print("Pump is on")    
         
     def get_pump_off(self):
     
        return print("Pump is off")


#zu Testen
#humi = clsHumidity(sensor = Adafruit_DHT.DHT11 , gpiopin = 25, offset = 0.0)
#print("Luftfeuchte: " + humi.getHumidity())
