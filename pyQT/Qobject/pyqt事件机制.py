import sys
from PyQt5.Qt import *

class App(QApplication):
    def notify(self,recevier,evt):
        if recevier.inherits('QPushButton')and evt.type()==QEvent.MouseButtonPress:
            print(recevier,evt)
        return super().notify(recevier,evt)



app=App(sys.argv)
window=QWidget()
def cao():
    print('按钮被点击了')
btn=QPushButton(window)
btn.setText('点击我')
btn.move(300,300)
btn.clicked.connect(cao)

window.show()
sys.exit(app.exec_())