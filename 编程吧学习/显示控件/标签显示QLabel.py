from PyQt5.Qt import *


class Window1(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('QLabel标签显示控件')
        self.resize(500,300)
        self.initUI()
        self.show()
    def initUI(self):
        self.lb1 = QLabel('我的位置在哪里?')
        self.lb2 = QLabel('请输入第一个内容')
        self.lb3 = QLabel('请输入第二个内容')
        self.lb3.setWordWrap(True)

        self.ra1 = QRadioButton('左边')
        self.ra2 = QRadioButton('中间')
        self.ra3 = QRadioButton('右边')

        self.gb = QButtonGroup()
        self.gb.addButton(self.ra1,1)
        self.gb.addButton(self.ra2,2)
        self.gb.addButton(self.ra3,3)



        self.btn1 = QPushButton('输入内容1')
        self.btn2 = QPushButton('输入内容2')

        grid = QGridLayout(self)
        grid.addWidget(self.lb1,0,0,1,3)
        grid.addWidget(self.ra1,1,0)
        grid.addWidget(self.ra2,1,1)
        grid.addWidget(self.ra3,1,2)
        grid.addWidget(self.lb2,2,0)
        grid.addWidget(self.btn1,3,0)
        grid.addWidget(self.lb3,4,0)
        grid.addWidget(self.btn2,5,0)

        self.gb.buttonClicked.connect(self.rbclicked)
        self.btn1.clicked.connect(self.showdialog)
        self.btn2.clicked.connect(self.showdialog)
    def showdialog(self):
        sender = self.sender()
        if sender == self.btn1:
            text,ok = QInputDialog.getText(self,'请输入','请输入内容1:')
            print(text,ok)
            if ok:
                self.lb2.setText(text)
        elif sender == self.btn2:
            text, ok = QInputDialog.getText(self, '请输入', '请输入内容1:')
            if ok:
                self.lb3.setText(text)


    def rbclicked(self):
        if self.gb.checkedId() ==1:
            self.lb1.setAlignment(Qt.AlignLeft|Qt.AlignVCenter)
        elif self.gb.checkedId() ==2:
            self.lb1.setAlignment(Qt.AlignCenter)
        elif self.gb.checkedId() ==3:
            self.lb1.setAlignment(Qt.AlignRight|Qt.AlignVCenter)
class Window2(QWidget):
    def __init__(self):
        super(Window2, self).__init__()
        self.initui()
        self.show()
    def initui(self):
        lb = QLabel(self)
        html = '''<style type="text/css">
                    table.imagetable {
                        font-family: verdana,arial,sans-serif;
                        font-size:11px;
                        color:#333333;
                        border-width: 1px;
                        border-color: #999999;
                        border-collapse: collapse;}'''

        lb.setText(html)
class Window3(QWidget):
    def __init__(self):
        super(Window3, self).__init__()
        self.initui()
        self.show()
    def initui(self):
        self.lb = QLabel(self)
        self.lb.setGeometry(100,50,300,200)
        self.pix = QPixmap(r'./movie.gif')
        self.lb.setPixmap(self.pix)

        self.btn1 = QPushButton('开始',self)
        # self.btn3 = QPushButton('暂停',self)
        self.btn2 = QPushButton('结束',self)
        self.btn1.move(100,20)
        self.btn2.move(250,20)
        # self.btn3.move(175,20)

        self.btn1.clicked.connect(self.run)
        self.btn2.clicked.connect(self.run)
        # self.btn3.clicked.connect(self.run)

    def run(self):

        movie = QMovie(r'./movie.gif')#创建Qmovie对象,参数为movie的地址
        sender = self.sender()
        if sender == self.btn1:
            self.lb.setMovie(movie)
            movie.start()#运行movie
        elif sender == self.btn2:
            movie.stop()#停止运行movie
            self.lb.setPixmap(self.pix)
        # elif sender == self.btn3:
        #     print(movie.state())





class Tabwindow(QTabWidget):
    def __init__(self):
        super(Tabwindow, self).__init__()
        self.resize(450,350)
        win1 = Window1()
        win2 = Window2()
        win3 = Window3()
        self.addTab(win1,'纯文本显示')
        self.addTab(win2,'富文本显示')
        self.addTab(win3,'动画显示')









if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    tabwin = Tabwindow()
    tabwin.show()

    sys.exit(app.exec_())