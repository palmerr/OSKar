import os, sys, time
import mysql.connector
from termcolor import colored
import Adafruit_DHT
import RPi.GPIO as GPIO
from six.moves import input
import classDatenbank
import classPruefer
import classFirma
import classTemperatur
import classHumidity
import classGpio



try:
    def TempHumi():
        # Temperatursensoren erstellen
        temp1 = classTemperatur.clsTemperatur(file ='/sys/bus/w1/devices/28-e365bc116461/w1_slave', offset = "0.15")
        temp2 = classTemperatur.clsTemperatur(file ='/sys/bus/w1/devices/28-316abc116461/w1_slave', offset = "0.16")
        temp3 = classTemperatur.clsTemperatur(file ='/sys/bus/w1/devices/28-0966bc116461/w1_slave', offset = "0.10")

        #Temperatursensor 1
        messdaten = temp1.getTemperatur()
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


        #Temperatursensor 2
        messdaten = temp2.getTemperatur()
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



        #Temperatursensor 3
        messdaten = temp3.getTemperatur()
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


        #Temperatur erstellen
        temp = ((floatTemp1+floatTemp2+floatTemp3) /3)
        fullTemp = '%6.2f' % temp

        #Luftfeuchtesensor erstellen
        humi = classHumidity.clsHumidity(sensor = Adafruit_DHT.DHT11 , gpiopin = 25, offset = 0.0)
        messdaten = float(humi.getHumidity())
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

        #Datenbankeintrag
        db = classDatenbank.clsDatenbank(host = "localhost",
                                         user = "oskar_db",
                                         passwd = "123456",
                                         db = "oskar")
        db.Connect()
        db.QueryInsert(sqlstatement= "insert into temp_humi",
                       params = "temp,humi",
                       values = (fullTemp)+","+(fullHumi))
        db.Disconnect()

    def Pruefer():
        #Abfrage ob Nachname i.O
        falsch = False
        while falsch == False:
            n= input("Bitte geben Sie Ihren Nachnamen ein: ")
            if n.isalpha() == False:
                print("Ihre Eingaben ist Falsch! Bitte nur Buchstaben ...")
                falsch = False
            elif n.isalpha() == True:
                nachname = n

                #Abfrage ob Vornamen i.O
                falsch = False
                while falsch == False:
                    v = input("Bitte geben Sie Ihren Vornamen ein: ")
                    if v.isalpha() == False:
                        print("Ihre Eingaben ist Falsch! Bitte nur Buchstaben ...")
                        falsch = False
                    elif v.isalpha() == True:
                        vorname = v

                        #Abfrage ob Kürzel kleiner 5 Zeichen
                        falsch = False
                        laenge = 7
                        while falsch == False:
                            k= input("Bitte geben Sie Ihren Kürzel ein: ")
                            if len(k) < laenge:
                                kuerzel = k
                                pruefer = classPruefer.clsPruefer(nachname = nachname, vorname= vorname, kuerzel= kuerzel)
                                print(pruefer.getPruefername())
                                #Datenbankeintrag
                                db1 = classDatenbank.clsDatenbank(host = "localhost",
                                                                  user = "oskar_db",
                                                                  passwd = "123456",
                                                                  db = "oskar")
                                db1.Connect()

                                db1.QueryInsert(sqlstatement= "insert into pruefer",
                                                params = "nachname,vorname,kuerzel",
                                                values = pruefer.getPruefername())
                                db1.Disconnect()
                                falsch = True
                            if len(k) > laenge:
                                print("Ihre Eingaben ist Falsch! Ihr Kürzel ist zu lang ...")
                                falsch = False

    def Firma():
        #Abfrage ob Firmenname i.O
        f= input("Bitte geben Sie Ihren Firmennamen ein: ")
        firma = f

        #Abfrage ob Strasse i.O
        s = input("Bitte geben Sie die Straße ein: ")
        strasse = s

        #Abfrage ob Hausnummer i.O
        h = input("Bitte geben Sie die Hausnummer ein: ")
        hausnummer = h

        #Abfrage ob Ort i.O
        falsch = False
        while falsch == False:
            o = input("Bitte geben Sie Ihre Ort ein: ")
            if o.isalpha() == False:
                print("Ihre Eingaben ist Falsch! Bitte nur Buchstaben ...")
                falsch = False
            elif o.isalpha() == True:
                ort = o

                #Abfrage ob PLZ i.O
                falsch = False
                laenge = 6
                while falsch == False:
                    p = input("Bitte geben Sie Ihren PLZ ein: ")
                    if o.isdigit() == False:
                        if len(p) == 5:
                            plz = p
                            firma = classFirma.clsFirma(firma = firma, strasse= strasse, hausnummer = hausnummer, plz = plz, ort = ort)
                            print("Firma: " + firma.getFirmenname())
                            #Datenbankeintrag
                            db2 = classDatenbank.clsDatenbank(host = "localhost",
                                                              user = "oskar_db",
                                                              passwd = "123456",
                                                              db = "oskar")
                            db2.Connect()

                            db2.QueryInsert(sqlstatement= "insert into firma",
                                            params = "firma,strasse,hausnummer,plz,ort",
                                            values = firma.getFirmenname())
                            db2.Disconnect()
                            falsch = True
                        else:
                            print("Ihre Eingaben ist Falsch! Ihre PLZ ist zu kurz oder zu lang ...")
                            falsch = False





    if __name__=='__main__':
        TempHumi()
        Pruefer()
        Firma()


except KeyboardInterrupt:

    # Programm wird beendet wenn CTRL+C gedrückt wird.
    print('Temperaturmessung wird beendet')
except Exception as e:
    print(str(e))
    sys.exit(1)
finally:
    # Das Programm wird hier beendet, sodass kein Fehler in die Console geschrieben wird.
    #print('Programm wird beendet.')
    sys.exit(0)
