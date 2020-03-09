from PyQt5.Qt import *
import sys

class My_Window(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(500,500)
        self.setWindowTitle('动画组学习')
        self.initui()
    def initui(self):
        self.red_btn = QPushButton('暂停',self)
        self.green_btn = QPushButton('开始',self)

        self.red_btn.resize(50,50)
        self.green_btn.resize(50,50)
        self.green_btn.move(100,100)
        self.red_btn.setStyleSheet('background-color:red')
        self.green_btn.setStyleSheet('background-color:green')

        self.animation = QPropertyAnimation(self.green_btn,b'pos',self)
        self.animation.setKeyValueAt(0.25,QPoint(350,100))
        self.animation.setKeyValueAt(0.5,QPoint(350,350))
        self.animation.setKeyValueAt(0.75,QPoint(100,350))
        self.animation.setKeyValueAt(1,QPoint(100,100))
        self.animation.setDuration(5000)
        # self.animation.setLoopCount(3)


        self.animation1 = QPropertyAnimation(self.red_btn, b'pos', self)
        self.animation1.setKeyValueAt(0.25, QPoint(0, 450))
        self.animation1.setKeyValueAt(0.5, QPoint(450, 450))
        self.animation1.setKeyValueAt(0.75, QPoint(450, 0))
        self.animation1.setKeyValueAt(1, QPoint(0, 0))
        self.animation1.setDuration(10000)
        # self.animation1.setLoopCount(3)

        self.animation2 = QParallelAnimationGroup(self)#并行动画组
        self.animation2 = QSequentialAnimationGroup(self)#串行动画组
        self.animation2.addAnimation(self.animation)
        self.animation2.addPause(5000)#等待多久可以执行下一个动画
        self.animation2.addAnimation(self.animation1)
        self.animation2.start()

        self.red_btn.clicked.connect(lambda :self.animation2.pause())
        self.green_btn.clicked.connect(lambda :self.animation2.resume())




if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = My_Window()
    win.show()
    sys.exit(app.exec_())
