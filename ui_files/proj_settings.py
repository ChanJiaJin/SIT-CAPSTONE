from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPalette, QColor, QBrush, QFont, QLinearGradient
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QDockWidget
from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout, QAction, QStyleFactory
from PyQt5.QtWidgets import QGroupBox, QTableView, QHeaderView
from PyQt5.QtWidgets import QTableWidgetItem, QLabel, QLineEdit, QPushButton, QComboBox

import sys

sys.path.insert(0, "../API_Scripts")

from mongoApi import addTask, fetchTasks, updateGantt


class Settings(QWidget):

  def __init__(self, title):
    QWidget.__init__(self)

    ###GANTT CHART SEGMENT HERE###
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
                               "width: 150px;")

    #connectiong signal function to update db
    self.addTask.clicked.connect(self.newTask(title))

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

    tasksList = fetchTasks(title)

    #setting up number of rows needed for table
    rowCount = len(tasksList)
    self.ganttTable.setRowCount(rowCount)
    self.projectsTable.setColumnCount(3)

    #et stretch for all columns
    header = self.ganttTable.horizontalHeader()
    header.setSectionResizeMode(0, QHeaderView.Stretch)
    header.setSectionResizeMode(1, QHeaderView.Stretch)
    header.setSectionResizeMode(2, QHeaderView.Stretch)

    #set horizontal headers
    headers = ["Task Description", "Start Date", "End Date"]
    self.ganttTable.setHorizontalHeaderLabels(headers)

    #remove vertical scroll bar
    self.ganttTable.setVerticalScrollBarPolicy(Qt.ScrollbarAlwaysOff)

    #setting items to populate table
    row = 0
    column = 0

    for task in tasksList:
      #extracting the data items ot be displayed for each item
      task = task[0]
      start = task[1]
      end = task[2]

      #setting up data items into 3 columns per row
      self.ganttTable.setItem(row, column, QTableWidgetItem(task))
      self.ganttTable.setItem(row, column + 1, QTableWidgetItem(start))
      self.ganttTable.setItem(row, column + 2, QTableWidgetItem(end))

      #adding one more row and resetting column back to 0
      row = +1
      column = 0

    #setting up button to update table's items into db
    self.update = QPushButton("Update")
    self.update.setStyleSheet("background-color: #BB86FC;"
                              "color: black;"
                              "border: 2px solid white;"
                              "font-size: 20px;"
                              "height: 50px;"
                              "width: 150px;")
    self.update.clicked.connect(self.update(title))

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

    ###MEMBERS SEGMENT HERE###
    #setting up members box title
    memebrsPalette = QPalette()
    membersBrush = QBrush(QColor(255, 255, 255))
    membersBrush.setStyle(Qt.SolidPattern)
    memebrsPalette.setBrush(QPalette.Disabled, QPalette.Window, membersBrush)

    memebrsFont = QFont()
    memebrsFont.setFamily("Calibri Light")
    memebrsFont.setPointSize(15)

    self.membersLabel = QLabel("Gantt Chart Items")
    self.membersLabel.setPalette(memebrsPalette)
    self.membersLabel.setFont(memebrsFont)
    self.membersLabel.setAutoFillBackground(False)
    self.membersLabel.setStyleSheet("""
              QLabel{
                  color: white;
                  font-size: 30px;
              }
          """)

    #setting up combo box for searching members
    self.search = QComboBox()
    self.search.setPlaceHolderText("Search for project members")
    self.search.setStyleSheet("""
          QComboBox{
              background-color: white;
              color: black;
              width: 300px;
              height: 30px;
              font-size: 20px;
          }
      """)

    #button to add member
    self.addMember = QPushButton("Add")
    self.addMember.setStyleSheet(
      "background-color: #BB86FC;"
       "color: black;"
       "border: 2px solid white;"
       "font-size: 20px;"
       "height: 50px;"
       "width: 150px;"
    )

    #table to showcase members and their details

  ###FUNCTIONS FOR SIGNALS AND SLOTS###
  def newTask(self, title):
    task = self.taskInput.text()
    start = self.start.text()
    end = self.end.text()

    addTask(title, task, start, end)

    self.ganttTable.clear()

    tasksList = fetchTasks()

    #setting items to populate table
    row = 0
    column = 0

    for task in tasksList:
      #extracting the 3 data items to be displayed for each item
      task = task[0]
      start = start[1]
      end = [2]

      #setting data items into 3 columns per row
      self.ganttTable.setItem(row, column, QTableWidgetItem(task))
      self.ganttTable.setItem(row, column + 1, QTableWidgetItem(start))
      self.ganttTable.setItem(row, column + 2, QTableWidgetItem(end))

      #adding one more row and resetting column back to 0
      row = +1
      column = 0


def update(self, title):
  #to get the row count and column count
  model = self.ganttTable.model()
  rowCount = model.rowCount()
  columnCount = model.columnCount()

  #empty array to be passed into function
  dataset = []

  #loop to loop through all data in the table
  for row in range(rowCount):
    #to set the dictionary to take in the data and the
    #key value pairs expected
    rowData = {"task": [], "start": [], "end": []}

    #to indicate which column data is being accessed now
    columnNo = 0
    for column in range(columnCount):
      #get index of the cell being referred to and data
      index = model.index(row, columnNo)
      #model.data() returns an object, so string conversion is needed
      cellData = str(model.data(index).toString())

      #if loop to generate key value pairs to be appended to
      #fit into mongodb update operator
      if columnNo == 0:
        rowData["task"] = cellData
      elif columnNo == 1:
        rowData["start"] = cellData
      elif columnNo == 2:
        rowData["end"] = cellData
      else:
        pass

      #to move up by one column for indexing
      columnNo += 1

    #To append disctionary into list
    dataset.append(rowData)
