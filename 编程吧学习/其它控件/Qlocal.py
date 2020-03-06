from PyQt5.Qt import *




class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('1233')
        self.resize(250,250)
        self.initUI()
    def initUI(self):
        # s = QComboBox(self)
        # s.addItem('one',Qt.Monday)
        # s.addItem('two',Qt.Friday)
        # s.currentIndexChanged.connect(lambda :print(s.currentData()))
        # print(s.itemData(1))
        label1 = QLabel('姓名:',self)
        # s = QLineEdit(self)
        # label1.setBuddy(s)
        label1.move(100,50)
        cld = QCalendarWidget(self)
        cld.setLocale(QLocale(0))
        cld.setFirstDayOfWeek(Qt.Thursday)
        cld.setGridVisible(True)
        cld.setDateRange(QDate(2015,1,1),QDate(2030,1,1))



        cb1 = QCheckBox('是否开启网格')
        cb1.setChecked(cld.isGridVisible())
        cb1.toggled.connect(cld.setGridVisible)

        cb2 = QCheckBox('是否打开表头')
        cb2.setChecked(True)
        cb2.toggled.connect(cld.setNavigationBarVisible)

        dtat = QDateEdit()
        dtat.setDisplayFormat('yyyy年 MM月 d日')
        dtat.setDateRange(cld.minimumDate(),cld.maximumDate())
        dtat.setDate(cld.minimumDate())

        dtat1 = QDateEdit()
        dtat1.setDate(cld.selectedDate())
        dtat1.dateChanged.connect(cld.setSelectedDate)

        cb3 = QComboBox()
        cb3.addItem('red',QColor(Qt.red))
        cb3.addItem('green',QColor(Qt.green))
        cb3.addItem('yellow',QColor(Qt.yellow))
        cb3.addItem('black',QColor(Qt.black))
        cb3.setCurrentIndex(3)
        cb3.currentIndexChanged.connect(self.colorchange)
        # cb3.setCurrentIndex(1)


        grid = QGridLayout(self)
        # grid.addWidget(label1,0,0)
        # grid.addWidget(s,0,1)
        grid.addWidget(cld,0,0)
        grid.addWidget(cb1,2,0)
        grid.addWidget(cb2,2,1)
        grid.addWidget(dtat,0,1)
        grid.addWidget(dtat1,1,1)
        grid.addWidget(cb3,2,1)

        self.cb3=cb3
        self.cld = cld
    def colorchange(self):
        tcf = QTextCharFormat()
        tcf.setForeground(self.cb3.itemData(self.cb3.currentIndex()))
        self.cld.setWeekdayTextFormat(Qt.Monday, tcf)
        self.cld.setWeekdayTextFormat(Qt.Tuesday, tcf)
        self.cld.setWeekdayTextFormat(Qt.Wednesday, tcf)
        self.cld.setWeekdayTextFormat(Qt.Thursday, tcf)
        self.cld.setWeekdayTextFormat(Qt.Friday, tcf)

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    window=Window()
    window.show()

    sys.exit(app.exec_())