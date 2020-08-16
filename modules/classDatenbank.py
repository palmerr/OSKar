import mysql.connector
from mysql.connector import errorcode
from termcolor import colored

class clsDatenbank(object):

    host=username=password=database=cnx=cursor=None
        
    def __init__(self,host,user,passwd,db):
        self.host = host
        self.username = user
        self.password = passwd
        self.database = db
        
    def Connect(self):
        config = {
            'user': self.username,
            'password': self.password,
            'host': self.host,
            'database': self.database
                }
        try:
            self.cnx = mysql.connector.connect(**config)
            self.cursor = self.cnx.cursor()
            print("DB Verbindung ist hergestellt")
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Fehler Username oder Passwort ist falsch")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Datenbankfehler")
            else:
                print(err)

    def QueryInsert(self, sqlstatement, params, values):
        if (params is not None):
            if (values is not None):
                sqlstatement = sqlstatement
                columns = params
                values = values
                sql = (sqlstatement)+"("+(columns)+")"+"values"+"("+(values)+")"
                print(sql)
                self.cursor.execute(sql)
        else:
            print("insert Befehl hat nicht funktioniert es fehlt ein Parameters")
            return False
        try:
            self.cnx.commit()
            print ("Transaction wurde beendet, Werte wurden hinzugefügt")
            return True
        except mysql.connector.Error as er:
            self.cnx.rollback()
            print ("Transaction hat ein 'rolled back' durchgeführt: " + err.erno)
            return False
        
    def QuerySelect(self,sqlstatement, params, header):
        if (params is not None):
            try:
                self.cursor.execute(sqlstatement, (params,))
                rtnvalue = self.cursor.fetchall()
                print(colored("[I] + executed select with params","green"))
                if header:
                    rtnvalue.insert(0,self.cursor.column_names)
                return rtnvalue
            except:
                print(colored("[C] + something went wrong while executing select with params:","red"))
                return False
        else:
            try:
                self.cursor.execute(sqlstatement)
                rtnvalue = self.cursor.fetchall()
                print(colored("[I] + executed select without params: " + sqlstatement,"green"))
                if header:
                    rtnvalue.insert(0,self.cursor.column_names)
                return rtnvalue
            except:
                print(colored("[C] + something went wrong while executing select without params","red"))
                return None
                
    def Disconnect(self):
        self.cnx.close()
        print("Verbindung wird geschlossen")
