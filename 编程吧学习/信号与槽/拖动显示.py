from PyQt5.Qt import *
import sys

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('我的程序')
        self.setWindowIcon(QIcon('123.png'))
        self.resize(500,500)
        self.move(1100,200)
        self.Myui()
        self.show()
    def Myui(self):
        btn=QPushButton('退出',self)
        btn.move(200,400)
        btn.clicked.connect(QCoreApplication.instance().quit)




if __name__ == '__main__':
    app=QApplication(sys.argv)
    win=Window()
    sys.exit(app.exec_())
