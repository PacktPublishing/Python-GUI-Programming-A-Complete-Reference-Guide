# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'demoAnimation1.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 238)
        self.pushButtonMoveDown = QtWidgets.QPushButton(Dialog)
        self.pushButtonMoveDown.setGeometry(QtCore.QRect(20, 50, 121, 23))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButtonMoveDown.setFont(font)
        self.pushButtonMoveDown.setObjectName("pushButtonMoveDown")
        self.labelPic = QtWidgets.QLabel(Dialog)
        self.labelPic.setGeometry(QtCore.QRect(160, 60, 91, 91))
        self.labelPic.setText("")
        self.labelPic.setPixmap(QtGui.QPixmap("coloredball.jpg"))
        self.labelPic.setObjectName("labelPic")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButtonMoveDown.setText(_translate("Dialog", "Move Down"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

