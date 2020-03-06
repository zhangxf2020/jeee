from PyQt5.Qt import *

class HolyShitBox(QSpinBox):
    def valueFromText(self, p_str):
        regExp = QRegExp("(\\d+)(\\s*[xx]\\s*\\d+)?")
        if regExp.exactMatch(p_str):
            return int(regExp.cap(1))
        else:
            return 0
    def textFromValue(self, num):
        return "{0} x {1}".format(num,num)
class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('QSpinBox使用')
        self.resize(250,250)
        self.initUI()
    def initUI(self):
        mylayout = QGridLayout(self)
        self.sp1 = QSpinBox(self)
        self.sp2 = QSpinBox(self)
        self.sp3 = HolyShitBox(self)

        self.s1 = QSlider(Qt.Horizontal,self)
        '''设置最小最大值'''
        self.sp1.setRange(-20,200)
        '''设置步长,如果小于0则什么都不做'''
        self.sp1.setSingleStep(10)
        '''设置数值是否可循环调整'''
        self.sp1.setWrapping(True)
        '''设置当前数值'''
        self.sp1.setValue(-10)

        '''设置值范围/步长/当前值/前缀显示/后缀显示/达到最小值显示提示文字'''
        self.sp2.setRange(0,100)
        self.sp2.setSingleStep(10)
        self.sp2.setValue(10)
        self.sp2.setPrefix('已充电..')
        self.sp2.setSuffix(' %,即将达到最大!')
        self.sp2.setSpecialValueText('电量已耗尽!!!')

        self.sp3.setRange(10,50)
        self.sp3.setValue(10)
        self.sp3.setWrapping(True)

        self.s1.setRange(-10,200)
        self.s1.setValue(-10)
        # self.s1.setSingleStep(10)

        lb1 = QLabel('普通微调框',self)
        lb2 = QLabel('加强微调框',self)
        lb3 = QLabel('超神微调框',self)
        mylayout.addWidget(lb1,0,0)
        mylayout.addWidget(lb2,1,0)
        mylayout.addWidget(lb3,2,0)
        mylayout.addWidget(self.sp1,0,1)
        mylayout.addWidget(self.sp2,1,1)
        mylayout.addWidget(self.sp3,2,1)
        mylayout.addWidget(self.s1,3,1)

        self.sp1.valueChanged[int].connect(self.slider1_changevalue)
        self.s1.valueChanged[int].connect(self.spinbox_changevalue)
        self.sp2.valueChanged[int].connect(self.slider2_changevalue)
    def slider1_changevalue(self,value):
        self.s1.setValue(value)

    def spinbox_changevalue(self,value):
        self.sp1.setValue(value)

    def slider2_changevalue(self, value):
        if value == self.sp2.maximum():
            QMessageBox.information(self,'提示','再充就爆炸啦!!!')
            self.sp2.setSuffix(' %,已达最大')
        elif self.sp2.minimum() <value:
            self.sp2.setSuffix(' %,即将达到最大!')


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    window=Window()
    window.show()

    sys.exit(app.exec_())