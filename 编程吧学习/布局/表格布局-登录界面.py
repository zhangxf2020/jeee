from PyQt5.Qt import *


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('表格布局')
        self.resize(250,250)
        self.initUI()
    def initUI(self):
        names=['账号:','密码:']
        frm = QFormLayout(self)

        for name in names:
            lb=QLabel(name,self)
            le=QLineEdit(self)
            frm.addRow(lb,le)

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    window=Window()
    window.show()

    sys.exit(app.exec_())