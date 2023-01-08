import sys
from PyQt5 import QtCore, QtGui, QtWidgets

#importing from currrent directory
from projects_page import Ui_projects_page as projPage

#importing from API_scripts folder
sys.path.append('../API_scripts')
from socket_funcs import closeWindow, createProject


class Ui_newProj_add_window(QtWidgets.QMainWindow):

    def setupUi(self, newProj_add_window):
        newProj_add_window.setObjectName("newProj_add_window")
        newProj_add_window.resize(500, 400)
        newProj_add_window.setMinimumSize(QtCore.QSize(500, 400))
        newProj_add_window.setMaximumSize(QtCore.QSize(500, 400))
        newProj_add_window.setStyleSheet("background-color: rgb(0, 127, 255);\n"
"color: white;\n"
"font-family: \"Calibri Light\";")
        self.centralwidget = QtWidgets.QWidget(newProj_add_window)
        self.centralwidget.setObjectName("centralwidget")
        self.newProj_window_title_label = QtWidgets.QLabel(self.centralwidget)
        self.newProj_window_title_label.setGeometry(QtCore.QRect(10, 20, 141, 21))
        font = QtGui.QFont()
        font.setFamily("Calibri Light")
        font.setPointSize(15)
        self.newProj_window_title_label.setFont(font)
        self.newProj_window_title_label.setAlignment(QtCore.Qt.AlignCenter)
        self.newProj_window_title_label.setObjectName("newProj_window_title_label")
        self.newProj_add_title_input = QtWidgets.QLineEdit(self.centralwidget)
        self.newProj_add_title_input.setGeometry(QtCore.QRect(20, 50, 441, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri Light")
        font.setPointSize(15)
        self.newProj_add_title_input.setFont(font)
        self.newProj_add_title_input.setStyleSheet("background-color: white;\n"
"color: black;\n"
"border: 2px solid black;\n"
"font-size: 20px;")
        self.newProj_add_title_input.setObjectName("newProj_add_title_input")
        self.newProj_window_abbv_label = QtWidgets.QLabel(self.centralwidget)
        self.newProj_window_abbv_label.setGeometry(QtCore.QRect(10, 100, 231, 21))
        font = QtGui.QFont()
        font.setFamily("Calibri Light")
        font.setPointSize(15)
        self.newProj_window_abbv_label.setFont(font)
        self.newProj_window_abbv_label.setAlignment(QtCore.Qt.AlignCenter)
        self.newProj_window_abbv_label.setObjectName("newProj_window_abbv_label")
        self.newProj_add_abbv_input = QtWidgets.QLineEdit(self.centralwidget)
        self.newProj_add_abbv_input.setGeometry(QtCore.QRect(20, 130, 441, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri Light")
        font.setPointSize(15)
        self.newProj_add_abbv_input.setFont(font)
        self.newProj_add_abbv_input.setStyleSheet("background-color: white;\n"
"color: black;\n"
"border: 2px solid black;\n"
"font-size: 20px;")
        self.newProj_add_abbv_input.setObjectName("newProj_add_abbv_input")
        self.newProj_window_code_label = QtWidgets.QLabel(self.centralwidget)
        self.newProj_window_code_label.setGeometry(QtCore.QRect(10, 180, 141, 21))
        font = QtGui.QFont()
        font.setFamily("Calibri Light")
        font.setPointSize(15)
        self.newProj_window_code_label.setFont(font)
        self.newProj_window_code_label.setAlignment(QtCore.Qt.AlignCenter)
        self.newProj_window_code_label.setObjectName("newProj_window_code_label")
        self.newProj_add_code_input = QtWidgets.QLineEdit(self.centralwidget)
        self.newProj_add_code_input.setGeometry(QtCore.QRect(20, 210, 441, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri Light")
        font.setPointSize(15)
        self.newProj_add_code_input.setFont(font)
        self.newProj_add_code_input.setStyleSheet("background-color: white;\n"
"color: black;\n"
"border: 2px solid black;\n"
"font-size: 20px;")
        self.newProj_add_code_input.setObjectName("newProj_add_code_input")
        self.newProj_cancel_btn = QtWidgets.QPushButton(self.centralwidget)
        self.newProj_cancel_btn.setGeometry(QtCore.QRect(30, 290, 131, 51))
        self.newProj_cancel_btn.setStyleSheet("background-color: red;\n"
"font-size: 20px;\n"
"border: 2px solid white;\n"
"color: white;\n"
"font-size: 20px;")
        self.newProj_cancel_btn.setObjectName("newProj_cancel_btn")
        self.newProj_ok_btn = QtWidgets.QPushButton(self.centralwidget)
        self.newProj_ok_btn.setGeometry(QtCore.QRect(310, 290, 131, 51))
        self.newProj_ok_btn.setStyleSheet("background-color: green;\n"
"font-size: 20px;\n"
"border: 2px solid white;\n"
"color: white;\n"
"font-size: 20px;")
        self.newProj_ok_btn.setObjectName("newProj_ok_btn")
        newProj_add_window.setCentralWidget(self.centralwidget)

        self.retranslateUi(newProj_add_window)
        QtCore.QMetaObject.connectSlotsByName(newProj_add_window)

        #connections
        # close window button event
        self.newProj_cancel_btn.clicked.connect(lambda: closeWindow(newProj_add_window))
        #pass on details to mongo 
        title = self.newProj_add_title_input.text()
        abbv = self.newProj_add_abbv_input.text()
        code = self.newProj_add_code_input.text()
        self.newProj_ok_btn.clicked.connect(lambda: createProject(newProj_add_window, title, abbv, code))

    def retranslateUi(self, newProj_add_window):
        _translate = QtCore.QCoreApplication.translate
        newProj_add_window.setWindowTitle(_translate("newProj_add_window", "Create New Project"))
        self.newProj_window_title_label.setText(_translate("newProj_add_window", "Project Title"))
        self.newProj_add_title_input.setPlaceholderText(_translate("newProj_add_window", "Title"))
        self.newProj_window_abbv_label.setText(_translate("newProj_add_window", "Project Abbreviation"))
        self.newProj_add_abbv_input.setPlaceholderText(_translate("newProj_add_window", "Abbrevaition"))
        self.newProj_window_code_label.setText(_translate("newProj_add_window", "Project Code"))
        self.newProj_add_code_input.setPlaceholderText(_translate("newProj_add_window", "Code"))
        self.newProj_cancel_btn.setText(_translate("newProj_add_window", "Cancel"))
        self.newProj_ok_btn.setText(_translate("newProj_add_window", "Ok"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_newProj_add_window()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
