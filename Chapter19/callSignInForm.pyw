import sqlite3, sys
from PyQt5.QtWidgets import QDialog, QApplication
from sqlite3 import Error

from demoSignInForm import *

class MyForm(QDialog):

    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.pushButtonSearch.clicked.connect(self.SearchRows)
        self.show()

    def SearchRows(self):
        sqlStatement="SELECT EmailAddress, Password FROM Users where EmailAddress like '"+self.ui.lineEditEmailAddress.text()+"' and Password like '"+ self.ui.lineEditPassword.text()+"'"
        try:
            conn = sqlite3.connect("ECommerce.db")
            cur = conn.cursor()    
            cur.execute(sqlStatement)
            row = cur.fetchone()
            if row==None:
                self.ui.labelResponse.setText("Sorry, Incorrect email address or password ")
            else:
                self.ui.labelResponse.setText("You are welcome ")
        except Error as e:
            self.ui.labelResponse.setText("Error in accessing row")
        finally:
            conn.close()

if __name__=="__main__":    
    app = QApplication(sys.argv)
    w = MyForm()
    w.show()
    sys.exit(app.exec_())
