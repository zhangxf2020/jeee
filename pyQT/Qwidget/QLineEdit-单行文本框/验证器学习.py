from PyQt5.Qt import *

class AgeValidator(QValidator):
    def validate(self, input_str, pos_int):
        try:
            if 18<= int(input_str) <= 160:
                return (QValidator.Acceptable,input_str,pos_int)
            elif 1<= int(input_str) <= 16:
                return (QValidator.Intermediate, input_str, pos_int)
            else:
                return (QValidator.Invalid, input_str, pos_int)
        except:
            if len(input_str) == 0:
                return (QValidator.Intermediate, input_str, pos_int)
            return (QValidator.Invalid, input_str, pos_int)
    def fixup(self, p_str):
        try:
            if int(p_str)<18:
                return '18'
            return '180'
        except:
            return '18'
class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('QLineEdit验证器的学习')
        self.resize(250,250)
        self.initUI()
    def initUI(self):
        self.validator()
    def validator(self):
        lb_a=QLineEdit(self)
        lb_a.move(50,50)
        lb_b=QLineEdit(self)
        lb_b.move(50,100)
        validator=AgeValidator()
        lb_a.setValidator(validator)


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    window=Window()
    window.show()

    sys.exit(app.exec_())