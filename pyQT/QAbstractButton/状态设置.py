from PyQt5.Qt import *
import sys

app = QApplication(sys.argv)
window=QWidget()
window.setWindowTitle('')
window.resize(500,500)
#***********状态设置***********开始
btn=QPushButton(window)
btn.setText('白日依山尽')
btn.move(100,100)

radio_button=QRadioButton(window)
radio_button.setText('黄河入海流')
radio_button.move(100,200)

checkbox=QCheckBox(window)
checkbox.setText('欲穷千里目')
checkbox.move(100,300)

btn.setStyleSheet('QPushButton:pressed {background-color:red;}')#修改按钮选中后的样式
#按下状态
# btn.setDown(True)
# radio_button.setDown(True)
# checkbox.setDown(True)

#控件是否可被选中
# print(btn.isCheckable())
# print(radio_button.isCheckable())
# print(checkbox.isCheckable())

#设置控件是否可以被选中
btn.setCheckable(True)
print(btn.isCheckable())

#获取当前控件的选中状态
print(btn.isChecked())
print(radio_button.isChecked())
print(checkbox.isChecked())

#设置控件的选中与否(状态)
btn.setChecked(False)
radio_button.setChecked(True)
checkbox.setChecked(True)

#反转选中状态
radio_button.toggle()
btn1=QPushButton(window)
btn1.setText('切换状态')
btn1.move(100,400)
btn1.pressed.connect(lambda :radio_button.setChecked(not radio_button.isChecked()))

#设置置灰手动不可使用状态,但可以使用代码控制状态
btn.setEnabled(False)
radio_button.setEnabled(False)
checkbox.setEnabled(False)
#***********状态设置***********结束


window.show()
sys.exit(app.exec_())