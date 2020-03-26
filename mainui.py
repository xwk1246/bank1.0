# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\Users\winston\Desktop\pyBank\mainui.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Main(object):
    def setupUi(self, Main):
        Main.setObjectName("Main")
        Main.resize(412, 302)
        self.centralwidget = QtWidgets.QWidget(Main)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.button_login = QtWidgets.QPushButton(self.centralwidget)
        self.button_login.setGeometry(QtCore.QRect(190, 200, 111, 31))
        self.button_login.setObjectName("button_login")
        self.label_title = QtWidgets.QLabel(self.centralwidget)
        self.label_title.setGeometry(QtCore.QRect(100, 30, 241, 41))
        font = QtGui.QFont()
        font.setFamily("Adobe Devanagari")
        font.setPointSize(36)
        self.label_title.setFont(font)
        self.label_title.setObjectName("label_title")
        self.lineEdit_acc = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_acc.setGeometry(QtCore.QRect(100, 110, 201, 20))
        self.lineEdit_acc.setObjectName("lineEdit_acc")
        self.lineEdit_psw = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_psw.setGeometry(QtCore.QRect(100, 140, 201, 20))
        self.lineEdit_psw.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_psw.setObjectName("lineEdit_psw")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(80, 200, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Adobe Devanagari")
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.button_reg = QtWidgets.QPushButton(self.centralwidget)
        self.button_reg.setGeometry(QtCore.QRect(190, 170, 111, 31))
        self.button_reg.setObjectName("button_reg")
        self.button_reset = QtWidgets.QPushButton(self.centralwidget)
        self.button_reset.setGeometry(QtCore.QRect(320, 260, 75, 23))
        self.button_reset.setObjectName("button_reset")
        Main.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Main)
        self.statusbar.setEnabled(True)
        self.statusbar.setObjectName("statusbar")
        Main.setStatusBar(self.statusbar)

        self.retranslateUi(Main)
        self.button_login.clicked.connect(Main.login)
        self.button_reg.clicked.connect(Main.open_reg)
        self.button_reset.clicked.connect(Main.reset)
        QtCore.QMetaObject.connectSlotsByName(Main)

    def retranslateUi(self, Main):
        _translate = QtCore.QCoreApplication.translate
        Main.setWindowTitle(_translate("Main", "PyBank"))
        self.button_login.setText(_translate("Main", "登入"))
        self.label_title.setText(_translate("Main", "PyBank 1.0"))
        self.lineEdit_acc.setPlaceholderText(_translate("Main", "請輸入帳號"))
        self.lineEdit_psw.setPlaceholderText(_translate("Main", "請輸入密碼"))
        self.button_reg.setText(_translate("Main", "註冊帳號"))
        self.button_reset.setText(_translate("Main", "清除帳號"))
