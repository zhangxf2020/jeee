from PyQt5.Qt import *
import random

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('猜数字游戏')
        self.resize(250,250)

        self.initUI()
        self.show()
    def initUI(self):
        lb=QLineEdit(self)
        lb.move(20,20)
        lb.setToolTip('请输入您认为的数字')
        lb.setText('点击这里输入数字')
        lb.selectAll()
        lb.setFocus()
        self.lb=lb
        self.num1 = random.randint(1, 10)
        btn=QPushButton('我猜',self)
        btn.move(50,50)
        btn.clicked.connect(self.text)
    def text(self):
        self.num=self.lb.text()

        try:
            if int(self.num)>self.num1:
                self.msg=QMessageBox.about(self,'结果','太大了')
                self.lb.setFocus()
            elif int(self.num)<self.num1:
                self.msg = QMessageBox.about(self, '结果', '太小了')
                self.lb.setFocus()
            else:
                self.msg = QMessageBox.about(self, '结果', '猜对了,进入下一轮')
                self.lb.clear()
                self.lb.setFocus()
                self.num1 = random.randint(1, 10)
        except:
            self.msg = QMessageBox.about(self, '错误', '您输入的数字不正确')
    def closeEvent(self, QCloseEvent):
        reply=QMessageBox.question(self,'确认','确认退出吗?',QMessageBox.Yes|QMessageBox.No,QMessageBox.No)
        if reply==QMessageBox.Yes:
            QCloseEvent.accept()
        else:
            QCloseEvent.ignore()




if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    window=Window()
    sys.exit(app.exec_())