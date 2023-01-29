from PyQt5.QtCore    import Qt
from PyQt5.QtGui     import QPalette, QColor, QBrush, QFont, QLinearGradient
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QDockWidget
from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout, QAction, QStyleFactory
from PyQt5.QtWidgets import QGroupBox, QStackedWidget
from PyQt5.QtWidgets import QLabel, QLineEdit, QPushButton

from proj_info import ProjectInfo

import sys
sys.path.insert(0, "../API_scripts")


class ProjWindow(QMainWindow):
    def __init__(self, title,abbv):
        QMainWindow.__init__(self)

        #positioning of window
        #positioning of window
        WinLeft = 100
        WinTop = 100

        #size of window
        WinWidth = 1800
        WinHeight = 1000
        self.setGeometry(WinLeft, WinTop, WinWidth, WinHeight)

        #window title
        self.setWindowTitle(title)

        #remove oddities
        self.setStyle(QStyleFactory.create("Cleanlooks"))

        #styling central widget
        self.setStyleSheet(
            "background-color: #121212;"
            "padding: 0;"
            "margin: 0;"
        )

        #buttons creation
        #all will be labels that act like buttons
        lblPalette = QPalette()
        lblBrush = QBrush(QColor(255,255,255))
        lblBrush.setStyle(Qt.SolidPattern)
        lblPalette.setBrush(QPalette.Disabled, QPalette.Window, lblBrush)

        abbvLbl = QFont()
        abbvLbl.setFamily("Calibri Light")
        abbvLbl.setPointSize(30)

        #title label
        self.titleLabel = QLabel(abbv)
        self.titleLabel.setPalette(lblPalette)
        self.titleLabel.setFont(abbvLbl)
        self.titleLabel.setAutoFillBackground(False)
        self.titleLabel.setAlignment(Qt.AlignCenter)
        self.titleLabel.setStyleSheet(
            "font-weight: bold;"
            "color: white;"
            "text-align: center;"
        )

        #side labels
        self.projDetails = QPushButton("Details")
        self.projDetails.setFlat(True)
        self.projDetails.setStyleSheet("""
            QPushButton {
                Background-color: none;
                color: white;
                border: none;
                font-size: 20px;
                height: 100%;
            }

            QPushButton:hover {
            background-color: #BB86FC;
            color: black;
            }
        """)

        self.issuesBoard = QPushButton("Issues Board")
        self.issuesBoard.setFlat(True)
        self.issuesBoard.setStyleSheet("""
            QPushButton {
                Background-color: none;
                color: white;
                border: none;
                font-size: 20px;
                height: 100%;
            }

            QPushButton:hover {
            background-color: #BB86FC;
            color: black;
            }
        """)

        self.docsList = QPushButton("Documentations")
        self.docsList.setFlat(True)
        self.docsList.setStyleSheet("""
            QPushButton {
                Background-color: none;
                color: white;
                border: none;
                font-size: 20px;
                height: 100%;
            }

            QPushButton:hover {
            background-color: #BB86FC;
            color: black;
            }
        """)

        self.ganttChart = QPushButton("Gantt Chart")
        self.ganttChart.setFlat(True)
        self.ganttChart.setStyleSheet("""
            QPushButton {
                Background-color: none;
                color: white;
                border: none;
                font-size: 20px;
                height: 100%;
            }

            QPushButton:hover {
            background-color: #BB86FC;
            color: black;
            }
        """)

        self.projSettings = QPushButton("Settings")
        self.projSettings.setFlat(True)
        self.projSettings.setStyleSheet("""
            QPushButton {
                Background-color: none;
                color: white;
                border: none;
                font-size: 20px;
                height: 100%;
            }

            QPushButton:hover {
            background-color: #BB86FC;
            color: black;
            }
        """)

        #sideBar
        sideBar = QGroupBox()
        sideBar.setStyleSheet(
            "background-color: #1F1B24;"
        )

        sideVBox = QVBoxLayout()
        sideVBox.addStretch()
        sideVBox.addWidget(self.titleLabel)
        sideVBox.addStretch()
        sideVBox.addWidget(self.projDetails)
        sideVBox.addStretch()
        sideVBox.addWidget(self.issuesBoard)
        sideVBox.addStretch()
        sideVBox.addWidget(self.docsList)
        sideVBox.addStretch()
        sideVBox.addWidget(self.ganttChart)
        sideVBox.addStretch()
        sideVBox.addWidget(self.projSettings)
        sideVBox.addStretch()

        sideBar.setLayout(sideVBox)

        #stacked widget to swap UI when needed
        self.stackBox = QStackedWidget()
        self.stackBox.addWidget(ProjectInfo(abbv))
        
        self.stackBox.setCurrentIndex(0)

        #adding sidebar and stacked widget into HBOX
        self.mainHBox = QHBoxLayout()
        self.mainHBox.addWidget(sideBar)
        self.mainHBox.addWidget(self.stackBox)

        self.setCentralWidget(QWidget(self))
        self.centralWidget().setLayout(self.mainHBox)


if __name__ == "__main__":
    MainEventThred = QApplication([])
    
    MainApplication = ProjWindow
    MainApplication.show()

    MainEventThred.exec()


        