from PyQt5.Qt import *
import sys

class My_Window(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(500,500)
        self.setWindowTitle('动画组学习')
        self.initui()
    def initui(self):
        red_btn = QPushButton(self)
        green_btn = QPushButton(self)
        red_btn.resize(50,50)
        green_btn.resize(50,50)
        green_btn.move(100,100)
        red_btn.setStyleSheet('background-color:red')
        green_btn.setStyleSheet('background-color:green')

        animation = QPropertyAnimation(green_btn,b'pos',self)
        animation.setKeyValueAt(0.25,QPoint(350,100))
        animation.setKeyValueAt(0.5,QPoint(350,350))
        animation.setKeyValueAt(0.75,QPoint(100,350))
        animation.setKeyValueAt(1,QPoint(100,100))
        animation.setDuration(5000)
        animation.start()

        animation1 = QPropertyAnimation(red_btn, b'pos', self)
        animation1.setKeyValueAt(0.25, QPoint(0, 450))
        animation1.setKeyValueAt(0.5, QPoint(450, 450))
        animation1.setKeyValueAt(0.75, QPoint(450, 0))
        animation1.setKeyValueAt(1, QPoint(0, 0))
        animation1.setDuration(5000)
        animation1.start()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = My_Window()
    win.show()
    sys.exit(app.exec_())
