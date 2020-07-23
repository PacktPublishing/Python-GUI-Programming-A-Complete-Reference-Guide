import sys

from PyQt5.QtWidgets import QDialog, QApplication
from geolocation.main import GoogleMaps

from demoGoogleMap2 import *

class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.pushButtonSearch.clicked.connect(self.displayLocation)
        self.show()
   
    def displayLocation(self):
        lng = float(self.ui.lineEditLongitude.text())
        lat = float(self.ui.lineEditLatitude.text())
        google_maps = GoogleMaps(api_key='xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx') 
        my_location = google_maps.search(lat=lat, lng=lng).first()
        self.ui.labelLocation.setText("Location: "+str(my_location))
        self.ui.labelCity.setText("City: "+str(my_location.city))
        self.ui.labelCountry.setText("Country: "+str(my_location.country))
        self.ui.labelPostalCode.setText("Postal Code: "+str(my_location.postal_code))
          
if __name__=="__main__":    
    app = QApplication(sys.argv)
    w = MyForm()
    w.show()
    sys.exit(app.exec_())


