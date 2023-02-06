from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPalette, QColor, QBrush, QFont, QLinearGradient
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QDockWidget
from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout, QAction, QStyleFactory
from PyQt5.QtWidgets import QGroupBox, QStackedWidget, QTableView
from PyQt5.QtWidgets import QLabel, QLineEdit, QPushButton

import sys


class Settings(QWidget):

  def __init__(self, title):
    QWidget.__init__(self)

    #setting up gantt chart box title
    ganttPalette = QPalette()
    ganttBrush = QBrush(QColor(255, 255, 255))
    ganttBrush.setStyle(Qt.SolidPattern)
    ganttPalette.setBrush(QPalette.Disabled, QPalette.Window, ganttBrush)

    ganttFont = QFont()
    ganttFont.setFamily("Calibri Light")
    ganttFont.setPointSize(15)

    self.ganttChartLabel = QLabel("Gantt Chart Items")
    self.ganttChartLabel.setPalette(ganttPalette)
    self.ganttChartLabel.setFont(ganttFont)
    self.ganttChartLabel.setAutoFillBackground(False)
    self.ganttChartLabel.setStyleSheet("""
              QLabel{
                  color: white;
                  font-size: 30px;
              }
          """)

    #setting up input fields for gantt chart box
    self.taskInput = QLineEdit()
    self.taskInput.setPlaceholderText("Task name")
    self.taskInput.setStyleSheet("""
          QLineEdit{
              background-color: white;
              color: black;
              width: 300px;
              height: 30px;
              font-size: 20px;
          }
      """)

    #setting up start and end buttons line edit
    self.start = QLineEdit()
    self.start.setPlaceholderText("Start")
    self.end = QLineEdit()
    self.end.setPlaceholderText("End")
    self.start.setStyleSheet("""
          QLineEdit{
              background-color: white;
              color: black;
              width: 100px;
              height: 30px;
              font-size: 20px;
          }
      """)
    self.end.setStyleSheet("""
          QLineEdit{
              background-color: white;
              color: black;
              width: 100px;
              height: 30px;
              font-size: 20px;
          }
      """)

    #setting up add task button for gantt chart box
    self.addTask = QPushButton("Add Task")
    self.addTask.setStyleSheet("background-color: #BB86FC;"
                               "color: black;"
                               "border: 2px solid white;"
                               "font-size: 20px;"
                               "height: 50px;"
                               "width: 150;")

    #setting up gantt chart box
    self.titleHBox = QHBoxLayout()
    self.titleHBox.addWidget(self.ganttChartLabel)
    self.titleHBox.addStretch()

    self.inputHBox = QHBoxLayout()
    self.inputHBox.addWidget(self.taskInput)
    self.inputHBox.addStretch()
    self.inputHBox.addWidget(self.start)
    self.inputHBox.addWidget(self.end)

    self.buttonHBox = QHBoxLayout()
    self.buttonHBox.addStretch()
    self.buttonHBox.addWidget(self.addTask)
    self.buttonHBox.addStretch()

    #setting up table for gantt chart items
    self.ganttTable = QTableView()
    self.ganttTable.setStyleSheet("""
        background-color: white;
        color: black;
        font-family: calibri-light
        font-size: 20px;
      """)

    #setting up vertical box for gantt chart section
    self.ganttVBox = QVBoxLayout()
    self.ganttVBox.addLayout(self.titleHBox)
    self.ganttVBox.addLayout(self.inputHBox)
    self.ganttVBox.addStretch()
    self.ganttVBox.addLayout(self.buttonHBox)

    #setting up group box for gantt chart section and setting layout
    self.ganttGrp = QGroupBox()
    self.ganttGrp.setStyleSheet("""
        height: 50%;
        width: 100%
        background-color: #1F1B24;
      """)

    self.ganttGrp.setLayout(self.ganttVBox)
