from PyQt5.Qt import *


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('')
        self.resize(500,500)
        # self.initUI()
        # self.信号状态改变()
        # self.按钮组()
        self.信号处理()
    def initUI(self):
        qb1=QRadioButton(self)#如果只有一个单选框,则可以自己变换选项,多个则只能互相变换
        qb2=QRadioButton(self)
        qb1.move(100,100)
        qb2.move(100,200)
        qb1.setText('男')
        qb2.setText('女')
        qb2.setChecked(True)#设置默认选中状态
        qb1.setShortcut('ALT+s')#设置快捷键
    def 信号状态改变(self):
        qb1 = QRadioButton(self)  # 如果只有一个单选框,则可以自己变换选项,多个则只能互相变换
        qb2 = QRadioButton(self)
        qb3 = QRadioButton(self)
        qb4 = QRadioButton(self)
        qb1.move(100, 100)
        qb2.move(100, 200)
        qb3.move(300, 100)
        qb4.move(300, 200)
        qb1.setText('男')
        qb2.setText('女')
        qb3.setText('是')
        qb4.setText('否')
        qb1.toggled.connect(lambda isChecked:print(isChecked))#连接是否选中的信号
        qb1.setAutoExclusive(False)#设置是否独占,不独占的话就不是互斥关系
    def 按钮组(self):
        qb1 = QRadioButton(self)  # 如果只有一个单选框,则可以自己变换选项,多个则只能互相变换
        qb2 = QRadioButton(self)
        qb3 = QRadioButton(self)
        qb4 = QRadioButton(self)
        qb1.move(100, 100)
        qb2.move(100, 200)
        qb3.move(300, 100)
        qb4.move(300, 200)
        qb1.setText('男')
        qb2.setText('女')
        qb3.setText('是')
        qb4.setText('否')
        qb1.setChecked(True)#设置按钮默认选中
        qb_group1=QButtonGroup(self)#添加按钮组
        qb_group1.addButton(qb1,1)
        qb_group1.addButton(qb2,2)
        qb_group2=QButtonGroup(self)
        qb_group2.addButton(qb3)
        qb_group2.addButton(qb4)

        print(qb_group1.buttons())#查看按钮组中对象
        print(qb_group1.button(1))#查看按钮组中id为1的对象
        print(qb_group1.checkedButton())#查看按钮组中被选中的对象
    def 信号处理(self):
        btn_nan=QRadioButton('男',self)
        btn_nan.move(100,100)
        btn_nv=QRadioButton('女',self)
        btn_nv.move(100,150)
        btn_group=QButtonGroup(self)
        btn_group.addButton(btn_nan,1)
        btn_group.addButton(btn_nv,2)
        def cao(val):

            print(btn_group.id(val))
        # btn_group.buttonClicked.connect(cao)#按钮组中有被点击
        # btn_group.buttonPressed.connect(cao)#按钮组中有被按下
        # btn_group.buttonReleased.connect(cao)#按钮组中有被释放
        btn_group.buttonToggled.connect(cao)#按钮组中状态有被改变



if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    window=Window()
    window.show()

    sys.exit(app.exec_())