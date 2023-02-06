from PyQt5.QtCore    import Qt, pyqtSignal
from PyQt5.QtGui     import QPalette, QColor, QBrush, QFont, QLinearGradient
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QDockWidget
from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout, QAction, QStyleFactory, QAbstractItemView
from PyQt5.QtWidgets import QGroupBox, QStackedWidget, QTableWidget, QTableWidgetItem, QHeaderView
from PyQt5.QtWidgets import QLabel, QLineEdit, QPushButton

from proj_window import ProjWindow

import sys
sys.path.insert(0, "../API_Scripts")

from mongoApi import fetchDetails, newProject


class MainWindow(QMainWindow):
    #signal for window to prep to emit
    submitData = pyqtSignal(str,str)

    def __init__ (self):
        QMainWindow.__init__(self)

        self.setWindowTitle("Project List")

        #positioning of window
        #positioning of window
        WinLeft = 100
        WinTop = 100

        #size of window
        WinWidth = 1500
        WinHeight = 800
        self.setGeometry(WinLeft, WinTop, WinWidth, WinHeight)

        #remove oddities
        self.setStyle(QStyleFactory.create("Cleanlooks"))

        #styling central widget
        self.setStyleSheet(
            "background-color: turquoise;"
            "padding: 0;"
            "margin: 0;"
        )

        #buttons creation
        #all will be labels that act like buttons
        lblPalette = QPalette()
        lblBrush = QBrush(QColor(255,255,255))
        lblBrush.setStyle(Qt.SolidPattern)
        lblPalette.setBrush(QPalette.Disabled, QPalette.Window, lblBrush)

        navLbl = QFont()
        navLbl.setFamily("Calibri Light")
        navLbl.setPointSize(20)

        #nav labels
        self.projectsLabel = QLabel("Projects")
        self.projectsLabel.setPalette(lblPalette)
        self.projectsLabel.setFont(navLbl)
        self.projectsLabel.setAutoFillBackground(False)

        self.myissuesLabel = QLabel("My Issues")
        self.myissuesLabel.setPalette(lblPalette)
        self.myissuesLabel.setFont(navLbl)
        self.myissuesLabel.setAutoFillBackground(False)

        #welcome user creation
        #uses label buttons' palette and font
        self.welcomeLabel = QLabel("Welcome user!")
        self.welcomeLabel.setPalette(lblPalette)
        self.welcomeLabel.setFont(navLbl)

        #setting up nav bar
        self.welcomeLabel.setAlignment(Qt.AlignLeft)
        self.projectsLabel.setAlignment(Qt.AlignRight)
        self.myissuesLabel.setAlignment(Qt.AlignRight)

        self.welcomeLabel.setStyleSheet(
            "margin-left: 30px;"
            "padding: 30px 0;"
        )

        self.projectsLabel.setStyleSheet(
            "margin-right: 30px;"
            "padding: 30px 0;"
        )

        self.myissuesLabel.setStyleSheet(
            "margin-right: 30px;"
            "padding: 30px 0;"
        )

        #navbar layout to be top of the window
        navHBox = QHBoxLayout()
        navHBox.addWidget(self.welcomeLabel)
        navHBox.addStretch()
        navHBox.addWidget(self.projectsLabel)
        navHBox.addWidget(self.myissuesLabel)

        #setting up project listing page
        #creating table widget of projects
        self.projectsTable = QTableWidget()
        self.projectsTable.setStyleSheet(
        "background-color: white;"
        "color: black;"
        "font-family: calibri-light;"
        "font-size: 20px;"
        )


        projectsList = fetchDetails()

        #setting the number of rows needed for table
        rowCount = len(projectsList)
        self.projectsTable.setRowCount(rowCount)
        self.projectsTable.setColumnCount(3)

        # set stretch for all columns
        header = self.projectsTable.horizontalHeader()       
        header.setSectionResizeMode(0, QHeaderView.Stretch)
        header.setSectionResizeMode(1, QHeaderView.Stretch)
        header.setSectionResizeMode(2, QHeaderView.Stretch)

        #remove vertical headers
        self.projectsTable.verticalHeader().hide()

        #set horizontal headers
        headers = ["Project Title", "Project Abbreviation", "Project Code"]
        self.projectsTable.setHorizontalHeaderLabels(headers)

        #remove vertical scroll bar
        self.projectsTable.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        #disable item editting function
        self.projectsTable.setEditTriggers(QAbstractItemView.NoEditTriggers)

        #selection behaviour changes from cell to row
        self.projectsTable.setSelectionBehavior(QAbstractItemView.SelectRows)

        #setting items to populate table
        #3 columns (Title), (Abbreviation), (Code)
        row = 0
        column = 0

        for proj in projectsList:

            #extracting the 3 data items to be displayed for each item
            title = proj[0]
            abbv = proj[1]
            code = proj[2]

            #setting data items into 3 columns per row
            self.projectsTable.setItem(row, column, QTableWidgetItem(title))
            self.projectsTable.setItem(row, column + 1, QTableWidgetItem(abbv))
            self.projectsTable.setItem(row, column + 2, QTableWidgetItem(code))

            #adding one more row and resetting column back to 0
            row += 1
            column = 0

        self.projectsTable.clicked.connect(self.openProj)

        #setting up new project side bar
        titleLbl = QFont()
        titleLbl.setFamily("Calibri Light")
        titleLbl.setPointSize(20)

        #Title of the side bar
        self.titleDisplay = QLabel()
        self.titleDisplay.setPalette(lblPalette)
        self.titleDisplay.setFont(titleLbl)
        self.titleDisplay.setAutoFillBackground(False)
        self.titleDisplay.setText("Create a new project")
        self.titleDisplay.setStyleSheet(
            "color: black;"
            "font-weight: bold;"
        )


        #Title, Abbv and Code line edits
        self.titleFill = QLineEdit()
        self.titleFill.setPlaceholderText("Project Title")

        self.abbvFill = QLineEdit()
        self.abbvFill.setPlaceholderText("Project Abbreviation")

        self.codeFill = QLineEdit()
        self.codeFill.setPlaceholderText("Project Code")

        self.titleFill.setStyleSheet(
            "background-color: white;"
            "color: black;"
            "border: 2px solid white;"
            "font-size: 20px;"
            "height: 30px;"
            "width: 500;"
        )

        self.abbvFill.setStyleSheet(
            "background-color: white;"
            "color: black;"
            "border: 2px solid white;"
            "font-size: 20px;"
            "height: 30px;"
            "width: 500;"
        )

        self.codeFill.setStyleSheet(
            "background-color: white;"
            "color: black;"
            "border: 2px solid white;"
            "font-size: 20px;"
            "height: 30px;"
            "width: 500;"
        )

        #label for showing up when fills are not filled properly
        warningPalette = QPalette()
        warningbrush = QBrush(QColor(255,0,0))
        warningbrush.setStyle(Qt.SolidPattern)
        warningPalette.setBrush(QPalette.Disabled, QPalette.Window, warningbrush)

        warningFont = QFont()
        warningFont.setFamily("Calibri Light")
        warningFont.setPointSize(10)

        self.warningLbl = QLabel()
        self.warningLbl.setPalette(warningPalette)
        self.warningLbl.setFont(warningFont)
        self.warningLbl.setAutoFillBackground(False)
        self.warningLbl.setText("")
        self.warningLbl.setStyleSheet(
            "font-weight: bold;"
            "color: red;"
        )

        #Ok and cancel buttons
        self.okButton = QPushButton("Ok")
        self.okButton.setStyleSheet(
            "background-color: green;"
            "color: white;"
            "border: 2px solid white;"
            "font-size: 20px;"
            "height: 30px;"
            "width: 100;"
        )

        self.cancelButton = QPushButton("Cancel")
        self.cancelButton.setStyleSheet(
            "background-color: red;"
            "color: white;"
            "border: 2px solid white;"
            "font-size: 20px;"
            "height: 30px;"
            "width: 100;"
        )

        #box for label so it does nto stretch and site in the center
        lblHBox = QHBoxLayout()
        lblHBox.addStretch()
        lblHBox.addWidget(self.titleDisplay)
        lblHBox.addStretch()

        #box for fields so they do not stretch
        fillVBox = QVBoxLayout()
        fillVBox.addWidget(self.titleFill)
        fillVBox.addWidget(self.abbvFill)
        fillVBox.addWidget(self.codeFill)

        fillHBox = QHBoxLayout()
        fillHBox.addStretch()
        fillHBox.addLayout(fillVBox)
        fillHBox.addStretch()

        #box for buttons so they do not stretch all the way
        btnHBox = QHBoxLayout()
        btnHBox.addStretch()
        btnHBox.addWidget(self.okButton)
        btnHBox.addStretch()
        btnHBox.addWidget(self.cancelButton)
        btnHBox.addStretch()

        #box for warning label
        warnHBOX = QHBoxLayout()
        warnHBOX.addStretch()
        warnHBOX.addWidget(self.warningLbl)
        warnHBOX.addStretch()

        #setting up side box for new project
        addVBox = QVBoxLayout()
        addVBox.addLayout(lblHBox)
        addVBox.addStretch()
        addVBox.addLayout(fillHBox)
        addVBox.addStretch()
        addVBox.addLayout(warnHBOX)
        addVBox.addStretch()
        addVBox.addLayout(btnHBox)
        addVBox.addStretch()

        #setting up horizontal box for projectsTable and addVBox
        mainHBox = QHBoxLayout()
        mainHBox.addWidget(self.projectsTable)
        mainHBox.addLayout(addVBox)

        #putting together all UI elements
        self.window = QVBoxLayout()
        self.window.addLayout(navHBox)
        self.window.addLayout(mainHBox)

        #set layout
        self.setCentralWidget(QWidget(self))
        self.centralWidget().setLayout(self.window)

        #function calls
        #method call
        self.okButton.clicked.connect(self.upload_data)
        self.cancelButton.clicked.connect(self.clearFills)

    #functions to send into API
    def upload_data(self):
        title = self.titleFill.text()
        abbv = self.abbvFill.text()
        code = self.codeFill.text()

        if title and abbv and code:
            newProject(title, abbv, code)
            self.titleFill.clear()
            self.abbvFill.clear()
            self.codeFill.clear()
            self.warningLbl.setText("New project created.")
            self.update()
        else:
            self.warningLbl.setText("Please fill in all required information correctly.")

    def clearFills(self):
        self.titleFill.clear()
        self.abbvFill.clear()
        self.codeFill.clear()

    #function to "refresh" table
    def update(self):
        self.projectsTable.clear()

        projectsList = fetchDetails()

        #setting items to populate table
        #3 columns (Title), (Abbreviation), (Code)
        row = 0
        column = 0
        
        for proj in projectsList:

            #extracting the 3 data items to be displayed for each item
            title = proj[0]
            abbv = proj[1]
            code = proj[2]

            #setting data items into 3 columns per row
            self.projectsTable.setItem(row, column, QTableWidgetItem(title))
            self.projectsTable.setItem(row, column + 1, QTableWidgetItem(abbv))
            self.projectsTable.setItem(row, column + 2, QTableWidgetItem(code))

            #adding one more row and resetting column back to 0
            row += 1
            column = 0

    #for opeening proj_window after selection
    def openProj(self):
        items = []
        for item in self.projectsTable.selectedItems():
            items.append(item.text())
        title = items[0]
        abbv = items[1]

        #to emit signal to pass data
        self.submitData.emit(title,abbv)

        #to open a new window by passing in the abbv
        self.window = ProjWindow(title,abbv)
        self.window.show()
        

if __name__ == "__main__":
    MainEventThred = QApplication([])

    MainApplication = MainWindow()
    MainApplication.show()

    MainEventThred.exec()

