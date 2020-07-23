# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'demoDisplayRowsOfTable.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(468, 434)
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
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(20, 70, 131, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.lineEditTableName = QtWidgets.QLineEdit(Dialog)
        self.lineEditTableName.setGeometry(QtCore.QRect(180, 70, 241, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEditTableName.setFont(font)
        self.lineEditTableName.setObjectName("lineEditTableName")
        self.pushButtonDisplayRows = QtWidgets.QPushButton(Dialog)
        self.pushButtonDisplayRows.setGeometry(QtCore.QRect(170, 120, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButtonDisplayRows.setFont(font)
        self.pushButtonDisplayRows.setObjectName("pushButtonDisplayRows")
        self.labelResponse = QtWidgets.QLabel(Dialog)
        self.labelResponse.setGeometry(QtCore.QRect(30, 390, 401, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.labelResponse.setFont(font)
        self.labelResponse.setText("")
        self.labelResponse.setObjectName("labelResponse")
        self.tableWidget = QtWidgets.QTableWidget(Dialog)
        self.tableWidget.setGeometry(QtCore.QRect(20, 170, 411, 191))
        self.tableWidget.setRowCount(3)
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setObjectName("tableWidget")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Enter database name"))
        self.label_2.setText(_translate("Dialog", "Enter table name"))
        self.pushButtonDisplayRows.setText(_translate("Dialog", "Display Rows"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

