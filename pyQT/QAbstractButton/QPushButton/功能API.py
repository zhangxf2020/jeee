from PyQt5.Qt import *
import sys

class Window(QWidget):
    def contextMenuEvent(self, evt) -> None:
        menu = QMenu(self)  # 2/设置一个菜单对象
        new_action = QAction(QIcon('xxx.png'), '新建', menu)  # 3创建菜单对象的行为
        open_action = QAction(QIcon('xxx.png'), '打开', menu)  # 3创建菜单对象的行为
        exit_action = QAction('退出', menu)  # 3创建菜单对象的行为
        # new_action.setText('新建')
        # new_action.setIcon(QIcon('xxx.png'))
        open_recent_menu = QMenu(menu)  # 7创建一个新的菜单作为子菜单
        open_recent_menu.setTitle('最近打开')
        open_recent_menu.setIcon(QIcon('xxx.png'))

        new_action.triggered.connect(lambda: print('新建文件'))  # 4/关联行为信号
        open_action.triggered.connect(lambda: print('打开文件'))  # 4/关联行为信号
        exit_action.triggered.connect(lambda: print('退出文件'))  # 4/关联行为信号

        file_action = QAction('pythonGUI编程')
        open_recent_menu.addAction(file_action)

        menu.addAction(new_action)  # 5/将行为绑定在菜单对象上
        menu.addAction(open_action)  # 5/将行为绑定在菜单对象上
        menu.addMenu(open_recent_menu)  # 8将子菜单绑定在菜单对象上
        menu.addSeparator()  # 6菜单中添加一个分割线
        menu.addAction(exit_action)  # 5/将行为绑定在菜单对象上

        menu.exec_(evt.globalPos())#将菜单展示在界面上(相对于全局)


app = QApplication(sys.argv)
window=Window()
window.setWindowTitle('按钮API')
window.resize(500,500)
btn=QPushButton(QIcon('xxx.png'),'我是按钮',window)
btn.move(100,100)
menu=QMenu()#2/设置一个菜单对象
new_action=QAction(QIcon('xxx.png'),'新建',menu)#3创建菜单对象的行为
open_action=QAction(QIcon('xxx.png'),'打开',menu)#3创建菜单对象的行为
exit_action=QAction('退出',menu)#3创建菜单对象的行为
# new_action.setText('新建')
# new_action.setIcon(QIcon('xxx.png'))
open_recent_menu=QMenu(menu)#7创建一个新的菜单作为子菜单
open_recent_menu.setTitle('最近打开')
open_recent_menu.setIcon(QIcon('xxx.png'))

new_action.triggered.connect(lambda :print('新建文件'))#4/关联行为信号
open_action.triggered.connect(lambda :print('打开文件'))#4/关联行为信号
exit_action.triggered.connect(lambda :print('退出文件'))#4/关联行为信号

file_action=QAction('pythonGUI编程')
open_recent_menu.addAction(file_action)

menu.addAction(new_action)#5/将行为绑定在菜单对象上
menu.addAction(open_action)#5/将行为绑定在菜单对象上
menu.addMenu(open_recent_menu)#8将子菜单绑定在菜单对象上
menu.addSeparator()#6菜单中添加一个分割线
menu.addAction(exit_action)#5/将行为绑定在菜单对象上


# btn.setMenu(menu)#1/将按钮设置一个菜单(传入菜单对象)
# btn.setFlat(True)#设置按钮的扁平化(背景没有了)
btn2=QPushButton('按钮2',window)
btn2.move(200,200)
btn2.setAutoDefault(True)#点击之后默认选中
# btn2.setDefault(True)#默认选中

def show_menu(point):
    menu = QMenu(window)  # 2/设置一个菜单对象
    new_action = QAction(QIcon('xxx.png'), '新建', menu)  # 3创建菜单对象的行为
    open_action = QAction(QIcon('xxx.png'), '打开', menu)  # 3创建菜单对象的行为
    exit_action = QAction('退出', menu)  # 3创建菜单对象的行为
    # new_action.setText('新建')
    # new_action.setIcon(QIcon('xxx.png'))
    open_recent_menu = QMenu(menu)  # 7创建一个新的菜单作为子菜单
    open_recent_menu.setTitle('最近打开')
    open_recent_menu.setIcon(QIcon('xxx.png'))

    new_action.triggered.connect(lambda: print('新建文件'))  # 4/关联行为信号
    open_action.triggered.connect(lambda: print('打开文件'))  # 4/关联行为信号
    exit_action.triggered.connect(lambda: print('退出文件'))  # 4/关联行为信号

    file_action = QAction('pythonGUI编程')
    open_recent_menu.addAction(file_action)

    menu.addAction(new_action)  # 5/将行为绑定在菜单对象上
    menu.addAction(open_action)  # 5/将行为绑定在菜单对象上
    menu.addMenu(open_recent_menu)  # 8将子菜单绑定在菜单对象上
    menu.addSeparator()  # 6菜单中添加一个分割线
    menu.addAction(exit_action)  # 5/将行为绑定在菜单对象上

    menu.exec_(window.mapToGlobal(point))  # 将菜单展示在界面上(相对于全局) 将局部坐标点通过方法映射为全局坐标点
window.setContextMenuPolicy(Qt.CustomContextMenu)#设置自定义桌面菜单
window.customContextMenuRequested.connect(show_menu)#设置自定义桌面菜单后会自动发射信号至这个函数

window.show()
# btn.showMenu()#代码显示菜单
sys.exit(app.exec_())