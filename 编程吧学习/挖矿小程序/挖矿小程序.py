from PyQt5.Qt import *
import sys

class My_Win(QWidget):
    def __init__(self):
        super(My_Win, self).__init__()
        self.setWindowTitle('挖矿小程序')
        self.setGeometry(1000,300,900,730)
        self.initui()
    def initui(self):
        self.lb1 = QLabel(self)
        self.lb1.setPixmap(QPixmap('./res/ready.png'))
        lb2 = QLabel('采矿进度:',self)
        lb2.move(30,705)
        lb3 = QLabel('挖矿时间:',self)
        lb3.move(750,683)
        self.pb  =QProgressBar (self)
        self.pb.resize(700,20)
        self.pb.move(100,702)
        self.sd = QSpinBox(self)
        self.sd.setRange(0,120)
        self.sd.setSingleStep(5)
        self.sd.setSuffix('秒')
        self.sd.move(820,680)
        start = QPushButton('开始', self)
        start.move(800,700)
        start.clicked.connect(self.start)


    def start(self):
        movie = QMovie('./res/farmer.gif')
        self.lb1.setMovie(movie)
        movie.start()
        self.sd.setReadOnly(True)
        self.timer = QTimer(self)
        self.timer.timeout.connect(lambda:self.mysingl(self.sd.value()))
        self.time =0
        self.timer.start(100)

    def mysingl(self,num):
        myther = QThread()
        self.time +=100/(num*10)
        if self.time ==100:
            print('hao l ')
            self.timer.stop()
        self.pb.setValue(self.time)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = My_Win()
    win.show()
    sys.exit(app.exec_())