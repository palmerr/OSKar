'''
Created on 21.04.2020

@author: motzma
'''
from PyQt5 import uic
from PyQt5.Qt import QWizardPage, QLabel, QVBoxLayout, QLineEdit

class callpage(QWizardPage):
    '''
    classdocs
    '''
    def __init__(self, controller):
        '''
        Constructor
        '''
        super().__init__()
        self.controller = controller
