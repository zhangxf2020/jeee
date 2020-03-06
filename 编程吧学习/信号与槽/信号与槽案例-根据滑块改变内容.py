from PyQt5.Qt import *


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('信号与槽案例')
        self.resize(250,250)
        self.initUI()
    def initUI(self):
        lcd=QLCDNumber(self)
        lcd.resize(100,30)
        lcd.move(80,50)
        dial=QDial(self)
        dial.move(70,100)
        dial.valueChanged.connect(lcd.display)
        sd=QSlider(self)
        sd.move(60,200)
        sd.resize(150,20)
        sd.setOrientation(Qt.Horizontal)
        sd.setTickPosition(QSlider.TicksBelow)
        sd.valueChanged.connect(lcd.display)


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    window=Window()
    window.show()

    sys.exit(app.exec_())