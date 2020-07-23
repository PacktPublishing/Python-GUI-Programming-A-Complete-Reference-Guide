import sqlite3, sys
from PyQt5.QtWidgets import QDialog, QApplication
from sqlite3 import Error

from demoDeleteUser import *

class MyForm(QDialog):

    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.pushButtonDelete.clicked.connect(self.DeleteUser)
        self.ui.pushButtonYes.clicked.connect(self.ConfirmDelete)
        self.ui.labelSure.hide()
        self.ui.pushButtonYes.hide()
        self.ui.pushButtonNo.hide()       
        self.show()

    def DeleteUser(self):
        selectStatement="SELECT * FROM Users where EmailAddress like '"+self.ui.lineEditEmailAddress.text()+"' and Password like '"+ self.ui.lineEditPassword.text()+"'"
        try:
            conn = sqlite3.connect("ECommerce.db")
            cur = conn.cursor()    
            cur.execute(selectStatement)
            row = cur.fetchone()
            if row==None:
                self.ui.labelSure.hide()
                self.ui.pushButtonYes.hide()
                self.ui.pushButtonNo.hide()   
                self.ui.labelResponse.setText("Sorry, Incorrect email address or password ")
            else:
                self.ui.labelSure.show()
                self.ui.pushButtonYes.show()
                self.ui.pushButtonNo.show()
                self.ui.labelResponse.setText("")
        except Error as e:
            self.ui.labelResponse.setText("Error in accessing user account")
        finally:
            conn.close()

    def ConfirmDelete(self):
        deleteStatement="DELETE FROM Users where EmailAddress like '"+self.ui.lineEditEmailAddress.text()+"' and Password like '"+ self.ui.lineEditPassword.text()+"'"      
        try:
            conn = sqlite3.connect("ECommerce.db")
            cur = conn.cursor()  
            with conn:
                cur.execute(deleteStatement)
                self.ui.labelResponse.setText("User successfully deleted")
        except Error as e:
            self.ui.labelResponse.setText("Error in deleting user account")
        finally:
            conn.close()

if __name__=="__main__":    
    app = QApplication(sys.argv)
    w = MyForm()
    w.show()
    sys.exit(app.exec_())
