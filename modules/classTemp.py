class clsTemp(object):

     def __init__(self, file, offset):
        self.file =file
        self.offset = offset
        
     def setFile(self, file):
          self.file = file
          file.close()

     def setOffset(self, offset):
          self.offset = offset


     def getTemp(self):
          fullFile = open(self.file)
          offset = float(self.offset)
          filecontent = fullFile.read()
          stringValue = filecontent.split("\n")[1].split(" ")[9]
          temp = float(stringValue[2:]) / 1000
          floatTemp = float(str(temp + offset))
          fullTemp = '%6.2f' % floatTemp
          return fullTemp


#zu Testen
#temp1 = clsTemp(file ='/sys/bus/w1/devices/28-3a9cbd116461/w1_slave', offset = "0.15")
#temp2 = clsTemperatur(file ='/sys/bus/w1/devices/28-1660bc116461/w1_slave', offset = "0.16")
#temp3 = clsTemperatur(file ='/sys/bus/w1/devices/28-0966bc116461/w1_slave', offset = "0.10")
#print("Temp1: " + temp1.getTemperatur())
#print("Temp2: " + temp2.getTemperatur())
#print("Temp3: " + temp3.getTemperatur())
