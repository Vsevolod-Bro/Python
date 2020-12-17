import configparser
from PyQt5 import QtWidgets, QtCore, QtGui
from FolderSync import Ui_mainWindow # импорт нашего сгенерированного файла
import sys
import shutil #for copy operations
import os


strIniPath = sys.path
class mywindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_mainWindow()
        self.ui.setupUi(self)

def btnClick ():
    snd=application.sender()
    strBtnName=str(snd.objectName())
    strBtnNum=strBtnName[4:]
    #FileCopy(strBtmNum)
    CopyIfNeed(strBtnNum)
    #print("OK " + strBtmNum)

#Get full file names from Folder with passed path (Return list of FileNames)
def listFiles(strCurPath):
    lstFiles=[]
    lstFullFiles = []
    #walk return 3 value
    for (strPath, dir, filenames) in os.walk(strCurPath):
        lstFiles.extend(filenames)
        for f in filenames:
            strFullFlie=strPath+strDelim+f
            lstFullFiles.append(strFullFlie)
        #out on first step of recursion (doesn't go into folders)
        break
    return lstFiles

#Copy a file depending number of the button pressed
def FileCopy(strBtnNum, file1):
    strFromCopy=dct_From["name"+strBtnNum]
    strToCopy=dct_To["name"+strBtnNum]
    #print(strFromCopy)
    #print(strToCopy)
    shutil.copyfile(strFromCopy+strDelim+file1, strToCopy+strDelim+file1 )

#Copy if in "To" no file or this one older than the source file
def CopyIfNeed(strBtnNum):
    #Time of last file modification
    strNameNo="name"+strBtnNum
    lstFilesFrom=listFiles(dct_From[strNameNo])
    lstFilesTo=listFiles(dct_To[strNameNo])
    for file in lstFilesFrom:
        if (file in lstFilesTo):
            MTimeFrom=os.stat(dct_From[strNameNo]+strDelim+file).st_mtime
            MTimeTo=os.stat(dct_To[strNameNo]+strDelim+file).st_mtime
            if MTimeFrom >MTimeTo:
                print("Change File from: " + dct_From[strNameNo]+strDelim+file + " To:" + dct_To[strNameNo]+strDelim+file)
                FileCopy(strBtnNum,file)
            else:
                print("Don't need copy file: " + file)
        else:
            print("Copy File from: " + dct_From[strNameNo] + strDelim + file + " To:" + dct_To[strNameNo] + strDelim + file)
            FileCopy(strBtnNum,file)


dct_Tasks={}
dct_From={}
dct_To={}
dct_Opt={}
lstBtn=[]
lstLbl=[]

#print(strIniPath[0])

config = configparser.ConfigParser()
# Warning - must use / in Windows path (only full path, otherwise don't work in console)
#config.read('D:/bvvPhyton/FolderSync/FldrS-cfg.ini')
#ini-file put near main file, path of ini-file take from path of main-file
config.read(strIniPath[0] + "//"+'FldrS-cfg.ini')
intTasks = 0
for Name in config['Tasks']:
    intTasks += 1
    Task = config['Tasks'][Name]
    dct_Tasks[Name] = Task
#print(dct_Tasks)
#print(intTasks)

intFrom = 0
for Name in config['From']:
    intFrom += 1
    From = config['From'][Name]
    dct_From[Name] = From
#print(dct_From)
#print(intFrom)

intTo = 0
for Name in config['To']:
    intTo += 1
    To = config['To'][Name]
    dct_To[Name] = To
#print(dct_To)
#print(intTo)

#Read "Options" section
intOpt=0
for Name in config['Options']:
    intOpt += 1
    Opt = config['Options'][Name]
    dct_Opt[Name] = Opt
#print(dct_Opt)

#Put to var Path Delimeter - Windows or Linux
strDelim=dct_Opt["delim"]
#print (strDelim)

app = QtWidgets.QApplication([])
application = mywindow()

intUpRight=10
intHigh=23

#Drawing button and label in Window
for num in range(1, intTasks+1):
    application.ui.lbl = QtWidgets.QLabel(application.ui.centralwidget)
    lstLbl.append(application.ui.lbl)
    application.ui.lbl.setGeometry(QtCore.QRect(10, intUpRight, 351, intHigh))
    font = QtGui.QFont()
    font.setFamily("Arial")
    font.setPointSize(11)
    application.ui.lbl.setFont(font)
    application.ui.lbl.setFrameShape(QtWidgets.QFrame.WinPanel)
    application.ui.lbl.setFrameShadow(QtWidgets.QFrame.Sunken)
    application.ui.lbl.setObjectName("lbl_"+str(num))

    application.ui.btn = QtWidgets.QPushButton(application.ui.centralwidget)
    lstBtn.append(application.ui.btn)
    application.ui.btn.setGeometry(QtCore.QRect(380, intUpRight, 75, intHigh))
    font = QtGui.QFont()
    font.setFamily("Arial")
    font.setPointSize(11)
    application.ui.btn.setFont(font)
    application.ui.btn.setFlat(False)
    application.ui.btn.setObjectName("btn_"+str(num))
    #Binding button with procedure click
    application.ui.btn.clicked.connect(btnClick)
    strTasks="name"+str(num)

    application.ui.lbl.setText(dct_Tasks[strTasks])
    application.ui.btn.setText("Synchro")

    intUpRight = intUpRight + intHigh * 2
 #   print(num)


# Binding
#lstBtn[0].clicked.connect(btnClick)


#Set Main Window Size
application.resize(468,intUpRight)


application.show()
sys.exit(app.exec())
