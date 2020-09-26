'''
Created on 26.09.2020

@author: palmerr
'''
from PyQt5 import uic
from PyQt5.Qt import QWizardPage, QLabel, QVBoxLayout, QLineEdit, QPushButton
import webbrowser


class intropage(QWizardPage):
    '''
    classdocs
    '''
    def __init__(self, controller):
        '''
        Constructor
        '''
        super().__init__()
        self.controller = controller
        self.page = uic.loadUi('./uis/intropage.ui')
        self.page.pageID = 1
        #return page
