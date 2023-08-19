# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'spower.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(582, 363)
        MainWindow.setStyleSheet("color: rgb(170, 0, 127);\n"
"font: 75 12pt \"MS Shell Dlg 2\";")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(130, 50, 271, 31))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(130, 90, 271, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(130, 130, 271, 31))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(130, 170, 271, 31))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(130, 10, 271, 31))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setGeometry(QtCore.QRect(130, 250, 271, 31))
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_10 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_10.setGeometry(QtCore.QRect(130, 290, 271, 31))
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_11 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_11.setGeometry(QtCore.QRect(130, 210, 271, 31))
        self.pushButton_11.setObjectName("pushButton_11")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Solar Power Generation Forecasting on the Basis of Weather"))
        self.pushButton.setText(_translate("MainWindow", "Ada Boost Accuracy"))
        self.pushButton_2.setText(_translate("MainWindow", "MNB Accuracy"))
        self.pushButton_3.setText(_translate("MainWindow", "Ada Boost Predictions"))
        self.pushButton_4.setText(_translate("MainWindow", "MNB Predictions"))
        self.pushButton_5.setText(_translate("MainWindow", "Weather Details"))
        self.pushButton_8.setText(_translate("MainWindow", "DL Classifier Predictions"))
        self.pushButton_10.setText(_translate("MainWindow", "Accuracies Comparison Plot"))
        self.pushButton_11.setText(_translate("MainWindow", "DL Classifier Accuracy"))


