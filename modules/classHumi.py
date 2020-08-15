#Für Test auskomentiert
#import Adafruit_DHT

class clsHumi(object):


     def __init__(self, sensor, gpiopin, offset):
         self.sensor = sensor

         self.gpiopin = gpiopin
         self.offset = offset

     def setSensor(self, sensor):
         self.sensor = sensor

     def setGpioPin(self, gpiopin):
         self.gpiopin = gpiopin

     def setOffset(self, offset):
         self.offset = offset

     def getHumi(self):
         sensor = self.sensor
         pin = self.gpiopin
         offset = float(self.offset)
         humidity, temperature = (sensor, pin)
         strhumidity = str(humidity)
         strhumidity1 = 60.0
         return strhumidity1


#zu Testen
#humi = clsHumidity(sensor = Adafruit_DHT.DHT11 , gpiopin = 25, offset = 0.0)
#humi = clsHumi(sensor = '/home/motze/ProjektX/classFertig/temp/humidity/humidity' , gpiopin = 25, offset = 0.0)
#print("Luftfeuchte: " + humi.getHumi())
