from PyQt5.Qt import *


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('界面搭建')
        self.resize(250,250)
        self.initUI()
    def initUI(self):
        self.状态栏()
        self.菜单栏()
        self.子菜单()
        self.简单菜单()
        self.工具栏()


    def 状态栏(self):
        self.statusBar().showMessage('准备就绪')
    def 菜单栏(self):
        self.menubar = self.menuBar()  # 得到实例的菜单栏
        self.filemenu = self.menubar.addMenu('文件(&F)')  # 在菜单栏上添加一个菜单
    def 简单菜单(self):
        #一个行为对象,行为对象可以设置信号/快捷键和行为名称
        def action():
            action1=QAction(QIcon('123.png'),'退出(&E)',self)
            action1.setShortcut('Ctrl+Q')
            action1.setStatusTip('退出程序')
            action1.triggered.connect(qApp.quit)
            return action1

        self.filemenu.addAction(action())#在菜单中添加一个行为

    def 子菜单(self):
        def action():
            action1=QAction(QIcon('123.png'),'新建(&N)',self)
            action1.setStatusTip('新建文件')
            action1.setShortcut('Ctrl+N')
            return action1
        '''设置两个行为,一个为保存,另一个为另存为'''
        seve_acttion = QAction(QIcon('123.png'), '保存(&S)', self)
        seve_acttion.setStatusTip('保存文件')
        seve_acttion1 = QAction(QIcon('123.png'), '另存为....(&O)', self)
        seve_acttion1.setStatusTip('另存文件...')
        '''创建一个子菜单对象,将上方的两个行为添加其内'''
        self.sevemenu=QMenu('保存方式',self)

        self.sevemenu.addAction(seve_acttion)
        self.sevemenu.addAction(seve_acttion1)

        self.filemenu.addAction(action())#在实例的菜单上添加一个行为(新建行为)
        self.filemenu.addMenu(self.sevemenu)#在实例的菜单上添加个子菜单(子菜单可以包含其他菜单)
        self.filemenu.addSeparator()  # 在刚刚的行为下方添加一个分割线

    '''上下文菜单,重写contextMenuEvent方法(右键菜单方法)'''
    def contextMenuEvent(self, event):
        menumou=QMenu()
        acto=menumou.addAction('新建')
        open=menumou.addAction('打开')
        close=menumou.addAction('关闭')
        action=menumou.exec_(self.mapToGlobal(event.pos()))#返回点击的事件
        if action==close:
            print(close,action)
            qApp.quit()
    def 工具栏(self):
        action1 = QAction(QIcon('123.png'), '新建(&N)', self)
        action1.setStatusTip('新建文件')
        action1.setShortcut('Ctrl+N')
        toolbar=self.addToolBar('工具栏')
        toolbar.addAction(action1)
if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    window=Window()
    window.show()

    sys.exit(app.exec_())