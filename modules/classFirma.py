class clsFirma(object):
       
    def __init__(self, firma, strasse, hausnummer, plz, ort):
        self.firma = firma
	
        self.strasse = strasse
        self.hausnummer = hausnummer
        self.plz = plz
        self.ort = ort

    def setStrasse(self, strasse):
        self.strasse = strasse
        
    def setHausnummer(self, hausnummer):
        self.hausnummer = hausnummer

    def setPLZ(self, plz):
        self.plz = plz 
        
    def setOrt(self, ort):
        self.ort = ort
         
    def getFirmenname(self):
        strFirma = self.firma
        if not self.strasse is None:
            strFirma = strFirma + "," + self.strasse
        
        if not self.hausnummer is None:
            strFirma = strFirma + " " + self.hausnummer

        if not self.plz is None:
            strFirma = strFirma + "," + self.plz
            
        if not self.ort is None:
            strFirma = strFirma + "," + self.ort

        return strFirma

#firma = clsFirma(firma = " OSK", strasse="       Elisbethenstrasse" ,hausnummer = "15", plz = "       88121", ort = "Ravensburg")
#print("Firma: " + firma.getFirmenname())
