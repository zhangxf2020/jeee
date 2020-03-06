from PyQt5.Qt import *


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('走马灯QProgressBar')
        self.resize(600,480)
        self.initUI()
    def initUI(self):
        self.pb1 = QProgressBar(self)
        self.pb2 = QProgressBar(self)
        self.pb3 = QProgressBar(self)
        self.pb4 = QProgressBar(self)
        self.pb5 = QProgressBar(self)
        self.pb6 = QProgressBar(self)
        '''格式化百分比字符串
        ％p - 被完成的百分比取代
        ％v - 被当前值替换
        ％m - 被总step所取代
        默认值是”％p％
        '''
        self.pb5.setFormat('%v')
        '''设置进度条增长方向,默认是False(从左往右)'''
        self.pb6.setInvertedAppearance(True)

        self.btn1 = QPushButton('外圈跑马灯',self)
        self.btn2 = QPushButton('内圈跑马灯',self)
        self.btn1.move(250,215)
        self.btn2.move(250,245)
        self.btn2.clicked.connect(self.doaction)
        self.btn1.clicked.connect(self.running)

        self.pb1.setOrientation(Qt.Horizontal)
        self.pb2.setOrientation(Qt.Vertical)
        self.pb3.setOrientation(Qt.Horizontal)
        self.pb4.setOrientation(Qt.Vertical)
        self.pb1.setGeometry(40,20,550,20)
        self.pb2.setGeometry(560,20,20,400)
        self.pb3.setGeometry(40,400,550,20)
        self.pb4.setGeometry(20,20,20,400)
        self.pb5.setGeometry(185,150,260,20)
        self.pb6.setGeometry(185,300,260,20)
        '''创建一个计时器'''
        self.timer = QBasicTimer()
        self.step =0
        '''开始计时,默认为0.1秒的速度'''
        self.timer.start(100,self)
        '''timerEvent处理时间内的事件'''
    def timerEvent(self, e):
        if self.step >= 100:
            self.timer.stop()
            QMessageBox.information(self, '提示', '内圈收工了!')
            self.btn2.setText('再来一次')
            self.step = 0
            return
        self.step = self.step + 1
        self.pb5.setValue(self.step)
        self.pb6.setValue(self.step)
    def doaction(self):
        if self.timer.isActive():
            self.timer.stop()
            self.btn2.setText('继续')
        else:
            self.timer.start(100,self)
            self.btn2.setText('停止')
    def running(self):
        self.pb1.setMinimum(0)
        self.pb1.setMaximum(0)
        '''对于竖状进度条,默认是从下往上走'''
        self.pb2.setInvertedAppearance(True)
        self.pb2.setMinimum(0)
        self.pb2.setMaximum(0)
        self.pb3.setInvertedAppearance(True)
        self.pb3.setMinimum(0)
        self.pb3.setMaximum(0)
        self.pb4.setMinimum(0)
        self.pb4.setMaximum(0)

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    window=Window()
    window.show()

    sys.exit(app.exec_())