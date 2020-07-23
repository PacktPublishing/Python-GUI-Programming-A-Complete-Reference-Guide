import sys

from PyQt5.QtWidgets import QDialog, QApplication
from geolocation.main import GoogleMaps

from demoGoogleMap1 import *

class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.pushButtonSearch.clicked.connect(self.displayDetails)
        self.show()
   
    def displayDetails(self):
        address = str(self.ui.lineEditLocation.text())
        google_maps = GoogleMaps(api_key='AIzaSyB3jE8Vd0tiGA8gYh4PamNJa2Dalngjpl0') 
        location = google_maps.search(location=address) # sends search to Google Maps.
        my_location = location.first() 
        self.ui.labelCity.setText("City: "+str(my_location.city))
        self.ui.labelPostalCode.setText("Postal Code: " +str(my_location.postal_code))
        self.ui.labelLongitude.setText("Longitude: "+str(my_location.lng))
        self.ui.labelLatitude.setText("Latitude: "+str(my_location.lat))
          
if __name__=="__main__":    
    app = QApplication(sys.argv)
    w = MyForm()
    w.show()
    sys.exit(app.exec_())


