'''
Created on 21.04.2020

@author: motzma
'''
from PyQt5 import uic
from PyQt5.Qt import QWizardPage, QLabel, QVBoxLayout, QLineEdit, QPushButton

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

        page = uic.loadUi('/home/motze/ProjektX_v1/classFertig/uis/protocolpage.ui')
        #return page

        self.btnProtocol = self.findChild(QPushButton, 'btnProtocol')
        #self.btnProtocol.clicked.connect(self.controller.btnProtocolClicked)

        return QWizardPage.initializePage(self) #page
