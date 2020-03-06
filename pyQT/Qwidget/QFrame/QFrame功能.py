from PyQt5.Qt import *


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('QFrame功能')
        self.resize(250,250)
        self.initUI()
    def initUI(self):
        frame=QFrame(self)
        frame.move(50,50)
        frame.resize(100,100)
        frame.setStyleSheet('background-color:red')

        # frame.setFrameShadow(QFrame.Raised)
        frame.setLineWidth(3)
        frame.setMidLineWidth(2)
        # frame.setFrameShape(QFrame.Box)
        frame.setFrameStyle(QFrame.Raised|QFrame.StyledPanel)


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    window=Window()
    window.show()

    sys.exit(app.exec_())