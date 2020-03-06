from PyQt5.Qt import *
import sys

app = QApplication(sys.argv)
window=QWidget()
window.setWindowTitle('排他性')
window.resize(500,500)
# for i in range(3):
#     btn=QPushButton(window)
#     btn.setText('btn'+str(i))
#     btn.move(50*i,50*i)
#
#     btn.setAutoExclusive(True)#设置排他性
#     btn.setCheckable(True)#设置按钮为可点击状态
for i in range(3):#单选默认具有排他性
    radiobtn=QRadioButton(window)
    radiobtn.setText('btn'+str(i))
    radiobtn.move(50*i,50*i)

    radiobtn.setAutoExclusive(False)#设置排他性


window.show()
sys.exit(app.exec_())