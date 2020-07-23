# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'demoDeleteUser.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(463, 299)
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(20, 20, 141, 16))
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
        self.label_4.setGeometry(QtCore.QRect(20, 70, 121, 16))
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
        self.pushButtonDelete = QtWidgets.QPushButton(Dialog)
        self.pushButtonDelete.setGeometry(QtCore.QRect(170, 120, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButtonDelete.setFont(font)
        self.pushButtonDelete.setObjectName("pushButtonDelete")
        self.labelSure = QtWidgets.QLabel(Dialog)
        self.labelSure.setGeometry(QtCore.QRect(60, 180, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.labelSure.setFont(font)
        self.labelSure.setObjectName("labelSure")
        self.pushButtonYes = QtWidgets.QPushButton(Dialog)
        self.pushButtonYes.setGeometry(QtCore.QRect(190, 180, 75, 23))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButtonYes.setFont(font)
        self.pushButtonYes.setObjectName("pushButtonYes")
        self.pushButtonNo = QtWidgets.QPushButton(Dialog)
        self.pushButtonNo.setGeometry(QtCore.QRect(320, 180, 75, 23))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButtonNo.setFont(font)
        self.pushButtonNo.setObjectName("pushButtonNo")
        self.labelResponse = QtWidgets.QLabel(Dialog)
        self.labelResponse.setGeometry(QtCore.QRect(30, 240, 391, 31))
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
        self.pushButtonDelete.setText(_translate("Dialog", "Delete User"))
        self.labelSure.setText(_translate("Dialog", "Are you Sure ?"))
        self.pushButtonYes.setText(_translate("Dialog", "Yes"))
        self.pushButtonNo.setText(_translate("Dialog", "No"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

