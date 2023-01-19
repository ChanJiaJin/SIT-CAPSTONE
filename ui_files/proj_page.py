from PyQt5.QtCore    import Qt
from PyQt5.QtGui     import QPalette, QColor, QBrush, QFont, QLinearGradient
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QDockWidget
from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout, QAction, QStyleFactory
from PyQt5.QtWidgets import QGroupBox, QStackedWidget, QTableWidget, QTableWidgetItem
from PyQt5.QtWidgets import QLabel, QLineEdit, QPushButton

import sys
sys.path.insert(0, "../API_Scripts")

from mongoApi import fetchDetails, fetchProject

class projectsStack(QWidget):
    def __init__(self,parent):
        QWidget.__init__(self)

        #creating table widget of projects
        projectsTable = QTableWidget()
        projectsTable.setStyleSheet(
            "background-color: light-gray;"
            "color: white;"
            "font-family: calibri-light;"
            "font-size: 10px;"
        )

        projectsList = fetchDetails()

        if len(projectsList) != 0:
            #setting items to populate table
            #3 columns (Title), (Abbreviation), (Code)
            row = 0
            column = 0
            for proj in projectsList:
                
                #extracting the 3 data items to be displayed for each item
                title = proj['title']
                abbv = proj['abbv']
                code = proj['code']

                #setting data items into 3 columns per row
                projectsTable.setItem(row, column, QTableWidgetItem(title))
                projectsTable.setItem(row, column + 1, QTableWidgetItem(abbv))
                projectsTable.setItem(row, column + 1, QTableWidgetItem(code))

                #adding one more row and resetting column back to 0
                row += 1
                column = 0

        projectsTable.clicked.connect(self.openProj)
        
    #function for table rows to access project details
    #using abbv
    def openProj(self, index):
        row = index.row()

        abbv = self.projectsTable.model().item(row,1)

        fetchProject(abbv)





