# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'createAssignment_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(789, 930)
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(20, 100, 101, 16))
        self.label_4.setObjectName("label_4")
        self.dateTimeEdit_startDay = QtWidgets.QDateTimeEdit(Dialog)
        self.dateTimeEdit_startDay.setGeometry(QtCore.QRect(160, 60, 141, 22))
        self.dateTimeEdit_startDay.setObjectName("dateTimeEdit_startDay")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(410, 100, 141, 16))
        self.label_5.setObjectName("label_5")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(20, 60, 121, 16))
        self.label_2.setObjectName("label_2")
        self.groupBox_compilation = QtWidgets.QGroupBox(Dialog)
        self.groupBox_compilation.setGeometry(QtCore.QRect(20, 290, 741, 81))
        font = QtGui.QFont()
        font.setItalic(True)
        self.groupBox_compilation.setFont(font)
        self.groupBox_compilation.setCheckable(True)
        self.groupBox_compilation.setChecked(False)
        self.groupBox_compilation.setObjectName("groupBox_compilation")
        self.label_13 = QtWidgets.QLabel(self.groupBox_compilation)
        self.label_13.setGeometry(QtCore.QRect(20, 40, 41, 16))
        self.label_13.setObjectName("label_13")
        self.lineEdit_compilation_tag = QtWidgets.QLineEdit(self.groupBox_compilation)
        self.lineEdit_compilation_tag.setGeometry(QtCore.QRect(60, 40, 113, 21))
        self.lineEdit_compilation_tag.setObjectName("lineEdit_compilation_tag")
        self.label_14 = QtWidgets.QLabel(self.groupBox_compilation)
        self.label_14.setGeometry(QtCore.QRect(220, 40, 72, 15))
        self.label_14.setObjectName("label_14")
        self.lineEdit_compilation_marks = QtWidgets.QLineEdit(self.groupBox_compilation)
        self.lineEdit_compilation_marks.setGeometry(QtCore.QRect(290, 40, 51, 21))
        self.lineEdit_compilation_marks.setObjectName("lineEdit_compilation_marks")
        self.label_15 = QtWidgets.QLabel(self.groupBox_compilation)
        self.label_15.setGeometry(QtCore.QRect(380, 40, 72, 15))
        self.label_15.setObjectName("label_15")
        self.lineEdit_compilation_command = QtWidgets.QLineEdit(self.groupBox_compilation)
        self.lineEdit_compilation_command.setGeometry(QtCore.QRect(460, 40, 211, 21))
        self.lineEdit_compilation_command.setObjectName("lineEdit_compilation_command")
        self.groupBox_attendance = QtWidgets.QGroupBox(Dialog)
        self.groupBox_attendance.setGeometry(QtCore.QRect(20, 210, 371, 71))
        font = QtGui.QFont()
        font.setItalic(True)
        self.groupBox_attendance.setFont(font)
        self.groupBox_attendance.setCheckable(True)
        self.groupBox_attendance.setChecked(False)
        self.groupBox_attendance.setObjectName("groupBox_attendance")
        self.label_12 = QtWidgets.QLabel(self.groupBox_attendance)
        self.label_12.setGeometry(QtCore.QRect(20, 30, 41, 16))
        self.label_12.setObjectName("label_12")
        self.lineEdit_attendance_tag = QtWidgets.QLineEdit(self.groupBox_attendance)
        self.lineEdit_attendance_tag.setGeometry(QtCore.QRect(60, 30, 113, 21))
        self.lineEdit_attendance_tag.setObjectName("lineEdit_attendance_tag")
        self.label_10 = QtWidgets.QLabel(self.groupBox_attendance)
        self.label_10.setGeometry(QtCore.QRect(220, 30, 72, 15))
        self.label_10.setObjectName("label_10")
        self.lineEdit_attendance_marks = QtWidgets.QLineEdit(self.groupBox_attendance)
        self.lineEdit_attendance_marks.setGeometry(QtCore.QRect(290, 30, 51, 21))
        self.lineEdit_attendance_marks.setObjectName("lineEdit_attendance_marks")
        self.spinBox_totalAttempts = QtWidgets.QSpinBox(Dialog)
        self.spinBox_totalAttempts.setGeometry(QtCore.QRect(160, 140, 43, 26))
        self.spinBox_totalAttempts.setObjectName("spinBox_totalAttempts")
        self.label_8 = QtWidgets.QLabel(Dialog)
        self.label_8.setGeometry(QtCore.QRect(20, 180, 51, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.dateTimeEdit_endDay = QtWidgets.QDateTimeEdit(Dialog)
        self.dateTimeEdit_endDay.setGeometry(QtCore.QRect(510, 60, 141, 22))
        self.dateTimeEdit_endDay.setObjectName("dateTimeEdit_endDay")
        self.label_totalMarks = QtWidgets.QLabel(Dialog)
        self.label_totalMarks.setGeometry(QtCore.QRect(595, 180, 121, 17))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_totalMarks.setFont(font)
        self.label_totalMarks.setObjectName("label_totalMarks")
        self.spinBox_penaltyPerDay = QtWidgets.QSpinBox(Dialog)
        self.spinBox_penaltyPerDay.setGeometry(QtCore.QRect(610, 90, 43, 26))
        self.spinBox_penaltyPerDay.setObjectName("spinBox_penaltyPerDay")
        self.lineEdit_collectFilename = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_collectFilename.setGeometry(QtCore.QRect(240, 180, 171, 24))
        self.lineEdit_collectFilename.setObjectName("lineEdit_collectFilename")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(300, 10, 41, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.dateTimeEdit_cutoffDay = QtWidgets.QDateTimeEdit(Dialog)
        self.dateTimeEdit_cutoffDay.setGeometry(QtCore.QRect(160, 100, 141, 22))
        self.dateTimeEdit_cutoffDay.setObjectName("dateTimeEdit_cutoffDay")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 10, 111, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        font.setKerning(True)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(410, 60, 72, 15))
        self.label_3.setObjectName("label_3")
        self.label_11 = QtWidgets.QLabel(Dialog)
        self.label_11.setGeometry(QtCore.QRect(480, 180, 108, 17))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.label_9 = QtWidgets.QLabel(Dialog)
        self.label_9.setGeometry(QtCore.QRect(91, 181, 136, 16))
        self.label_9.setObjectName("label_9")
        self.weekNumber_label = QtWidgets.QLabel(Dialog)
        self.weekNumber_label.setGeometry(QtCore.QRect(510, 10, 41, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.weekNumber_label.setFont(font)
        self.weekNumber_label.setObjectName("weekNumber_label")
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(20, 140, 121, 16))
        self.label_7.setObjectName("label_7")
        self.lineEdit_assName = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_assName.setGeometry(QtCore.QRect(360, 10, 71, 21))
        self.lineEdit_assName.setObjectName("lineEdit_assName")
        self.groupBox_customTest1 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_customTest1.setGeometry(QtCore.QRect(20, 400, 741, 191))
        font = QtGui.QFont()
        font.setItalic(True)
        self.groupBox_customTest1.setFont(font)
        self.groupBox_customTest1.setObjectName("groupBox_customTest1")
        self.label_16 = QtWidgets.QLabel(self.groupBox_customTest1)
        self.label_16.setGeometry(QtCore.QRect(20, 20, 41, 16))
        self.label_16.setObjectName("label_16")
        self.lineEdit_tag = QtWidgets.QLineEdit(self.groupBox_customTest1)
        self.lineEdit_tag.setGeometry(QtCore.QRect(60, 20, 111, 21))
        self.lineEdit_tag.setText("")
        self.lineEdit_tag.setObjectName("lineEdit_tag")
        self.label_17 = QtWidgets.QLabel(self.groupBox_customTest1)
        self.label_17.setGeometry(QtCore.QRect(220, 20, 72, 15))
        self.label_17.setObjectName("label_17")
        self.lineEdit_marks = QtWidgets.QLineEdit(self.groupBox_customTest1)
        self.lineEdit_marks.setGeometry(QtCore.QRect(290, 20, 51, 21))
        self.lineEdit_marks.setObjectName("lineEdit_marks")
        self.label_18 = QtWidgets.QLabel(self.groupBox_customTest1)
        self.label_18.setGeometry(QtCore.QRect(380, 20, 72, 15))
        self.label_18.setObjectName("label_18")
        self.lineEdit_command = QtWidgets.QLineEdit(self.groupBox_customTest1)
        self.lineEdit_command.setGeometry(QtCore.QRect(460, 20, 211, 21))
        self.lineEdit_command.setObjectName("lineEdit_command")
        self.checkBox_inputDataFile = QtWidgets.QCheckBox(self.groupBox_customTest1)
        self.checkBox_inputDataFile.setGeometry(QtCore.QRect(20, 50, 161, 19))
        self.checkBox_inputDataFile.setObjectName("checkBox_inputDataFile")
        self.label_inputDataFile = QtWidgets.QLabel(self.groupBox_customTest1)
        self.label_inputDataFile.setGeometry(QtCore.QRect(160, 50, 511, 16))
        self.label_inputDataFile.setText("")
        self.label_inputDataFile.setObjectName("label_inputDataFile")
        self.checkBox_answerFile = QtWidgets.QCheckBox(self.groupBox_customTest1)
        self.checkBox_answerFile.setGeometry(QtCore.QRect(20, 80, 131, 19))
        self.checkBox_answerFile.setObjectName("checkBox_answerFile")
        self.checkBox_filterFile = QtWidgets.QCheckBox(self.groupBox_customTest1)
        self.checkBox_filterFile.setGeometry(QtCore.QRect(20, 110, 121, 19))
        self.checkBox_filterFile.setObjectName("checkBox_filterFile")
        self.label_answerFile = QtWidgets.QLabel(self.groupBox_customTest1)
        self.label_answerFile.setGeometry(QtCore.QRect(150, 80, 521, 16))
        self.label_answerFile.setText("")
        self.label_answerFile.setObjectName("label_answerFile")
        self.label_filterFile = QtWidgets.QLabel(self.groupBox_customTest1)
        self.label_filterFile.setGeometry(QtCore.QRect(140, 110, 331, 16))
        self.label_filterFile.setText("")
        self.label_filterFile.setObjectName("label_filterFile")
        self.label_28 = QtWidgets.QLabel(self.groupBox_customTest1)
        self.label_28.setGeometry(QtCore.QRect(20, 150, 101, 20))
        self.label_28.setObjectName("label_28")
        self.lineEdit_filterCommand = QtWidgets.QLineEdit(self.groupBox_customTest1)
        self.lineEdit_filterCommand.setGeometry(QtCore.QRect(100, 150, 171, 21))
        self.lineEdit_filterCommand.setObjectName("lineEdit_filterCommand")
        self.addTest = QtWidgets.QPushButton(self.groupBox_customTest1)
        self.addTest.setGeometry(QtCore.QRect(640, 150, 80, 23))
        font = QtGui.QFont()
        font.setItalic(False)
        self.addTest.setFont(font)
        self.addTest.setObjectName("addTest")
        self.weekNumber_comboBox = QtWidgets.QComboBox(Dialog)
        self.weekNumber_comboBox.setGeometry(QtCore.QRect(580, 10, 79, 23))
        self.weekNumber_comboBox.setObjectName("weekNumber_comboBox")
        self.label_module = QtWidgets.QLabel(Dialog)
        self.label_module.setGeometry(QtCore.QRect(150, 10, 57, 15))
        self.label_module.setText("")
        self.label_module.setObjectName("label_module")
        self.label_19 = QtWidgets.QLabel(Dialog)
        self.label_19.setGeometry(QtCore.QRect(20, 380, 71, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_19.setFont(font)
        self.label_19.setObjectName("label_19")
        self.testsGroupBox = QtWidgets.QGroupBox(Dialog)
        self.testsGroupBox.setGeometry(QtCore.QRect(20, 630, 741, 211))
        self.testsGroupBox.setTitle("")
        self.testsGroupBox.setObjectName("testsGroupBox")
        self.testList = QtWidgets.QListWidget(self.testsGroupBox)
        self.testList.setGeometry(QtCore.QRect(10, 10, 491, 191))
        self.testList.setObjectName("testList")
        self.editButton = QtWidgets.QPushButton(self.testsGroupBox)
        self.editButton.setGeometry(QtCore.QRect(570, 30, 80, 23))
        self.editButton.setObjectName("editButton")
        self.label_21 = QtWidgets.QLabel(self.testsGroupBox)
        self.label_21.setGeometry(QtCore.QRect(580, 100, 57, 15))
        self.label_21.setAlignment(QtCore.Qt.AlignCenter)
        self.label_21.setObjectName("label_21")
        self.removeButton = QtWidgets.QPushButton(self.testsGroupBox)
        self.removeButton.setGeometry(QtCore.QRect(570, 160, 80, 23))
        self.removeButton.setObjectName("removeButton")
        self.label_20 = QtWidgets.QLabel(Dialog)
        self.label_20.setGeometry(QtCore.QRect(20, 610, 91, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_20.setFont(font)
        self.label_20.setObjectName("label_20")
        self.createButton = QtWidgets.QPushButton(Dialog)
        self.createButton.setGeometry(QtCore.QRect(660, 880, 80, 23))
        self.createButton.setObjectName("createButton")
        self.cancelButton = QtWidgets.QPushButton(Dialog)
        self.cancelButton.setGeometry(QtCore.QRect(560, 880, 80, 23))
        self.cancelButton.setObjectName("cancelButton")
        self.autoGenerate_checkBox = QtWidgets.QCheckBox(Dialog)
        self.autoGenerate_checkBox.setGeometry(QtCore.QRect(410, 130, 171, 21))
        self.autoGenerate_checkBox.setObjectName("autoGenerate_checkBox")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_4.setText(_translate("Dialog", "Cutoff Day:"))
        self.label_5.setText(_translate("Dialog", "Penalty per day (%):"))
        self.label_2.setText(_translate("Dialog", "Start Day:"))
        self.groupBox_compilation.setTitle(_translate("Dialog", "Compilation"))
        self.label_13.setText(_translate("Dialog", "Tag:"))
        self.lineEdit_compilation_tag.setText(_translate("Dialog", "compilation"))
        self.label_14.setText(_translate("Dialog", "Marks:"))
        self.label_15.setText(_translate("Dialog", "Command:"))
        self.groupBox_attendance.setTitle(_translate("Dialog", "Attendance"))
        self.label_12.setText(_translate("Dialog", "Tag:"))
        self.lineEdit_attendance_tag.setText(_translate("Dialog", "attendance"))
        self.label_10.setText(_translate("Dialog", "Marks:"))
        self.label_8.setText(_translate("Dialog", "Tests:"))
        self.label_totalMarks.setText(_translate("Dialog", "0"))
        self.lineEdit_collectFilename.setPlaceholderText(_translate("Dialog", "spin.cc"))
        self.label_6.setText(_translate("Dialog", "Name:"))
        self.label.setText(_translate("Dialog", "Module Code:"))
        self.label_3.setText(_translate("Dialog", "End Day:"))
        self.label_11.setText(_translate("Dialog", "Total Marks:"))
        self.label_9.setText(_translate("Dialog", "Collect Filename:"))
        self.weekNumber_label.setText(_translate("Dialog", "Week:"))
        self.label_7.setText(_translate("Dialog", "Total Attempts:"))
        self.label_16.setText(_translate("Dialog", "Tag:"))
        self.label_17.setText(_translate("Dialog", "Marks:"))
        self.label_18.setText(_translate("Dialog", "Command:"))
        self.checkBox_inputDataFile.setText(_translate("Dialog", "Input Data File"))
        self.checkBox_answerFile.setText(_translate("Dialog", "Answer File"))
        self.checkBox_filterFile.setText(_translate("Dialog", "Filter File"))
        self.label_28.setText(_translate("Dialog", "Filter Cmd:"))
        self.addTest.setText(_translate("Dialog", "Add Test"))
        self.label_19.setText(_translate("Dialog", "Add Test:"))
        self.editButton.setText(_translate("Dialog", "Edit"))
        self.label_21.setText(_translate("Dialog", "or"))
        self.removeButton.setText(_translate("Dialog", "Remove"))
        self.label_20.setText(_translate("Dialog", "Added Tests:"))
        self.createButton.setText(_translate("Dialog", "Create"))
        self.cancelButton.setText(_translate("Dialog", "Cancel"))
        self.autoGenerate_checkBox.setText(_translate("Dialog", "Auto-generate dates"))
