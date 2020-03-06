from PyQt5.Qt import *


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('永远')
        self.resize(500,500)
        # self.initUI()
        self.QObject对象的父子关系操作()
    def initUI(self):
        with open('Qobject.qss','r') as f:
            qApp.setStyleSheet(f.read())

        lable1=QLabel(self)
        lable1.setObjectName('notice')
        lable1.setText('白毛浮绿水!')

        lable2=QLabel(self)
        lable2.move(0,100)
        lable2.setText('红掌拨清波!')

        btn=QPushButton(self)
        btn.move(0,50)
        btn.setText('鹅鹅鹅')

    def QObject对象的父子关系操作(self):
        obj0=QObject()
        obj1=QObject()
        obj2=QObject()
        obj3=QObject()
        obj4=QObject()
        obj5=QObject()
        print('obj0',obj0)
        print('obj1',obj1)
        print('obj2',obj2)
        print('obj3',obj3)
        print('obj4',obj4)
        print('obj5',obj5)
        obj1.setParent(obj0)
        obj2.setParent(obj0)
        obj3.setParent(obj1)
        obj4.setParent(obj2)
        obj5.setParent(obj2)
        # print(obj4.parent())#直接父对象,最后设置的
        # print(obj0.children())#获取了所有的直接子对象
        print(obj0.findChild(QObject))#找到子对象即停止
if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    window=Window()
    window.show()

    sys.exit(app.exec_())

