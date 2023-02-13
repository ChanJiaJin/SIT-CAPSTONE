from PyQt5.QtCore    import Qt
from PyQt5.QtGui     import QPalette, QColor, QBrush, QFont, QLinearGradient
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QDockWidget
from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout, QAction, QStyleFactory
from PyQt5.QtWidgets import QGroupBox, QLabel, QLineEdit, QPushButton


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
        insPalette.setStyle(Qt.SolidPattern)
        insPalette.setBrush(QPalette.Disabled, QPalette.Window, insPalette)

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

