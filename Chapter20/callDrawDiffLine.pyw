import sys

from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5.QtGui import QPainter, QPen
from PyQt5.QtCore import Qt

from demoDrawDiffLine import *

class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.lineType="SolidLine"
        self.pos1 = [0,0]
        self.pos2 = [0,0]
        self.show()

    def paintEvent(self, event):   
        qp = QPainter()
        qp.begin(self)
        pen = QPen(Qt.black, 4)
        self.lineTypeFormat="Qt."+self.lineType
        if self.lineTypeFormat == "Qt.SolidLine":
            pen.setStyle(Qt.SolidLine)
        elif self.lineTypeFormat == "Qt.DashLine":
            pen.setStyle(Qt.DashLine)
        elif self.lineTypeFormat =="Qt.DashDotLine":
            pen.setStyle(Qt.DashDotLine)
        elif self.lineTypeFormat =="Qt.DotLine":
            pen.setStyle(Qt.DotLine)
        elif self.lineTypeFormat =="Qt.DashDotDotLine":
            pen.setStyle(Qt.DashDotDotLine)
        qp.setPen(pen)       
        qp.drawLine(self.pos1[0], self.pos1[1], self.pos2[0], self.pos2[1])        
        qp.end()
        
    def mousePressEvent(self, event):
        if event.buttons() & QtCore.Qt.LeftButton:
            self.pos1[0], self.pos1[1] = event.pos().x(), event.pos().y()
                        
    def mouseReleaseEvent(self, event):
        self.lineType=self.ui.listWidgetLineType.currentItem().text()
        self.pos2[0], self.pos2[1] = event.pos().x(), event.pos().y()    
        self.update()
                  
if __name__=="__main__":    
    app = QApplication(sys.argv)
    w = MyForm()
    w.show()
    sys.exit(app.exec_())
