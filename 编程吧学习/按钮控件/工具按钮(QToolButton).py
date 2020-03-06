from PyQt5.Qt import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('QToolButton控件')
        self.resize(250,250)
        self.initUI()
    def initUI(self):
        tb=QToolButton(self)
        tb.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)#设置按钮风格
        '''
        #Qt.ToolButtonIconOnly    仅显示图标-默认
        #Qt.ToolButtonTextOnly    仅显示文字
        #Qt.ToolButtonTextBesideIcon    文本显示在图标旁边
        #Qt.ToolButtonTextUnderIcon    文本显示在图标下方
        #Qt.ToolButtonFollowStyle   遵循风格
        #toolButtonStyle()   #获取样式风格
        '''

        tb.setIcon(QIcon(r'.\3421.jpg'))
        tb.setText('支付方式')
        tb.setToolTip('选择适合你的支付方式')

        # tb.setArrowType(Qt.UpArrow)#设置箭头
        '''
        # Qt.NoArrow     无箭头
        # Qt.UpArrow     向上箭头
        # Qt.DownArrow    向下箭头
        # Qt.LeftArrow    向左箭头
        # Qt.RightArrow    向右箭头
        # arrowType()   获取箭头类型
        '''

        tb.setPopupMode(QToolButton.MenuButtonPopup)#设置菜单弹出模式
        '''
        # QToolButton.DelayedPopup    鼠标按住一会才显示-默认
        # QToolButton.MenuButtonPopup    有一个专门的指示箭头,点击箭头才显示
        # QToolButton.InstantPopup    点了按钮就显示,点击信号不会发射
        '''

        tb.setAutoRaise(True)
        '''
        # 设置是否自动提升-鼠标在上面时会自动凸起
        '''
        self.alipayAct = QAction(QIcon(r'.\3421.jpg'), '支付宝支付', self)
        self.wechatAct = QAction(QIcon(r'.\3421.jpg'), '微信支付', self)
        self.visaAct = QAction(QIcon(r'.\3421.jpg'), 'Visa卡支付', self)
        self.master_cardAct = QAction(QIcon(r'.\3421.jpg'), '万事达卡支付', self)

        menu = QMenu()
        menu.addActions([self.alipayAct,self.wechatAct])
        menu.addSeparator()
        menu.addActions([self.visaAct,self.master_cardAct])
        tb.setMenu(menu)
        self.alipayAct.triggered.connect(self.on_click)
        self.wechatAct.triggered.connect(self.on_click)
        self.visaAct.triggered.connect(self.on_click)
        self.master_cardAct.triggered.connect(self.on_click)
    def on_click(self):

        if self.sender() == self.alipayAct:
            QDesktopServices.openUrl(QUrl('https://www.alipay.com/'))
        elif self.sender() == self.wechatAct:
            QDesktopServices.openUrl(QUrl('https://pay.weixin.qq.com/index.php'))
        elif self.sender() == self.visaAct:
            QDesktopServices.openUrl(QUrl('https://www.visa.com.cn/'))
        else:
            QDesktopServices.openUrl(QUrl('https://www.mastercard.com.cn/zh-cn.html'))
        '''
        # 点击的当前控件满足条件时,打开相应的网页
        '''
if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    window=Window()
    window.show()

    sys.exit(app.exec_())