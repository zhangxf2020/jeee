from PyQt5.Qt import *
import sys

app = QApplication(sys.argv)
window=QWidget()
lab=QLabel(window)
lab.setText('红色的')
lab.setStyleSheet('background:green;')
lab.move(0,200)

def cao():
    str=lab.text()
    lab.setText(str+'红色的')
    print(str+'红色的')

btn=QPushButton(window)
btn.setText('点击我')
btn.move(100,100)
btn.clicked.connect(cao)

window.show()
sys.exit(app.exec_())
