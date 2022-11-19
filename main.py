import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
import random

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow,self).__init__()
        self.setGeometry(1400,100,400,400)
        self.setWindowTitle("This is the main file")
        self.initUI()
    
    def initUI(self):
        pass




def main():
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()