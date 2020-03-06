from PyQt5.Qt import *


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('QTextEdit-多行文本框-验证父对象方法')
        self.resize(250,250)
        self.initUI()
    def initUI(self):
        te=QTextEdit(self)
        te.resize(150,150)

        #设置显示滚动条
        te.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        #设置不显示滚动条
        te.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        btn=QPushButton(self)
        btn.setIcon(QIcon('xxx.png'))
        #设置角落按钮
        te.setCornerWidget(btn)


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    window=Window()
    window.show()

    sys.exit(app.exec_())