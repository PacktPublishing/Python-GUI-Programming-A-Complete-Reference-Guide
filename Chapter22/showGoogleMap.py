# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'showGoogleMap.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(562, 488)
        self.widget = QWebEngineView(Dialog)
        self.widget.setGeometry(QtCore.QRect(10, 160, 531, 301))
        self.widget.setObjectName("widget")
        self.pushButtonShowMap = QtWidgets.QPushButton(Dialog)
        self.pushButtonShowMap.setGeometry(QtCore.QRect(210, 110, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButtonShowMap.setFont(font)
        self.pushButtonShowMap.setObjectName("pushButtonShowMap")
        self.lineEditLongitude = QtWidgets.QLineEdit(Dialog)
        self.lineEditLongitude.setGeometry(QtCore.QRect(100, 20, 331, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEditLongitude.setFont(font)
        self.lineEditLongitude.setObjectName("lineEditLongitude")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 20, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.lineEditLatitude = QtWidgets.QLineEdit(Dialog)
        self.lineEditLatitude.setGeometry(QtCore.QRect(100, 60, 331, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEditLatitude.setFont(font)
        self.lineEditLatitude.setObjectName("lineEditLatitude")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(20, 60, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButtonShowMap.setText(_translate("Dialog", "Show Map"))
        self.label.setText(_translate("Dialog", "Longitude"))
        self.label_2.setText(_translate("Dialog", "Latitude"))

from PyQt5.QtWebEngineWidgets import QWebEngineView

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

