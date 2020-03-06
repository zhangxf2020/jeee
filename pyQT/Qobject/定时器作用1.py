from PyQt5.Qt import *


class Window(QWidget):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.setWindowTitle('定时器作用1')
        self.resize(100,100)
        self.myid=self.startTimer(100)
        self.initUI()
    def initUI(self):
        pass

    def timerEvent(self,*args,**kwargs):
        current_w=self.width()
        current_h=self.height()
        self.resize(current_w+10,current_h+10)

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    window=Window()

    window.show()

    sys.exit(app.exec_())