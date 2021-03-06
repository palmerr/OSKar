﻿'''
Created on 21.04.2020

@author: motzma
'''

from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QRadioButton, QWidget, QWizard, QLCDNumber, QVBoxLayout, QPushButton, QWizardPage, QLabel, QPushButton, QLineEdit, QTextEdit
from PyQt5 import uic
from PyQt5.QtGui import QPixmap
import PyQt5.QtCore
import os, sys, time
from views import introPage
from views import protocolPage

class View(QWizard):
    '''
    classdocs
    '''

    def __init__(self, controller):
        '''
        Constructor
        '''
        super().__init__()
        self.IndependentPages=1

        self.controller = controller

        self.page1 = introPage.intropage(controller)
        self.page2 = protocolPage.protocolpage(controller)
        self.page3 = self.createUserPage()
        self.page4 = self.createCompanyPage()
        self.page5 = self.createCallPage()
        self.page6 = self.createExamPage()
        self.page7 = self.createSummaryPage()
        self.page8 = self.createFinishPage()

        self.title = "OSKar V1.0"
        self.top = 200
        self.left = 500
        self.width = 500
        self.height = 400

        self.InitWindow()

    def InitWindow(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.addPage(self.page1.page)
        self.addPage(self.page2.page)
        self.addPage(self.page3)
        self.addPage(self.page4)
        self.addPage(self.page5)
        self.addPage(self.page6)
        self.addPage(self.page7)
        self.addPage(self.page8)

        # textboxen userpage
        # add action to textbox
        self.txtBoxN = self.findChild(QLineEdit, 'txtInsertName')
        self.txtBoxN.textChanged.connect(self.controller.userArray)
        self.txtBoxV = self.findChild(QLineEdit, 'txtInsertVorname')
        self.txtBoxV.textChanged.connect(self.controller.userArray)
        self.txtBoxK = self.findChild(QLineEdit, 'txtInsertKuerzel')
        self.txtBoxK.textChanged.connect(self.controller.userArray)

        # textboxen companypage
        # add action to textbox
        self.txtBoxU = self.findChild(QLineEdit, 'txtInsertUnternehmen')
        self.txtBoxU.textChanged.connect(self.controller.companyArray)
        self.txtBoxS = self.findChild(QLineEdit, 'txtInsertStrasse')
        self.txtBoxS.textChanged.connect(self.controller.companyArray)
        self.txtBoxH = self.findChild(QLineEdit, 'txtInsertHausnummer')
        self.txtBoxH.textChanged.connect(self.controller.companyArray)
        self.txtBoxP = self.findChild(QLineEdit, 'txtInsertPostleitzahl')
        self.txtBoxP.textChanged.connect(self.controller.companyArray)
        self.txtBoxO = self.findChild(QLineEdit, 'txtInsertOrt')
        self.txtBoxO.textChanged.connect(self.controller.companyArray)



        # lcd callpage
        self.lcdTemp = self.findChild(QLCDNumber, 'lcdTemp')
        self.lcdHumi = self.findChild(QLCDNumber, 'lcdHumi')


        # textarea pruefpage
        self.txtArea = self.findChild(QTextEdit, 'txtArea')

        # label pruefpage
        self.label = self.findChild(QLabel, 'lblInsert')

        self.show()

    def createUserPage(self):
        page = uic.loadUi('./uis/userpage.ui')

        # register field for disabling next button
        txtBoxN = page.findChild(QLineEdit, 'txtInsertName')
        page.registerField('txtBoxN*',txtBoxN)
        txtBoxV = page.findChild(QLineEdit, 'txtInsertVorname')
        page.registerField('txtBoxV*',txtBoxV)
        txtBoxK = page.findChild(QLineEdit, 'txtInsertKuerzel')
        page.registerField('txtBoxK*',txtBoxK)

        return page

    def createCompanyPage(self):
        page = uic.loadUi('./uis/companypage.ui')

        # register field for disabling next button
        txtBoxU = page.findChild(QLineEdit, 'txtInsertUnternehmen')
        page.registerField('txtBoxU*',txtBoxU)
        txtBoxS = page.findChild(QLineEdit, 'txtInsertStrasse')
        page.registerField('txtBoxS*',txtBoxS)
        txtBoxH = page.findChild(QLineEdit, 'txtInsertHausnummer')
        page.registerField('txtBoxH*',txtBoxH)
        txtBoxP = page.findChild(QLineEdit, 'txtInsertHausnummer')
        page.registerField('txtBoxP*',txtBoxP)
        txtBoxO = page.findChild(QLineEdit, 'txtInsertOrt')
        page.registerField('txtBoxO*',txtBoxO)

        return page

    def createCallPage(self):
        page = uic.loadUi('./uis/callpage.ui')
        return page

    def createSummaryPage(self):
        page = uic.loadUi('./uis/summarypage.ui')
        return page

    def createExamPage(self):
        page = uic.loadUi('./uis/exampage.ui')
        return page

    def createFinishPage(self):
        page = QWizardPage()
        page.setTitle("Introduction")

        label = QLabel("This is the last page.")
        label.setWordWrap(True)

        layout = QVBoxLayout()
        layout.addWidget(label)
        page.setLayout(layout)

        return page

    def validateCurrentPage(self):
        print("view: validateCurrentPage")
        curPage = self.currentPage()
        if curPage.pageID == 1:
            print("> Next button on Intro Page")
            self.controller.introPage(curPage)
        elif curPage.pageID == 2:
            print("> Next button on Protocol Page")
            self.controller.protocolPage(curPage)
        return True
