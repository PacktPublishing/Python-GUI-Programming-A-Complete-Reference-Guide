# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'demoMouseClicks.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(565, 265)
        self.labelPress = QtWidgets.QLabel(Dialog)
        self.labelPress.setGeometry(QtCore.QRect(20, 60, 521, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.labelPress.setFont(font)
        self.labelPress.setText("")
        self.labelPress.setObjectName("labelPress")
        self.labelRelease = QtWidgets.QLabel(Dialog)
        self.labelRelease.setGeometry(QtCore.QRect(20, 100, 521, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.labelRelease.setFont(font)
        self.labelRelease.setText("")
        self.labelRelease.setObjectName("labelRelease")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 10, 531, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Displays the x, y co-ordinates where mouse button is pressed and released"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

