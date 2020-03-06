from PyQt5.Qt import *

class Storage():
    @staticmethod
    def storage():
        account_pwd={'123':'321','456':'654','789':'987'}
        # account_pwd[account]=pwd
        return account_pwd

class AccountTool:
    ACCOUNT_ERROR = 1
    PWD_ERROR=2
    SUCCESS=3
    @staticmethod
    def check_login(account,pwd):
        account_pwd= Storage.storage()
        if account not in account_pwd.keys():
            return AccountTool.ACCOUNT_ERROR
        if pwd!=account_pwd[account]:
            return AccountTool.PWD_ERROR
        return AccountTool.SUCCESS


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('QLineEdit-单行文本框')
        self.resize(250,250)
        self.setMinimumSize(200,200)
        self.initUI()
    def initUI(self):
        # self.创建()
        # self.案例1()
        # self.输出模式()
        # self.案例2()
        self.限定限制()
    def 创建(self):
        Pl=QLineEdit('st',self)
        Pl.setText('gzlin')
        btn=QPushButton('按钮',self)
        btn.move(100,100)
        # btn.clicked.connect(lambda : Pl.insert('888'))#在光标处插入
        btn.clicked.connect(lambda : print(Pl.text()))#提取文本框内容
    def 案例1(self):
        '''创建2个文本框,1个按钮,点击按钮将文本框A内容复制到文本框B'''
        wb1=QLineEdit(self)
        wb2=QLineEdit(self)
        btn=QPushButton('复制',self)
        btn.move(50,150)
        # def cao():
        #     str=wb1.text()
        #     wb2.setText(str)
        btn.clicked.connect(lambda :wb2.setText(wb1.text()))
        wb1.move(50,50)
        wb2.move(50,100)
    def 输出模式(self):
        wb1 = QLineEdit(self)
        wb1.move(50, 50)
        label=QLabel('此处显示打印结果',self)
        label.move(50,100)
        btn = QPushButton('打印', self)
        btn.move(50, 150)
        # wb1.setEchoMode(QLineEdit.NoEcho)#什么都看不见
        wb1.setEchoMode(QLineEdit.Normal)#一直能看见
        wb1.setEchoMode(QLineEdit.Password)#密码方式
        wb1.setEchoMode(QLineEdit.PasswordEchoOnEdit)#编辑时能看见,移除焦点无法看见
        # btn.clicked.connect(lambda :label.setText(wb1.text()))#获取真实内容
        btn.clicked.connect(lambda :label.setText(wb1.displayText()))#获取看到的内容
    def 案例2(self):
        '''创建2个文本框和1个按钮,2个文本框一个输入账号,一个输入密码,点击登录按钮后
        获取账号和密码信息,与正确的账号密码对比,如果账号错误,则清空账号和密码框,如果密码
        错误则清除密码框
        账号:hher_12345;密码:8574mki'''
        # label1=QLabel('账号:',self)
        # label1.move(10,50)
        # label1=QLabel('密码:',self)
        # label1.move(10, 100)
        self.account_le=QLineEdit(self)
        self.account_le.setPlaceholderText('请输入账号')#占位文本
        #设置默认记住文本

        completer=QCompleter(Storage.storage().keys(),self.account_le)
        self.account_le.setCompleter(completer)


        #明文密文切换函数
        def cao():
            if self.pwd_le.echoMode()==QLineEdit.Password:
                self.pwd_le.setEchoMode(QLineEdit.Normal)
            else:
                self.pwd_le.setEchoMode(QLineEdit.Password)

        self.pwd_le=QLineEdit(self)
        self.pwd_le.setPlaceholderText('请输入密码')#设置占位文本
        #设置输入内容默认为密文显示
        self.pwd_le.setEchoMode(QLineEdit.Password)
        action=QAction(self.pwd_le)
        action.setIcon(QIcon('xxx.png'))
        action.triggered.connect(cao)
        #设置明文密文切换显示
        self.pwd_le.addAction(action,QLineEdit.TrailingPosition)
        # 设置快捷清除按钮
        self.pwd_le.setClearButtonEnabled(True)

        self.btn=QPushButton('登     录',self)
        self.btn.clicked.connect(self.cao)
    #案例2使用
    # def cao(self):
    #         account=self.account_le.text()
    #         pressed=self.pwd_le.text()
    #
    #         state=AccountTool.check_login(account,pressed)
    #
    #         if state == AccountTool.ACCOUNT_ERROR:
    #             self.account_le.setText('')
    #             self.pwd_le.setText('')
    #             self.account_le.setFocus()
    #             return None
    #         if state==AccountTool.PWD_ERROR:
    #             self.pwd_le.setText('')
    #             self.pwd_le.setFocus()
    #             return None
    #         if state==AccountTool.SUCCESS:
    #             self.btn.setText('登录成功')
    def 限定限制(self):
        le_a=QLineEdit(self)
        #设置长度限制,也可以限制使用代码输入的内容
        le_a.setMaxLength(5)
        #设置只读模式,当使用代码输入内容时则不好使
        # le_a.setReadOnly(True)

    #窗口尺寸行为,窗口在创建时自动运行了,案例2使用
    # def resizeEvent(self, QResizeEvent) -> None:
    #     wb_width=150
    #     wb_hight=40
    #     space=20
    #
    #     self.account_le.resize(wb_width,wb_hight)
    #     self.pwd_le.resize(wb_width,wb_hight)
    #     self.btn.resize(wb_width,wb_hight)
    #
    #     x=(self.width()-wb_width)/2
    #
    #     self.account_le.move(x,self.height()/8)
    #     self.pwd_le.move(x,self.account_le.y()+wb_hight+space)
    #     self.btn.move(x,self.pwd_le.y()+wb_hight+space)







if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    window=Window()
    window.show()

    sys.exit(app.exec_())