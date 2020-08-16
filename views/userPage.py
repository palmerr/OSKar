'''
Created on 21.04.2020

@author: motzma
'''
from PyQt5 import uic
from PyQt5.Qt import QWizardPage, QLabel, QVBoxLayout, QLineEdit

class userpage(QWizardPage):
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
        txtInsertName = page.findChild(QLineEdit, 'txtInsertName')
        page.registerField('txtInsertName*',txtInsertName)

        txtInsertVorname = page.findChild(QLineEdit, 'txtInsertVorname')
        page.registerField('txtInsertVorname*',txtInsertVorname)

        txtInsertKuerzel = page.findChild(QLineEdit, 'txtInsertKuerzel')
        page.registerField('txtInsertKuerzel*',txtInsertKuerzel)
