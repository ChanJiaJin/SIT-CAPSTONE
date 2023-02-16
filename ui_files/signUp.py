from PyQt5.QtCore    import Qt
from PyQt5.QtGui     import QPalette, QColor, QBrush, QFont, QLinearGradient
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QDockWidget
from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout, QAction, QStyleFactory
from PyQt5.QtWidgets import QGroupBox, QLabel, QLineEdit, QPushButton

import time

import sys
sys.path.insert(0, "../API_Scripts")
from mongoApi import addUser

class signUp(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        #/-----------WINDOW SETUP-----------/#

        #positioning of window
        #positioning of window
        WinLeft = 100
        WinTop = 100

        #size of window
        WinWidth = 500
        WinHeight = 500
        self.setGeometry(WinLeft, WinTop, WinWidth, WinHeight)

        #window title
        self.setWindowTitle("Sign Up")

        #remove oddities
        self.setStyle(QStyleFactory.create("Cleanlooks"))

        #styling central widget
        self.setStyleSheet(
            "background-color: #121212;"
            "padding: 0;"
            "margin: 0;"
        )

        #/-----------WIDGETS SETUP-----------/#
        #page title setup
        titlePalette = QPalette()
        titleBrush = QBrush(QColor(255,255,255))
        titleBrush.setStyle(Qt.SolidPattern)
        titlePalette.setBrush(QPalette.Disabled, QPalette.Window, titleBrush)

        titleFont = QFont()
        titleFont.setFamily("Calibri Light")
        titleFont.setPointSize(30)

        #title label
        self.titleLabel = QLabel("Sign Up")
        self.titleLabel.setPalette(titlePalette)
        self.titleLabel.setFont(titleFont)
        self.titleLabel.setAutoFillBackground(False)
        self.titleLabel.setAlignment(Qt.AlignCenter)
        self.titleLabel.setStyleSheet(
            "font-weight: bold;"
            "color: white;"
            "text-align: center;"
        )

        #instrutions labels setup
        insPalette = QPalette()
        insBrush = QBrush(QColor(255,255,255))
        insBrush.setStyle(Qt.SolidPattern)
        insPalette.setBrush(QPalette.Disabled, QPalette.Window, insBrush)

        insFont = QFont()
        insFont.setFamily("Calibri Light")
        insFont.setPointSize(20)

        #instrutions label
        self.loginLabel = QLabel("Enter your login details")
        self.loginLabel.setPalette(insPalette)
        self.loginLabel.setFont(insFont)
        self.loginLabel.setAutoFillBackground(False)
        self.loginLabel.setAlignment(Qt.AlignCenter)
        self.loginLabel.setStyleSheet(
            "font-weight: bold;"
            "color: white;"
            "text-align: center;"
        )

        self.persLabel = QLabel("Enter your company details")
        self.persLabel.setPalette(insPalette)
        self.persLabel.setFont(insFont)
        self.persLabel.setAutoFillBackground(False)
        self.persLabel.setAlignment(Qt.AlignCenter)
        self.persLabel.setStyleSheet(
            "font-weight: bold;"
            "color: white;"
            "text-align: center;"
        )

        #input fields setup
        self.email = QLineEdit()
        self.email.setPlaceholderText("Email")
        self.email.setStyleSheet("""
        QLineEdit{
        background-color: white;
        color: black;
        width: 300px;
        height: 30px;
        font-size: 20px;
        }
        """)

        self.password = QLineEdit()
        self.password.setPlaceholderText("password")
        self.password.setEchoMode(QLineEdit.Password)
        self.password.setStyleSheet("""
        QLineEdit{
        background-color: white;
        color: black;
        width: 300px;
        height: 30px;
        font-size: 20px;
        }
        """)

        self.confirm = QLineEdit()
        self.confirm.setPlaceholderText("Re-enter password")
        self.confirm.setEchoMode(QLineEdit.Password)
        self.confirm.setStyleSheet("""
        QLineEdit{
        background-color: white;
        color: black;
        width: 300px;
        height: 30px;
        font-size: 20px;
        }
        """)

        self.name = QLineEdit()
        self.name.setPlaceholderText("Name")
        self.name.setStyleSheet("""
        QLineEdit{
        background-color: white;
        color: black;
        width: 300px;
        height: 30px;
        font-size: 20px;
        }
        """)

        self.department = QLineEdit()
        self.department.setPlaceholderText("Department")
        self.department.setStyleSheet("""
        QLineEdit{
        background-color: white;
        color: black;
        width: 300px;
        height: 30px;
        font-size: 20px;
        }
        """)
        
        self.discipline = QLineEdit()
        self.discipline.setPlaceholderText("Discipline")
        self.discipline.setStyleSheet("""
        QLineEdit{
        background-color: white;
        color: black;
        width: 300px;
        height: 30px;
        font-size: 20px;
        }
        """)

        #setting up buttons
        self.apply = QPushButton("Sign Up")
        self.apply.setStyleSheet(
            "background-color: green;"
            "color: white;"
            "border: 2px solid white;"
            "font-size: 20px;"
            "height: 30px;"
            "width: 100;"
        )

        self.cancel = QPushButton("Cancel")
        self.cancel.setStyleSheet(
            "background-color: red;"
            "color: white;"
            "border: 2px solid white;"
            "font-size: 20px;"
            "height: 30px;"
            "width: 100;"
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

        #/-----------OVERALL SETUP-----------/#
        #all major containers set up
        self.loginStack = QVBoxLayout()
        self.loginStack.addWidget(self.loginLabel)
        self.loginStack.addStretch()
        self.loginStack.addWidget(self.email)
        self.loginStack.addStretch()
        self.loginStack.addWidget(self.password)
        self.loginStack.addStretch()
        self.loginStack.addWidget(self.confirm)

        self.detailsStack = QVBoxLayout()
        self.detailsStack.addWidget(self.persLabel)
        self.detailsStack.addStretch()
        self.detailsStack.addWidget(self.name)
        self.detailsStack.addStretch()
        self.detailsStack.addWidget(self.department)
        self.detailsStack.addStretch()
        self.detailsStack.addWidget(self.discipline)

        self.warningStack = QHBoxLayout()
        self.warningStack.addStretch()
        self.warningStack.addWidget(self.warningLbl)
        self.warningStack.addStretch()

        self.buttons = QHBoxLayout()
        self.buttons.addStretch()
        self.buttons.addWidget(self.cancel)
        self.buttons.addStretch()
        self.buttons.addWidget(self.apply)
        self.buttons.addStretch()

        #horizontal box setup for login and details
        self.loginHbox = QHBoxLayout()
        self.loginHbox.addStretch()
        self.loginHbox.addLayout(self.loginStack)
        self.loginHbox.addStretch()

        self.detailsHBox = QHBoxLayout()
        self.detailsHBox.addStretch()
        self.detailsHBox.addLayout(self.detailsStack)
        self.detailsHBox.addStretch()

        #overall main container
        self.main = QVBoxLayout()
        self.main.addStretch()
        self.main.addLayout(self.loginHbox)
        self.main.addStretch()
        self.main.addLayout(self.detailsHBox)
        self.main.addStretch()
        self.main.addLayout(self.warningStack)
        self.main.addStretch()
        self.main.addLayout(self.buttons)
        self.main.addStretch()


        #/-----------MAIN WINDOW-----------/#
        self.setCentralWidget(QWidget(self))
        self.centralWidget().setLayout(self.main)

        #/-----------BUTTON CONNECTION-----------/#
        self.apply.clicked.connect(self.newUser)

    
    #/-----------API FUNCTIONS-----------/#
    #functions to send into API
    def newUser(self):
        email = self.email.text()
        password = self.password.text()
        confirm = self.confirm.text()
        name = self.name.text()
        department = self.department.text()
        discipline = self.discipline.text()

        if email and password and confirm and name and department and discipline:
            if password == confirm:
                addUser(name, department, discipline, email, password)
                self.titleFill.clear()
                self.warningLbl.setText("Account created, please login.")
                time.sleep(3)
            else:
                self.warningLbl.setText("Passwords do not match.")
        else:
            self.warningLbl.setText("Please fill in all information required.")



if __name__ == "__main__":
    MainEventThred = QApplication([])
    
    MainApplication = signUp()
    MainApplication.show()

    MainEventThred.exec()