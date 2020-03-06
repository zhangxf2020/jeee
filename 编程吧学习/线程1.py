from PyQt5.Qt import *


class Thread(QThread):
    my_signal = pyqtSignal(int)
    def __init__(self):
        super(Thread, self).__init__()
        self.is_on = True
        self.count = 0

    def run(self):
        while self.is_on:
            print(self.count)
            self.count +=1
            self.my_signal.emit(self.count)
            self.sleep(1)



'''
import sys

class My_Win(QWidget):
    def __init__(self):
        super(My_Win, self).__init__()
        self.setWindowTitle('')
        self.setGeometry(1000,300,300,300)
        self.thread = Thread()
        self.thread.my_signal.connect(self.set_label_func)
        self.initui()
    def initui(self):
        btn = QPushButton('开始',self)
        btn1 = QPushButton('停止',self)
        self.label = QLabel(self)
        mylayout = QGridLayout(self)
        mylayout.addWidget(btn,0,0)
        mylayout.addWidget(btn1,0,1)
        mylayout.addWidget(self.label,1,0,1,2)
        btn.clicked.connect(self.start)
        btn1.clicked.connect(self.end)

    def start(self):
        self.thread.is_on =True
        self.thread.start()
    def end(self):
        self.thread.is_on = False
        self.thread.count = 0
    def set_label_func(self,num):
        self.label.setText(str(num))



if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = My_Win()
    win.show()
    sys.exit(app.exec_())
'''




import sys

class My_Win(QWidget):
    def __init__(self):
        super(My_Win, self).__init__()
        self.setWindowTitle('dd')
        self.setGeometry(1000,300,300,300)
        self.s = Thread()
        self.initui()
    def initui(self):
        self.lab = QLabel('     ',self)
        self.s.my_signal.connect(self.gaibian)
        self.s.start()
    def gaibian(self,num):
        self.lab.setText(str(num))



if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = My_Win()
    win.show()
    sys.exit(app.exec_())