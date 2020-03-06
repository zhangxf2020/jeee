from PyQt5.Qt import *
import sys

class MYwindow(QWidget):

    def mouseMoveEvent(self, me) -> None:
        # QMouseEvent
        print('鼠标移动了!',me.localPos())
app = QApplication(sys.argv)
window=MYwindow()
window.setMouseTracking(True)
window.show()
sys.exit(app.exec_())
