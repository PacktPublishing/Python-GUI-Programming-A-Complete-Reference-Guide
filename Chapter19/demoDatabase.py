# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'demoDatabase.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(453, 159)
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
        self.pushButtonCreateDB = QtWidgets.QPushButton(Dialog)
        self.pushButtonCreateDB.setGeometry(QtCore.QRect(160, 70, 141, 23))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButtonCreateDB.setFont(font)
        self.pushButtonCreateDB.setObjectName("pushButtonCreateDB")
        self.labelResponse = QtWidgets.QLabel(Dialog)
        self.labelResponse.setGeometry(QtCore.QRect(40, 120, 391, 20))
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
        self.pushButtonCreateDB.setText(_translate("Dialog", "Create Database"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

