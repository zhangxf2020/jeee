from PyQt5.Qt import *
import sys

app = QApplication(sys.argv)
window=QWidget()
window.setWindowTitle('模拟点击操作')
window.resize(500,500)
btn=QPushButton(window)
btn.setText('我是按钮')
btn.move(200,200)
btn.pressed.connect(lambda :print('"我是按钮"被点击了'))

# btn.click()
# btn.animateClick(1000)

btn2=QPushButton(window)
btn2.move(100,100)
btn2.setText('代码控制按钮的点击')

def cao():
    btn.animateClick(2000)#动画点击(可以看到点击效果)
btn2.pressed.connect(cao)
window.show()
sys.exit(app.exec_())