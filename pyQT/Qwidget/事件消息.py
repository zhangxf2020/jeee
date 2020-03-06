from PyQt5.Qt import *


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('事件消息的学习')
        self.resize(500,500)
        self.initUI()
    def initUI(self):
        pass


    def showEvent(self, a0:QShowEvent) -> None:#显示事件
        print('窗口被展示出来')
    def closeEvent(self, a0:QCloseEvent) -> None:#关闭事件
        print('窗口被关闭了')
    def moveEvent(self, a0:QMoveEvent) -> None:#移动事件
        print('窗口在移动')
    def resizeEvent(self, a0:QResizeEvent) -> None:#尺寸改变
        print('窗口大小改变')
    def enterEvent(self, a0:QEvent) -> None:#鼠标进来
        print('鼠标进来了')
        self.setStyleSheet('background-color:green')
    def leaveEvent(self,QEvent) -> None:#鼠标出去
        print('鼠标出去了')
        self.setStyleSheet('background-color:yellow')
    def mousePressEvent(self, a0:QMouseEvent) -> None:
        print('鼠标按下')
    def mouseReleaseEvent(self, a0:QMouseEvent) -> None:
        print('鼠标被释放')
    def mouseDoubleClickEvent(self, a0:QMouseEvent) -> None:
        print('鼠标双击了')
    def mouseMoveEvent(self, a0:QMouseEvent) -> None:
        print('鼠标按下移动了')
     #**********键盘事件************开始
    def keyPressEvent(self, a0:QKeyEvent) -> None:
        print('键盘上一个键按下了')
    def keyReleaseEvent(self, a0: QKeyEvent) -> None:
        print('键盘上键松开了')
     #**********键盘事件************结束

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    window=Window()
    window.show()

    sys.exit(app.exec_())