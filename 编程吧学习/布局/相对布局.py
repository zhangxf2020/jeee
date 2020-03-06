from PyQt5.Qt import *


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('相对布局')
        self.resize(250,250)
        self.initUI()
    def initUI(self):
        btn1=QPushButton('石头',self)
        btn2=QPushButton('剪刀',self)
        btn3=QPushButton('布',self)
        #addStretch(1):将控件中间的空白部位按比例划分
        laytH=QHBoxLayout()
        laytH.addStretch(1)
        laytH.addWidget(btn1)
        laytH.addStretch(1)
        laytH.addWidget(btn2)
        laytH.addStretch(1)
        laytH.addWidget(btn3)
        laytH.addStretch(100)

        laytV=QVBoxLayout()
        laytV.addStretch(1)
        laytV.addLayout(laytH)

        self.setLayout(laytV)



if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    window=Window()
    window.show()

    sys.exit(app.exec_())