from PyQt5.Qt import *
import sys

class mylabel(QLabel):
    def enterEvent(self, ev:QMouseEvent) -> None:
        self.setText('欢迎光临')
    def leaveEvent(self, ev:QMouseEvent) -> None:
        self.setText('谢谢惠顾')
    def keyPressEvent(self, evt) -> None:
        if evt.key()==Qt.Key_Tab:
            print('您按下了Tab键')
        elif evt.modifiers()==Qt.ControlModifier|Qt.ShiftModifier and evt.key()==Qt.Key_S:
            print('您点击了CTRL+S键')
app = QApplication(sys.argv)
window=QWidget()
window.setWindowTitle('鼠标相关操作')
window.resize(500,500)
label=mylabel(window)
label.resize(200,200)
label.setText('我是一个标签')
label.move(200,200)
label.setStyleSheet('background-color:yellow')
label.grabKeyboard()
window.show()
sys.exit(app.exec_())