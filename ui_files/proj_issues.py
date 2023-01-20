from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPalette, QColor, QBrush, QFont, QLinearGradient
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QDockWidget
from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout, QAction, QStyleFactory
from PyQt5.QtWidgets import QGroupBox, QStackedWidget, QTableWidget, QTableWidgetItem
from PyQt5.QtWidgets import QFormLayout
from PyQt5.QtWidgets import QLabel, QLineEdit, QPushButton

import sys

sys.path.insert(0, "../API_Scripts")

def projectIssues(abbv):
  def __init__(self,parent):
    QWidget.__init__(self,parent)

    lblPalette = QPalette()
    lblBrush = QBrush(QColor(255, 255, 255))
    lblBrush.setSTyle(Qt.SolidPattern)
    lblPalette.setBrush(QPalette.Disabled, QPalette.Window, lblBrush)

    lblFont = QFont()
    lblFont.setFamily("Calibri Light")
    lblFont.setPointSize(15)

    #workflow and phase form
    self.form = QFormLayout()
    self.form.addRow(self.tr("&Wofk Flow:"), flowComboBox)
    self.form.addRow(self.tr("&Phase:"), phaseComboBox)


    #raise Issue Button
    self.raiseIssue = QPushButton("Raise Issue")
    self.raiseIssue.setStyleSheet(
      "background-color: red;"
      "color: white;"
      "border: 2px solid white;"
      "font-size: 20px;"
      "height: 30px;"
      "width: 100px;"
    )

    #top bar HBoxLayout
    topHBox = QHBoxLayout()
    topHBox.addLayout(self.form)
    topHBox.addStretch()
    topHBox.addWidget(self.raiseIssue)

    #issues table
    self.issuesTable = QTableWidgetItem
    