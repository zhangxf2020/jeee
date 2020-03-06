from PyQt5.Qt import *
import datetime


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('QLCDNumber液晶显示屏')
        self.resize(500,120)
        self.initUI()
    def initUI(self):

        self.d1 = datetime.datetime.strptime('2020-1-24 00:00:00','%Y-%m-%d %H:%M:%S')

        self.lcd = QLCDNumber()
        self.lcd.setDigitCount(12)
        self.lcd.setMode(QLCDNumber.Dec)
        self.lcd.setSegmentStyle(QLCDNumber.Flat)  # Mac系统需要加上，否则下面的color不生效。
        self.lcd.setStyleSheet("border: 2px solid black; color: red; background: silver")

        self.lb = QLabel('距离除夕还剩余:')


        self.gridlayout = QGridLayout(self)
        self.gridlayout.addWidget(self.lb, 0, 0)
        self.gridlayout.addWidget(self.lcd,1,0)

        timer = QTimer(self)
        timer.setInterval(1000)
        timer.timeout.connect(self.refresh)
        timer.start()


    def refresh(self):
        time = datetime.datetime.now()
        timeing = self.d1 - time
        hour = int(timeing.seconds /60/60)
        minute = int((timeing.seconds - hour*60*60)/60)
        second = timeing.seconds - hour*60*60 - minute*60
        # print(timeing.days+' '+hour+' '+minute+' '+second)
        print('{}天{}小时{}分钟{}秒'.format(timeing.days,hour,minute,second))
        str1 = str(timeing.days)+":"+str(hour)+":"+str(minute)+":"+str(second)
        self.lcd.display(str1)





if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    window=Window()
    window.show()

    sys.exit(app.exec_())