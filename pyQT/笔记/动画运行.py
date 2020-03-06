from PyQt5.Qt import *
import sys

class My_Win(QWidget):
    def __init__(self):
        super(My_Win, self).__init__()
        self.setWindowTitle('动画运行')
        self.setGeometry(1000,300,300,300)
        self.flog = 0
        self.initui()
    def initui(self):
        # self.动画效果()
        self.线性变化()
    def 动画效果(self):

        btn = QPushButton('test',self)
        btn.resize(50,50)
        # btn.move(100,100)

        # andmin = QPropertyAnimation(btn,b'pos',self)#设置坐标变化
        andmin = QPropertyAnimation(btn,b'size',self)#设置尺寸变化
        andmin = QPropertyAnimation(btn,b'geometry',self)#设置窗体变化
        andmin = QPropertyAnimation(self,b'windowOpacity',self)#设置不透明变化
        # andmin.setStartValue(QRect(0,0,0,0))
        # andmin.setEndValue(QRect(300,300,300,300))

        andmin.setStartValue(1)
        andmin.setKeyValueAt(0.5,0.5)#设置差值,第一个参数--在总时长的什么部分,第二个参数--变化值
        andmin.setKeyValueAt(1,1)#设置差值,第一个参数--在总时长的什么部分(0-1),第二个参数--变化值
        # andmin.setEndValue(0)
        andmin.setDuration(10000)
        andmin.start()
    def 线性变化(self):
        self.btn = QPushButton('test',self)
        self.btn.resize(50,50)
        self.btn.clicked.connect(self.btn_clicked)

        self.aadnmin = QPropertyAnimation(self.btn,b'pos',self)
        self.aadnmin.setStartValue(QPoint(0,0))
        self.aadnmin.setEndValue(QPoint(250,250))
        self.aadnmin.setEasingCurve(QEasingCurve.OutInBounce)
        self.aadnmin.setLoopCount(3)#设置循环次数
        # self.aadnmin.setDirection(QAbstractAnimation.Backward)#设置动画方向(此处是反着走)
        # self.aadnmin.currentLoopChanged[int].connect(lambda x: [self.aadnmin.setDirection(QAbstractAnimation.Backward),print(x)] [x==1] )#循环次数信号,从0开始
        self.aadnmin.directionChanged.connect(lambda x:print(x))#方向改变发射信号
        self.aadnmin.finished.connect(lambda :print('动画完成了'))#全部循环完毕之后
        self.aadnmin.stateChanged.connect(lambda ns,os:print('状态发生改变了',ns,os))

        self.aadnmin.setDuration(3000)
        self.aadnmin.start()

    def btn_clicked(self):
        #第一种方式,设置标记
        # if self.flog ==0:
        #     self.aadnmin.pause()
        #     self.flog =1
        # else:
        #     self.aadnmin.start()
        #     self.flog =0
        #第二种方式,判断是否运行
        if self.aadnmin.state()==QPropertyAnimation.Running:
            self.aadnmin.pause()
        elif self.aadnmin.state() == QPropertyAnimation.Paused:
            self.aadnmin.resume()
        elif self.aadnmin.state() == QPropertyAnimation.Stopped:
            self.aadnmin.start()




if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = My_Win()
    win.show()
    sys.exit(app.exec_())