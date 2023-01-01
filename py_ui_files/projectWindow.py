# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'projectWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_projectWindow(object):
    def setupUi(self, projectWindow):
        projectWindow.setObjectName("projectWindow")
        projectWindow.resize(1000, 800)
        projectWindow.setMinimumSize(QtCore.QSize(1000, 800))
        projectWindow.setMaximumSize(QtCore.QSize(1000, 800))
        font = QtGui.QFont()
        font.setFamily("Calibri Light")
        font.setPointSize(10)
        projectWindow.setFont(font)
        projectWindow.setStyleSheet("background-color: rgb(0, 127, 255);\n"
"font-family: \"Calibri Light\";\n"
"color: white;")
        self.centralwidget = QtWidgets.QWidget(projectWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.myIssues_btn = QtWidgets.QTabWidget(self.centralwidget)
        self.myIssues_btn.setGeometry(QtCore.QRect(0, 0, 1500, 1000))
        self.myIssues_btn.setMinimumSize(QtCore.QSize(1500, 1000))
        self.myIssues_btn.setMaximumSize(QtCore.QSize(1500, 1000))
        self.myIssues_btn.setStyleSheet("font-size: 15px;\n"
"color: black;")
        self.myIssues_btn.setObjectName("myIssues_btn")
        self.generalDetails_btn = QtWidgets.QWidget()
        font = QtGui.QFont()
        font.setFamily("Calibri Light")
        font.setPointSize(-1)
        self.generalDetails_btn.setFont(font)
        self.generalDetails_btn.setObjectName("generalDetails_btn")
        self.generalDetails_proj_abbv = QtWidgets.QLabel(self.generalDetails_btn)
        self.generalDetails_proj_abbv.setGeometry(QtCore.QRect(310, 50, 231, 41))
        font = QtGui.QFont()
        font.setFamily("Calibri Light")
        font.setPointSize(-1)
        self.generalDetails_proj_abbv.setFont(font)
        self.generalDetails_proj_abbv.setStyleSheet("font-size: 20px;\n"
"color: white;")
        self.generalDetails_proj_abbv.setObjectName("generalDetails_proj_abbv")
        self.generalDetails_proj_code = QtWidgets.QLabel(self.generalDetails_btn)
        self.generalDetails_proj_code.setGeometry(QtCore.QRect(10, 50, 201, 41))
        font = QtGui.QFont()
        font.setFamily("Calibri Light")
        font.setPointSize(-1)
        self.generalDetails_proj_code.setFont(font)
        self.generalDetails_proj_code.setStyleSheet("font-size: 20px;\n"
"color: white;")
        self.generalDetails_proj_code.setObjectName("generalDetails_proj_code")
        self.generalDetails_proj_phase = QtWidgets.QLabel(self.generalDetails_btn)
        self.generalDetails_proj_phase.setGeometry(QtCore.QRect(540, 120, 391, 41))
        font = QtGui.QFont()
        font.setFamily("Calibri Light")
        font.setPointSize(-1)
        self.generalDetails_proj_phase.setFont(font)
        self.generalDetails_proj_phase.setStyleSheet("font-size: 20px;\n"
"color: white;")
        self.generalDetails_proj_phase.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.generalDetails_proj_phase.setObjectName("generalDetails_proj_phase")
        self.generalDetails_proj_completion = QtWidgets.QLabel(self.generalDetails_btn)
        self.generalDetails_proj_completion.setGeometry(QtCore.QRect(540, 160, 391, 41))
        font = QtGui.QFont()
        font.setFamily("Calibri Light")
        font.setPointSize(-1)
        self.generalDetails_proj_completion.setFont(font)
        self.generalDetails_proj_completion.setStyleSheet("font-size: 20px;\n"
"color: white;")
        self.generalDetails_proj_completion.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.generalDetails_proj_completion.setObjectName("generalDetails_proj_completion")
        self.generalDetails_issues_box = QtWidgets.QGroupBox(self.generalDetails_btn)
        self.generalDetails_issues_box.setGeometry(QtCore.QRect(10, 100, 511, 121))
        self.generalDetails_issues_box.setStyleSheet("background-color:\"light grey\";\n"
"color: white;\n"
"border: 2px solid white;\n"
"border-radius: 10px;\n"
"font-size: 15px;")
        self.generalDetails_issues_box.setTitle("")
        self.generalDetails_issues_box.setObjectName("generalDetails_issues_box")
        self.generalDescription_open_issues = QtWidgets.QLabel(self.generalDetails_issues_box)
        self.generalDescription_open_issues.setGeometry(QtCore.QRect(10, 10, 491, 41))
        self.generalDescription_open_issues.setStyleSheet("font-size: 20px;\n"
"border: none;\n"
"color: red;")
        self.generalDescription_open_issues.setObjectName("generalDescription_open_issues")
        self.generalDescription_closed_issues = QtWidgets.QLabel(self.generalDetails_issues_box)
        self.generalDescription_closed_issues.setGeometry(QtCore.QRect(10, 60, 491, 41))
        self.generalDescription_closed_issues.setStyleSheet("font-size: 20px;\n"
"border: none;\n"
"color: green;")
        self.generalDescription_closed_issues.setObjectName("generalDescription_closed_issues")
        self.generalDetails_docs_box = QtWidgets.QGroupBox(self.generalDetails_btn)
        self.generalDetails_docs_box.setGeometry(QtCore.QRect(10, 240, 971, 121))
        self.generalDetails_docs_box.setStyleSheet("background-color:\"light grey\";\n"
"color: white;\n"
"border: 2px solid white;\n"
"border-radius: 10px;\n"
"font-size: 15px;")
        self.generalDetails_docs_box.setTitle("")
        self.generalDetails_docs_box.setObjectName("generalDetails_docs_box")
        self.generalDescription_dwg_count = QtWidgets.QLabel(self.generalDetails_docs_box)
        self.generalDescription_dwg_count.setGeometry(QtCore.QRect(10, 10, 261, 41))
        self.generalDescription_dwg_count.setStyleSheet("font-size: 20px;\n"
"border: none;\n"
"color: black;")
        self.generalDescription_dwg_count.setObjectName("generalDescription_dwg_count")
        self.generalDescription_bim_count = QtWidgets.QLabel(self.generalDetails_docs_box)
        self.generalDescription_bim_count.setGeometry(QtCore.QRect(10, 60, 261, 41))
        self.generalDescription_bim_count.setStyleSheet("font-size: 20px;\n"
"border: none;\n"
"color: black;")
        self.generalDescription_bim_count.setObjectName("generalDescription_bim_count")
        self.generalDescription_excel_count = QtWidgets.QLabel(self.generalDetails_docs_box)
        self.generalDescription_excel_count.setGeometry(QtCore.QRect(530, 60, 261, 41))
        self.generalDescription_excel_count.setStyleSheet("font-size: 20px;\n"
"border: none;\n"
"color: black;")
        self.generalDescription_excel_count.setObjectName("generalDescription_excel_count")
        self.generalDescription_pdf_count = QtWidgets.QLabel(self.generalDetails_docs_box)
        self.generalDescription_pdf_count.setGeometry(QtCore.QRect(530, 10, 261, 41))
        self.generalDescription_pdf_count.setStyleSheet("font-size: 20px;\n"
"border: none;\n"
"color: black;")
        self.generalDescription_pdf_count.setObjectName("generalDescription_pdf_count")
        self.tableView = QtWidgets.QTableView(self.generalDetails_btn)
        self.tableView.setGeometry(QtCore.QRect(10, 370, 971, 391))
        self.tableView.setStyleSheet("background-color: \"light grey\";\n"
"color: black;\n"
"font-size: 15px;\n"
"border: 2px solid white;")
        self.tableView.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableView.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.tableView.setObjectName("tableView")
        self.generalDetails_proj_title = QtWidgets.QLabel(self.generalDetails_btn)
        self.generalDetails_proj_title.setGeometry(QtCore.QRect(10, 10, 231, 41))
        font = QtGui.QFont()
        font.setFamily("Calibri Light")
        font.setPointSize(-1)
        self.generalDetails_proj_title.setFont(font)
        self.generalDetails_proj_title.setStyleSheet("font-size: 20px;\n"
"color: white;")
        self.generalDetails_proj_title.setObjectName("generalDetails_proj_title")
        self.myIssues_btn.addTab(self.generalDetails_btn, "")
        self.workFlow_btn = QtWidgets.QWidget()
        self.workFlow_btn.setObjectName("workFlow_btn")
        self.workFlow_current_pahse = QtWidgets.QLabel(self.workFlow_btn)
        self.workFlow_current_pahse.setGeometry(QtCore.QRect(10, 50, 511, 41))
        font = QtGui.QFont()
        font.setFamily("Calibri Light")
        font.setPointSize(-1)
        self.workFlow_current_pahse.setFont(font)
        self.workFlow_current_pahse.setStyleSheet("font-size: 20px;\n"
"color: white;")
        self.workFlow_current_pahse.setObjectName("workFlow_current_pahse")
        self.workFlow_work_flow_name = QtWidgets.QLabel(self.workFlow_btn)
        self.workFlow_work_flow_name.setGeometry(QtCore.QRect(10, 10, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Calibri Light")
        font.setPointSize(-1)
        self.workFlow_work_flow_name.setFont(font)
        self.workFlow_work_flow_name.setStyleSheet("font-size: 20px;\n"
"color: white;")
        self.workFlow_work_flow_name.setAlignment(QtCore.Qt.AlignCenter)
        self.workFlow_work_flow_name.setObjectName("workFlow_work_flow_name")
        self.flowEdit_btn = QtWidgets.QPushButton(self.workFlow_btn)
        self.flowEdit_btn.setGeometry(QtCore.QRect(770, 20, 181, 61))
        self.flowEdit_btn.setStyleSheet("background-color: white;\n"
"color: black;\n"
"border: 2px solid black;\n"
"font-size: 20px;")
        self.flowEdit_btn.setObjectName("flowEdit_btn")
        self.scrollArea = QtWidgets.QScrollArea(self.workFlow_btn)
        self.scrollArea.setGeometry(QtCore.QRect(10, 100, 981, 661))
        self.scrollArea.setStyleSheet("background-color: \"light grey\";\n"
"color: white;\n"
"border-radius: 10px;\n"
"border: 2px solid white;")
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 977, 657))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.issueBoard_card = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        self.issueBoard_card.setGeometry(QtCore.QRect(290, 10, 311, 191))
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
        self.setStatus_btn = QtWidgets.QPushButton(self.issueBoard_card)
        self.setStatus_btn.setGeometry(QtCore.QRect(80, 140, 141, 41))
        self.setStatus_btn.setStyleSheet("background-color: red;\n"
"color: white;\n"
"border: 2px solid white;\n"
"border-radius: none;\n"
"font-size: 15px;\n"
"font-weight: bold")
        self.setStatus_btn.setObjectName("setStatus_btn")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.workFlow_list = QtWidgets.QComboBox(self.workFlow_btn)
        self.workFlow_list.setGeometry(QtCore.QRect(110, 20, 321, 31))
        self.workFlow_list.setStyleSheet("background-color: white;\n"
"color: black;\n"
"border: 2px solid black;\n"
"font-size: 20px;")
        self.workFlow_list.setObjectName("workFlow_list")
        self.myIssues_btn.addTab(self.workFlow_btn, "")
        self.issuesBoard_btn = QtWidgets.QWidget()
        self.issuesBoard_btn.setObjectName("issuesBoard_btn")
        self.label_2 = QtWidgets.QLabel(self.issuesBoard_btn)
        self.label_2.setGeometry(QtCore.QRect(10, 50, 91, 41))
        font = QtGui.QFont()
        font.setFamily("Calibri Light")
        font.setPointSize(-1)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("font-size: 20px;\n"
"color: white;")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label = QtWidgets.QLabel(self.issuesBoard_btn)
        self.label.setGeometry(QtCore.QRect(10, 10, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Calibri Light")
        font.setPointSize(-1)
        self.label.setFont(font)
        self.label.setStyleSheet("font-size: 20px;\n"
"color: white;")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.workFlow_list_2 = QtWidgets.QComboBox(self.issuesBoard_btn)
        self.workFlow_list_2.setGeometry(QtCore.QRect(110, 20, 341, 31))
        self.workFlow_list_2.setStyleSheet("background-color: white;\n"
"color: black;\n"
"border: 2px solid black;\n"
"font-size: 20px;")
        self.workFlow_list_2.setObjectName("workFlow_list_2")
        self.phase_list = QtWidgets.QComboBox(self.issuesBoard_btn)
        self.phase_list.setGeometry(QtCore.QRect(110, 60, 341, 31))
        self.phase_list.setStyleSheet("background-color: white;\n"
"color: black;\n"
"border: 2px solid black;\n"
"font-size: 20px;")
        self.phase_list.setObjectName("phase_list")
        self.pendingIssues_table = QtWidgets.QTableView(self.issuesBoard_btn)
        self.pendingIssues_table.setGeometry(QtCore.QRect(20, 160, 300, 550))
        self.pendingIssues_table.setMinimumSize(QtCore.QSize(300, 550))
        self.pendingIssues_table.setMaximumSize(QtCore.QSize(300, 550))
        self.pendingIssues_table.setStyleSheet("background-color: \"Light gray\";\n"
"color: black;\n"
"border: 2px solid black;\n"
"")
        self.pendingIssues_table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.pendingIssues_table.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.pendingIssues_table.setObjectName("pendingIssues_table")
        self.raiseIssue_btn = QtWidgets.QPushButton(self.issuesBoard_btn)
        self.raiseIssue_btn.setGeometry(QtCore.QRect(810, 30, 171, 51))
        self.raiseIssue_btn.setStyleSheet("background-color: white;\n"
"color: black;\n"
"border: 2px solid black;\n"
"font-size: 20px;")
        self.raiseIssue_btn.setObjectName("raiseIssue_btn")
        self.showIssues_btn = QtWidgets.QPushButton(self.issuesBoard_btn)
        self.showIssues_btn.setGeometry(QtCore.QRect(460, 30, 171, 51))
        self.showIssues_btn.setStyleSheet("background-color: white;\n"
"color: black;\n"
"border: 2px solid black;\n"
"font-size: 20px;")
        self.showIssues_btn.setObjectName("showIssues_btn")
        self.groupBox = QtWidgets.QGroupBox(self.issuesBoard_btn)
        self.groupBox.setGeometry(QtCore.QRect(-10, 100, 1011, 671))
        self.groupBox.setStyleSheet("border: 2px solid white;")
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.pendingIssues_table_2 = QtWidgets.QTableView(self.groupBox)
        self.pendingIssues_table_2.setGeometry(QtCore.QRect(360, 60, 300, 550))
        self.pendingIssues_table_2.setMinimumSize(QtCore.QSize(300, 550))
        self.pendingIssues_table_2.setMaximumSize(QtCore.QSize(300, 550))
        self.pendingIssues_table_2.setStyleSheet("background-color: \"Light gray\";\n"
"color: black;\n"
"border: 2px solid black;\n"
"")
        self.pendingIssues_table_2.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.pendingIssues_table_2.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.pendingIssues_table_2.setObjectName("pendingIssues_table_2")
        self.issuesBoard_pending_issues_count = QtWidgets.QLabel(self.groupBox)
        self.issuesBoard_pending_issues_count.setGeometry(QtCore.QRect(370, 20, 281, 31))
        self.issuesBoard_pending_issues_count.setStyleSheet("color: white;\n"
"font-size: 20px;\n"
"font-weight: bold;\n"
"border: none;")
        self.issuesBoard_pending_issues_count.setAlignment(QtCore.Qt.AlignCenter)
        self.issuesBoard_pending_issues_count.setObjectName("issuesBoard_pending_issues_count")
        self.issuesBoard_closed_issues_count = QtWidgets.QLabel(self.groupBox)
        self.issuesBoard_closed_issues_count.setGeometry(QtCore.QRect(700, 20, 281, 31))
        self.issuesBoard_closed_issues_count.setStyleSheet("color: white;\n"
"font-size: 20px;\n"
"font-weight: bold;\n"
"border: none;")
        self.issuesBoard_closed_issues_count.setAlignment(QtCore.Qt.AlignCenter)
        self.issuesBoard_closed_issues_count.setObjectName("issuesBoard_closed_issues_count")
        self.pendingIssues_table_3 = QtWidgets.QTableView(self.groupBox)
        self.pendingIssues_table_3.setGeometry(QtCore.QRect(690, 60, 300, 550))
        self.pendingIssues_table_3.setMinimumSize(QtCore.QSize(300, 550))
        self.pendingIssues_table_3.setMaximumSize(QtCore.QSize(300, 550))
        self.pendingIssues_table_3.setStyleSheet("background-color: \"Light gray\";\n"
"color: black;\n"
"border: 2px solid black;\n"
"")
        self.pendingIssues_table_3.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.pendingIssues_table_3.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.pendingIssues_table_3.setObjectName("pendingIssues_table_3")
        self.issuesBoard_open_issues_count = QtWidgets.QLabel(self.groupBox)
        self.issuesBoard_open_issues_count.setGeometry(QtCore.QRect(40, 20, 281, 31))
        self.issuesBoard_open_issues_count.setStyleSheet("color: white;\n"
"font-size: 20px;\n"
"font-weight: bold;\n"
"border: none;")
        self.issuesBoard_open_issues_count.setAlignment(QtCore.Qt.AlignCenter)
        self.issuesBoard_open_issues_count.setObjectName("issuesBoard_open_issues_count")
        self.groupBox.raise_()
        self.label_2.raise_()
        self.label.raise_()
        self.workFlow_list_2.raise_()
        self.phase_list.raise_()
        self.pendingIssues_table.raise_()
        self.raiseIssue_btn.raise_()
        self.showIssues_btn.raise_()
        self.myIssues_btn.addTab(self.issuesBoard_btn, "")
        self.docsList_btn = QtWidgets.QWidget()
        self.docsList_btn.setObjectName("docsList_btn")
        self.add_newDocs_list_btn = QtWidgets.QPushButton(self.docsList_btn)
        self.add_newDocs_list_btn.setGeometry(QtCore.QRect(760, 20, 221, 51))
        self.add_newDocs_list_btn.setStyleSheet("background-color: white;\n"
"border: 2px solid black;\n"
"color: black;\n"
"font-size: 20px;")
        self.add_newDocs_list_btn.setObjectName("add_newDocs_list_btn")
        self.docsList_table = QtWidgets.QTableView(self.docsList_btn)
        self.docsList_table.setGeometry(QtCore.QRect(20, 100, 961, 651))
        self.docsList_table.setStyleSheet("background-color:\"Light gray\";\n"
"border: 2px solid balck;\n"
"color: black;\n"
"font-size: 20px;")
        self.docsList_table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.docsList_table.setTabKeyNavigation(False)
        self.docsList_table.setProperty("showDropIndicator", True)
        self.docsList_table.setDragDropOverwriteMode(False)
        self.docsList_table.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.docsList_table.setObjectName("docsList_table")
        self.label_3 = QtWidgets.QLabel(self.docsList_btn)
        self.label_3.setGeometry(QtCore.QRect(20, 20, 111, 41))
        self.label_3.setStyleSheet("background-color: none;\n"
"color: white;\n"
"font-size: 20px;\n"
"border: none;")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.docs_workflow_list = QtWidgets.QComboBox(self.docsList_btn)
        self.docs_workflow_list.setGeometry(QtCore.QRect(130, 20, 321, 41))
        self.docs_workflow_list.setStyleSheet("background-color: white;\n"
"border: 2px solid balck;\n"
"font-size: 20px;\n"
"color: black;")
        self.docs_workflow_list.setObjectName("docs_workflow_list")
        self.myIssues_btn.addTab(self.docsList_btn, "")
        self.ganttChart_btn = QtWidgets.QWidget()
        self.ganttChart_btn.setObjectName("ganttChart_btn")
        self.ganttCahrt_display = QtWidgets.QScrollArea(self.ganttChart_btn)
        self.ganttCahrt_display.setGeometry(QtCore.QRect(-20, 130, 1021, 671))
        self.ganttCahrt_display.setStyleSheet("background-color: \"Light gray\";\n"
"color: black;\n"
"border: 2px solid black;\n"
"font-size: 15px;")
        self.ganttCahrt_display.setWidgetResizable(True)
        self.ganttCahrt_display.setObjectName("ganttCahrt_display")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 1017, 667))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.ganttCahrt_display.setWidget(self.scrollAreaWidgetContents_2)
        self.ganttChart_proj_title = QtWidgets.QLabel(self.ganttChart_btn)
        self.ganttChart_proj_title.setGeometry(QtCore.QRect(10, 20, 551, 31))
        self.ganttChart_proj_title.setStyleSheet("border: none;\n"
"font-size: 20px;\n"
"color: white;\n"
"")
        self.ganttChart_proj_title.setAlignment(QtCore.Qt.AlignCenter)
        self.ganttChart_proj_title.setObjectName("ganttChart_proj_title")
        self.ganttChart_proj_code = QtWidgets.QLabel(self.ganttChart_btn)
        self.ganttChart_proj_code.setGeometry(QtCore.QRect(10, 50, 551, 31))
        self.ganttChart_proj_code.setStyleSheet("border: none;\n"
"font-size: 20px;\n"
"color: white;\n"
"")
        self.ganttChart_proj_code.setAlignment(QtCore.Qt.AlignCenter)
        self.ganttChart_proj_code.setObjectName("ganttChart_proj_code")
        self.pushButton = QtWidgets.QPushButton(self.ganttChart_btn)
        self.pushButton.setGeometry(QtCore.QRect(800, 20, 181, 61))
        self.pushButton.setStyleSheet("background-color: white;\n"
"color: black;\n"
"border: 2px solid black;\n"
"font-size: 20px;")
        self.pushButton.setObjectName("pushButton")
        self.myIssues_btn.addTab(self.ganttChart_btn, "")
        self.projMembers_btn = QtWidgets.QWidget()
        self.projMembers_btn.setObjectName("projMembers_btn")
        self.members_totalMembers_count = QtWidgets.QLabel(self.projMembers_btn)
        self.members_totalMembers_count.setGeometry(QtCore.QRect(10, 10, 361, 31))
        self.members_totalMembers_count.setStyleSheet("color: white;\n"
"font-size: 20px;")
        self.members_totalMembers_count.setAlignment(QtCore.Qt.AlignCenter)
        self.members_totalMembers_count.setObjectName("members_totalMembers_count")
        self.members_editmembers_btn = QtWidgets.QPushButton(self.projMembers_btn)
        self.members_editmembers_btn.setGeometry(QtCore.QRect(840, 10, 151, 41))
        self.members_editmembers_btn.setStyleSheet("background-color: white;\n"
"color: black;\n"
"font-size: 20px;")
        self.members_editmembers_btn.setObjectName("members_editmembers_btn")
        self.members_sortDepartment_btn = QtWidgets.QPushButton(self.projMembers_btn)
        self.members_sortDepartment_btn.setGeometry(QtCore.QRect(790, 70, 201, 41))
        self.members_sortDepartment_btn.setStyleSheet("background-color: white;\n"
"color: black;\n"
"font-size: 20px;")
        self.members_sortDepartment_btn.setObjectName("members_sortDepartment_btn")
        self.members_sortName_btn = QtWidgets.QPushButton(self.projMembers_btn)
        self.members_sortName_btn.setGeometry(QtCore.QRect(630, 70, 151, 41))
        self.members_sortName_btn.setStyleSheet("background-color: white;\n"
"color: black;\n"
"font-size: 20px;")
        self.members_sortName_btn.setObjectName("members_sortName_btn")
        self.members_tableDisplay = QtWidgets.QTableWidget(self.projMembers_btn)
        self.members_tableDisplay.setGeometry(QtCore.QRect(-20, 120, 1021, 681))
        self.members_tableDisplay.setStyleSheet("background-color: \"Light Gray\";\n"
"color: white;\n"
"border: 2px solid white;\n"
"font-size: 20px;")
        self.members_tableDisplay.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.members_tableDisplay.setObjectName("members_tableDisplay")
        self.members_tableDisplay.setColumnCount(0)
        self.members_tableDisplay.setRowCount(0)
        self.myIssues_btn.addTab(self.projMembers_btn, "")
        projectWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(projectWindow)
        self.statusbar.setObjectName("statusbar")
        projectWindow.setStatusBar(self.statusbar)

        self.retranslateUi(projectWindow)
        self.myIssues_btn.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(projectWindow)

    def retranslateUi(self, projectWindow):
        _translate = QtCore.QCoreApplication.translate
        projectWindow.setWindowTitle(_translate("projectWindow", "Project Window"))
        self.generalDetails_proj_abbv.setText(_translate("projectWindow", "<Proj abbv>"))
        self.generalDetails_proj_code.setText(_translate("projectWindow", "<Proj code>"))
        self.generalDetails_proj_phase.setText(_translate("projectWindow", "<Phase:>"))
        self.generalDetails_proj_completion.setText(_translate("projectWindow", "<Completion:>"))
        self.generalDescription_open_issues.setText(_translate("projectWindow", "<No. of open issues: >"))
        self.generalDescription_closed_issues.setText(_translate("projectWindow", "<No. of closed issues: >"))
        self.generalDescription_dwg_count.setText(_translate("projectWindow", "<No. DWG files: >"))
        self.generalDescription_bim_count.setText(_translate("projectWindow", "<No. BIM files: >"))
        self.generalDescription_excel_count.setText(_translate("projectWindow", "<No. Excel files: >"))
        self.generalDescription_pdf_count.setText(_translate("projectWindow", "<No. PDF files: >"))
        self.generalDetails_proj_title.setText(_translate("projectWindow", "<Proj title>"))
        self.myIssues_btn.setTabText(self.myIssues_btn.indexOf(self.generalDetails_btn), _translate("projectWindow", "General Details"))
        self.workFlow_current_pahse.setText(_translate("projectWindow", "<Current Phase: >"))
        self.workFlow_work_flow_name.setText(_translate("projectWindow", "Workflow:"))
        self.flowEdit_btn.setText(_translate("projectWindow", "Edit Work FLow"))
        self.phase_name.setText(_translate("projectWindow", "<Phase:>"))
        self.phase_status.setText(_translate("projectWindow", "<Status:>"))
        self.phase_openIssues_count.setText(_translate("projectWindow", "<Open Issues:>"))
        self.phase_totalIssues_count.setText(_translate("projectWindow", "<Total issues:>"))
        self.phase_internal_flowName.setText(_translate("projectWindow", "<Internal Flow:>"))
        self.phase_totalDocs_count.setText(_translate("projectWindow", "<No. of docs:>"))
        self.setStatus_btn.setText(_translate("projectWindow", "CLOSE PHASE"))
        self.myIssues_btn.setTabText(self.myIssues_btn.indexOf(self.workFlow_btn), _translate("projectWindow", "Work Flow"))
        self.label_2.setText(_translate("projectWindow", "Phase:"))
        self.label.setText(_translate("projectWindow", "Workflow:"))
        self.raiseIssue_btn.setText(_translate("projectWindow", "Raise Issue"))
        self.showIssues_btn.setText(_translate("projectWindow", "Show Issues"))
        self.issuesBoard_pending_issues_count.setText(_translate("projectWindow", "<Pending Issues:>"))
        self.issuesBoard_closed_issues_count.setText(_translate("projectWindow", "<Closed Issues:>"))
        self.issuesBoard_open_issues_count.setText(_translate("projectWindow", "<Open Issues:>"))
        self.myIssues_btn.setTabText(self.myIssues_btn.indexOf(self.issuesBoard_btn), _translate("projectWindow", "Issues Board"))
        self.add_newDocs_list_btn.setText(_translate("projectWindow", "New Document List"))
        self.label_3.setText(_translate("projectWindow", "Workflow:"))
        self.myIssues_btn.setTabText(self.myIssues_btn.indexOf(self.docsList_btn), _translate("projectWindow", "Doccumentation"))
        self.ganttChart_proj_title.setText(_translate("projectWindow", "<Proj Title>"))
        self.ganttChart_proj_code.setText(_translate("projectWindow", "<Proj Code>"))
        self.pushButton.setText(_translate("projectWindow", "Edit Chart"))
        self.myIssues_btn.setTabText(self.myIssues_btn.indexOf(self.ganttChart_btn), _translate("projectWindow", "Gantt Chart"))
        self.members_totalMembers_count.setText(_translate("projectWindow", "<Total Members:>"))
        self.members_editmembers_btn.setText(_translate("projectWindow", "Edit Members"))
        self.members_sortDepartment_btn.setText(_translate("projectWindow", "Sort by Department"))
        self.members_sortName_btn.setText(_translate("projectWindow", "Sort by Name"))
        self.myIssues_btn.setTabText(self.myIssues_btn.indexOf(self.projMembers_btn), _translate("projectWindow", "Project Members"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_projectWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())