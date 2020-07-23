# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'demoDrawText.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(620, 407)
        self.textEdit = QtWidgets.QTextEdit(Dialog)
        self.textEdit.setGeometry(QtCore.QRect(20, 40, 201, 141))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.textEdit.setFont(font)
        self.textEdit.setObjectName("textEdit")
        self.listWidgetFont = QtWidgets.QListWidget(Dialog)
        self.listWidgetFont.setGeometry(QtCore.QRect(230, 40, 161, 141))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.listWidgetFont.setFont(font)
        self.listWidgetFont.setObjectName("listWidgetFont")
        item = QtWidgets.QListWidgetItem()
        self.listWidgetFont.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidgetFont.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidgetFont.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidgetFont.addItem(item)
        self.comboBoxFontSize = QtWidgets.QComboBox(Dialog)
        self.comboBoxFontSize.setGeometry(QtCore.QRect(410, 40, 69, 22))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.comboBoxFontSize.setFont(font)
        self.comboBoxFontSize.setObjectName("comboBoxFontSize")
        self.comboBoxFontSize.addItem("")
        self.comboBoxFontSize.addItem("")
        self.comboBoxFontSize.addItem("")
        self.comboBoxFontSize.addItem("")
        self.comboBoxFontSize.addItem("")
        self.pushButtonDrawText = QtWidgets.QPushButton(Dialog)
        self.pushButtonDrawText.setGeometry(QtCore.QRect(510, 40, 91, 23))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButtonDrawText.setFont(font)
        self.pushButtonDrawText.setObjectName("pushButtonDrawText")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 10, 581, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        __sortingEnabled = self.listWidgetFont.isSortingEnabled()
        self.listWidgetFont.setSortingEnabled(False)
        item = self.listWidgetFont.item(0)
        item.setText(_translate("Dialog", "Arial"))
        item = self.listWidgetFont.item(1)
        item.setText(_translate("Dialog", "Courier New"))
        item = self.listWidgetFont.item(2)
        item.setText(_translate("Dialog", "Times New Roman"))
        item = self.listWidgetFont.item(3)
        item.setText(_translate("Dialog", "Sans Serif"))
        self.listWidgetFont.setSortingEnabled(__sortingEnabled)
        self.comboBoxFontSize.setItemText(0, _translate("Dialog", "12"))
        self.comboBoxFontSize.setItemText(1, _translate("Dialog", "14"))
        self.comboBoxFontSize.setItemText(2, _translate("Dialog", "16"))
        self.comboBoxFontSize.setItemText(3, _translate("Dialog", "18"))
        self.comboBoxFontSize.setItemText(4, _translate("Dialog", "20"))
        self.pushButtonDrawText.setText(_translate("Dialog", "Draw Text"))
        self.label.setText(_translate("Dialog", "Enter some text in left most box, select font and size and click Draw Text button"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

