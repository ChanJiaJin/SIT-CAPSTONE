# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'edit_ganttChart_choose_date_range_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_edit_ganttChart_choose_date_range_window(object):
    def setupUi(self, edit_ganttChart_choose_date_range_window):
        edit_ganttChart_choose_date_range_window.setObjectName("edit_ganttChart_choose_date_range_window")
        edit_ganttChart_choose_date_range_window.resize(800, 686)
        edit_ganttChart_choose_date_range_window.setStyleSheet("background-color: rgb(0, 127, 255);\n"
"color: white;\n"
"font-family: \"calibri Light\";")
        self.centralwidget = QtWidgets.QWidget(edit_ganttChart_choose_date_range_window)
        self.centralwidget.setObjectName("centralwidget")
        self.calendarWidget = QtWidgets.QCalendarWidget(self.centralwidget)
        self.calendarWidget.setGeometry(QtCore.QRect(0, 0, 801, 501))
        self.calendarWidget.setStyleSheet("background-color: white;\n"
"color: black;\n"
"font-size: 20px;")
        self.calendarWidget.setVerticalHeaderFormat(QtWidgets.QCalendarWidget.NoVerticalHeader)
        self.calendarWidget.setObjectName("calendarWidget")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(110, 570, 101, 21))
        self.label_3.setStyleSheet("font-size: 20px;\n"
"color: white;\n"
"border: none;")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(110, 610, 111, 21))
        self.label_4.setStyleSheet("font-size: 20px;\n"
"color: white;\n"
"border: none;")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.edit_ganttChart_date_rage_input = QtWidgets.QLineEdit(self.centralwidget)
        self.edit_ganttChart_date_rage_input.setGeometry(QtCore.QRect(220, 610, 211, 21))
        self.edit_ganttChart_date_rage_input.setStyleSheet("background-color: \"Light gray\";\n"
"color: black;\n"
"font-size: 20px;\n"
"Border: 2px solid black;")
        self.edit_ganttChart_date_rage_input.setText("")
        self.edit_ganttChart_date_rage_input.setObjectName("edit_ganttChart_date_rage_input")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(110, 530, 101, 21))
        self.label_2.setStyleSheet("font-size: 20px;\n"
"color: white;\n"
"border: none;")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.edit_ganttChart_choose_range_btn = QtWidgets.QPushButton(self.centralwidget)
        self.edit_ganttChart_choose_range_btn.setGeometry(QtCore.QRect(470, 560, 141, 41))
        self.edit_ganttChart_choose_range_btn.setStyleSheet("background-color: white;\n"
"color: black;\n"
"border: 2px solid black;\n"
"border-radius: none;\n"
"font-size: 20px;")
        self.edit_ganttChart_choose_range_btn.setObjectName("edit_ganttChart_choose_range_btn")
        self.edit_ganttChart_end_input3 = QtWidgets.QLineEdit(self.centralwidget)
        self.edit_ganttChart_end_input3.setGeometry(QtCore.QRect(220, 570, 211, 21))
        self.edit_ganttChart_end_input3.setStyleSheet("background-color: \"Light gray\";\n"
"color: black;\n"
"font-size: 20px;\n"
"Border: 2px solid black;")
        self.edit_ganttChart_end_input3.setText("")
        self.edit_ganttChart_end_input3.setObjectName("edit_ganttChart_end_input3")
        self.edit_ganttChart_start_input = QtWidgets.QLineEdit(self.centralwidget)
        self.edit_ganttChart_start_input.setGeometry(QtCore.QRect(220, 530, 211, 21))
        self.edit_ganttChart_start_input.setStyleSheet("background-color: \"Light gray\";\n"
"color: black;\n"
"font-size: 20px;\n"
"Border: 2px solid black;")
        self.edit_ganttChart_start_input.setObjectName("edit_ganttChart_start_input")
        edit_ganttChart_choose_date_range_window.setCentralWidget(self.centralwidget)

        self.retranslateUi(edit_ganttChart_choose_date_range_window)
        QtCore.QMetaObject.connectSlotsByName(edit_ganttChart_choose_date_range_window)

    def retranslateUi(self, edit_ganttChart_choose_date_range_window):
        _translate = QtCore.QCoreApplication.translate
        edit_ganttChart_choose_date_range_window.setWindowTitle(_translate("edit_ganttChart_choose_date_range_window", "Choose Date Range"))
        self.label_3.setText(_translate("edit_ganttChart_choose_date_range_window", "End Date"))
        self.label_4.setText(_translate("edit_ganttChart_choose_date_range_window", "Date Range"))
        self.label_2.setText(_translate("edit_ganttChart_choose_date_range_window", "Start Date"))
        self.edit_ganttChart_choose_range_btn.setText(_translate("edit_ganttChart_choose_date_range_window", "Choose range"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    edit_ganttChart_choose_date_range_window = QtWidgets.QMainWindow()
    ui = Ui_edit_ganttChart_choose_date_range_window()
    ui.setupUi(edit_ganttChart_choose_date_range_window)
    edit_ganttChart_choose_date_range_window.show()
    sys.exit(app.exec_())