from PyQt5.Qt import *


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('网格布局')
        self.resize(250,250)
        self.initUI()
    def initUI(self):
        names=['Cls', 'Bc', '', 'Close',
                 '7', '8', '9', '/',
                 '4', '5', '6', '*',
                 '1', '2', '3', '-',
                 '0', '.', '=', '+']
        grid=QGridLayout()
        self.lcd = QLCDNumber()
        grid.addWidget(self.lcd, 0, 0, 3, 0)
        grid.setSpacing(5)
        self.setLayout(grid)
        positions=[(x,y) for x in range(4,9) for y in range(0,4)]
        print(positions)
        for name,position in zip(names,positions):
            if name == '':
                continue
            button = QPushButton(name)
            grid.addWidget(button, *position)
            button.clicked.connect(self.subscreen)
    def subscreen(self):
        sender=self.sender().text()
        str=['/','*','-','+','=','.']
        if sender in str:
            self.lcd.display('A')
        else:
            self.lcd.display(sender)


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    window=Window()
    window.show()

    sys.exit(app.exec_())