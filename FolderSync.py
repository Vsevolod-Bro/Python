# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'FolderSync.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(468, 111)
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setObjectName("centralwidget")
        # self.lbl_1 = QtWidgets.QLabel(self.centralwidget)
        # self.lbl_1.setGeometry(QtCore.QRect(10, 10, 351, 23))
        # font = QtGui.QFont()
        # font.setFamily("Arial")
        # font.setPointSize(11)
        # self.lbl_1.setFont(font)
        # self.lbl_1.setFrameShape(QtWidgets.QFrame.WinPanel)
        # self.lbl_1.setFrameShadow(QtWidgets.QFrame.Sunken)
        # self.lbl_1.setObjectName("lbl_1")
        # self.btn_1 = QtWidgets.QPushButton(self.centralwidget)
        # self.btn_1.setGeometry(QtCore.QRect(380, 10, 75, 23))
        # font = QtGui.QFont()
        # font.setFamily("Arial")
        # font.setPointSize(11)
        # self.btn_1.setFont(font)
        # self.btn_1.setFlat(False)
        # self.btn_1.setObjectName("btn_1")
        mainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(mainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 468, 21))
        self.menubar.setObjectName("menubar")
        mainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(mainWindow)
        self.statusbar.setObjectName("statusbar")
        mainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "Folders Synchronization"))
        #self.lbl_1.setText(_translate("mainWindow", "Folder1"))
        #self.btn_1.setText(_translate("mainWindow", "Synchro"))
