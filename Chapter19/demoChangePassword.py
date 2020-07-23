# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'demoChangePassword.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(478, 332)
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(30, 20, 141, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.lineEditEmailAddress = QtWidgets.QLineEdit(Dialog)
        self.lineEditEmailAddress.setGeometry(QtCore.QRect(190, 20, 241, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEditEmailAddress.setFont(font)
        self.lineEditEmailAddress.setObjectName("lineEditEmailAddress")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(30, 70, 121, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.lineEditOldPassword = QtWidgets.QLineEdit(Dialog)
        self.lineEditOldPassword.setGeometry(QtCore.QRect(190, 70, 241, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEditOldPassword.setFont(font)
        self.lineEditOldPassword.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEditOldPassword.setObjectName("lineEditOldPassword")
        self.pushButtonChangePassword = QtWidgets.QPushButton(Dialog)
        self.pushButtonChangePassword.setGeometry(QtCore.QRect(160, 230, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButtonChangePassword.setFont(font)
        self.pushButtonChangePassword.setObjectName("pushButtonChangePassword")
        self.labelResponse = QtWidgets.QLabel(Dialog)
        self.labelResponse.setGeometry(QtCore.QRect(30, 280, 411, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.labelResponse.setFont(font)
        self.labelResponse.setText("")
        self.labelResponse.setObjectName("labelResponse")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(40, 120, 131, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(10, 180, 181, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.lineEditNewPassword = QtWidgets.QLineEdit(Dialog)
        self.lineEditNewPassword.setGeometry(QtCore.QRect(190, 120, 241, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEditNewPassword.setFont(font)
        self.lineEditNewPassword.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEditNewPassword.setObjectName("lineEditNewPassword")
        self.lineEditRePassword = QtWidgets.QLineEdit(Dialog)
        self.lineEditRePassword.setGeometry(QtCore.QRect(190, 180, 241, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEditRePassword.setFont(font)
        self.lineEditRePassword.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEditRePassword.setObjectName("lineEditRePassword")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_3.setText(_translate("Dialog", "Email Address"))
        self.label_4.setText(_translate("Dialog", "Old Password"))
        self.pushButtonChangePassword.setText(_translate("Dialog", "Change Password"))
        self.label.setText(_translate("Dialog", "New Password"))
        self.label_2.setText(_translate("Dialog", "Re-enter New Password"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

