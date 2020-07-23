import sys
from PyQt5.QtWidgets import QDialog, QApplication
from demoMousetrack import *

class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.setMouseTracking(True)
        self.ui.setupUi(self)
        self.show()
           
    def mouseMoveEvent(self, event):      
        x = event.x()
        y = event.y()    
        text = "x: {0},  y: {1}".format(x, y)
        self.ui.label.setText(text)

if __name__=="__main__":    
    app = QApplication(sys.argv)
    w = MyForm()
    w.show()
    sys.exit(app.exec_())
