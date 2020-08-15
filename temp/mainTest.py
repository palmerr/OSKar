import os, sys, time
import classPruefer
import projektXUi



nachname = projektXUi.Window.createUserPage(txtInsertName)
vorname = projektXUi.Window(txtInsertVorname)
kuerzel = projektXUi.Window(txtInsertKuerzel)
pruefer = classPruefer.clsPruefer(nachname = nachname, vorname= vorname, kuerzel= kuerzel)
print(pruefer.getPruefername())
