from PyQt5.Qt import *
import sys

# class MyButton(QPushButton):
#     def mousePressEvent(self, QMouseEvent) -> None:
#         self.num=self.text()
#         self.setText(str(int(self.num)+1))
app = QApplication(sys.argv)
window=QWidget()
window.setWindowTitle('点击变化按钮文字')
window.resize(500,500)
btn=QPushButton(window)
btn.move(200,200)
# btn.setText('1')

#***********文本操作***********开始
# btn.clicked.connect(lambda :btn.setText(str(int(btn.text())+1)))
#***********文本操作***********结束


#***********图标操作***********开始
icon=QIcon('xxx.png')
btn.setIcon(icon)
size=QSize(50,50)
btn.setIconSize(size)

print(btn.icon())
print(btn.iconSize())
#***********图标操作***********结束

#***********快捷键***********开始
btn.setText('1')#如果有字母则直接可以使用字母作为快捷键
btn.pressed.connect(lambda :btn.setText(str(int(btn.text())+1)))

btn.setShortcut('Alt+a')#否则可以手动设置快捷键

#***********快捷键***********结束

#***********自动重复***********开始
btn.setAutoRepeat(True)#自动点击开启
print(btn.autoRepeat())
btn.setAutoRepeatDelay(2000)#延迟多少时间后触发
btn.setAutoRepeatInterval(200)#触发频率设置

#***********自动重复***********结束
window.show()
sys.exit(app.exec_())