from PyQt5.Qt import *


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('QCheckBox-多选框')
        self.resize(500,500)
        self.initUI()
    def initUI(self):
        # self.功能()
        self.信号()
    def 功能(self):
        cb=QCheckBox('python',self)
        cb.setTristate(True)#设置三态
        # cb.setCheckState(Qt.Unchecked) #默认未选中 0
        # cb.setCheckState(Qt.PartiallyChecked)#默认半选中 1
        # cb.setCheckState(Qt.Checked)#默认被选中 2

        print(cb.checkState())
    def 信号(self):
        cb=QCheckBox('python',self)
        cb.setTristate(True)
        # cb.stateChanged.connect(lambda state:print(state))#三态信号
        cb.toggled.connect(lambda isChecked:print(isChecked))#父类信号


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    window=Window()
    window.show()

    sys.exit(app.exec_())