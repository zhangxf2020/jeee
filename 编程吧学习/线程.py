from PyQt5.Qt import *

class Thread(QThread):
    sinout = pyqtSignal(str)
    def __init__(self):
        super(Thread, self).__init__()
        self.work = True
        self.num=0
    def __del__(self):
        self.work = False
        self.wait()

    def run(self):
        while self.work == True:
            file_str = 'File index{0}'.format(self.num)
            self.num +=1
            self.sinout.emit(file_str)
            self.sleep(2)
    
    
from PyQt5.QtWidgets import *
import sys

class My_Win(QWidget):
    def __init__(self):
        super(My_Win, self).__init__()
        self.setWindowTitle('主线程')
        self.setGeometry(1000,300,300,300)
        self.thread = Thread()
        self.initui()
    def initui(self):
        self.listFile = QListWidget(self)
        self.listFile.move(20,30)
        self.btn = QPushButton('开始',self)
        self.btn.clicked.connect(self.start)
        self.thread.sinout.connect(self.slotAdd)
    def slotAdd(self,file_inf):
        self.listFile.addItem(file_inf)

    def start(self):
        self.btn.setEnabled(False)
        self.thread.start()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = My_Win()
    win.show()
    sys.exit(app.exec_())