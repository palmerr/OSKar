'''
Created on 21.04.2020

@author: motzma
'''
from PyQt5 import uic
from PyQt5.Qt import QWizardPage, QLabel, QVBoxLayout, QLineEdit

class companypage(QWizardPage):
    '''
    classdocs
    '''
    def __init__(self, controller):
        '''
        Constructor
        '''
        super().__init__()
        self.controller = controller
        # register field for disabling next button
        txtInsertUnternehmen = page.findChild(QLineEdit, 'txtInsertUnternehmen')
        page.registerField('txtInsertUnternehmen*',txtInsertUnternehmen)

        txtInsertStrasse = page.findChild(QLineEdit, 'txtInsertStrasse')
        page.registerField('txtInsertStrasse*',txtInsertStrasse)

        txtInsertHausnummer = page.findChild(QLineEdit, 'txtInsertHausnummer')
        page.registerField('txtInsertHausnummer*',txtInsertHausnummer)

        txtInsertPostleitzahl = page.findChild(QLineEdit, 'txtInsertPostleitzahl')
        page.registerField('txtInsertPostleitzahl*',txtInsertPostleitzahl)

        txtInsertOrt = page.findChild(QLineEdit, 'txtInsertOrt')
        page.registerField('txtInsertOrt*',txtInsertOrt)
