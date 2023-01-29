from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPalette, QColor, QBrush, QFont, QLinearGradient
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QDockWidget
from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout, QAction, QStyleFactory
from PyQt5.QtWidgets import QGroupBox, QStackedWidget, QTableWidget, QTableWidgetItem, QHeaderView
from PyQt5.QtWidgets import QLabel, QLineEdit, QPushButton

import sys

sys.path.insert(0, "../API_Scripts")

from mongoApi import fetchDetails


class projectsStack(QWidget):

  def __init__(self, parent):
    QWidget.__init__(self)

    #creating table widget of projects
    projectsTable = QTableWidget()
    projectsTable.setStyleSheet(
    "background-color: white;"
    "color: black;"
    "font-family: calibri-light;"
    "font-size: 20px;"
    )


    projectsList = fetchDetails()

    #setting items to populate table
    #3 columns (Title), (Abbreviation), (Code)
    row = 0
    column = 0

    #setting the number of rows needed for table
    rowCount = len(projectsList)
    projectsTable.setRowCount(rowCount)
    projectsTable.setColumnCount(3)

    # set stretch for all columns
    header = projectsTable.horizontalHeader()       
    header.setSectionResizeMode(0, QHeaderView.Stretch)
    header.setSectionResizeMode(1, QHeaderView.Stretch)
    header.setSectionResizeMode(2, QHeaderView.Stretch)

    #remove vertical headers
    projectsTable.verticalHeader().hide()

    for proj in projectsList:

      #for converting set object into list
      #to access element
      projList = list(proj)

      #extracting the 3 data items to be displayed for each item
      title = projList[0]
      abbv = projList[1]
      code = projList[2]

      #setting data items into 3 columns per row
      projectsTable.setItem(row, column, QTableWidgetItem(title))
      projectsTable.setItem(row, column + 1, QTableWidgetItem(abbv))
      projectsTable.setItem(row, column + 2, QTableWidgetItem(code))

      #adding one more row and resetting column back to 0
      row += 1
      column = 0

    projectsTable.clicked.connect(self.openProj)

    tableLayout = QVBoxLayout()
    tableLayout.addWidget(projectsTable)
    self.setLayout(tableLayout)

  #function for table rows to access project details
  #using abbv
  def openProj(self, index):
    row = index.row()

    abbv = self.projectsTable.model().item(row, 1)

    
