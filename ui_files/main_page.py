from PyQt5.QtCore    import Qt
from PyQt5.QtGui     import QPalette, QColor, QBrush, QFont, QLinearGradient
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QDockWidget
from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout, QAction, QStyleFactory
from PyQt5.QtWidgets import QGroupBox, QStackedWidget
from PyQt5.QtWidgets import QLabel, QLineEdit, QPushButton

from proj_page import projectsStack
from add_project import AddProjectWindow

import sys
sys.path.insert(0, "../API_scripts")


class CenterPanel(QWidget):
    def __init__(self, parent):
        QWidget.__init__(self)

        #buttons creation
        #all will be labels that act like buttons
        lblPalette = QPalette()
        lblBrush = QBrush(QColor(255,255,255))
        lblBrush.setStyle(Qt.SolidPattern)
        lblPalette.setBrush(QPalette.Disabled, QPalette.Window, lblBrush)

        navLbl = QFont()
        navLbl.setFamily("Calibri Light")
        navLbl.setPointSize(20)

        sideLbl = QFont()
        sideLbl.setFamily("Calibri Light")
        sideLbl.setPointSize(15)

        #nav labels
        self.projectsLabel = QLabel("Projects")
        self.projectsLabel.setPalette(lblPalette)
        self.projectsLabel.setFont(navLbl)
        self.projectsLabel.setAutoFillBackground(False)

        self.myissuesLabel = QLabel("My Issues")
        self.myissuesLabel.setPalette(lblPalette)
        self.myissuesLabel.setFont(navLbl)
        self.myissuesLabel.setAutoFillBackground(False)

        #side labels
        self.projDetailsLabel = QLabel("Details")
        self.projDetailsLabel.setPalette(lblPalette)
        self.projDetailsLabel.setFont(sideLbl)
        self.projDetailsLabel.setAutoFillBackground(False)

        self.flowLabel = QLabel("Work Flow")
        self.flowLabel.setPalette(lblPalette)
        self.flowLabel.setFont(sideLbl)
        self.flowLabel.setAutoFillBackground(False)

        self.issuesBoardLabel = QLabel("Issues Board")
        self.issuesBoardLabel.setPalette(lblPalette)
        self.issuesBoardLabel.setFont(sideLbl)
        self.issuesBoardLabel.setAutoFillBackground(False)

        self.docsListLabel = QLabel("Documentations")
        self.docsListLabel.setPalette(lblPalette)
        self.docsListLabel.setFont(sideLbl)
        self.docsListLabel.setAutoFillBackground(False)

        self.ganttChartLabel = QLabel("Gantt Chart")
        self.ganttChartLabel.setPalette(lblPalette)
        self.ganttChartLabel.setFont(sideLbl)
        self.ganttChartLabel.setAutoFillBackground(False)

        self.membersLabel = QLabel("Members")
        self.membersLabel.setPalette(lblPalette)
        self.membersLabel.setFont(sideLbl)
        self.membersLabel.setAutoFillBackground(False)

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

        navHBox = QHBoxLayout()
        navHBox.addWidget(self.welcomeLabel)
        navHBox.addStretch()
        navHBox.addWidget(self.projectsLabel)
        navHBox.addWidget(self.myissuesLabel)

        #sideBar
        sideBar = QGroupBox()
        sideBar.setStyleSheet(
            "background-color: white;"
        )

        sideVBox = QVBoxLayout()
        sideVBox.addStretch()
        sideVBox.addWidget(self.projDetailsLabel)
        sideVBox.addStretch()
        sideVBox.addWidget(self.flowLabel)
        sideVBox.addStretch()
        sideVBox.addWidget(self.issuesBoardLabel)
        sideVBox.addStretch()
        sideVBox.addWidget(self.docsListLabel)
        sideVBox.addStretch()
        sideVBox.addWidget(self.ganttChartLabel)
        sideVBox.addStretch()
        sideVBox.addWidget(self.membersLabel)
        sideVBox.addStretch()

        sideBar.setLayout(sideVBox)

        #stacked widget to swap UI when needed

        #stackBox.addWidget(projectsStack(parent))


        #stackBox.setCurrentIndex(0)

        #adding in new project button
        self.addProj = QPushButton("New Project")
        self.addProj.setStyleSheet(
            "background-color: white;"
            "color: black;"
            "font-size: 25px;"
            "height: 60px;"
            "width: 300px;"
        )

        #proj button layout
        newHBox = QHBoxLayout()
        newHBox.addStretch()
        newHBox.addWidget(self.addProj)
        newHBox.addStretch()

        #adding stacked widget and button together
        rightVBox = QVBoxLayout()
        #rightVBox.addWidget(stackBox)
        rightVBox.addLayout(newHBox)

        #adding sidebar and stacked widget into HBOX
        mainHBox = QHBoxLayout()
        mainHBox.addWidget(sideBar)
        mainHBox.addLayout(rightVBox)

        #laying QVBox to stack up the navbar on the rest
        mainVBox = QVBoxLayout()
        mainVBox.addLayout(navHBox)
        mainVBox.addLayout(mainHBox)

        self.setLayout(mainVBox)

        #method call
        self.addProj.clicked.connect(self.openWindow)

    #function to open window
    def openWindow(self):
        self.window = QMainWindow()
        self.ui = AddProjectWindow
        self.ui.__init__(self.window)
        self.window.show()

#main window to encompass all elements set up
class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        self.setWindowTitle("App name")

        #positioning of window
        #positioning of window
        WinLeft = 100
        WinTop = 100

        #size of window
        WinWidth = 1800
        WinHeight = 1000
        self.setGeometry(WinLeft, WinTop, WinWidth, WinHeight)

        #setting central widget > CenterPanel() which was just made above
        self.CenterPane = CenterPanel(self)
        self.setCentralWidget(self.CenterPane)

        #remove oddities
        self.setStyle(QStyleFactory.create("Cleanlooks"))

        #styling central widget
        self.setStyleSheet(
            "background-color: turquoise;"
            "padding: 0;"
            "margin: 0;"
        )

if __name__ == "__main__":
    MainEventThred = QApplication([])

    MainApplication = MainWindow()
    MainApplication.show()

    MainEventThred.exec()


        