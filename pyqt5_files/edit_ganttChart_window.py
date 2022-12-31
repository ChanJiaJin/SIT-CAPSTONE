# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'edit_ganttChart_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ganttChart_edit_window(object):
    def setupUi(self, ganttChart_edit_window):
        ganttChart_edit_window.setObjectName("ganttChart_edit_window")
        ganttChart_edit_window.resize(1000, 800)
        ganttChart_edit_window.setMinimumSize(QtCore.QSize(1000, 800))
        ganttChart_edit_window.setMaximumSize(QtCore.QSize(1000, 800))
        ganttChart_edit_window.setStyleSheet("background-color: rgb(0, 127, 255);\n"
"color: white;\n"
"font-family: \"Calibri light\"")
        self.centralwidget = QtWidgets.QWidget(ganttChart_edit_window)
        self.centralwidget.setObjectName("centralwidget")
        self.edit_ganttChart_table_display = QtWidgets.QTableView(self.centralwidget)
        self.edit_ganttChart_table_display.setGeometry(QtCore.QRect(10, 170, 981, 551))
        self.edit_ganttChart_table_display.setStyleSheet("background-color: white;\n"
"color: black;\n"
"font-size: 20px;\n"
"border: 2px solid black;")
        self.edit_ganttChart_table_display.setEditTriggers(QtWidgets.QAbstractItemView.DoubleClicked)
        self.edit_ganttChart_table_display.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.edit_ganttChart_table_display.setObjectName("edit_ganttChart_table_display")
        self.edit_ganttChart_confirm_btn = QtWidgets.QPushButton(self.centralwidget)
        self.edit_ganttChart_confirm_btn.setGeometry(QtCore.QRect(430, 730, 141, 41))
        self.edit_ganttChart_confirm_btn.setStyleSheet("background-color: green;\n"
"color: white;\n"
"border: 2px solid white;\n"
"border-radius: none;\n"
"font-size: 20px;\n"
"font-weight: bold")
        self.edit_ganttChart_confirm_btn.setObjectName("edit_ganttChart_confirm_btn")
        self.edit_ganttChart_task_input = QtWidgets.QLineEdit(self.centralwidget)
        self.edit_ganttChart_task_input.setGeometry(QtCore.QRect(70, 10, 421, 21))
        self.edit_ganttChart_task_input.setStyleSheet("background-color: white;\n"
"color: black;\n"
"font-size: 20px;\n"
"Border: 2px solid black;")
        self.edit_ganttChart_task_input.setObjectName("edit_ganttChart_task_input")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 51, 21))
        self.label.setStyleSheet("font-size: 20px;\n"
"color: white;\n"
"border: none;")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.edit_ganttChart_enter_entry_btn = QtWidgets.QPushButton(self.centralwidget)
        self.edit_ganttChart_enter_entry_btn.setGeometry(QtCore.QRect(680, 50, 141, 41))
        self.edit_ganttChart_enter_entry_btn.setStyleSheet("background-color: white;\n"
"color: black;\n"
"border: 2px solid black;\n"
"border-radius: none;\n"
"font-size: 20px;")
        self.edit_ganttChart_enter_entry_btn.setObjectName("edit_ganttChart_enter_entry_btn")
        self.edit_ganttChart_start_input = QtWidgets.QLineEdit(self.centralwidget)
        self.edit_ganttChart_start_input.setGeometry(QtCore.QRect(110, 50, 211, 21))
        self.edit_ganttChart_start_input.setStyleSheet("background-color: \"Light gray\";\n"
"color: black;\n"
"font-size: 20px;\n"
"Border: 2px solid black;")
        self.edit_ganttChart_start_input.setObjectName("edit_ganttChart_start_input")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(0, 50, 101, 21))
        self.label_2.setStyleSheet("font-size: 20px;\n"
"color: white;\n"
"border: none;")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.edit_ganttChart_end_input3 = QtWidgets.QLineEdit(self.centralwidget)
        self.edit_ganttChart_end_input3.setGeometry(QtCore.QRect(110, 90, 211, 21))
        self.edit_ganttChart_end_input3.setStyleSheet("background-color: \"Light gray\";\n"
"color: black;\n"
"font-size: 20px;\n"
"Border: 2px solid black;")
        self.edit_ganttChart_end_input3.setText("")
        self.edit_ganttChart_end_input3.setObjectName("edit_ganttChart_end_input3")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(0, 90, 101, 21))
        self.label_3.setStyleSheet("font-size: 20px;\n"
"color: white;\n"
"border: none;")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.edit_ganttChart_choose_range_btn = QtWidgets.QPushButton(self.centralwidget)
        self.edit_ganttChart_choose_range_btn.setGeometry(QtCore.QRect(340, 80, 141, 41))
        self.edit_ganttChart_choose_range_btn.setStyleSheet("background-color: white;\n"
"color: black;\n"
"border: 2px solid black;\n"
"border-radius: none;\n"
"font-size: 20px;")
        self.edit_ganttChart_choose_range_btn.setObjectName("edit_ganttChart_choose_range_btn")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(0, 130, 111, 21))
        self.label_4.setStyleSheet("font-size: 20px;\n"
"color: white;\n"
"border: none;")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.edit_ganttChart_date_rage_input = QtWidgets.QLineEdit(self.centralwidget)
        self.edit_ganttChart_date_rage_input.setGeometry(QtCore.QRect(110, 130, 211, 21))
        self.edit_ganttChart_date_rage_input.setStyleSheet("background-color: \"Light gray\";\n"
"color: black;\n"
"font-size: 20px;\n"
"Border: 2px solid black;")
        self.edit_ganttChart_date_rage_input.setText("")
        self.edit_ganttChart_date_rage_input.setObjectName("edit_ganttChart_date_rage_input")
        ganttChart_edit_window.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(ganttChart_edit_window)
        self.statusbar.setObjectName("statusbar")
        ganttChart_edit_window.setStatusBar(self.statusbar)

        self.retranslateUi(ganttChart_edit_window)
        QtCore.QMetaObject.connectSlotsByName(ganttChart_edit_window)

    def retranslateUi(self, ganttChart_edit_window):
        _translate = QtCore.QCoreApplication.translate
        ganttChart_edit_window.setWindowTitle(_translate("ganttChart_edit_window", "Edit Gantt Chart"))
        self.edit_ganttChart_confirm_btn.setText(_translate("ganttChart_edit_window", "Confirm"))
        self.label.setText(_translate("ganttChart_edit_window", "Task"))
        self.edit_ganttChart_enter_entry_btn.setText(_translate("ganttChart_edit_window", "Enter Entry"))
        self.label_2.setText(_translate("ganttChart_edit_window", "Start Date"))
        self.label_3.setText(_translate("ganttChart_edit_window", "End Date"))
        self.edit_ganttChart_choose_range_btn.setText(_translate("ganttChart_edit_window", "Choose range"))
        self.label_4.setText(_translate("ganttChart_edit_window", "Date Range"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ganttChart_edit_window = QtWidgets.QMainWindow()
    ui = Ui_ganttChart_edit_window()
    ui.setupUi(ganttChart_edit_window)
    ganttChart_edit_window.show()
    sys.exit(app.exec_())
