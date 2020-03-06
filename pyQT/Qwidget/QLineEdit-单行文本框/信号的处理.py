from PyQt5.Qt import *


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('信号的处理')
        self.resize(250,250)
        self.initUI()
    def initUI(self):
        le=QLineEdit(self)
        le.move(50,50)

        #文本编辑时发射信号
        # le.textEdited.connect(lambda val:print('内容遭受了编辑',val))
        #文本发生改变时发射信号
        # le.textChanged.connect(lambda val:print('内容遭受了改变',val))
        #按下回车时发射信号
        # le.returnPressed.connect(lambda :print('内容发生了改变'))
        #结束编辑时发射信号(失去焦点)
        le.editingFinished.connect(lambda val:print('已经结束了编辑',val))
        #光标位置发生改变时发射信号
        # le.cursorPositionChanged.connect(lambda :print('光标移动了'))
        #选中的文本发生改变时发射信号
        # le.selectionChanged.connect(lambda :print('文本被选中了'))
if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    window=Window()
    window.show()

    sys.exit(app.exec_())