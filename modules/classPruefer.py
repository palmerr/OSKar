class clsPruefer(object):

    def __init__(self, nachname, vorname, kuerzel):
        self.nachname = nachname
        
        self.vorname = vorname
        self.kuerzel = kuerzel
    
    def setVorname(self, vorname):
        self.vorname = vorname

    def setKuerzel(self, kuerzel):
        self.kuerzel = kuerzel

    def getPruefername(self):
        strPruefer = self.nachname
        if not self.vorname is None:
            strPruefer = "\""+strPruefer + "\"" + "," + "\""+ self.vorname+"\""

        if not self.kuerzel is None:
            strPruefer = strPruefer + "," + "\""+self.kuerzel+"\""

        return strPruefer

#pruefer = clsPruefer(nachname = "Motz" ,vorname="Markus" ,kuerzel = "1mto4")
#print("Prüfer: " + pruefer.getPruefername())
