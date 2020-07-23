# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'demoGoogleMap3.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(503, 267)
        self.lineEditFirstLocation = QtWidgets.QLineEdit(Dialog)
        self.lineEditFirstLocation.setGeometry(QtCore.QRect(210, 50, 271, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEditFirstLocation.setFont(font)
        self.lineEditFirstLocation.setObjectName("lineEditFirstLocation")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 50, 141, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButtonFindDistance = QtWidgets.QPushButton(Dialog)
        self.pushButtonFindDistance.setGeometry(QtCore.QRect(190, 140, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButtonFindDistance.setFont(font)
        self.pushButtonFindDistance.setObjectName("pushButtonFindDistance")
        self.labelDistance = QtWidgets.QLabel(Dialog)
        self.labelDistance.setGeometry(QtCore.QRect(30, 190, 431, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.labelDistance.setFont(font)
        self.labelDistance.setText("")
        self.labelDistance.setObjectName("labelDistance")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(60, 10, 421, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(20, 91, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.lineEditSecondLocation = QtWidgets.QLineEdit(Dialog)
        self.lineEditSecondLocation.setGeometry(QtCore.QRect(210, 90, 271, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEditSecondLocation.setFont(font)
        self.lineEditSecondLocation.setObjectName("lineEditSecondLocation")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Enter first location"))
        self.pushButtonFindDistance.setText(_translate("Dialog", "Find Distance"))
        self.label_2.setText(_translate("Dialog", "Find out the distance between two locations"))
        self.label_3.setText(_translate("Dialog", "Enter second location"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

