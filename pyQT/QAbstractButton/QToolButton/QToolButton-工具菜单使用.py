

from PyQt5.Qt import *


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('QToolButton(工具栏)使用')
        self.resize(500,500)
        self.initUI()
    def initUI(self):
        # self.风格()
        # self.设置箭头()
        # self.扁平化()
        # self.菜单样式()
        self.信号发射()
    def 风格(self):
        btn = QToolButton(self)
        btn.setIcon(QIcon('xxx.png'))
        btn.setText('返回')
        btn.setIconSize(QSize(20, 20))
        btn.setToolTip('这是一个返回按钮')
        # btn.setToolButtonStyle(Qt.ToolButtonTextOnly)#设置按钮的风格,只显示文本
        btn.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)  # 设置按钮风格,文本显示在图标下方
    def 设置箭头(self):
        btn=QToolButton(self)
        btn.move(100,100)
        NoArrow = ...  # type: 'Qt.ArrowType' #没有箭头
        UpArrow = ...  # type: 'Qt.ArrowType'#向上箭头
        DownArrow = ...  # type: 'Qt.ArrowType'#向下箭头
        LeftArrow = ...  # type: 'Qt.ArrowType'#向左箭头
        RightArrow = ...  # type: 'Qt.ArrowType'#向右箭头
        btn.setArrowType(Qt.LeftArrow)#设置箭头
    def 扁平化(self):
        btn=QToolButton(self)
        btn.move(100,200)
        btn.setText('扁平化按钮')
        btn.setAutoRaise(True)
    def 菜单样式(self):
        bt=QToolButton(self)
        bt.move(100,300)
        bt.setText('菜单样式')

        menu=QMenu(bt)

        action=QAction(QIcon('xxx.png'),'行为',bt)
        action.triggered.connect(lambda: print('菜单信号触发了'))
        sub_menu=QMenu(menu)
        sub_menu.setTitle('子菜单')
        sub_menu.setIcon(QIcon('xxx.png'))

        menu.addAction(action)
        menu.addSeparator()
        menu.addMenu(sub_menu)
        bt.clicked.connect(lambda: print('按钮信号触发了'))
        bt.setMenu(menu)
        # bt.setPopupMode(QToolButton.DelayedPopup)#默认状态,长按会弹出菜单
        bt.setPopupMode(QToolButton.MenuButtonPopup)#有一个专门的指示箭头
        # bt.setPopupMode(QToolButton.InstantPopup)#点击按钮就显示,不会触发按钮事件
    def 信号发射(self):
        tb=QToolButton(self)
        tb.move(100,100)
        tb.setText('信号发射')
        menu = QMenu(tb)

        action1 = QAction(QIcon('xxx.png'), '行为1', tb)
        action2 = QAction(QIcon('xxx.png'), '行为2', tb)
        action1.setData({'xiaohua':'maliya'})#设置行为的数据
        action2.setData([6,5,4])#设置行为的数据
        action1.triggered.connect(lambda: print('菜单信号触发了'))
        sub_menu = QMenu(menu)
        sub_menu.setTitle('子菜单')
        sub_menu.setIcon(QIcon('xxx.png'))

        menu.addAction(action1)
        menu.addAction(action2)
        menu.addSeparator()
        menu.addMenu(sub_menu)
        def data(action):
            print('行为信号触发了',action.data())#可取得行为的数据
        tb.triggered.connect(data)#使用triggered绑定方法,可与行为方法同时触发
        tb.setMenu(menu)

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    window=Window()
    window.show()

    sys.exit(app.exec_())