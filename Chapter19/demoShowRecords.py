# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'demoShowRecords.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(476, 236)
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(30, 20, 141, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.lineEditEmailAddress = QtWidgets.QLineEdit(Dialog)
        self.lineEditEmailAddress.setGeometry(QtCore.QRect(180, 20, 241, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEditEmailAddress.setFont(font)
        self.lineEditEmailAddress.setObjectName("lineEditEmailAddress")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(60, 70, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.lineEditPassword = QtWidgets.QLineEdit(Dialog)
        self.lineEditPassword.setGeometry(QtCore.QRect(180, 70, 241, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEditPassword.setFont(font)
        self.lineEditPassword.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEditPassword.setObjectName("lineEditPassword")
        self.pushButtonFirst = QtWidgets.QPushButton(Dialog)
        self.pushButtonFirst.setGeometry(QtCore.QRect(10, 120, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButtonFirst.setFont(font)
        self.pushButtonFirst.setObjectName("pushButtonFirst")
        self.pushButtonPrevious = QtWidgets.QPushButton(Dialog)
        self.pushButtonPrevious.setGeometry(QtCore.QRect(140, 120, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButtonPrevious.setFont(font)
        self.pushButtonPrevious.setObjectName("pushButtonPrevious")
        self.pushButtonNext = QtWidgets.QPushButton(Dialog)
        self.pushButtonNext.setGeometry(QtCore.QRect(250, 120, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButtonNext.setFont(font)
        self.pushButtonNext.setObjectName("pushButtonNext")
        self.pushButtonLast = QtWidgets.QPushButton(Dialog)
        self.pushButtonLast.setGeometry(QtCore.QRect(360, 120, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButtonLast.setFont(font)
        self.pushButtonLast.setObjectName("pushButtonLast")
        self.labelResponse = QtWidgets.QLabel(Dialog)
        self.labelResponse.setGeometry(QtCore.QRect(20, 180, 431, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.labelResponse.setFont(font)
        self.labelResponse.setText("")
        self.labelResponse.setObjectName("labelResponse")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_3.setText(_translate("Dialog", "Email Address"))
        self.label_4.setText(_translate("Dialog", "Password"))
        self.pushButtonFirst.setText(_translate("Dialog", "First Row"))
        self.pushButtonPrevious.setText(_translate("Dialog", "Previous"))
        self.pushButtonNext.setText(_translate("Dialog", "Next"))
        self.pushButtonLast.setText(_translate("Dialog", "Last Row"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

