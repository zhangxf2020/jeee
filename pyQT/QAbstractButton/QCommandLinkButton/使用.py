from PyQt5.Qt import *
import sys

app = QApplication(sys.argv)
window=QWidget()
window.setWindowTitle('QCommandLinkButton')
window.resize(500,500)
btn=QCommandLinkButton('标题','描述',window)
btn.setText('主技能')#修改标题
btn.setDescription('副技能')#修改描述
btn.setIcon(QIcon('xxx.png'))
window.show()
sys.exit(app.exec_())