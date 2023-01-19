from PyQt5.QtCore    import Qt
from PyQt5.QtGui     import QPalette, QColor, QBrush, QFont, QLinearGradient
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QDockWidget
from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout, QAction, QStyleFactory
from PyQt5.QtWidgets import QGroupBox, QStackedWidget
from PyQt5.QtWidgets import QLabel, QLineEdit, QPushButton

import sys
sys.path.insert(0, "../API_scripts")
from mongoApi import newProject


class AddProject(QWidget):
    def __init__(self, parent):

        QWidget.__init__(self, parent)

        lblPalette = QPalette()
        lblBrush = QBrush(QColor(255,255,255))
        lblBrush.setStyle(Qt.SolidPattern)
        lblPalette.setBrush(QPalette.Disabled, QPalette.Window, lblBrush)

        titleLbl = QFont()
        titleLbl.setFamily("Calibri Light")
        titleLbl.setPointSize(30)

        #Title of the page
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
            "width: 500px;"
        )

        self.abbvFill.setStyleSheet(
            "background-color: white;"
            "color: black;"
            "border: 2px solid white;"
            "font-size: 20px;"
            "height: 30px;"
            "width: 500px;"
        )

        self.codeFill.setStyleSheet(
            "background-color: white;"
            "color: black;"
            "border: 2px solid white;"
            "font-size: 20px;"
            "height: 30px;"
            "width: 500px;"
        )

        #label for showing up when fills are not filled properly
        warningPalette = QPalette()
        warningbrush = QBrush(QColor(255,0,0))
        warningbrush.setStyle(Qt.SolidPattern)
        warningPalette.setBrush(QPalette.Disabled, QPalette.Window, warningbrush)

        warningFont = QFont()
        warningFont.setFamily("Calibri Light")
        warningFont.setPointSize(20)

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
            "width: 100px;"
        )

        self.cancelButton = QPushButton("Cancel")
        self.cancelButton.setStyleSheet(
            "background-color: red;"
            "color: white;"
            "border: 2px solid white;"
            "font-size: 20px;"
            "height: 30px;"
            "width: 100px;"
        )

        #layout setting
        titleHBox = QHBoxLayout()
        titleHBox.addWidget(self.titleDisplay)
        titleHBox.addStretch()

        lineVBox = QVBoxLayout()
        lineVBox.addWidget(self.titleFill)
        lineVBox.addWidget(self.abbvFill)
        lineVBox.addWidget(self.codeFill)

        lineHBox = QHBoxLayout()
        lineHBox.addStretch()
        lineHBox.addLayout(lineVBox)
        lineHBox.addStretch()

        warningHBox = QHBoxLayout()
        warningHBox.addStretch()
        warningHBox.addWidget(self.warningLbl)
        warningHBox.addStretch()

        buttonHBox = QHBoxLayout()
        buttonHBox.addStretch()
        buttonHBox.addWidget(self.cancelButton)
        buttonHBox.addStretch()
        buttonHBox.addWidget(self.okButton)
        buttonHBox.addStretch()

        mainVBox = QVBoxLayout()
        mainVBox.addLayout(titleHBox)
        mainVBox.addStretch()
        mainVBox.addLayout(lineHBox)
        mainVBox.addStretch()
        mainVBox.addLayout(warningHBox)
        mainVBox.addStretch()
        mainVBox.addLayout(buttonHBox)
        mainVBox.addStretch()


        #set layout in MainWindow
        self.setLayout(mainVBox)

        #method call
        self.okButton.clicked.connect(self.upload_data)
        self.cancelButton.clicked.connect(self.closeWindow)

    #functins to send into API
    def upload_data(self):
        title = self.titleFill.text()
        abbv = self.abbvFill.text()
        code = self.codeFill.text()

        if title and abbv and code:
            print(title)
            print(abbv)
            print(code)
            newProject(title, abbv, code)
            self.parent().close()
        else:
            self.warningLbl.setText("Please fill in all required information correctly.")

    def closeWindow(self):
        self.parent().close()


class AddProjectWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        self.setWindowTitle("Add new project")

        #positioning of window
        WinLeft = 200
        WinTop = 200

        #size of window
        WinWidth = 800
        WinHeight = 500
        self.setGeometry(WinLeft, WinTop, WinWidth, WinHeight)

        #setting max window size
        self.setMaximumSize(WinWidth, WinHeight)

        #setting min window size
        self.setMinimumSize(WinWidth, WinHeight)

        #setting central widget > AddProject
        self.CenterPane = AddProject(self)
        self.setCentralWidget(self.CenterPane)

        #remove oddities
        self.setStyle(QStyleFactory.create("Cleanlooks"))

        #style central widget
        self.setStyleSheet(
            "background-color: turquoise;"
        )

if __name__ == "__main__":
    MainEventThred = QApplication([])

    MainApplication = AddProjectWindow()
    MainApplication.show()

    MainEventThred.exec()




        
