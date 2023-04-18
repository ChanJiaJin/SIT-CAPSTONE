from PyQt5.QtCore    import Qt, QFile
from PyQt5.QtGui     import QPalette, QColor, QBrush, QFont, QLinearGradient
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QDockWidget
from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout, QAction, QStyleFactory
from PyQt5.QtWidgets import QLabel, QLineEdit, QPushButton

from sign_up import signUp
from main_window import MainWindow

import time

import sys
sys.path.insert(0, "../API_Scripts")
from mongoApi import verUser

class CenterPanel(QWidget):
    def __init__(self, parent):
        QWidget.__init__(self)

        #setting palette and brush for label
        lblPalette = QPalette()
        lblBrush = QBrush(QColor(0,127,255))
        lblBrush.setStyle(Qt.SolidPattern)
        lblPalette.setBrush(QPalette.Disabled, QPalette.Window, lblBrush)

        #setting font family and size for label
        lblFont = QFont()
        lblFont.setFamily("Calibri Light")
        lblFont.setPointSize(40)

        #create title label
        self.lblDisplay = QLabel()
        self.lblDisplay.setPalette(lblPalette)
        self.lblDisplay.setFont(lblFont)
        self.lblDisplay.setAutoFillBackground(False)
        self.lblDisplay.setText("Hello and good day. Please sign in.")
        self.lblDisplay.setStyleSheet(
            "color: white;"
            "font-weight: bold;"
        )

        #create warning label
        warningFont = QFont()
        warningFont.setFamily("Calibri Light")
        warningFont.setPointSize(15)

        self.warning = QLabel()
        self.warning.setPalette(lblPalette)
        self.warning.setFont(warningFont)
        self.warning.setAutoFillBackground(False)
        self.warning.setText("")

        #create sign in label and font family and size
        signUpFont = QFont()
        signUpFont.setFamily("calibri Light")
        signUpFont.setPointSize(15)

        self.signUp = QPushButton("No account? Sign up here.")
        self.signUp.setStyleSheet(
            """
                QPushButton {
                    color: white;
                    border-radius: 10px;
                    font-size: 25px;
                    height: 50px;
                    width: 500px;
                }

                QPushButton:hover {
                    color: blue;
                }
            """
        )

        #create username and password fills
        self.usernameFill = QLineEdit()
        self.usernameFill.setPlaceholderText("Email")

        self.passwordFill = QLineEdit()
        self.passwordFill.setPlaceholderText("Password")
        self.passwordFill.setEchoMode(QLineEdit.Password)

        self.usernameFill.setStyleSheet(
            "background-color: white;"
            "color: black;"
            "border-radius: 10px;"
            "border: 2px solid white;"
            "font-size: 25px;"
            "height: 50px;"
            "width: 500px"
        )
        
        self.passwordFill.setStyleSheet(
            "background-color: white;"
            "color: black;"
            "border-radius: 10px;"
            "border: 2px solid white;"
            "font-size: 25px;"
            "height: 50px;"
            "width: 500px"
        )

        #button
        self.loginButton = QPushButton("Login")
        self.loginButton.setStyleSheet("""
                QPushButton {
                    background-color: white;
                    color: black;
                    border-radius: 10px;
                    font-size: 25px;
                    height: 50px;
                    width: 500px;
                }

                QPushButton:hover {
                    background-color: green;
                    color: white;
                }
            """
        )

        #add fields to their own respective HBoxes
        titleHBox = QHBoxLayout()
        titleHBox.addStretch()
        titleHBox.addWidget(self.lblDisplay)
        titleHBox.addStretch()
        titleHBox.setAlignment(Qt.AlignHCenter)

        userHBox = QHBoxLayout()
        userHBox.addStretch()
        userHBox.addWidget(self.usernameFill)
        userHBox.addStretch()
        userHBox.setAlignment(Qt.AlignHCenter)

        pwHBox = QHBoxLayout()
        pwHBox.addStretch()
        pwHBox.addWidget(self.passwordFill)
        pwHBox.addStretch()
        pwHBox.setAlignment(Qt.AlignHCenter)

        warningHBox = QHBoxLayout()
        warningHBox.addStretch()
        warningHBox.addWidget(self.warning)
        warningHBox.addStretch()
        warningHBox.setAlignment(Qt.AlignHCenter)
    
        loginBtnBox = QHBoxLayout()
        loginBtnBox.addWidget(self.loginButton)
        loginBtnBox.setAlignment(Qt.AlignHCenter)

        signUpBox = QHBoxLayout()
        signUpBox.addStretch()
        signUpBox.addWidget(self.signUp)
        signUpBox.addStretch()

        #adding all elements in a vertical box now
        VBox = QVBoxLayout()
        VBox.addStretch()
        VBox.addLayout(titleHBox)
        VBox.addStretch()
        VBox.addLayout(userHBox)
        VBox.addLayout(pwHBox)
        VBox.addStretch()
        VBox.addLayout(warningHBox)
        VBox.addStretch()
        VBox.addLayout(loginBtnBox)
        VBox.addStretch()
        VBox.addLayout(signUpBox)
        VBox.addStretch()
        VBox.setAlignment(Qt.AlignHCenter)

        #assigning layout to center pane QWidget
        self.setLayout(VBox)

        #functions calls
        self.loginButton.clicked.connect(self.login)
        self.signUp.clicked.connect(self.signUpCall)

    #for sign up of new user
    def signUpCall(self):
        self.window = signUp()
        self.window.show()

    #for loging in
    def login(self):
        check = True
        statement = ""
        email = self.usernameFill.text()
        password = self.passwordFill.text()

        #to check if any values are entered so the API does not
        #return error of out of range
        if email and password:
            confirmation = verUser(email, password, check, statement)
        
            #extract values from confirmation
            checkResult = confirmation[1]
            state = confirmation[0]

            #allow login or not
            if checkResult:
                self.warning.setText(state)
                self.warning.setStyleSheet(
                "color: green;"
                )

                time.sleep(3)

                self.window = MainWindow()
                self.window.show()
            else:
                self.warning.setText(state)
                self.warning.setStyleSheet(
                "color: red;"
                )
        else:
            self.warning.setText("Please enter login credentials.")
            self.warning.setStyleSheet(
                "color: red;"
            )


#main window to encompass all elements set up
class LoginWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        self.setWindowTitle("Login")

        #positioning of window
        WinLeft = 200
        WinTop = 200

        #size of window
        WinWidth = 500
        WinHeight = 500
        self.setGeometry(WinLeft, WinTop, WinWidth, WinHeight)

        #setting central widget > CenterPanel() which was just made above
        self.CenterPane = CenterPanel(self)
        self.setCentralWidget(self.CenterPane)

        #remove oddities
        self.setStyle(QStyleFactory.create("Cleanlooks"))

        #styling central widget
        self.setStyleSheet(
            "background-color: #121212;"
            "padding: 0;"
            "margin: 0;"
        )

if __name__ == "__main__":
    MainEventThred = QApplication([])

    MainApplication = LoginWindow()
    MainApplication.show()

    MainEventThred.exec()