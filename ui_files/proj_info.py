from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPalette, QColor, QBrush, QFont, QLinearGradient
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QDockWidget
from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout, QAction, QStyleFactory
from PyQt5.QtWidgets import QGroupBox, QStackedWidget, QTableWidget, QTableWidgetItem
from PyQt5.QtWidgets import QLabel, QLineEdit, QPushButton

import sys

sys.path.insert(0, "../API_Scripts")

from mongoApi import fetchDetails

class ProjectInfo(QWidget):
  def __init__(self, abbv):
    QWidget.__init__(self)

    lblPalette = QPalette()
    lblBrush = QBrush(QColor(255, 255, 255))
    lblBrush.setStyle(Qt.SolidPattern)
    lblPalette.setBrush(QPalette.Disabled, QPalette.Window, lblBrush)

    lblFont = QFont()
    lblFont.setFamily("Calibri Light")
    lblFont.setPointSize(15)

    #information labels
    self.ttileLabel = QLabel("Project Title: ")
    self.ttileLabel.setPalette(lblPalette)
    self.ttileLabel.setFont(lblFont)
    self.ttileLabel.setAutoFillBackground(False)

    self.abbvlabel = QLabel("Project Abbreviation: ")
    self.abbvlabel.setPalette(lblPalette)
    self.abbvlabel.setFont(lblFont)
    self.abbvlabel.setAutoFillBackground(False)

    self.codeLabel = QLabel("Project Code: ")
    self.codeLabel.setPalette(lblPalette)
    self.codeLabel.setFont(lblFont)
    self.codeLabel.setAutoFillBackground(False)

    self.currentLabel = QLabel("Current Task: ")
    self.currentLabel.setPalette(lblPalette)
    self.currentLabel.setFont(lblFont)
    self.currentLabel.setAutoFillBackground(False)

    self.outstandinglabel = QLabel("outstanding Tasks: ")
    self.outstandinglabel.setPalette(lblPalette)
    self.outstandinglabel.setFont(lblFont)
    self.outstandinglabel.setAutoFillBackground(False)

    self.overrunLabel = QLabel("Overrun Status: ")
    self.overrunLabel.setPalette(lblPalette)
    self.overrunLabel.setFont(lblFont)
    self.overrunLabel.setAutoFillBackground(False)

    self.ttileLabel.setStyleSheet("""
            QLabel {
                color: white;
            }
        """)
    
    self.abbvlabel.setStyleSheet("""
            QLabel {
                color: white;
            }
        """)
    
    self.codeLabel.setStyleSheet("""
            QLabel {
                color: white;
            }
        """)
    
    self.currentLabel.setStyleSheet("""
            QLabel {
                color: white;
            }
        """)
    
    self.outstandinglabel.setStyleSheet("""
            QLabel {
                color: white;
            }
        """)
    
    self.overrunLabel.setStyleSheet("""
            QLabel {
                color: white;
            }
        """)

    #setting up top box for ttile, abbv and code
    self.infoBox = QVBoxLayout()
    self.infoBox.addWidget(self.ttileLabel)
    self.infoBox.addWidget(self.abbvlabel)
    self.infoBox.addWidget(self.codeLabel)

    #setting up top box
    self.topBox = QHBoxLayout()
    self.topBox.addLayout(self.infoBox)
    self.topBox.addStretch()
    self.topBox.addWidget(self.currentLabel)
    self.topBox.addStretch()
    self.topBox.addWidget(self.outstandinglabel)
    self.topBox.addStretch()
    self.topBox.addWidget(self.overrunLabel)

    #setting up main box
    self.mainBox = QVBoxLayout()
    self.mainBox.addLayout(self.topBox)

    self.setLayout(self.mainBox)
