from PyQt5.Qt import *
import sys,random,time

class MyWindows(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('石头剪刀布')
        self.setGeometry(900,250,1000,500)
        self.initUI()
        self.show()
    def initUI(self):
        self.btn1=QPushButton('石头',self)
        self.btn2=QPushButton('剪刀',self)
        self.btn3=QPushButton('布',self)
        self.btn1.move(100,200)
        self.btn2.move(200,200)
        self.btn3.move(300,200)
        self.btn1.clicked.connect(self.computer)
        self.btn2.clicked.connect(self.computer)
        self.btn3.clicked.connect(self.computer)

    def computer(self):
        num=random.randint(1,3)
        player=0
        if self.sender().text()=='石头':
            player = 1

        elif self.sender().text()=='剪刀':
            player = 2

        elif self.sender().text()=='布':
            player = 3

        if num==player:
            QMessageBox.about(self,'提示','打成平手')
        elif player==1 and num==2:
            QMessageBox.about(self, '提示', '恭喜你赢了,电脑出剪刀')
        elif player==1 and num==3:
            QMessageBox.about(self, '提示', '很遗憾你输了,电脑出布')
        elif player==2 and num==1:
            QMessageBox.about(self, '提示', '很遗憾你输了,电脑出石头')
        elif player==2 and num==3:
            QMessageBox.about(self, '提示', '恭喜你赢了,电脑出布')
        elif player==3 and num==1:
            QMessageBox.about(self, '提示', '恭喜你赢了,电脑出石头')
        elif player==3 and num==2:
            QMessageBox.about(self, '提示', '很遗憾你输了,电脑出剪刀')






if __name__ == '__main__':
    app=QApplication(sys.argv)
    win=MyWindows()
    sys.exit(app.exec_())