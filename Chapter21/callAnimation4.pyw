import sys

from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5.QtCore import QRect, QPointF, QPropertyAnimation, pyqtProperty
from PyQt5.QtGui import QPainter, QPainterPath

from demoAnimation4 import *

class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.pushButtonMoveCurve.clicked.connect(self.startAnimation)
        self.path = QPainterPath()
        self.path.moveTo(30, 30)
        self.path.cubicTo(30, 30, 80, 180, 180, 170)                
        self.ui.labelPic.pos = QPointF(20, 20)      
        self.show()

    def paintEvent(self, e):          
        qp = QPainter()
        qp.begin(self)
        qp.drawPath(self.path)
        qp.end()  

    def startAnimation(self):
        self.anim = QPropertyAnimation(self.ui.labelPic, b'pos')
        self.anim.setDuration(4000)        
        self.anim.setStartValue(QPointF(20, 20))        
        positionValues = [n/80 for n in range(0, 50)]
        for i in positionValues:
            self.anim.setKeyValueAt(i, self.path.pointAtPercent(i))  
        self.anim.setEndValue(QPointF(160, 150))
        self.anim.start()
        
if __name__=="__main__":    
    app = QApplication(sys.argv)
    w = MyForm()
    w.show()
    sys.exit(app.exec_())
