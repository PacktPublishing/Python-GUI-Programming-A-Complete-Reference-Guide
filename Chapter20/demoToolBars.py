# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'demoToolBars.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(488, 337)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionCircle = QtWidgets.QAction(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/Graphics/circleIcon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionCircle.setIcon(icon)
        self.actionCircle.setObjectName("actionCircle")
        self.actionRectangle = QtWidgets.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/Graphics/rectangleIcon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionRectangle.setIcon(icon1)
        self.actionRectangle.setObjectName("actionRectangle")
        self.actionLine = QtWidgets.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/Graphics/lineIcon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionLine.setIcon(icon2)
        self.actionLine.setObjectName("actionLine")
        self.toolBar.addAction(self.actionCircle)
        self.toolBar.addAction(self.actionRectangle)
        self.toolBar.addAction(self.actionLine)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.actionCircle.setText(_translate("MainWindow", "Circle"))
        self.actionCircle.setShortcut(_translate("MainWindow", "Ctrl+C"))
        self.actionRectangle.setText(_translate("MainWindow", "Rectangle"))
        self.actionRectangle.setShortcut(_translate("MainWindow", "Ctrl+R"))
        self.actionLine.setText(_translate("MainWindow", "Line"))
        self.actionLine.setToolTip(_translate("MainWindow", "Line"))
        self.actionLine.setShortcut(_translate("MainWindow", "Ctrl+L"))

import iconresource_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

