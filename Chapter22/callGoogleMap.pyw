import sys

from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.QtWebEngineWidgets import QWebEngineView

from showGoogleMap import *

class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.pushButtonShowMap.clicked.connect(self.dispSite)
        self.show()


    def dispSite(self):
        lng = float(self.ui.lineEditLongitude.text())
        lat = float(self.ui.lineEditLatitude.text())
        URL="https://www.google.com/maps/@"+self.ui.lineEditLatitude.text()+","+self.ui.lineEditLongitude.text()+",9z"
        self.ui.widget.load(QUrl(URL))
        
if __name__=="__main__":    
    app = QApplication(sys.argv)
    w = MyForm()
    w.show()
    sys.exit(app.exec_())
