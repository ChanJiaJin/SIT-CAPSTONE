from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPalette, QColor, QBrush, QFont, QLinearGradient
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QDockWidget
from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout, QAction, QStyleFactory
from PyQt5.QtWidgets import QGroupBox, QTableWidget, QHeaderView
from PyQt5.QtWidgets import QTableWidgetItem, QLabel, QLineEdit, QPushButton, QComboBox

import sys

sys.path.insert(0, "../API_Scripts")
from mongoApi import newTask, fetchTasks, updateGantt
from mongoApi import addmembers, fetchMembers, fetchUsers


class Settings(QWidget):

  def __init__(self, abbv):
    QWidget.__init__(self)

    ### GANTT CHART SEGMENT HERE###
    # setting up gantt chart box title
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

    # setting up input fields for gantt chart box
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

    # setting up start and end buttons line edit
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

    # setting up add task button for gantt chart box
    self.add = QPushButton("Add Task")
    self.add.setStyleSheet("background-color: #BB86FC;"
                           "color: black;"
                           "border: 2px solid white;"
                           "font-size: 20px;"
                           "height: 50px;"
                           "width: 150px;")

    # setting up gantt chart box
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
    self.buttonHBox.addWidget(self.add)
    self.buttonHBox.addStretch()

    # setting up table for gantt chart items
    self.gantt = QTableWidget()
    self.gantt.setStyleSheet("""
        background-color: white;
        color: black;
        font-family: calibri-light;
        font-size: 20px;
        """)

    tasksList = fetchTasks(abbv)

    # setting up number of rows needed for table
    tasksRowCount = len(tasksList)
    self.gantt.setRowCount(tasksRowCount)
    self.gantt.setColumnCount(3)

    #set stretch for all columns
    taskHeader = self.gantt.horizontalHeader()
    taskHeader.setSectionResizeMode(0, QHeaderView.Stretch)
    taskHeader.setSectionResizeMode(1, QHeaderView.Stretch)
    taskHeader.setSectionResizeMode(2, QHeaderView.Stretch)

    # set horizontal headers
    taskHeader = ["Task Description", "Start Date", "End Date"]
    self.gantt.setHorizontalHeaderLabels(taskHeader)

    # remove vertical scroll bar
    self.gantt.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

    # setting items to populate table
    taskRow = 0
    taskColumn = 0

    for task in tasksList:
      # extracting the data items ot be displayed for each item
      task = task[0]
      start = task[1]
      end = task[2]

      # setting up data items into 3 columns per row
      self.gantt.setItem(taskRow, taskColumn, QTableWidgetItem(task))
      self.gantt.setItem(taskRow, taskColumn + 1, QTableWidgetItem(start))
      self.gantt.setItem(taskRow, taskColumn + 2, QTableWidgetItem(end))

      # adding one more row and resetting column back to 0
      taskRow = +1
      taskColumn = 0

    # setting up button to update table's items into db
    self.updateTable = QPushButton("Update")
    self.updateTable.setStyleSheet("background-color: #BB86FC;"
                                   "color: black;"
                                   "border: 2px solid white;"
                                   "font-size: 20px;"
                                   "height: 50px;"
                                   "width: 150px;")

    # setting up vertical box for gantt chart section
    self.ganttVBox = QVBoxLayout()
    self.ganttVBox.addLayout(self.titleHBox)
    self.ganttVBox.addLayout(self.inputHBox)
    self.ganttVBox.addStretch()
    self.ganttVBox.addLayout(self.buttonHBox)

    # setting up group box for gantt chart section and setting layout
    self.ganttGrp = QGroupBox()
    self.ganttGrp.setStyleSheet("""
        height: 50%;
        width: 100%;
        background-color: #1F1B24;
        """)

    self.ganttGrp.setLayout(self.ganttVBox)

    ### MEMBERS SEGMENT HERE###
    # setting up members box title
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

    # setting up combo box for searching members
    self.search = QComboBox()
    self.search.setPlaceholderText("Search for project members")
    self.search.setStyleSheet("""
        QComboBox{
        background-color: white;
        color: black;
        width: 300px;
        height: 30px;
        font-size: 20px;
        }
        """)

    # button to add member
    self.addMember = QPushButton("Add")
    self.addMember.setStyleSheet("background-color: #BB86FC;"
                                 "color: black;"
                                 "border: 2px solid white;"
                                 "font-size: 20px;"
                                 "height: 50px;"
                                 "width: 150px;")

    # table to showcase members and their details
    self.members = QTableWidget()
    self.members.setStyleSheet("""
        background-color: white;
        color: black;
        font-family: calibri-light;
        font-size: 20px;
membersRowCount        

              """)

    membersList = fetchMembers(abbv)

    #setting up number of rows needed for table
    membersRowCount = len(membersList)
    self.members.setRowCount(membersRowCount)
    self.members.setColumnCount(4)

    #set stretch for all columns
    memberHeader = self.members.horizontalHeader()
    memberHeader.setSectionResizeMode(0, QHeaderView.Stretch)
    memberHeader.setSectionResizeMode(1, QHeaderView.Stretch)
    memberHeader.setSectionResizeMode(2, QHeaderView.Stretch)
    memberHeader.setSectionResizeMode(3, QHeaderView.Stretch)

    #set horizontal headers
    memberHeader = ["Name", "Department", "Discipline", "Email"]
    self.members.setHorizontalHeaderLabels(memberHeader)

    #remove vertical scroll bar
    self.members.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

    #setting items to populate table
    memRow = 0
    memColumn = 0

    for member in membersList:
      #extracting the data items to be displayed for each item
      name = member[0]
      dept = member[1]
      disc = member[2]
      email = member[3]

      #setting up data tiems into 4 columns per row
      self.gantt.setItem(memRow, memColumn, QTableWidgetItem(name))
      self.gantt.setItem(memRow, memColumn + 1, QTableWidgetItem(dept))
      self.gantt.setItem(memRow, memColumn + 2, QTableWidgetItem(disc))
      self.gantt.setItem(memRow, memColumn + 2, QTableWidgetItem(email))

      #adding one mroe row and resetting column back to 0
      memRow = +1
      memColumn = 0


    #for settingup members box
    self.memLabel = QHBoxLayout()
    self.memLabel.addWidget(self.membersLabel)
    self.memLabel.addStretch()
    
    self.memFindHBox = QHBoxLayout()
    self.memFindHBox.addStretch()
    self.memFindHBox.addWidget(self.search)
    self.memFindHBox.addWidget(self.addMember)
    self.memFindHBox.addStretch()

    self.memVBox = QVBoxLayout()
    self.memVBox.addLayout(self.memLabel)
    self.memVBox.addLayout(self.memFindHBox)
    self.memVBox.addWidget(self.memebrs)

    self.memGrp = QGroupBox()
    self.memGrp.setLayout(self.memVBox)

      
    ###FOR CONNECTIONS TO UI ELEMENTS###
    self.updateTable.clicked.connect(lambda: self.update(abbv))
    self.add.clicked.connect(lambda: self.addTask(abbv))

    ###FOR SETTING UP OVERALL LAYOUT###
    self.overall = QVBoxLayout()
    self.overall.addWidget(self.ganttGrp)
    self.overall.addWidget(self.memGrp)
    self.setLayout(self.overall)

  ### FUNCTIONS FOR SIGNALS AND SLOTS###
  def addTask(self, abbv):
    self.gantt.clear()
    task = self.taskInput.text()
    start = self.start.text()
    end = self.end.text()

    newTask(abbv, task, start, end)

    tasksList = fetchTasks(abbv)

    # setting items to populate table
    row = 0
    column = 0

    for task in tasksList:
      # extracting the 3 data items to be displayed for each item
      task = task[0]
      start = start[1]
      end = [2]

      # setting data items into 3 columns per row
      self.gantt.setItem(row, column, QTableWidgetItem(task))
      self.gantt.setItem(row, column + 1, QTableWidgetItem(start))
      self.gantt.setItem(row, column + 2, QTableWidgetItem(end))

      # adding one more row and resetting column back to 0
      row = +1
      column = 0

  def update(self, abbv):
    # to get the row count and column count
    model = self.gantt.model()
    rowCount = model.rowCount()
    columnCount = model.columnCount()

    # empty array to be passed into function
    dataset = []

    # loop to loop through all data in the table
    for row in range(rowCount):
      task = None
      start = None
      end = None

      # to indicate which column data is being accessed now
      columnNo = 0
      for column in range(columnCount):
        # get index of the cell being referred to and data
        index = model.index(row, columnNo)
        # model.data() returns an object, so string conversion is needed
        cellData = str(model.data(index).toString())

        # if loop to generate key value pairs to be appended to
        # fit into mongodb update operator
        if columnNo == 0:
          task = cellData
        elif columnNo == 1:
          start = cellData
        elif columnNo == 2:
          end = cellData
        else:
          pass

        # to move up by one column for indexing
      columnNo += 1

      # to set the dictionary to take in the data and the
      # key value pairs expected
      rowData = {"task": task, "start": start, "end": end}

      # To append disctionary into list
      dataset.append(rowData)

    updateGantt(abbv, dataset)
