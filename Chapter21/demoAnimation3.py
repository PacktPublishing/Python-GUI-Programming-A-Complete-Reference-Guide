# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'demoAnimation3.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(495, 282)
        self.pushButtonBounce = QtWidgets.QPushButton(Dialog)
        self.pushButtonBounce.setGeometry(QtCore.QRect(180, 100, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButtonBounce.setFont(font)
        self.pushButtonBounce.setObjectName("pushButtonBounce")
        self.labelPic = QtWidgets.QLabel(Dialog)
        self.labelPic.setGeometry(QtCore.QRect(0, 0, 81, 91))
        self.labelPic.setText("")
        self.labelPic.setPixmap(QtGui.QPixmap("coloredball.jpg"))
        self.labelPic.setObjectName("labelPic")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButtonBounce.setText(_translate("Dialog", "Bounce"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

