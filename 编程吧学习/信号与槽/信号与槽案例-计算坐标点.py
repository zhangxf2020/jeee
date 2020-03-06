from PyQt5.Qt import *


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('计算坐标点')
        self.resize(1000,500)
        self.initUI()
        self.setMouseTracking(True)
        print("初始化:"+str(self.pos))
    def initUI(self):
        self.lb=QLabel(self)
        self.lb.resize(1000,15)

        self.pos=None
    def mouseMoveEvent(self, QMouseEvent):
        self.num=round(((QMouseEvent.x()-500)**2+(QMouseEvent.y()-250)**2)**0.5)
        self.lb.setText('鼠标坐标:({},{})  距离中心点距离:{}'.format(QMouseEvent.x(),QMouseEvent.y(),self.num))
        print('修改前'+str(self.pos))
        self.jj=QMouseEvent.pos()
        print(self.pos)
        self.update()

    def paintEvent(self, QPaintEvent):
        try:
            q=QPainter(self)
            q.drawLine(0,0,self.jj.x(),self.jj.y())
        except:
            return None


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)

    window=Window()
    window.show()

    sys.exit(app.exec_())