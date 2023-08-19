import sys
import os
from weather import *
from PyQt5 import QtWidgets, QtGui, QtCore

import sqlite3
con = sqlite3.connect('spower1')

#import MySQLdb as mdb
#con = mdb.connect('localhost', 'team1', 'test623', 'drless1'); 

class MyForm(QtWidgets.QMainWindow):
  def __init__(self,parent=None):
     QtWidgets.QWidget.__init__(self,parent)
     self.ui = Ui_MainWindow()
     self.ui.setupUi(self)
     self.ui.pushButton.clicked.connect(self.insertvalues)
     self.ui.pushButton_2.clicked.connect(self.testabc)
     self.ui.pushButton_3.clicked.connect(self.testmnb)
     self.ui.pushButton_4.clicked.connect(self.testdlc)
 
  def insertvalues(self):
    with con:
      cur = con.cursor()
      week = str(self.ui.lineEdit_9.text())
      s1 = str(self.ui.lineEdit_4.text())
      s2 = str(self.ui.lineEdit_5.text())
      s3 = str(self.ui.lineEdit_6.text())
      s4 = str(self.ui.lineEdit_8.text())
      s5 = str(self.ui.lineEdit_7.text())
      s6 = str(self.ui.lineEdit_11.text())
      cur.execute('INSERT INTO weather VALUES(?,?,?,?,?,?,?)',(week,s1,s2,s3,s4,s5,s6))
      con.commit()

  def testabc(self):
    with con:
        cur = con.cursor()
        wid = str(self.ui.lineEdit_9.text())
        cur.execute('select mintemp,maxtemp,rainfall,evop,humidity,pressure from weather where weekno = ?',[wid])
        record1 = cur.fetchone()
        s1 = record1[0]
        s2 = record1[1]
        s3 = record1[2]
        s4 = record1[3]
        s5 = record1[4]
        s6 = record1[5]
    str1 = "python"+" abc3a.py"+" "+s1+" "+s2+" "+s3+" "+s4+" "+s5+" "+s6
    os.system(str1)

  def testmnb(self):
    with con:
        cur = con.cursor()
        wid = str(self.ui.lineEdit_9.text())
        cur.execute('select mintemp,maxtemp,rainfall,evop,humidity,pressure from weather where weekno = ?',[wid])
        record1 = cur.fetchone()
        s1 = record1[0]
        s2 = record1[1]
        s3 = record1[2]
        s4 = record1[3]
        s5 = record1[4]
        s6 = record1[5]
    str1 = "python"+" mnb3a.py"+" "+s1+" "+s2+" "+s3+" "+s4+" "+s5+" "+s6
    os.system(str1)
	
	
  def testdlc(self):
    with con:
        cur = con.cursor()
        wid = str(self.ui.lineEdit_9.text())
        cur.execute('select mintemp,maxtemp,rainfall,evop,humidity,pressure from weather where weekno = ?',[wid])
        record1 = cur.fetchone()
        s1 = record1[0]
        s2 = record1[1]
        s3 = record1[2]
        s4 = record1[3]
        s5 = record1[4]
        s6 = record1[5]
    str1 = "python"+" cnn1a.py"+" "+s1+" "+s2+" "+s3+" "+s4+" "+s5+" "+s6
    os.system(str1)

if __name__ == "__main__":  
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyForm()
    myapp.show()
    sys.exit(app.exec_())
