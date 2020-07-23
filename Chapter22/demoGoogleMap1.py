# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'demoGoogleMap1.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(503, 362)
        self.lineEditLocation = QtWidgets.QLineEdit(Dialog)
        self.lineEditLocation.setGeometry(QtCore.QRect(170, 49, 271, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEditLocation.setFont(font)
        self.lineEditLocation.setObjectName("lineEditLocation")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 50, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButtonSearch = QtWidgets.QPushButton(Dialog)
        self.pushButtonSearch.setGeometry(QtCore.QRect(180, 100, 75, 23))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButtonSearch.setFont(font)
        self.pushButtonSearch.setObjectName("pushButtonSearch")
        self.labelCity = QtWidgets.QLabel(Dialog)
        self.labelCity.setGeometry(QtCore.QRect(30, 150, 431, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.labelCity.setFont(font)
        self.labelCity.setText("")
        self.labelCity.setObjectName("labelCity")
        self.labelPostalCode = QtWidgets.QLabel(Dialog)
        self.labelPostalCode.setGeometry(QtCore.QRect(30, 200, 431, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.labelPostalCode.setFont(font)
        self.labelPostalCode.setText("")
        self.labelPostalCode.setObjectName("labelPostalCode")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(50, 10, 431, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.labelLongitude = QtWidgets.QLabel(Dialog)
        self.labelLongitude.setGeometry(QtCore.QRect(30, 250, 431, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.labelLongitude.setFont(font)
        self.labelLongitude.setText("")
        self.labelLongitude.setObjectName("labelLongitude")
        self.labelLatitude = QtWidgets.QLabel(Dialog)
        self.labelLatitude.setGeometry(QtCore.QRect(30, 300, 431, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.labelLatitude.setFont(font)
        self.labelLatitude.setText("")
        self.labelLatitude.setObjectName("labelLatitude")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Enter location"))
        self.pushButtonSearch.setText(_translate("Dialog", "Search"))
        self.label_2.setText(_translate("Dialog", "Find out the City, Postal Code, Longitude and Latitude"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

