from PyQt5.Qt import *


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('信号与槽')
        self.resize(250,250)
        self.initUI()
    def initUI(self):
        self.lb=QLabel('方向',self)
        self.lb.move(100,100)
    def keyPressEvent(self, QKeyEvent):
        print(QKeyEvent)
        if QKeyEvent.key()==Qt.Key_Up:
            self.lb.setText('↑')
            return None
        if QKeyEvent.key()==Qt.Key_Down:
            self.lb.setText('↓')
            return None
        if QKeyEvent.key()==Qt.Key_Left:
            self.lb.setText('←')
            return None
        if QKeyEvent.key()==Qt.Key_Right:
            self.lb.setText('→')
            return None
if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    window=Window()
    window.show()

    sys.exit(app.exec_())