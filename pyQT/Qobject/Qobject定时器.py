from PyQt5.Qt import *

class MyLable(QLabel):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.setText('10')
        self.setStyleSheet('font-size:33px;')
        self.move(100, 100)
        self.timer_id=self.startTimer(1000)#执行starttimer自动调用对象的timerevent函数
    def timerEvent(self,*args,**kwargs):#重写对象的timerevent函数,作用是每隔一秒减少一个数字
        current_sec=int(self.text())
        current_sec-=1
        self.setText(str(current_sec))
        if current_sec==0:
            self.killTimer(self.timer_id) #满足条件后关掉定时器(定时器ID)
    def Setcec(self,sec):
        self.setText(str(sec))



class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('定时器的使用')
        self.resize(200,200)
        self.initUI()
    def initUI(self):
        lable=MyLable(self)
        lable.Setcec(50)
        # lable.startTimer(1000)



if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    window=Window()
    window.show()

    sys.exit(app.exec_())