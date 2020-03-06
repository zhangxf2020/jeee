from PyQt5.Qt import *


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('进度条单独实验')
        self.resize(250,250)
        self.initUI()
    def initUI(self):
        pb1 = QProgressBar(self)
        self.pb2 = QProgressBar(self)
        pb1.setGeometry(40,20,180,20)
        self.pb2.setGeometry(40,50,180,20)
        self.pb3 = QProgressBar(self)
        self.pb3.setOrientation(Qt.Vertical)
        self.pb3.move(10,50)
        self.pb3.resize(20,180)
        self.pb3.setMinimum(0)
        self.pb3.setMaximum(0)
        pb1.setMinimum(0)
        pb1.setMaximum(0)
        self.btn1 = QPushButton('停止',self)
        self.btn1.clicked.connect(self.running)
        self.step = 0
        self.timer = QBasicTimer()
        self.timer.start(1000,self)
    def timerEvent(self, *args, **kwargs):
        self.step += 0.1
        self.pb2.setValue(self.step)
    def running(self):
        if self.timer.isActive():
            self.timer.stop()
            self.btn1.setText('继续')
        else:
            self.timer.start(100,self)
            self.btn1.setText('停止')
QWidget


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    window=Window()
    window.show()

    sys.exit(app.exec_())