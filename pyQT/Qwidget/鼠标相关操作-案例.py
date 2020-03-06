from PyQt5.Qt import *

import sys
class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('鼠标操作相关案例')
        self.resize(500, 500)
        self.move(1000, 200)
        self.setMouseTracking(True)#打开鼠标移进跟踪
        self.setCursor(QCursor(QPixmap('xxx.png').scaled(10, 10)))#设定鼠标样式(设定样式为(图片(路径).大小))
        lable = QLabel(self)
        lable.setText('白日依山尽,黄河入海流')
        lable.move(200, 300)
        lable.setStyleSheet('background-color:yellow')

    def mouseMoveEvent(self, ev) -> None:
        print('shubiaoyidongle',ev.localPos())
        lable=self.findChild(QLabel)
        lable.move(ev.localPos().x(),ev.localPos().y())

app = QApplication(sys.argv)
window=MyWindow()


window.show()
sys.exit(app.exec_())
