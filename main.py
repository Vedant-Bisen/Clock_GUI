from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
import time


class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow,self).__init__()
        self.setGeometry(100, 1500, 500, 500)
        self.setWindowTitle("Clock")
        self.InitUI()
        
        

    def InitUI(self):
        pass
        
        
    

def main():
    app = QApplication(sys.argv)    
    win = MyWindow()
    win.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
