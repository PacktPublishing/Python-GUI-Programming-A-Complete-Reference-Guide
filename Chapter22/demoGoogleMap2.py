# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'demoGoogleMap2.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(503, 418)
        self.lineEditLongitude = QtWidgets.QLineEdit(Dialog)
        self.lineEditLongitude.setGeometry(QtCore.QRect(170, 49, 271, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEditLongitude.setFont(font)
        self.lineEditLongitude.setObjectName("lineEditLongitude")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 50, 141, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButtonSearch = QtWidgets.QPushButton(Dialog)
        self.pushButtonSearch.setGeometry(QtCore.QRect(190, 140, 75, 23))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButtonSearch.setFont(font)
        self.pushButtonSearch.setObjectName("pushButtonSearch")
        self.labelLocation = QtWidgets.QLabel(Dialog)
        self.labelLocation.setGeometry(QtCore.QRect(30, 190, 431, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.labelLocation.setFont(font)
        self.labelLocation.setText("")
        self.labelLocation.setObjectName("labelLocation")
        self.labelCity = QtWidgets.QLabel(Dialog)
        self.labelCity.setGeometry(QtCore.QRect(30, 240, 431, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.labelCity.setFont(font)
        self.labelCity.setText("")
        self.labelCity.setObjectName("labelCity")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(60, 10, 421, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.labelCountry = QtWidgets.QLabel(Dialog)
        self.labelCountry.setGeometry(QtCore.QRect(30, 290, 431, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.labelCountry.setFont(font)
        self.labelCountry.setText("")
        self.labelCountry.setObjectName("labelCountry")
        self.labelPostalCode = QtWidgets.QLabel(Dialog)
        self.labelPostalCode.setGeometry(QtCore.QRect(30, 340, 431, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.labelPostalCode.setFont(font)
        self.labelPostalCode.setText("")
        self.labelPostalCode.setObjectName("labelPostalCode")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(20, 91, 141, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.lineEditLatitude = QtWidgets.QLineEdit(Dialog)
        self.lineEditLatitude.setGeometry(QtCore.QRect(170, 90, 271, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEditLatitude.setFont(font)
        self.lineEditLatitude.setObjectName("lineEditLatitude")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Enter Longitude"))
        self.pushButtonSearch.setText(_translate("Dialog", "Search"))
        self.label_2.setText(_translate("Dialog", "Find out the Location, City, Country and Postal Code"))
        self.label_3.setText(_translate("Dialog", "Enter Latitude"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

