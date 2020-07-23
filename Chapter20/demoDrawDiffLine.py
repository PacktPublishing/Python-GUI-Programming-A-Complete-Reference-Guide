# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'demoDrawDiffLine.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(527, 409)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 10, 481, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.listWidgetLineType = QtWidgets.QListWidget(Dialog)
        self.listWidgetLineType.setGeometry(QtCore.QRect(10, 70, 131, 141))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.listWidgetLineType.setFont(font)
        self.listWidgetLineType.setObjectName("listWidgetLineType")
        item = QtWidgets.QListWidgetItem()
        self.listWidgetLineType.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidgetLineType.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidgetLineType.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidgetLineType.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidgetLineType.addItem(item)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Select the style from the list and then click and drag to draw a line"))
        __sortingEnabled = self.listWidgetLineType.isSortingEnabled()
        self.listWidgetLineType.setSortingEnabled(False)
        item = self.listWidgetLineType.item(0)
        item.setText(_translate("Dialog", "SolidLine"))
        item = self.listWidgetLineType.item(1)
        item.setText(_translate("Dialog", "DashLine"))
        item = self.listWidgetLineType.item(2)
        item.setText(_translate("Dialog", "DashDotLine"))
        item = self.listWidgetLineType.item(3)
        item.setText(_translate("Dialog", "DotLine"))
        item = self.listWidgetLineType.item(4)
        item.setText(_translate("Dialog", "DashDotDotLine"))
        self.listWidgetLineType.setSortingEnabled(__sortingEnabled)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

