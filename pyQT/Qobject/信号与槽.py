from PyQt5.Qt import *


class Window(QWidget):
    def __init__(self,name):
        super().__init__()
        self.setWindowTitle(name)
        self.resize(500,500)
        self.initUI()
    def initUI(self):
        btn1=QPushButton(self)
        btn1.move(250,250)
        btn1.setText('点击我')
        btn1.clicked.connect(self.obj_dayin)
    def obj_dayin(self):
            print('打印的东西')



if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    # window=Window('haha')
    window=QWidget()
    def cao(title):
        window.blockSignals(True)#暂时断开与槽的联系
        print('窗口内容变化了',title)
        window.setWindowTitle('jj-'+title)
        window.blockSignals(False)#关闭断开与槽的联系

    window.windowTitleChanged.connect(cao)

    window.setWindowTitle('sea')
    window.setWindowTitle('sea1')
    window.show()

    sys.exit(app.exec_())