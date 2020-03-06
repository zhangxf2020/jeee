
from PyQt5.Qt import  *

import sys

class Window(QWidget):
    def mousePressEvent(self, QMouseEvent) -> None:
        print('主窗口被点击')

class MYwindow(QWidget):
    def mousePressEvent(self, QMouseEvent) -> None:
        print('副窗口被点击')
class rrr(QLabel):
    # def mousePressEvent(self, QMouseEvent) -> None:
    #     print('标签被点击')
    pass
app = QApplication(sys.argv)
window=Window()
window.setWindowTitle('事件转发')
window.resize(500,500)
mywindow=MYwindow(window)
mywindow.resize(200,200)
mywindow.setAttribute(Qt.WA_StyledBackground,True)
mywindow.setStyleSheet('background-color:red;')
label=rrr(mywindow)
label.setText('白日依山尽黄河入海流')
mywindow.setStyleSheet('background-color:yellow;')
label.move(50,100)



window.show()
sys.exit(app.exec_())