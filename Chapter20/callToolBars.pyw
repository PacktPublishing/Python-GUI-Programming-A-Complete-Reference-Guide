import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtGui import QPainter

from demoToolBars import *

class AppWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.pos1 = [0,0]
        self.pos2 = [0,0]
        self.toDraw=""
        self.ui.actionCircle.triggered.connect(self.drawCircle)
        self.ui.actionRectangle.triggered.connect(self.drawRectangle)
        self.ui.actionLine.triggered.connect(self.drawLine)
        self.show()

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        if self.toDraw=="rectangle":
            width = self.pos2[0]-self.pos1[0]
            height = self.pos2[1] - self.pos1[1]     
            qp.drawRect(self.pos1[0], self.pos1[1], width, height)
        if self.toDraw=="line":
            qp.drawLine(self.pos1[0], self.pos1[1], self.pos2[0], self.pos2[1])
        if self.toDraw=="circle":
            width = self.pos2[0]-self.pos1[0]
            height = self.pos2[1] - self.pos1[1]           
            rect = QtCore.QRect(self.pos1[0], self.pos1[1], width, height)
            startAngle = 0
            arcLength = 360 *16
            qp.drawArc(rect, startAngle, arcLength)      
        qp.end()
        
    def mousePressEvent(self, event):
        if event.buttons() & QtCore.Qt.LeftButton:
            self.pos1[0], self.pos1[1] = event.pos().x(), event.pos().y()
                        
    def mouseReleaseEvent(self, event):
        self.pos2[0], self.pos2[1] = event.pos().x(), event.pos().y()    
        self.update()
               
    def drawCircle(self):
        self.toDraw="circle"

    def drawRectangle(self):
        self.toDraw="rectangle"

    def drawLine(self):
        self.toDraw="line"

app = QApplication(sys.argv)
w = AppWindow()
w.show()
sys.exit(app.exec_())




