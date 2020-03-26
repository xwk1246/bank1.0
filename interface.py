# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\Users\winston\Desktop\pyBank\interface.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_inter(object):
    def setupUi(self, inter):
        inter.setObjectName("inter")
        inter.resize(371, 259)
        self.label_user = QtWidgets.QLabel(inter)
        self.label_user.setGeometry(QtCore.QRect(130, 30, 151, 16))
        font = QtGui.QFont()
        font.setFamily("新細明體")
        font.setPointSize(12)
        self.label_user.setFont(font)
        self.label_user.setText("")
        self.label_user.setObjectName("label_user")
        self.label1 = QtWidgets.QLabel(inter)
        self.label1.setGeometry(QtCore.QRect(40, 30, 81, 21))
        font = QtGui.QFont()
        font.setFamily("Adobe Devanagari")
        font.setPointSize(12)
        self.label1.setFont(font)
        self.label1.setObjectName("label1")
        self.label2 = QtWidgets.QLabel(inter)
        self.label2.setGeometry(QtCore.QRect(40, 60, 81, 21))
        font = QtGui.QFont()
        font.setFamily("Adobe Devanagari")
        font.setPointSize(12)
        self.label2.setFont(font)
        self.label2.setObjectName("label2")
        self.Button_deposit = QtWidgets.QPushButton(inter)
        self.Button_deposit.setGeometry(QtCore.QRect(200, 130, 111, 31))
        self.Button_deposit.setObjectName("Button_deposit")
        self.Button_withdraw = QtWidgets.QPushButton(inter)
        self.Button_withdraw.setGeometry(QtCore.QRect(200, 180, 111, 31))
        self.Button_withdraw.setObjectName("Button_withdraw")
        self.lineEdit = QtWidgets.QLineEdit(inter)
        self.lineEdit.setGeometry(QtCore.QRect(40, 130, 131, 31))
        self.lineEdit.setInputMask("")
        self.lineEdit.setObjectName("lineEdit")
        self.label_balance = QtWidgets.QLabel(inter)
        self.label_balance.setGeometry(QtCore.QRect(130, 60, 151, 16))
        font = QtGui.QFont()
        font.setFamily("新細明體")
        font.setPointSize(12)
        self.label_balance.setFont(font)
        self.label_balance.setText("")
        self.label_balance.setObjectName("label_balance")
        self.label_status = QtWidgets.QLabel(inter)
        self.label_status.setGeometry(QtCore.QRect(40, 190, 131, 20))
        font = QtGui.QFont()
        font.setFamily("Adobe Devanagari")
        font.setPointSize(11)
        self.label_status.setFont(font)
        self.label_status.setText("")
        self.label_status.setObjectName("label_status")

        self.retranslateUi(inter)
        self.Button_withdraw.clicked.connect(inter.withdraw)
        self.Button_deposit.clicked.connect(inter.deposit)
        QtCore.QMetaObject.connectSlotsByName(inter)

    def retranslateUi(self, inter):
        _translate = QtCore.QCoreApplication.translate
        inter.setWindowTitle(_translate("inter", "功能"))
        self.label1.setText(_translate("inter", "當前帳號："))
        self.label2.setText(_translate("inter", "剩餘金額："))
        self.Button_deposit.setText(_translate("inter", "存款"))
        self.Button_withdraw.setText(_translate("inter", "提款"))
        self.lineEdit.setPlaceholderText(_translate("inter", "請輸入金額"))
