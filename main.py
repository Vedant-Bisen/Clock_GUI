import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import time as tm

class MainWindow(QMainWindow):
    def __init__(self,parent = None):
        super(MainWindow,self).__init__()
        self.setGeometry(1400,100,500,500)
        self.setWindowTitle("Timer")
        self.setStyleSheet("background-color : rgb(100,100,100)")
        self.initUI()
    
    def initUI(self):

        #Creating a flag
        self.count = 0
        self.start = False

        #Creating label
        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(200, 200, 100, 50)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setStyleSheet("border: 1px solid black;")

        #Creating a timer button
        self.timer_button = QtWidgets.QPushButton(self)
        self.timer_button.setGeometry(200, 150, 100, 50)
        self.timer_button.setText("Click to set time")
        self.timer_button.clicked.connect(self.get_seconds)

        #Creating a start Button
        self.start_button = QtWidgets.QPushButton(self)
        self.start_button.setGeometry(200, 300, 100, 50)
        self.start_button.setText("Click to Start")
        self.start_button.clicked.connect(self.get_seconds)


        #Connecting timer to showtime
        timer = QTimer(self)
        timer.timeout.connect(self.showtime)
        timer.start(100)


    def showtime(self):
        if self.start:
            self.count -=1

            if self.count == 0:
                self.start = False
                self.label.setText("Completed")
        
        if self.start:
            text = str(self.count / 100)

            self.label.setText(text)
        

    def get_seconds(self):
        self.start = True

        seconds, done = QInputDialog.getInt(self, "Seconds", "Enter the number of secs: ")

        if done:
            self.count = seconds * 100 

            self.label.setText(str(seconds))
        


def main():
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()