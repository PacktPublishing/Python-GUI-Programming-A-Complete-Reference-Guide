# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'demoInsertRowsInTable.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(509, 343)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 20, 151, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.lineEditDBName = QtWidgets.QLineEdit(Dialog)
        self.lineEditDBName.setGeometry(QtCore.QRect(180, 20, 241, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEditDBName.setFont(font)
        self.lineEditDBName.setObjectName("lineEditDBName")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(20, 70, 131, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.lineEditTableName = QtWidgets.QLineEdit(Dialog)
        self.lineEditTableName.setGeometry(QtCore.QRect(180, 70, 241, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEditTableName.setFont(font)
        self.lineEditTableName.setObjectName("lineEditTableName")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(20, 120, 141, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.lineEditEmailAddress = QtWidgets.QLineEdit(Dialog)
        self.lineEditEmailAddress.setGeometry(QtCore.QRect(180, 120, 241, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEditEmailAddress.setFont(font)
        self.lineEditEmailAddress.setObjectName("lineEditEmailAddress")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(30, 170, 121, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.lineEditPassword = QtWidgets.QLineEdit(Dialog)
        self.lineEditPassword.setGeometry(QtCore.QRect(180, 170, 241, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEditPassword.setFont(font)
        self.lineEditPassword.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEditPassword.setObjectName("lineEditPassword")
        self.pushButtonInsertRow = QtWidgets.QPushButton(Dialog)
        self.pushButtonInsertRow.setGeometry(QtCore.QRect(190, 230, 141, 23))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButtonInsertRow.setFont(font)
        self.pushButtonInsertRow.setObjectName("pushButtonInsertRow")
        self.labelResponse = QtWidgets.QLabel(Dialog)
        self.labelResponse.setGeometry(QtCore.QRect(30, 290, 441, 20))
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
        self.label.setText(_translate("Dialog", "Enter database name"))
        self.label_2.setText(_translate("Dialog", "Enter table name"))
        self.label_3.setText(_translate("Dialog", "Email Address"))
        self.label_4.setText(_translate("Dialog", "Password"))
        self.pushButtonInsertRow.setText(_translate("Dialog", "Insert Row"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

