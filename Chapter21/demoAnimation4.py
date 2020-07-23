# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'demoAnimation4.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(495, 282)
        self.pushButtonMoveCurve = QtWidgets.QPushButton(Dialog)
        self.pushButtonMoveCurve.setGeometry(QtCore.QRect(170, 100, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButtonMoveCurve.setFont(font)
        self.pushButtonMoveCurve.setObjectName("pushButtonMoveCurve")
        self.labelPic = QtWidgets.QLabel(Dialog)
        self.labelPic.setGeometry(QtCore.QRect(10, 0, 81, 91))
        self.labelPic.setText("")
        self.labelPic.setPixmap(QtGui.QPixmap("coloredball.jpg"))
        self.labelPic.setObjectName("labelPic")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButtonMoveCurve.setText(_translate("Dialog", "Move With Curve"))

