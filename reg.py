# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\Users\winston\Desktop\pyBank\bank1.0\reg.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 154)
        self.create_acc = QtWidgets.QLineEdit(Dialog)
        self.create_acc.setGeometry(QtCore.QRect(70, 40, 141, 20))
        self.create_acc.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.create_acc.setMaxLength(12)
        self.create_acc.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.create_acc.setObjectName("create_acc")
        self.create_psw = QtWidgets.QLineEdit(Dialog)
        self.create_psw.setGeometry(QtCore.QRect(70, 70, 141, 20))
        self.create_psw.setMaxLength(20)
        self.create_psw.setEchoMode(QtWidgets.QLineEdit.Password)
        self.create_psw.setObjectName("create_psw")
        self.confirm_psw = QtWidgets.QLineEdit(Dialog)
        self.confirm_psw.setGeometry(QtCore.QRect(70, 100, 141, 20))
        self.confirm_psw.setInputMask("")
        self.confirm_psw.setMaxLength(20)
        self.confirm_psw.setEchoMode(QtWidgets.QLineEdit.Password)
        self.confirm_psw.setObjectName("confirm_psw")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(270, 100, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(260, 70, 131, 21))
        self.label.setText("")
        self.label.setObjectName("label")

        self.retranslateUi(Dialog)
        self.pushButton.clicked.connect(Dialog.submit)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "註冊"))
        self.create_acc.setPlaceholderText(_translate("Dialog", "建立帳號"))
        self.create_psw.setPlaceholderText(_translate("Dialog", "建立密碼"))
        self.confirm_psw.setPlaceholderText(_translate("Dialog", "確認密碼"))
        self.pushButton.setText(_translate("Dialog", "提交"))
