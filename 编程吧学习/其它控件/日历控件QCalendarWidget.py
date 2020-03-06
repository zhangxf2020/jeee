from PyQt5.Qt import *
import sys

class Window(QWidget):
    def __init__(self):
        super(Window,self).__init__()
        self.setWindowTitle('Calendar Widget')
        '''调用日历函数/常规选项窗口'''
        self.createPreviewGroupBox()
        self.createGeneralOptionGroupBox()
        self.createDatesGroupBox()
        self.createTextFormatsGroupBox()

        self.layout = QGridLayout()
        '''添加日历窗口:'''
        self.layout.addWidget(self.previewGroupBox,0,0)
        '''添加常规选项窗口'''
        self.layout.addWidget(self.generalOptionGroupBox,0,1)

        self.layout.addWidget(self.datesGroupBox,1,0)

        self.layout.addWidget(self.textFormatsGroupBox,1,1)

        self.layout.setSizeConstraint(QLayout.SetFixedSize)

        self.setLayout(self.layout)
        self.previewLayout.setRowMinimumHeight(0, self.calendar.sizeHint().height())
        self.previewLayout.setColumnMinimumWidth(0, self.calendar.sizeHint().width())


    '''日历页面'''
    def createPreviewGroupBox(self):
        self.previewGroupBox = QGroupBox('PreView')

        self.calendar = QCalendarWidget()
        '''设置日历的最大,最小可选择年月日'''
        self.calendar.setMinimumDate(QDate(1900,1,1))
        self.calendar.setMaximumDate(QDate(2022,1,1))
        '''是否显示网格线(日期之间的方块线)'''
        self.calendar.setGridVisible(True)
        '''更改页面(切换月份)发射信号'''
        self.calendar.currentPageChanged.connect(self.reformatCalendarPage)

        self.previewLayout =QGridLayout()
        self.previewLayout.addWidget(self.calendar,0,0,Qt.AlignCenter)

        self.previewGroupBox.setLayout(self.previewLayout)

    '''常规选项'''
    def createGeneralOptionGroupBox(self):
        self.generalOptionGroupBox = QGroupBox('General Options')

        '''创建下拉列表,装载多语言格式'''
        self.localeCombo = QComboBox()
        curLocaleIndex = -1
        index = 0
        countries = []
        for i in range(QLocale.C, QLocale.LastLanguage+1):
            lang = QLocale(i)
            countries.append(lang.country())
            for j in range(len(countries)):
                country = countries[j]
                label = QLocale.languageToString(lang.language())
                label += '/'
                label += QLocale.countryToString(country)
                locale = QLocale(i, country)
                if self.locale().language() == lang and self.locale().country() == country:
                    curLocaleIndex = index
                self.localeCombo.addItem(label, locale)
                index += 1
        if curLocaleIndex != -1:
            self.localeCombo.setCurrentIndex(curLocaleIndex)
        localeLabel = QLabel('&Locale')
        localeLabel.setBuddy(self.localeCombo)

        '''设置星期下拉菜单,映射其星期枚举'''
        self.firstDayCombo = QComboBox()
        self.firstDayCombo.addItem('Sunday', Qt.Sunday)
        self.firstDayCombo.addItem('Monday', Qt.Monday)
        self.firstDayCombo.addItem('Tuesday', Qt.Tuesday)
        self.firstDayCombo.addItem('Wendnesday', Qt.Wednesday)
        self.firstDayCombo.addItem('Thursday', Qt.Thursday)
        self.firstDayCombo.addItem('Friday', Qt.Friday)
        self.firstDayCombo.addItem('Saturday', Qt.Saturday)

        firstDayLabel = QLabel('Wee&k starts on:')
        firstDayLabel.setBuddy(self.firstDayCombo)

        self.selectionModeCombo = QComboBox()
        self.selectionModeCombo.addItem('Single selection', QCalendarWidget.SingleSelection)
        self.selectionModeCombo.addItem('None', QCalendarWidget.NoSelection)

        selectionModeLabel = QLabel('&Selection mode:')
        selectionModeLabel.setBuddy(self.selectionModeCombo)

        '''设置网格单选框,设置是否勾选(与日历是否开启网格显示一致)'''
        gridCheckBox = QCheckBox('&Grid')
        gridCheckBox.setChecked(self.calendar.isGridVisible())
        '''设置表头单选框,设置是否勾选(与日历是否开启表头显示一致)'''
        navigationCheckBox = QCheckBox('&Navigation bar')
        navigationCheckBox.setChecked(True)

        '''设置周表头显示格式,显示单个单词/断名字/长名字/无表头'''
        self.horizontalHeaderCombo = QComboBox()
        self.horizontalHeaderCombo.addItem('Single letter day names', QCalendarWidget.SingleLetterDayNames)
        self.horizontalHeaderCombo.addItem('Short day names', QCalendarWidget.ShortDayNames)
        self.horizontalHeaderCombo.addItem('Long day names', QCalendarWidget.LongDayNames)
        self.horizontalHeaderCombo.addItem('None', QCalendarWidget.NoHorizontalHeader)
        self.horizontalHeaderCombo.setCurrentIndex(1)

        horizontalHeaderLabel = QLabel('&Horizontal header:')
        horizontalHeaderLabel.setBuddy(self.horizontalHeaderCombo)

        '''设置是否显示每月周数'''
        self.verticalHeaderCombo = QComboBox()
        self.verticalHeaderCombo.addItem('ISO week numbers', QCalendarWidget.ISOWeekNumbers)
        self.verticalHeaderCombo.addItem('None', QCalendarWidget.NoVerticalHeader)

        verticalHeaderLabel = QLabel('&Vertical header:')
        verticalHeaderLabel.setBuddy(self.verticalHeaderCombo)

        '''当多语言下拉列表改变时,调用函数'''
        self.localeCombo.currentIndexChanged.connect(self.localeChanged)
        self.firstDayCombo.currentIndexChanged.connect(self.firstDayChanged)
        self.selectionModeCombo.currentIndexChanged.connect(self.selectionModeChanged)
        '''当网格勾选框有操作时,调用日历控件的打开/关闭网格显示'''
        gridCheckBox.toggled.connect(self.calendar.setGridVisible)
        '''当表头勾选框有操作时,调用日历控件的打开/关闭表头显示'''
        navigationCheckBox.toggled.connect(self.calendar.setNavigationBarVisible)
        self.horizontalHeaderCombo.currentIndexChanged.connect(self.horizontalHeaderChanged)
        self.verticalHeaderCombo.currentIndexChanged.connect(self.veritcalHeaderChanged)

        checkBoxLayout = QHBoxLayout()
        checkBoxLayout.addWidget(gridCheckBox)
        checkBoxLayout.addStretch()
        checkBoxLayout.addWidget(navigationCheckBox)

        outerLayout = QGridLayout()
        outerLayout.addWidget(localeLabel, 0, 0)
        outerLayout.addWidget(self.localeCombo, 0, 1)
        outerLayout.addWidget(firstDayLabel, 1, 0)
        outerLayout.addWidget(self.firstDayCombo, 1, 1)
        outerLayout.addWidget(selectionModeLabel, 2, 0)
        outerLayout.addWidget(self.selectionModeCombo, 2, 1)
        outerLayout.addLayout(checkBoxLayout, 3, 0, 1, 2)
        outerLayout.addWidget(horizontalHeaderLabel, 4, 0)
        outerLayout.addWidget(self.horizontalHeaderCombo, 4, 1)
        outerLayout.addWidget(verticalHeaderLabel, 5, 0)
        outerLayout.addWidget(self.verticalHeaderCombo, 5, 1)
        self.generalOptionGroupBox.setLayout(outerLayout)

        '''执行一次更改第一天显示的函数,下拉表当前选项序列号为参数'''
        self.firstDayChanged(self.firstDayCombo.currentIndex())
        self.selectionModeChanged(self.selectionModeCombo.currentIndex())
        self.horizontalHeaderChanged(self.horizontalHeaderCombo.currentIndex())
        self.veritcalHeaderChanged(self.verticalHeaderCombo.currentIndex())
    '''修改日历显示格式'''

    def createDatesGroupBox(self):
        self.datesGroupBox = QGroupBox('Dates')

        '''设置日期输入框,设置其显示格式,最大最小值保持与日历一致,当前显示为日历最小日期'''
        self.minimumDateEdit = QDateEdit()
        self.minimumDateEdit.setDisplayFormat('MMM d yyyy')
        self.minimumDateEdit.setDateRange(self.calendar.minimumDate(), self.calendar.maximumDate())
        self.minimumDateEdit.setDate(self.calendar.minimumDate())

        minimumDateLabel = QLabel('&Minimum Date:')
        minimumDateLabel.setBuddy(self.minimumDateEdit)

        '''设置日期输入框,设置其格式,设置当前显示为日历选择一致'''
        self.currentDateEdit = QDateEdit()
        self.currentDateEdit.setDisplayFormat('MMM d yyyy')
        self.currentDateEdit.setDate(self.calendar.selectedDate())
        self.currentDateEdit.setDateRange(self.calendar.minimumDate(), self.calendar.maximumDate())

        currentDateLabel = QLabel('Current Date:')
        currentDateLabel.setBuddy(self.currentDateEdit)

        '''设置日期输入框,设置其显示格式,最大最小值保持与日历一致,当前显示为日历最大日期'''
        self.maximumDateEdit = QDateEdit()
        self.maximumDateEdit.setDisplayFormat('MMM d yyyy')
        self.maximumDateEdit.setDateRange(self.calendar.minimumDate(), self.calendar.maximumDate())
        self.maximumDateEdit.setDate(self.calendar.maximumDate())

        maximumDateLabel = QLabel('Ma&ximum Date:')
        maximumDateLabel.setBuddy(self.maximumDateEdit)

        '''日期输入框改变之后发射信号,执行日历日期设置函数(参数为输入框改变时传出的Qdata)'''
        self.currentDateEdit.dateChanged.connect(self.calendar.setSelectedDate)
        '''选择日历日期后发射信号'''
        self.calendar.selectionChanged.connect(self.selectDateChanged)
        self.minimumDateEdit.dateChanged.connect(self.minimumDateChanged)
        self.maximumDateEdit.dateChanged.connect(self.maximumDateChanged)

        dateBoxLayout = QGridLayout()
        dateBoxLayout.addWidget(currentDateLabel, 1, 0)
        dateBoxLayout.addWidget(self.currentDateEdit, 1, 1)
        dateBoxLayout.addWidget(minimumDateLabel, 0, 0)
        dateBoxLayout.addWidget(self.minimumDateEdit, 0, 1)
        dateBoxLayout.addWidget(maximumDateLabel, 2, 0)
        dateBoxLayout.addWidget(self.maximumDateEdit, 2, 1)
        dateBoxLayout.setRowStretch(3, 1)

        self.datesGroupBox.setLayout(dateBoxLayout)

    def createTextFormatsGroupBox(self):
        self.textFormatsGroupBox = QGroupBox('Text Formats')

        self.weekdayColorCombo = self.createColorComboBox()
        self.weekdayColorCombo.setCurrentIndex(self.weekdayColorCombo.findText('Black'))

        weekdayColorLabel = QLabel('&Weekday color:')
        weekdayColorLabel.setBuddy(self.weekdayColorCombo)

        self.weekendColorCombo = self.createColorComboBox()
        self.weekendColorCombo.setCurrentIndex(self.weekdayColorCombo.findText('Red'))

        weekendColorLabel = QLabel('Week&end color:')
        weekendColorLabel.setBuddy(self.weekendColorCombo)

        self.headerTextFormatCombo = QComboBox()
        self.headerTextFormatCombo.addItem('Bold')
        self.headerTextFormatCombo.addItem('Italic')
        self.headerTextFormatCombo.addItem('Plain')

        headerTextFormatLabel = QLabel('&Header text:')
        headerTextFormatLabel.setBuddy(self.headerTextFormatCombo)

        self.firstFridayCheckBox = QCheckBox('&First Friday in blue')

        self.mayFirstCheckBox = QCheckBox('May &1 in red')

        self.weekdayColorCombo.currentIndexChanged.connect(self.weekdayFormatChanged)
        self.weekendColorCombo.currentIndexChanged.connect(self.reformatCalendarPage)
        self.weekendColorCombo.currentIndexChanged.connect(self.weekendFormatChanged)
        self.weekendColorCombo.currentIndexChanged.connect(self.reformatCalendarPage)
        self.headerTextFormatCombo.currentIndexChanged.connect(self.reformatHeaders)
        self.firstFridayCheckBox.toggled.connect(self.reformatCalendarPage)
        self.mayFirstCheckBox.toggled.connect(self.reformatCalendarPage)

        checkBoxLayout = QHBoxLayout()
        checkBoxLayout.addWidget(self.firstFridayCheckBox)
        checkBoxLayout.addStretch()
        checkBoxLayout.addWidget(self.mayFirstCheckBox)

        outerLayout = QGridLayout()
        outerLayout.addWidget(weekdayColorLabel, 0, 0)
        outerLayout.addWidget(self.weekdayColorCombo, 0, 1)
        outerLayout.addWidget(weekendColorLabel, 1, 0)
        outerLayout.addWidget(self.weekendColorCombo, 1, 1)
        outerLayout.addWidget(headerTextFormatLabel, 2, 0)
        outerLayout.addWidget(self.headerTextFormatCombo, 2, 1)
        outerLayout.addLayout(checkBoxLayout, 3, 0, 1, 2)
        self.textFormatsGroupBox.setLayout(outerLayout)

        self.weekdayFormatChanged()
        self.weekendFormatChanged()
        self.reformatHeaders()
        self.reformatCalendarPage()

    def localeChanged(self,index):
        newLocale = QLocale(self.localeCombo.itemData(index))
        self.calendar.setLocale(newLocale)
        newLocaleFirstDayIndex = self.firstDayCombo.findData(newLocale.firstDayOfWeek())
        self.firstDayCombo.setCurrentIndex(newLocaleFirstDayIndex)
    def firstDayChanged(self,index):
        '''将当前日历的第一列修改为下拉列表所选择索引对应的映射(星期的枚举)'''
        self.calendar.setFirstDayOfWeek(self.firstDayCombo.itemData(index))
    def selectionModeChanged(self,index):
        self.calendar.setSelectionMode(self.selectionModeCombo.itemData(index))
    def horizontalHeaderChanged(self,index):
        self.calendar.setHorizontalHeaderFormat(self.horizontalHeaderCombo.itemData(index))
    def veritcalHeaderChanged(self,index):
        self.calendar.setVerticalHeaderFormat(self.verticalHeaderCombo.itemData(index))
    def selectDateChanged(self):
        '''设置当前日期框日期与所选择的日期一致'''
        self.currentDateEdit.setDate(self.calendar.selectedDate())
    def minimumDateChanged(self,date):
        '''设置日历日期最小值为输入框中选择的值,同时把输入框日期至为日历最小日期'''
        self.calendar.setMinimumDate(date)
        self.minimumDateEdit.setDate(self.calendar.minimumDate())
    def maximumDateChanged(self,date):
        '''设置日历日期最大值为输入框中选择的值,同时把输入框日期至为日历最大日期'''
        self.calendar.setMaximumDate(date)
        self.minimumDateEdit.setDate(self.calendar.minimumDate())
    def weekdayFormatChanged(self):
        txFormat = QTextCharFormat()
        txFormat.setForeground(self.weekdayColorCombo.itemData(self.weekdayColorCombo.currentIndex()))
        self.calendar.setWeekdayTextFormat(Qt.Monday, txFormat)
        self.calendar.setWeekdayTextFormat(Qt.Tuesday, txFormat)
        self.calendar.setWeekdayTextFormat(Qt.Wednesday, txFormat)
        self.calendar.setWeekdayTextFormat(Qt.Thursday, txFormat)
        self.calendar.setWeekdayTextFormat(Qt.Friday, txFormat)
    def weekendFormatChanged(self):
        txFormat = QTextCharFormat()
        txFormat.setForeground(self.weekendColorCombo.itemData(self.weekendColorCombo.currentIndex()))
        self.calendar.setWeekdayTextFormat(Qt.Saturday, txFormat)
        self.calendar.setWeekdayTextFormat(Qt.Sunday, txFormat)

    def reformatHeaders(self):
        '''设置表头格式'''
        text = self.headerTextFormatCombo.currentText()
        txFormat = QTextCharFormat()

        if text == 'Bold':
            txFormat.setFontWeight(QFont.Bold)
        elif text == 'Italic':
            txFormat.setFontItalic(True)
        elif text == 'Plain':
            txFormat.setForeground(QColor(Qt.green))
        self.calendar.setHeaderTextFormat(txFormat)


    def reformatCalendarPage(self):
        mayFirstFormat = QTextCharFormat()
        mayFirst = QDate(self.calendar.yearShown(), 5, 1)

        firstFridayFormat = QTextCharFormat()
        firstFriday = QDate(self.calendar.yearShown(), self.calendar.monthShown(), 1)
        while firstFriday.dayOfWeek() != Qt.Friday:
            firstFriday = firstFriday.addDays(1)

        if self.firstFridayCheckBox.isChecked():
            firstFridayFormat.setForeground(Qt.blue)
        else:
            dayOfWeek = firstFriday.dayOfWeek()
            firstFridayFormat.setForeground(self.calendar.weekdayTextFormat(dayOfWeek).foreground())

        self.calendar.setDateTextFormat(firstFriday, firstFridayFormat)

        if self.mayFirstCheckBox.isChecked():
            mayFirstFormat.setForeground(Qt.red)
        elif not self.firstFridayCheckBox.isChecked():
            dayOfWeek = mayFirst.dayOfWeek()
            self.calendar.setDateTextFormat(mayFirst, self.calendar.weekdayTextFormat(dayOfWeek))

        self.calendar.setDateTextFormat(mayFirst, mayFirstFormat)


    def createColorComboBox(self):
        comboBox = QComboBox()
        comboBox.addItem('Red', QColor(Qt.red))
        comboBox.addItem('Blue', QColor(Qt.blue))
        comboBox.addItem('Black', QColor(Qt.black))
        comboBox.addItem('Magenta', QColor(Qt.magenta))
        return comboBox






if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec_())

