import sys

from PyQt5.QtWidgets import QDialog, QApplication
from googlemaps.client import Client
from googlemaps.distance_matrix import distance_matrix

from demoGoogleMap3 import *

class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.pushButtonFindDistance.clicked.connect(self.displayDistance)
        self.show()
   
    def displayDistance(self):
        api_key = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
        gmaps = Client(api_key)
        data = distance_matrix(gmaps, self.ui.lineEditFirstLocation.text(), self.ui.lineEditSecondLocation.text())
        distance = data['rows'][0]['elements'][0]['distance']['text']
        self.ui.labelDistance.setText("Distance between "+self.ui.lineEditFirstLocation.text()+" and "+self.ui.lineEditSecondLocation.text()+" is "+str(distance))
          
if __name__=="__main__":    
    app = QApplication(sys.argv)
    w = MyForm()
    w.show()
    sys.exit(app.exec_())


