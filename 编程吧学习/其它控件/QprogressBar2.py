from PyQt5.Qt import *


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('实验2')
        self.resize(250,250)
        self.initUI()
    def initUI(self):
        lb1 = QLabel('     1   ',self)
        lb1.setAlignment(Qt.AlignCenter)


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    window=Window()
    window.show()

    sys.exit(app.exec_())