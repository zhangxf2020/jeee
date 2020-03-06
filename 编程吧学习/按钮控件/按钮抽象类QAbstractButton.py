from PyQt5.Qt import *


class Window1(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('QAbstractButton按钮抽象类')
        # self.resize(250,250)
        self.initUI()
    def initUI(self):

        btn1 = QPushButton('芝',self)
        btn2 = QPushButton('麻',self)
        btn3 = QPushButton('开',self)
        btn4 = QPushButton('门',self)

        label1 = QLabel('密码输入区:',self)
        label1.move(0,10)
        label2 = QLabel('正确密码：麻', self)
        label2.move(0,100)
        label3 = QLabel('你输入的密码：', self)
        label3.move(0,150)
        self.label4 = QLabel('   ',self)
        self.label4.move(100,150)
        btn1.resize(40,40)
        btn2.resize(40,40)
        btn3.resize(40,40)
        btn4.resize(40,40)

        btn1.move(60,20)
        btn2.move(110,20)
        btn3.move(60,60)
        btn4.move(110,60)
        '''
        # 设置按钮按下去的效果打开(即按下去不弹开的效果)
        '''
        btn1.setCheckable(True)
        btn2.setCheckable(True)
        btn3.setCheckable(True)
        btn4.setCheckable(True)
        '''# 设置按钮按下去的效果互斥'''
        btn1.setAutoExclusive(True)
        btn2.setAutoExclusive(True)
        btn3.setAutoExclusive(True)
        btn4.setAutoExclusive(True)

        btn1.clicked.connect(self.showpasswd)
        btn2.clicked.connect(self.showpasswd)
        btn3.clicked.connect(self.showpasswd)
        btn4.clicked.connect(self.showpasswd)
    def showpasswd(self):
        word = self.sender().text()
        self.label4.setText(word)
        if self.label4.text()=='麻':
            QMessageBox.information(self,'答对了','恭喜你,密码正确,可以开门了')
class Window2(QWidget):
    def __init__(self):
        super().__init__()
        self.init()
        self.show()
    def init(self):
        btn1 = QPushButton('芝', self)
        btn2 = QPushButton('麻', self)
        btn3 = QPushButton('开', self)
        btn4 = QPushButton('门', self)

        label1 = QLabel('密码输入区:', self)
        label1.move(0, 10)
        label2 = QLabel('正确密码：芝麻开门', self)
        label2.move(0, 100)
        label3 = QLabel('你输入的密码：', self)
        label3.move(0, 150)
        self.label4 = QLabel('           ', self)
        self.label4.move(100, 150)
        btn1.resize(40, 40)
        btn2.resize(40, 40)
        btn3.resize(40, 40)
        btn4.resize(40, 40)

        btn1.move(60, 20)
        btn2.move(110, 20)
        btn3.move(60, 60)
        btn4.move(110, 60)
        '''
        # 设置按钮按下去的效果打开(即按下去不弹开的效果)
        '''
        btn1.setCheckable(True)
        btn2.setCheckable(True)
        btn3.setCheckable(True)
        btn4.setCheckable(True)
        btn1.isChecked()

        btn1.clicked.connect(self.showpasswd)
        btn2.clicked.connect(self.showpasswd)
        btn3.clicked.connect(self.showpasswd)
        btn4.clicked.connect(self.showpasswd)
        self.password = ''
    def showpasswd(self,pressed):
        word = self.sender().text()
        if len(self.password) < 4:
            if self.sender().isChecked():
                self.password += word
            else:
                '''str.replace()作用是将原字符中的x更换为X
                '''
                self.password = self.password.replace(word,'')
        else:
            self.password = self.password.replace(word, '')
        self.label4.setText(self.password)
        if len(self.password) == 4 and self.password == '芝麻开门':
            QMessageBox.information(self, '提示', '恭喜，密码正确，可以进入！')

class Window3(QWidget):
    def __init__(self):
        super().__init__()
        self.init()
        self.show()
    def init(self):
        mylyout = QVBoxLayout(self)
        mylyout1 = QHBoxLayout()
        gid = QGridLayout()
        self.btn1 = QPushButton('1')
        self.btn2 = QPushButton('2')
        self.btn3 = QPushButton('3')
        self.btn11 = QPushButton('1')
        self.btn12 = QPushButton('2')
        self.btn13 = QPushButton('3')
        self.btn21 = QPushButton('1')
        self.btn22 = QPushButton('2')
        self.btn23 = QPushButton('3')
        self.btn1.setCheckable(True)
        self.btn2.setCheckable(True)
        self.btn3.setCheckable(True)
        self.btn11.setCheckable(True)
        self.btn12.setCheckable(True)
        self.btn13.setCheckable(True)
        self.btn21.setCheckable(True)
        self.btn22.setCheckable(True)
        self.btn23.setCheckable(True)

        self.gr1 = QButtonGroup(self)
        self.gr2 = QButtonGroup(self)
        self.gr3 = QButtonGroup(self)

        self.gr1.addButton(self.btn1,1)
        self.gr1.addButton(self.btn2,2)
        self.gr1.addButton(self.btn3,3)
        self.gr2.addButton(self.btn11,1)
        self.gr2.addButton(self.btn12,2)
        self.gr2.addButton(self.btn13,3)
        self.gr3.addButton(self.btn21,1)
        self.gr3.addButton(self.btn22,2)
        self.gr3.addButton(self.btn23,3)



        gid.addWidget(self.btn1,0,0)
        gid.addWidget(self.btn2,0,1)
        gid.addWidget(self.btn3,0,2)
        gid.addWidget(self.btn11,1,0)
        gid.addWidget(self.btn12,1,1)
        gid.addWidget(self.btn13,1,2)
        gid.addWidget(self.btn21,2,0)
        gid.addWidget(self.btn22,2,1)
        gid.addWidget(self.btn23,2,2)

        lb1 = QLabel('密码输入区:')
        lb2 = QLabel('当前密码为:321')


        lb3 = QLabel('当前密码显示为:')
        self.lb4 = QLabel()
        mylyout1.addWidget(lb3)
        mylyout1.addWidget(self.lb4)
        mylyout.addWidget(lb1)
        mylyout.addLayout(gid)
        mylyout.addWidget(lb2)
        mylyout.addLayout(mylyout1)

        self.pwd1,self.pwd2,self.pwd3 = '','',''

        self.gr1.buttonClicked.connect(self.setpassword)
        self.gr2.buttonClicked.connect(self.setpassword)
        self.gr3.buttonClicked.connect(self.setpassword)
    def setpassword(self):
        sender = self.sender()
        '''只要当前操作的控件是按钮组中的控件,就把所点击控件的id传给对应的字符串'''
        if sender == self.gr1:
            self.pwd1 = str(self.gr1.checkedId())
        elif sender == self.gr2:
            self.pwd2 = str(self.gr2.checkedId())
        elif sender == self.gr3:
            self.pwd3 = str(self.gr3.checkedId())
        self.lb4.setText(self.pwd1+self.pwd2+self.pwd3)
        if self.lb4.text() =='321':
            QMessageBox.information(self,'提示','恭喜,正确!')




class Main_tab(QTabWidget):
    def __init__(self):
        super().__init__()
        self.tab()
        self.setGeometry(200,200,300,250)
    def tab(self):
        win1 = Window1()
        win2 = Window2()
        win3 = Window3()
        self.addTab(win1,'第一个程序')
        self.addTab(win2,'第二个程序')
        self.addTab(win3,'第三个程序')





if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    window=Main_tab()
    window.show()

    sys.exit(app.exec_())