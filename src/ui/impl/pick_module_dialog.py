# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'handin_lecturer_main_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(500, 300)
        Dialog.setMinimumSize(QtCore.QSize(500, 300))
        Dialog.setMaximumSize(QtCore.QSize(500, 300))
        self.label_alert = QtWidgets.QLabel(Dialog)
        self.label_alert.setObjectName("label_alert")
        self.label_alert.setGeometry(175, 20, 160, 30)
        self.comboBox_modules = QtWidgets.QComboBox(Dialog)
        self.comboBox_modules.setObjectName("comboBox_modules")
        self.comboBox_modules.setGeometry(175, 100, 150, 30)
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setGeometry(175, 180, 150, 30)
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Handin System (Lecturer)"))
        self.pushButton.setText(_translate("Dialog", "Next"))
        self.label_alert.setText(_translate("Dialog", "Pick a module to access."))
