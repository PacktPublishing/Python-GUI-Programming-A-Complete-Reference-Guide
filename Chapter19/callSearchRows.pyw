import sqlite3, sys
from PyQt5.QtWidgets import QDialog, QApplication
from sqlite3 import Error

from demoSearchRows import *

class MyForm(QDialog):

    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.pushButtonSearch.clicked.connect(self.SearchRows)
        self.show()

    def SearchRows(self):
        sqlStatement="SELECT Password FROM "+self.ui.lineEditTableName.text()+" where EmailAddress like '"+self.ui.lineEditEmailAddress.text()+"'"
        try:
            conn = sqlite3.connect(self.ui.lineEditDBName.text()+".db")
            cur = conn.cursor()    
            cur.execute(sqlStatement)
            row = cur.fetchone()
            if row==None:
                self.ui.labelResponse.setText("Sorry, No User found with this email address")
                self.ui.lineEditPassword.setText("")
            else:
                self.ui.labelResponse.setText("Email Address Found, Password of this User is :")
                self.ui.lineEditPassword.setText(row[0])
        except Error as e:
            self.ui.labelResponse.setText("Error in accessing row")
        finally:
            conn.close()

if __name__=="__main__":    
    app = QApplication(sys.argv)
    w = MyForm()
    w.show()
    sys.exit(app.exec_())
