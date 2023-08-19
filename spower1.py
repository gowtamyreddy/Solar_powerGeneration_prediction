import sys
import os
from spower import *
from PyQt5 import QtWidgets, QtGui, QtCore

class MyForm(QtWidgets.QMainWindow):
  def __init__(self,parent=None):
     QtWidgets.QWidget.__init__(self,parent)
     self.ui = Ui_MainWindow()
     self.ui.setupUi(self)
     self.ui.pushButton.clicked.connect(self.abcacc)
     self.ui.pushButton_2.clicked.connect(self.mnbacc)
     self.ui.pushButton_3.clicked.connect(self.abcpred)
     self.ui.pushButton_4.clicked.connect(self.mnbpred)
     self.ui.pushButton_5.clicked.connect(self.wdetails)
     self.ui.pushButton_11.clicked.connect(self.dlacc)
     self.ui.pushButton_8.clicked.connect(self.dlpred)
     self.ui.pushButton_10.clicked.connect(self.accomp)
      

  def abcacc(self):
    os.system("python abc3acc.py")

  def wdetails(self):
    os.system("python weather1.py")

  def mnbacc(self):
    os.system("python mnb3acc.py")

  def abcpred(self):
    os.system("python abc3.py")

  def mnbpred(self):
    os.system("python mnb3.py")
	
  def dlacc(self):
    os.system("python cnn1acc.py")
	
  def dlpred(self):
    os.system("python cnn1.py")
	
  def accomp(self):
    os.system("python cplot1.py")

    
if __name__ == "__main__":  
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyForm()
    myapp.show()
    sys.exit(app.exec_())
