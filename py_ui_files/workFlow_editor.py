# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'workFlow_editor.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_create_workFlow_window(object):
    def setupUi(self, create_workFlow_window):
        create_workFlow_window.setObjectName("create_workFlow_window")
        create_workFlow_window.resize(1000, 800)
        create_workFlow_window.setMinimumSize(QtCore.QSize(1000, 800))
        create_workFlow_window.setMaximumSize(QtCore.QSize(1000, 800))
        create_workFlow_window.setStyleSheet("background-color: rgb(0, 127, 255);\n"
"color: white;\n"
"font-family: \"Calibri light\";\n"
"\n"
"")
        self.centralwidget = QtWidgets.QWidget(create_workFlow_window)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 20, 161, 31))
        self.label.setStyleSheet("color: white;\n"
"font-size: 20px;")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.edit_workFlow_name_input = QtWidgets.QLineEdit(self.centralwidget)
        self.edit_workFlow_name_input.setGeometry(QtCore.QRect(170, 20, 351, 31))
        self.edit_workFlow_name_input.setStyleSheet("background-color: white;\n"
"color: black;\n"
"border: 2px solid balck;\n"
"font-size: 20px;")
        self.edit_workFlow_name_input.setObjectName("edit_workFlow_name_input")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(660, 20, 101, 31))
        self.label_2.setStyleSheet("color: white;\n"
"font-size: 20px;")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(760, 20, 221, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri light")
        font.setPointSize(20)
        self.comboBox.setFont(font)
        self.comboBox.setStyleSheet("background-color: white;\n"
"color: black;\n"
"border: 2px solid balck;\n"
"")
        self.comboBox.setEditable(False)
        self.comboBox.setCurrentText("")
        self.comboBox.setObjectName("comboBox")
        self.edit_workFlow_display = QtWidgets.QGroupBox(self.centralwidget)
        self.edit_workFlow_display.setGeometry(QtCore.QRect(10, 60, 611, 631))
        self.edit_workFlow_display.setStyleSheet("background-color: \"light gray\";\n"
"border: 2px solid white;")
        self.edit_workFlow_display.setTitle("")
        self.edit_workFlow_display.setObjectName("edit_workFlow_display")
        self.edit_workFlow_scroll_area = QtWidgets.QScrollArea(self.edit_workFlow_display)
        self.edit_workFlow_scroll_area.setGeometry(QtCore.QRect(0, 0, 611, 631))
        self.edit_workFlow_scroll_area.setWidgetResizable(True)
        self.edit_workFlow_scroll_area.setObjectName("edit_workFlow_scroll_area")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 607, 627))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.issueBoard_card = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        self.issueBoard_card.setGeometry(QtCore.QRect(140, 10, 311, 131))
        self.issueBoard_card.setStyleSheet("background-color: white;\n"
"color: black;\n"
"border: 2px solid black;\n"
"font-size: 20x;")
        self.issueBoard_card.setTitle("")
        self.issueBoard_card.setObjectName("issueBoard_card")
        self.phase_name = QtWidgets.QLabel(self.issueBoard_card)
        self.phase_name.setGeometry(QtCore.QRect(10, 10, 281, 16))
        self.phase_name.setStyleSheet("border: none;\n"
"font-size: 15px;\n"
"font-weight: bold;")
        self.phase_name.setObjectName("phase_name")
        self.phase_status = QtWidgets.QLabel(self.issueBoard_card)
        self.phase_status.setGeometry(QtCore.QRect(10, 30, 281, 16))
        self.phase_status.setStyleSheet("border: none;\n"
"font-size: 15px;")
        self.phase_status.setObjectName("phase_status")
        self.phase_openIssues_count = QtWidgets.QLabel(self.issueBoard_card)
        self.phase_openIssues_count.setGeometry(QtCore.QRect(10, 70, 281, 16))
        self.phase_openIssues_count.setStyleSheet("border: none;\n"
"font-size: 15px;")
        self.phase_openIssues_count.setObjectName("phase_openIssues_count")
        self.phase_totalIssues_count = QtWidgets.QLabel(self.issueBoard_card)
        self.phase_totalIssues_count.setGeometry(QtCore.QRect(10, 50, 291, 16))
        self.phase_totalIssues_count.setStyleSheet("border: none;\n"
"font-size: 15px;")
        self.phase_totalIssues_count.setObjectName("phase_totalIssues_count")
        self.phase_internal_flowName = QtWidgets.QLabel(self.issueBoard_card)
        self.phase_internal_flowName.setGeometry(QtCore.QRect(10, 110, 281, 16))
        self.phase_internal_flowName.setStyleSheet("border: none;\n"
"font-size: 15px;")
        self.phase_internal_flowName.setObjectName("phase_internal_flowName")
        self.phase_totalDocs_count = QtWidgets.QLabel(self.issueBoard_card)
        self.phase_totalDocs_count.setGeometry(QtCore.QRect(10, 90, 281, 16))
        self.phase_totalDocs_count.setStyleSheet("border: none;\n"
"font-size: 15px;")
        self.phase_totalDocs_count.setObjectName("phase_totalDocs_count")
        self.edit_workFlow_scroll_area.setWidget(self.scrollAreaWidgetContents)
        self.edit_workFlow_new_phase_box = QtWidgets.QGroupBox(self.centralwidget)
        self.edit_workFlow_new_phase_box.setGeometry(QtCore.QRect(640, 60, 341, 281))
        self.edit_workFlow_new_phase_box.setStyleSheet("border: 2px solid white;")
        self.edit_workFlow_new_phase_box.setObjectName("edit_workFlow_new_phase_box")
        self.edit_workFlow_add_phase_btn = QtWidgets.QPushButton(self.edit_workFlow_new_phase_box)
        self.edit_workFlow_add_phase_btn.setGeometry(QtCore.QRect(110, 240, 131, 31))
        self.edit_workFlow_add_phase_btn.setStyleSheet("background-color: white;\n"
"color: black;\n"
"border: 2px solid black;\n"
"font-size: 15px;")
        self.edit_workFlow_add_phase_btn.setObjectName("edit_workFlow_add_phase_btn")
        self.edit_workFlow_new_phase_name_input = QtWidgets.QLineEdit(self.edit_workFlow_new_phase_box)
        self.edit_workFlow_new_phase_name_input.setGeometry(QtCore.QRect(10, 30, 311, 41))
        self.edit_workFlow_new_phase_name_input.setStyleSheet("background-color: white;\n"
"color: black;\n"
"border: 2px solid black;\n"
"font-size: 15px;")
        self.edit_workFlow_new_phase_name_input.setObjectName("edit_workFlow_new_phase_name_input")
        self.edit_workFlow_new_phase_lead_list = QtWidgets.QComboBox(self.edit_workFlow_new_phase_box)
        self.edit_workFlow_new_phase_lead_list.setGeometry(QtCore.QRect(10, 110, 311, 31))
        self.edit_workFlow_new_phase_lead_list.setStyleSheet("background-color: white;\n"
"color: black;\n"
"font-size: 15px;")
        self.edit_workFlow_new_phase_lead_list.setCurrentText("")
        self.edit_workFlow_new_phase_lead_list.setObjectName("edit_workFlow_new_phase_lead_list")
        self.edit_workFlow_new_phase_end_list = QtWidgets.QComboBox(self.edit_workFlow_new_phase_box)
        self.edit_workFlow_new_phase_end_list.setGeometry(QtCore.QRect(10, 180, 311, 31))
        self.edit_workFlow_new_phase_end_list.setStyleSheet("background-color: white;\n"
"color: black;\n"
"font-size: 15px;")
        self.edit_workFlow_new_phase_end_list.setObjectName("edit_workFlow_new_phase_end_list")
        self.edit_workFlow_edit_phase_box = QtWidgets.QGroupBox(self.centralwidget)
        self.edit_workFlow_edit_phase_box.setGeometry(QtCore.QRect(640, 380, 341, 281))
        self.edit_workFlow_edit_phase_box.setStyleSheet("border: 2px solid white;")
        self.edit_workFlow_edit_phase_box.setObjectName("edit_workFlow_edit_phase_box")
        self.edit_workFlow_edit_phase_btn = QtWidgets.QPushButton(self.edit_workFlow_edit_phase_box)
        self.edit_workFlow_edit_phase_btn.setGeometry(QtCore.QRect(110, 240, 131, 31))
        self.edit_workFlow_edit_phase_btn.setStyleSheet("background-color: white;\n"
"color: black;\n"
"border: 2px solid black;\n"
"font-size: 15px;")
        self.edit_workFlow_edit_phase_btn.setObjectName("edit_workFlow_edit_phase_btn")
        self.edit_workFlow_edit_phase_name_input = QtWidgets.QLineEdit(self.edit_workFlow_edit_phase_box)
        self.edit_workFlow_edit_phase_name_input.setGeometry(QtCore.QRect(10, 30, 311, 41))
        self.edit_workFlow_edit_phase_name_input.setStyleSheet("background-color: white;\n"
"color: black;\n"
"border: 2px solid black;\n"
"font-size: 15px;")
        self.edit_workFlow_edit_phase_name_input.setObjectName("edit_workFlow_edit_phase_name_input")
        self.edit_workFlow_edit_phase_lead_list = QtWidgets.QComboBox(self.edit_workFlow_edit_phase_box)
        self.edit_workFlow_edit_phase_lead_list.setGeometry(QtCore.QRect(10, 110, 311, 31))
        self.edit_workFlow_edit_phase_lead_list.setStyleSheet("background-color: white;\n"
"color: black;\n"
"font-size: 15px;")
        self.edit_workFlow_edit_phase_lead_list.setCurrentText("")
        self.edit_workFlow_edit_phase_lead_list.setObjectName("edit_workFlow_edit_phase_lead_list")
        self.edit_workFlow_edit_phase_end_list = QtWidgets.QComboBox(self.edit_workFlow_edit_phase_box)
        self.edit_workFlow_edit_phase_end_list.setGeometry(QtCore.QRect(10, 180, 311, 31))
        self.edit_workFlow_edit_phase_end_list.setStyleSheet("background-color: white;\n"
"color: black;\n"
"font-size: 15px;")
        self.edit_workFlow_edit_phase_end_list.setObjectName("edit_workFlow_edit_phase_end_list")
        self.edit_workFlow_ok_btn = QtWidgets.QPushButton(self.centralwidget)
        self.edit_workFlow_ok_btn.setGeometry(QtCore.QRect(570, 720, 131, 51))
        self.edit_workFlow_ok_btn.setStyleSheet("background-color: green;\n"
"border: 2px solid white;\n"
"border-radius: none;\n"
"font-size: 15px;\n"
"font-weight: bold;\n"
"color: white;")
        self.edit_workFlow_ok_btn.setObjectName("edit_workFlow_ok_btn")
        self.edit_workFlow_cancel_btn = QtWidgets.QPushButton(self.centralwidget)
        self.edit_workFlow_cancel_btn.setGeometry(QtCore.QRect(290, 720, 131, 51))
        self.edit_workFlow_cancel_btn.setStyleSheet("background-color: red;\n"
"border: 2px solid white;\n"
"border-radius: none;\n"
"font-size: 15px;\n"
"font-weight: bold")
        self.edit_workFlow_cancel_btn.setObjectName("edit_workFlow_cancel_btn")
        create_workFlow_window.setCentralWidget(self.centralwidget)

        self.retranslateUi(create_workFlow_window)
        QtCore.QMetaObject.connectSlotsByName(create_workFlow_window)

    def retranslateUi(self, create_workFlow_window):
        _translate = QtCore.QCoreApplication.translate
        create_workFlow_window.setWindowTitle(_translate("create_workFlow_window", "Work flow editor"))
        self.label.setText(_translate("create_workFlow_window", "Work Flow Name"))
        self.edit_workFlow_name_input.setPlaceholderText(_translate("create_workFlow_window", "Name"))
        self.label_2.setText(_translate("create_workFlow_window", "Flow Tree"))
        self.phase_name.setText(_translate("create_workFlow_window", "<Phase:>"))
        self.phase_status.setText(_translate("create_workFlow_window", "<Status:>"))
        self.phase_openIssues_count.setText(_translate("create_workFlow_window", "<Open Issues:>"))
        self.phase_totalIssues_count.setText(_translate("create_workFlow_window", "<Total issues:>"))
        self.phase_internal_flowName.setText(_translate("create_workFlow_window", "<Internal Flow:>"))
        self.phase_totalDocs_count.setText(_translate("create_workFlow_window", "<No. of docs:>"))
        self.edit_workFlow_new_phase_box.setTitle(_translate("create_workFlow_window", "Add New Phase"))
        self.edit_workFlow_add_phase_btn.setText(_translate("create_workFlow_window", "Add Phase"))
        self.edit_workFlow_new_phase_name_input.setPlaceholderText(_translate("create_workFlow_window", "Phase name"))
        self.edit_workFlow_edit_phase_box.setTitle(_translate("create_workFlow_window", "Edit Phase"))
        self.edit_workFlow_edit_phase_btn.setText(_translate("create_workFlow_window", "Edit Phase"))
        self.edit_workFlow_edit_phase_name_input.setPlaceholderText(_translate("create_workFlow_window", "Phase name"))
        self.edit_workFlow_ok_btn.setText(_translate("create_workFlow_window", "Ok"))
        self.edit_workFlow_cancel_btn.setText(_translate("create_workFlow_window", "Cancel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    create_workFlow_window = QtWidgets.QMainWindow()
    ui = Ui_create_workFlow_window()
    ui.setupUi(create_workFlow_window)
    create_workFlow_window.show()
    sys.exit(app.exec_())