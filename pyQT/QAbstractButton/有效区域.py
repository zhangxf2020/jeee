from PyQt5.Qt import *
import sys,math

class Btn(QPushButton):
    def hitButton(self, Point) -> bool:
        # if Point.x()>=self.width()/2 and Point.y()>=self.height()/2:#有效区域为按钮的右下角
        #     return True
        # else:
        #     return False
        yuanxin_x=self.width()/2
        yuanxin_y=self.height()/2
        banjing=self.height()/2
        juli= math.fabs(math.sqrt(math.pow(Point.x()-yuanxin_x,2)+math.pow(Point.y()-yuanxin_y,2)))
        if juli>banjing:
            return False
        else:
            return True
    def paintEvent(self,QPaintEvent) -> None:
        super().paintEvent(QPaintEvent)#继承父类的绘制方法
        painter=QPainter(self)#创建一个画家,给其一个画布(self)
        painter.setPen(QPen(QColor(100,250,111),4))#给画家一个画笔(画笔对象(这只画笔颜色和大小)
        painter.drawEllipse(self.rect())#让画家执行画椭圆方法(椭圆的半径)

app = QApplication(sys.argv)
window=QWidget()
window.setWindowTitle('有效区域设置')
window.resize(500,500)
btn=Btn(window)
btn.setText('点击按钮')
btn.resize(200,200)
btn.move(100,100)
btn.setCheckable(True)#设置按钮可被选中
# btn.clicked.connect(lambda :print('我被点击了'))#clicked,鼠标点击松开后触发,并且移开控件之后不会触发
# btn.pressed.connect(lambda :print('我被按下了'))#pressed,鼠标按下后触发
# btn.released.connect(lambda :print('我被释放了'))#released,鼠标松开后触发,移开控件之后也会触发
btn.toggled.connect(lambda value:print('按钮的状态被切换了',value))#toggled,按钮被选中/取消选中时触发,前提是控件必须可被选中

window.show()
sys.exit(app.exec_())
