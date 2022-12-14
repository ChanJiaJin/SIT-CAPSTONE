# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'add_newDocs_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_add_newDocs_window(object):
    def setupUi(self, add_newDocs_window):
        add_newDocs_window.setObjectName("add_newDocs_window")
        add_newDocs_window.resize(800, 800)
        add_newDocs_window.setMinimumSize(QtCore.QSize(800, 800))
        add_newDocs_window.setMaximumSize(QtCore.QSize(800, 800))
        add_newDocs_window.setStyleSheet("background-color: rgb(0, 127, 255);\n"
"color: white;\n"
"font-family: \"Calibri Light\";")
        self.centralwidget = QtWidgets.QWidget(add_newDocs_window)
        self.centralwidget.setObjectName("centralwidget")
        self.tableView = QtWidgets.QTableView(self.centralwidget)
        self.tableView.setGeometry(QtCore.QRect(10, 130, 781, 551))
        self.tableView.setStyleSheet("background-color: white;\n"
"color: black;\n"
"border: 2px solid black;")
        self.tableView.setEditTriggers(QtWidgets.QAbstractItemView.DoubleClicked)
        self.tableView.setTabKeyNavigation(False)
        self.tableView.setProperty("showDropIndicator", False)
        self.tableView.setObjectName("tableView")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(100, 20, 141, 31))
        self.label.setStyleSheet("border: none;\n"
"font-size: 20px;\n"
"")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.add_newDocs_header_input = QtWidgets.QLineEdit(self.centralwidget)
        self.add_newDocs_header_input.setGeometry(QtCore.QRect(250, 20, 401, 31))
        self.add_newDocs_header_input.setStyleSheet("background-color: white;\n"
"color: black;\n"
"border: 2px solid black;\n"
"font-size: 20px;")
        self.add_newDocs_header_input.setObjectName("add_newDocs_header_input")
        self.add_newDocs_add_column_btn = QtWidgets.QPushButton(self.centralwidget)
        self.add_newDocs_add_column_btn.setGeometry(QtCore.QRect(290, 70, 221, 51))
        self.add_newDocs_add_column_btn.setStyleSheet("background-color: white;\n"
"border: 2px solid black;\n"
"color: black;\n"
"font-size: 20px;")
        self.add_newDocs_add_column_btn.setObjectName("add_newDocs_add_column_btn")
        self.add_newDocs_add_docs_btn = QtWidgets.QPushButton(self.centralwidget)
        self.add_newDocs_add_docs_btn.setGeometry(QtCore.QRect(340, 710, 141, 41))
        self.add_newDocs_add_docs_btn.setStyleSheet("background-color: green;\n"
"color: white;\n"
"border: 2px solid white;\n"
"border-radius: none;\n"
"font-size: 15px;\n"
"font-weight: bold")
        self.add_newDocs_add_docs_btn.setObjectName("add_newDocs_add_docs_btn")
        add_newDocs_window.setCentralWidget(self.centralwidget)

        self.retranslateUi(add_newDocs_window)
        QtCore.QMetaObject.connectSlotsByName(add_newDocs_window)

    def retranslateUi(self, add_newDocs_window):
        _translate = QtCore.QCoreApplication.translate
        add_newDocs_window.setWindowTitle(_translate("add_newDocs_window", "Add new doccument"))
        self.label.setText(_translate("add_newDocs_window", "Colum header:"))
        self.add_newDocs_add_column_btn.setText(_translate("add_newDocs_window", "Add Column Header"))
        self.add_newDocs_add_docs_btn.setText(_translate("add_newDocs_window", "Add Document"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    add_newDocs_window = QtWidgets.QMainWindow()
    ui = Ui_add_newDocs_window()
    ui.setupUi(add_newDocs_window)
    add_newDocs_window.show()
    sys.exit(app.exec_())
