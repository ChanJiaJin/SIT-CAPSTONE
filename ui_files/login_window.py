from PyQt5.QtCore    import Qt, QFile
from PyQt5.QtGui     import QPalette, QColor, QBrush, QFont, QLinearGradient
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QDockWidget
from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout, QAction, QStyleFactory
from PyQt5.QtWidgets import QLabel, QLineEdit, QPushButton

from signUp import signUp

import sys

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

        #create ttile label
        self.lblDisplay = QLabel()
        self.lblDisplay.setPalette(lblPalette)
        self.lblDisplay.setFont(lblFont)
        self.lblDisplay.setAutoFillBackground(False)
        self.lblDisplay.setText("Hello and good day. Please sign in.")
        self.lblDisplay.setStyleSheet(
            "color: white;"
            "font-weight: bold;"
        )

        #create sign in label and font family and size
        signUpFont = QFont()
        signUpFont.setFamily("calibri Light")
        signUpFont.setPointSize(15)

        self.signUp  = QLabel()
        self.signUp.setPalette(lblPalette)
        self.signUp.setFont(signUpFont)
        self.signUp.setAutoFillBackground(False)
        self.signUp.setText("No account? Sign up here.")
        self.signUp.setStyleSheet("""
            QLabel {
                Background-color: none;
                color: white;
            }

            QLabel:hover {
            color: #ADD8E6;
            }
        """
        )

        #create username and password fills
        self.usernameFill = QLineEdit()
        self.usernameFill.setPlaceholderText("Username or email")

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
        VBox.addLayout(loginBtnBox)
        VBox.addStretch()
        VBox.addLayout(signUpBox)
        VBox.addStretch()
        VBox.setAlignment(Qt.AlignHCenter)

        #assigning layout to center pane QWidget
        self.setLayout(VBox)

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