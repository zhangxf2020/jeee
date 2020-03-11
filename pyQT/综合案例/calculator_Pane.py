from PyQt5.Qt import *
import sys
from Resources.caculator import Ui_Form

class CaculatorPlne(QWidget,Ui_Form):
    def __init__(self,parent=None,*args,**kwargs):
        super(CaculatorPlne, self).__init__(parent,*args,**kwargs)
        self.setAttribute(Qt.WA_StyledBackground,True)
        self.setupUi(self)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = CaculatorPlne()
    win.show()
    sys.exit(app.exec_())