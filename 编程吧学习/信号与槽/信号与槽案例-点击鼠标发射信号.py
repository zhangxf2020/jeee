from PyQt5.Qt import *

class singl(QObject):
    mysingl=pyqtSignal()

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('点击鼠标发射信号')
        self.resize(250,250)
        self.initUI()
    def initUI(self):
        self.singl=singl()
        self.singl.mysingl.connect(self.mouseevent)
    def mouseevent(self):
        QMessageBox.about(self, '提示', '点击鼠标了吧')

    def mousePressEvent(self, QMouseEvent):
        self.singl.mysingl.emit()

pyqtSignal

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    window=Window()
    window.show()

    sys.exit(app.exec_())