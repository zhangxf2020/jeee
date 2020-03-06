from PyQt5.Qt import *


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('鼠标拖拽窗口移动')
        self.resize(500,500)
        self.move_flg=False
        self.initUI()
    def initUI(self):
        pass
    def mousePressEvent(self, evt):
        if evt.button()==Qt.LeftButton:
            self.move_flg=True#只有标记为True时才触发点击操作
            self.mou_x=evt.globalX()
            self.mou_y=evt.globalY()

            self.chuangkou_x=self.x()
            self.chuangkou_y=self.y()
            # print(self.chuangkou_zuobiao)
            # print(self.mou_zuobiao)
    def mouseMoveEvent(self, QMouseEvent) -> None:
        if self.move_flg:
            self.yidong_x=QMouseEvent.globalX()
            self.yidong_y=QMouseEvent.globalY()

            self.xiangliang_x=self.yidong_x-self.mou_x
            self.xiangliang_y=self.yidong_y-self.mou_y
            self.move(self.chuangkou_x+self.xiangliang_x,self.chuangkou_y+self.xiangliang_y)

    def mouseReleaseEvent(self,QMouseEvent) -> None:
        self.move_flg = False
        print('鼠标松开')

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    window=Window()
    window.show()
    window.setMouseTracking(True)#跟踪鼠标
    sys.exit(app.exec_())