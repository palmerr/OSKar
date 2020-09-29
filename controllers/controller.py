'''
Created on 21.04.2020

@author: motzma
'''

from views.view import *
from modules  import classTemp
from modules import classHumi
from PyQt5.Qt import QApplication
from PyQt5.QtWidgets import QLCDNumber
import sys

class Controller(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.App = QApplication(sys.argv)
        self.view = View(self)
        self.getTemp()
        self.getHumi()
        # self.module = Module(self)


    def start(self):
        sys.exit(self.App.exec())


    def btnProtocolClicked(self):
        print("Klick")

    def userArray(self):
        pass

    def companyArray(self):
        pass

    def getTemp(self):
        temp1 = classTemp.clsTemp(file ='temp/27-00044a1f53fa/w1_slave', offset = "0.0")
        temp2 = classTemp.clsTemp(file ='temp/28-00044a1f53fa/w1_slave', offset = "0.0")
        temp3 = classTemp.clsTemp(file ='temp/29-00044a1f53fa/w1_slave', offset = "0.0")

        #TempSensor1
        messdaten = temp1.getTemp()
        schleifenZaehler = 0
        schleifenAnzahl = 1000
        arryList = []
        summeTemp = 0
        while schleifenZaehler <= schleifenAnzahl:
            arryList.append(messdaten)
            schleifenZaehler = schleifenZaehler + 1

        for i in arryList:
            summeTemp += float(i)

        summeGesammt = summeTemp / schleifenAnzahl
        floatTemp1= float(summeGesammt)

        #TempSensor 2
        messdaten = temp2.getTemp()
        schleifenZaehler = 0
        schleifenAnzahl = 1000
        arryList = []
        summeTemp = 0
        while schleifenZaehler <= schleifenAnzahl:
            arryList.append(messdaten)
            schleifenZaehler = schleifenZaehler + 1

        for i in arryList:
            summeTemp += float(i)

        summeGesammt=summeTemp / schleifenAnzahl
        floatTemp2 = float(summeGesammt)

        #TempSensor 3
        messdaten = temp3.getTemp()
        schleifenZaehler = 0
        schleifenAnzahl = 1000
        arryList = []
        summeTemp = 0
        while schleifenZaehler <= schleifenAnzahl:
            arryList.append(messdaten)
            schleifenZaehler = schleifenZaehler + 1

        for i in arryList:
            summeTemp += float(i)

        summeGesammt=summeTemp / schleifenAnzahl
        floatTemp3 = float(summeGesammt)

        #Temp erstellen
        temp = ((floatTemp1+floatTemp2+floatTemp3) /3)
        fullTemp = '%6.2f' % temp
        print(temp)
        self.view.lcdTemp.display(fullTemp)
        return temp

    def getHumi(self):
        humi = classHumi.clsHumi(sensor = 'temp/humidity/humidity', gpiopin = 25, offset = 0.0)

        #HumiSensor
        messdaten = float(humi.getHumi())
        schleifenZaehler = 0
        schleifenAnzahl = 1000
        arryList = []
        summeHumi = 0

        while schleifenZaehler <= schleifenAnzahl:
            arryList.append(messdaten)
            schleifenZaehler = schleifenZaehler + 1

        for i in arryList:
             summeHumi += float(i)

        summeGesammt= summeHumi / schleifenAnzahl
        floathumi = float(summeGesammt)
        fullHumi = '%6.0f' % floathumi
        self.view.lcdHumi.display(fullHumi)
        return floathumi

    def introPage(self, page):
        print("Controller: Intropage")
        print("Page ID: " + str(page.pageID))
    def protocolPage(self, page):
        print("Controller: Controllerpage")
        print("Page ID: " + str(page.pageID))