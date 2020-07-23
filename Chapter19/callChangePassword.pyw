import sqlite3, sys
from PyQt5.QtWidgets import QDialog, QApplication
from sqlite3 import Error

from demoChangePassword import *

class MyForm(QDialog):

    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.pushButtonChangePassword.clicked.connect(self.ChangePassword)
        self.show()

    def ChangePassword(self):
        selectStatement="SELECT EmailAddress, Password FROM Users where EmailAddress like '"+self.ui.lineEditEmailAddress.text()+"' and Password like '"+ self.ui.lineEditOldPassword.text()+"'"
        try:
            conn = sqlite3.connect("ECommerce.db")
            cur = conn.cursor()    
            cur.execute(selectStatement)
            row = cur.fetchone()
            if row==None:
                self.ui.labelResponse.setText("Sorry, Incorrect email address or password ")
            else:
                if self.ui.lineEditNewPassword.text()== self.ui.lineEditRePassword.text():
                    updateStatement="UPDATE Users set Password = '" + self.ui.lineEditNewPassword.text()+"' WHERE EmailAddress like '"+self.ui.lineEditEmailAddress.text()+"'"
                    with conn:
                        cur.execute(updateStatement)
                        self.ui.labelResponse.setText("Password successfully changed")
                else:
                    self.ui.labelResponse.setText("The two passwords don't match")
        except Error as e:
            self.ui.labelResponse.setText("Error in accessing row")
        finally:
            conn.close()

if __name__=="__main__":    
    app = QApplication(sys.argv)
    w = MyForm()
    w.show()
    sys.exit(app.exec_())
