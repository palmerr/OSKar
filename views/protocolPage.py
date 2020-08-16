'''
Created on 21.04.2020

@author: motzma
'''
from PyQt5 import uic
from PyQt5.Qt import QWizardPage, QLabel, QVBoxLayout, QLineEdit, QPushButton
import webbrowser


class protocolpage(QWizardPage):
    '''
    classdocs
    '''
    def __init__(self, controller):
        '''
        Constructor
        '''
        super().__init__()
        self.controller = controller

        self.page = uic.loadUi('./uis/protocolpage.ui')
        #return page

        self.btnProtocol = self.page.findChild(QPushButton, 'btnProtocol')
        self.btnProtocol.clicked.connect(self.btnProtocolClicked)

    def btnProtocolClicked(self, button):
        webbrowser.open_new(r'./temp/javascript-klassen.pdf')

    def validatePage():
        print("validatePage")
        return False
