from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPalette, QColor, QBrush, QFont, QLinearGradient
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QDockWidget
from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout, QAction, QStyleFactory
from PyQt5.QtWidgets import QGroupBox, QStackedWidget, QTableWidget, QTableWidgetItem
from PyQt5.QtWidgets import QLabel, QLineEdit, QPushButton

import sys

sys.path.insert(0, "../API_Scripts")

from mongoApi import fetchDetails


def projectInfo(abbv):

  def __init__(self, parent):
    QWidget.__init__(self)

    lblPalette = QPalette()
    lblBrush = QBrush(QColor(255, 255, 255))
    lblBrush.setSTyle(Qt.SolidPattern)
    lblPalette.setBrush(QPalette.Disabled, QPalette.Window, lblBrush)

    lblFont = QFont()
    lblFont.setFamily("Calibri Light")
    lblFont.setPointSize(15)

    #project details segment
    self.titleLbl = QLabel("Project Title")
    self.titleLbl.setPalette(lblPalette)
    self.titleLbl.setFont(lblFont)
    self.titleLbl.setAutoFillBackground(False)

    self.abbvLbl = QLabel("Project Abbreviation")
    self.abbvLbl.setPalette(lblPalette)
    self.abbvLbl.setFont(lblFont)
    self.abbvLbl.setAutoFillBackground(False)

    self.codeLbl = QLabel("Project Code")
    self.codeLbl.setPalette(lblPalette)
    self.codeLbl.setFont(lblFont)
    self.codeLbl.setAutoFillBackground(False)

    self.phaseLbl = QLabel("Project Phase")
    self.phaseLbl.setPalette(lblPalette)
    self.phaseLbl.setFont(lblFont)
    self.phaseLbl.setAutoFillBackground(False)

    #project completion and issues status segment
    self.totalLbl = QLabel("Total Issues")
    self.totalLbl.setPalette(lblPalette)
    self.totalLbl.setFont(lblFont)
    self.totalLbl.setAutoFillBackground(False)

    self.openLbl = QLabel("Open Issues")
    self.openLbl.setPalette(lblPalette)
    self.openLbl.setFont(lblFont)
    self.openLbl.setAutoFillBackground(False)

    self.closedLbl = QLabel("Closed Issues")
    self.closedLbl.setPalette(lblPalette)
    self.closedLbl.setFont(lblFont)
    self.closedLbl.setAutoFillBackground(False)

    self.completionlbl = QLabel("Project Completion")
    self.completionlbl.setPalette(lblPalette)
    self.completionlbl.setFont(lblFont)
    self.completionlbl.setAutoFillBackground(False)

    #layout box setup for both segments
    detailsVBox = QVBoxLayout()
    detailsVBox.addWidget(self.titleLbl)
    detailsVBox.addWidget(self.abbvLbl)
    detailsVBox.addWidget(self.codeLbl)
    detailsVBox.addWidget(self.phaseLbl)

    phaseVBox = QVboxLayout()
    phaseVBox.addWidget(self.totalLbl)
    phaseVBox.addWidget(self.openLbl)
    phaseVBox.addWidget(self.closedLbl)
    phaseVBox.addWidget(self.completionlbl)

    #details groupbox
    self.detailsGrp = QGroupBox("PRoject Details")
    self.detailsGrp.setLayout(detailsVBox)
    self.detailsGrp.isCheckable(False)
    self.detailsGrp.alignment("AlignLeft")

    #issues groupbox
    self.issuesGrp = QGroupBox("Issues")
    self.issuesGrp.setLayout(phaseVBox)
    self.issuesGrp.isCheckable(False)
    self.detailsGrp.alignment("AlignLeft")

    #top box layout
    topHBox = QHBoxLayout()
    topHBox.addLayout(detailsVBox)
    topHBox.addStretch()
    topHBox.addLayout(phaseVBox)

    #Documents groupbox and layout
    
