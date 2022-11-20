import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
import random
import time

class MainWindow(QMainWindow):
    def __init__(self,parent = None):
        super(MainWindow,self).__init__()
        self.setGeometry(1400,100,500,500)
        self.setWindowTitle("Timer")
        self.initUI()
    
    def initUI(self):

        #Setting Background Color
        self.Background = QtWidgets.QWidget()
        self.layout = QtWidgets.QGridLayout()
        self.setCentralWidget(self.Background)
        self.Background.setLayout(self.layout)
        self.Background.setStyleSheet("background-color : rgb(100, 100, 100)")
        self.Background.setObjectName("BackGround")


        #Creating a TextBox
        self.TextBox = QtWidgets.QLineEdit()
        self.label = QtWidgets.QLabel("Hi")

        #Creating a button
        self.button = QtWidgets.QPushButton(self)
        self.button.setText("Push me!")
        
        #Connecting TextBox to button
        self.button.clicked.connect(self.timer)

        #Adding to layout
        self.layout.addWidget(self.label, 0, 0)
        self.layout.addWidget(self.TextBox, 1, 0)
        self.layout.addWidget(self.button, 1, 1)


    def Textchanged(self):
        pass

    def timer(self):
        s = self.TextBox.text()
        for i in range(int(s)):
            i -= 1
            self.label.setText(str(i))




def main():
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()