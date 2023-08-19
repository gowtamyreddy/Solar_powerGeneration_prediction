# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'weather.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(545, 410)
        MainWindow.setStyleSheet("color: rgb(170, 0, 127);\n"
"font: 75 12pt \"MS Shell Dlg 2\";")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(10, 300, 251, 31))
        self.pushButton.setObjectName("pushButton")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(450, 50, 71, 33))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(10, 50, 431, 21))
        self.label_4.setObjectName("label_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_5.setGeometry(QtCore.QRect(450, 90, 71, 33))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_6.setGeometry(QtCore.QRect(450, 130, 71, 33))
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(10, 90, 451, 21))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(10, 130, 381, 21))
        self.label_7.setObjectName("label_7")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(10, 10, 171, 21))
        self.label_5.setObjectName("label_5")
        self.lineEdit_9 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_9.setGeometry(QtCore.QRect(450, 10, 71, 33))
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.lineEdit_7 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_7.setGeometry(QtCore.QRect(450, 210, 71, 33))
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(10, 211, 441, 20))
        self.label_8.setObjectName("label_8")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(270, 300, 251, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(10, 340, 251, 31))
        self.pushButton_3.setObjectName("pushButton_3")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(10, 170, 381, 21))
        self.label_10.setObjectName("label_10")
        self.lineEdit_8 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_8.setGeometry(QtCore.QRect(450, 170, 71, 33))
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.lineEdit_11 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_11.setGeometry(QtCore.QRect(450, 250, 71, 33))
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(10, 250, 391, 21))
        self.label_12.setObjectName("label_12")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(270, 340, 251, 31))
        self.pushButton_4.setObjectName("pushButton_4")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Weather Details"))
        self.pushButton.setText(_translate("MainWindow", "Store Weather Details in Data base"))
        self.label_4.setText(_translate("MainWindow", "Average Min.Temparature (0.00 to 50.00):"))
        self.label_6.setText(_translate("MainWindow", "Average Max.Temparature (0.00 to 50.00):"))
        self.label_7.setText(_translate("MainWindow", "Total rainfall in the week (0.00 to 40.00):"))
        self.label_5.setText(_translate("MainWindow", "Week No.( 1 to 9999):"))
        self.label_8.setText(_translate("MainWindow", "Average humidity (36.00 to 99.00):"))
        self.pushButton_2.setText(_translate("MainWindow", "Ada Boost Prediction"))
        self.pushButton_3.setText(_translate("MainWindow", "MNB Prediction"))
        self.label_10.setText(_translate("MainWindow", "Evaporation in the week(0.00 to 14.00 ):"))
        self.label_12.setText(_translate("MainWindow", "Average Atmospheric pressure (980.00 to 1050.00)"))
        self.pushButton_4.setText(_translate("MainWindow", "DL Prediction"))


