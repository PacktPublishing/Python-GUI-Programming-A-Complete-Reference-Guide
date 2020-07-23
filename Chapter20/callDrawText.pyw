import sys

from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5.QtGui import QPainter, QColor, QFont
from PyQt5.QtCore import Qt

from demoDrawText import *

class MyForm(QDialog):

    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.pushButtonDrawText.clicked.connect(self.dispText)
        self.textToDraw=""
        self.fontName="Courier New"
        self.fontSize=5
        self.show()

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)  
        qp.setPen(QColor(168, 34, 3))
        qp.setFont(QFont(self.fontName, self.fontSize))
        qp.drawText(event.rect(), Qt.AlignCenter, self.textToDraw)  
        qp.end()  

    def dispText(self):
        self.fontName=self.ui.listWidgetFont.currentItem().text()
        self.fontSize=int(self.ui.comboBoxFontSize.itemText(self.ui.comboBoxFontSize.currentIndex()))
        self.textToDraw=self.ui.textEdit.toPlainText()
        self.update()

if __name__=="__main__":    
    app = QApplication(sys.argv)
    w = MyForm()
    w.show()
    sys.exit(app.exec_())
