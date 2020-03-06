from PyQt5.Qt import *


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('QLineEdit-光标位置控制')
        self.resize(250,250)
        self.initUI()
    def initUI(self):
        # self.光标位置练习()
        self.案例1()
    def 光标位置练习(self):
        le=QLineEdit(self)
        le.move(50,50)

        def setcursor():
            # le.cursorBackward(True,3)#设置向后移动x个距离,并且设置选中TRUE
            # le.cursorForward(False,4)#设置向前(向右)移动X个距离,并且设置不选中False
            # le.cursorWordBackward(True)#向左移动一个单词的距离
            # le.cursorWordForward(True)#向右移动一个单词的距离
            # le.home(True)#移到最开始
            # le.end(True)#移到末尾
            # le.setCursorPosition(5)#设置移动的位置
            # print(le.cursorPosition())#获取光标位置
            print(le.cursorPositionAt(QPoint(50,5)))#获取指定坐标点设置光标位置,按照内容总长度算

            le.setFocus()
        btn=QPushButton('设置光标',self)
        btn.move(50,100)
        btn.clicked.connect(setcursor)
    def 案例1(self):
        '''设置长内容后,自动将光标移动到最前方'''
        le = QLineEdit(self)
        le.move(50, 50)

        le.setText('白日依山尽'*5)
        le.home(False)








if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    window=Window()
    window.show()

    sys.exit(app.exec_())