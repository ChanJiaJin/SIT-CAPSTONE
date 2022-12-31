# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'members_addMembers_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_members_editMembers_window(object):
    def setupUi(self, members_editMembers_window):
        members_editMembers_window.setObjectName("members_editMembers_window")
        members_editMembers_window.resize(1300, 800)
        members_editMembers_window.setMinimumSize(QtCore.QSize(1300, 800))
        members_editMembers_window.setMaximumSize(QtCore.QSize(1300, 800))
        members_editMembers_window.setStyleSheet("background-color: rgb(0, 127, 255);\n"
"color: white;\n"
"font-family: \"Calibri Light\";")
        self.centralwidget = QtWidgets.QWidget(members_editMembers_window)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(-10, -10, 861, 821))
        self.groupBox.setStyleSheet("border: 2px solid white;")
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.members_addMembers_table = QtWidgets.QTableView(self.groupBox)
        self.members_addMembers_table.setGeometry(QtCore.QRect(0, -10, 861, 841))
        self.members_addMembers_table.setStyleSheet("background-color: white;\n"
"color: black;\n"
"font-size: 20px;\n"
"border: 2px solid black;")
        self.members_addMembers_table.setEditTriggers(QtWidgets.QAbstractItemView.DoubleClicked)
        self.members_addMembers_table.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.members_addMembers_table.setObjectName("members_addMembers_table")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(860, 10, 61, 31))
        self.label.setStyleSheet("color: white;\n"
"border: none;\n"
"font-size: 20px;")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(860, 70, 111, 31))
        self.label_2.setStyleSheet("color: white;\n"
"border: none;\n"
"font-size: 20px;")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(860, 130, 61, 31))
        self.label_3.setStyleSheet("color: white;\n"
"border: none;\n"
"font-size: 20px;")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.members_addMembers_name_input = QtWidgets.QLineEdit(self.centralwidget)
        self.members_addMembers_name_input.setGeometry(QtCore.QRect(970, 10, 321, 31))
        self.members_addMembers_name_input.setStyleSheet("background-color: white;\n"
"color: black;\n"
"border: 2px solid black;\n"
"font-size: 20px;")
        self.members_addMembers_name_input.setObjectName("members_addMembers_name_input")
        self.members_addMembers_dept_input = QtWidgets.QLineEdit(self.centralwidget)
        self.members_addMembers_dept_input.setGeometry(QtCore.QRect(970, 70, 321, 31))
        self.members_addMembers_dept_input.setStyleSheet("background-color: white;\n"
"color: black;\n"
"border: 2px solid black;\n"
"font-size: 20px;")
        self.members_addMembers_dept_input.setObjectName("members_addMembers_dept_input")
        self.members_addMembers_email_input = QtWidgets.QLineEdit(self.centralwidget)
        self.members_addMembers_email_input.setGeometry(QtCore.QRect(970, 130, 321, 31))
        self.members_addMembers_email_input.setStyleSheet("background-color: white;\n"
"color: black;\n"
"border: 2px solid black;\n"
"font-size: 20px;")
        self.members_addMembers_email_input.setObjectName("members_addMembers_email_input")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(1030, 200, 151, 51))
        self.pushButton.setStyleSheet("background-color: white;\n"
"color: black;\n"
"font-size: 20px;\n"
"border: 2px solid black;")
        self.pushButton.setObjectName("pushButton")
        members_editMembers_window.setCentralWidget(self.centralwidget)

        self.retranslateUi(members_editMembers_window)
        QtCore.QMetaObject.connectSlotsByName(members_editMembers_window)

    def retranslateUi(self, members_editMembers_window):
        _translate = QtCore.QCoreApplication.translate
        members_editMembers_window.setWindowTitle(_translate("members_editMembers_window", "Edit project members"))
        self.label.setText(_translate("members_editMembers_window", "Name"))
        self.label_2.setText(_translate("members_editMembers_window", "Department"))
        self.label_3.setText(_translate("members_editMembers_window", "Email"))
        self.pushButton.setText(_translate("members_editMembers_window", "Add Member"))