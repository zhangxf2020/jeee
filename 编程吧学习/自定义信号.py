from PyQt5.Qt import *
import sys

class My_Win(QWidget):
    my_singl = pyqtSignal(int)
    def __init__(self):
        super(My_Win, self).__init__()
        self.setWindowTitle('dd')
        self.setGeometry(1000,300,300,300)

        self.num =0
        self.initui()
    def initui(self):
        btn = QPushButton(self)
        btn.clicked.connect(self.start)
        self.lb1 = QLabel('   ',self)
        self.lb1.move(20,50)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.end)

    def start(self):
        self.timer.start(1000)

        self.my_singl.connect(self.jddj)
    def end(self):
        self.num +=1
        if self.num ==10:
            self.num =0
        self.my_singl.emit(self.num)

    def jddj(self,ass):
        self.lb1.setText(str(ass))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = My_Win()
    win.show()
    sys.exit(app.exec_())