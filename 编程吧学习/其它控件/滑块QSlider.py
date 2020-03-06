from PyQt5.Qt import *


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('QSlider例子')
        self.resize(650,250)
        self.initUI()
    def initUI(self):
        self.sld1 = QSlider(Qt.Vertical,self)
        self.sld2 = QSlider(Qt.Horizontal,self)
        self.sld2.move(450,220)
        '''设置滑块的位置,宽和高'''
        self.sld1.setGeometry(20,30,20,100)
        '''设置滑块的最小,最大值'''
        self.sld1.setMinimum(0)
        self.sld1.setMaximum(99)
        '''设置刻度的显示方式
        QSlider.NoTicks 0  不绘制任何刻度线
        QSlider.TicksBothSides 3  在滑块的两侧绘制刻度线
        QSlider.TicksAbove 1  在（水平）滑块上方绘制刻度线
        QSlider.TicksBelow 2  在（水平）滑块下方绘制刻度线
        QSlider.TicksLeft  TicksAbove 在（垂直）滑块左侧绘制刻度线    
        QSlider.TicksRight TicksBelow 在（垂直）滑块右侧绘制刻度线'''
        self.sld1.setTickPosition(QSlider.TicksLeft)

        self.lb1 = QLabel(self)
        self.lb1.setPixmap(QPixmap(r'./pic/1.jpg'))
        self.lb1.move(50,30)
        self.lb2 = QLabel('滑动块1当前值: 0 ',self)
        self.lb3 = QLabel('滑动块2当前值: 0 ',self)
        self.lb3.move(0,10)


        self.sld1.valueChanged[int].connect(self.changevalue)
        self.sld2.valueChanged[int].connect(self.changevalue)
    def changevalue(self,value):
        sender = self.sender()
        if sender == self.sld1:
            self.sld2.setValue(value)
        else:self.sld1.setValue(value)
        self.lb2.setText('滑动块1当前值:'+str(value))
        self.lb3.setText('滑动块2当前值:'+str(value))
        if value == 0:
            '''设置标签图片'''
            self.lb1.setPixmap(QPixmap(r'./pic/1.jpg'))
        elif value < 30:
            self.lb1.setPixmap(QPixmap(r'./pic/2.jpg'))
        elif value < 60:
            self.lb1.setPixmap(QPixmap(r'./pic/3.jpg'))
        else:self.lb1.setPixmap(QPixmap(r'./pic/4.jpg'))

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    window=Window()
    window.show()

    sys.exit(app.exec_())