import sqlite3, sys
from PyQt5.QtWidgets import QDialog, QApplication,QTableWidgetItem
from sqlite3 import Error

from demoShowRecords import *

rowNo=1
sqlStatement="SELECT EmailAddress, Password FROM Users"
conn = sqlite3.connect("ECommerce.db")
cur = conn.cursor()  

class MyForm(QDialog):

    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        cur.execute(sqlStatement)
        self.ui.pushButtonFirst.clicked.connect(self.ShowFirstRow)
        self.ui.pushButtonPrevious.clicked.connect(self.ShowPreviousRow)
        self.ui.pushButtonNext.clicked.connect(self.ShowNextRow)
        self.ui.pushButtonLast.clicked.connect(self.ShowLastRow)
        self.show()

    def ShowFirstRow(self):       
        try: 
            cur.execute(sqlStatement)
            row=cur.fetchone()
            if row:
                self.ui.lineEditEmailAddress.setText(row[0])
                self.ui.lineEditPassword.setText(row[1])    
        except Error as e:
            self.ui.labelResponse.setText("Error in accessing table")


    def ShowPreviousRow(self):
        global rowNo
        rowNo -= 1
        sqlStatement="SELECT EmailAddress, Password FROM Users where rowid="+str(rowNo)
        cur.execute(sqlStatement)
        row=cur.fetchone()
        if row:
            self.ui.labelResponse.setText("")
            self.ui.lineEditEmailAddress.setText(row[0])
            self.ui.lineEditPassword.setText(row[1])
        else:
            rowNo += 1
            self.ui.labelResponse.setText("This is the first row")
       
            
    def ShowNextRow(self):
        global rowNo
        rowNo += 1
        sqlStatement="SELECT EmailAddress, Password FROM Users where rowid="+str(rowNo)
        cur.execute(sqlStatement)
        row=cur.fetchone()
        if row:
            self.ui.labelResponse.setText("")
            self.ui.lineEditEmailAddress.setText(row[0])
            self.ui.lineEditPassword.setText(row[1])
        else:
            rowNo -= 1
            self.ui.labelResponse.setText("This is the last row")

    def ShowLastRow(self):
        cur.execute(sqlStatement)
        for row in cur.fetchall():
            self.ui.lineEditEmailAddress.setText(row[0])
            self.ui.lineEditPassword.setText(row[1])

        
if __name__=="__main__":    
    app = QApplication(sys.argv)
    w = MyForm()
    w.show()
    sys.exit(app.exec_())
