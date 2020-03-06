from PyQt5.Qt import *
import webbrowser

class Window(QToolBox):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('工具箱QToolBox')
        self.setWindowFlags(Qt.Dialog)
        self.resize(250,500)
        self.initUI()
    def initUI(self):
        favorites = [
            [
                {'des':'百度搜索','pic':r'image/se/baidu.ico'},
                {'des': '搜狗搜索', 'pic': r'image/se/sougo.ico'},
                {'des': '必应搜索', 'pic': r'image/se/bing.ico'},
                {'des': '360搜索', 'pic': r'image/se/360.ico'},
                {'des': '谷歌搜索', 'pic': r'image/se/google.ico'},
                {'des': '雅虎搜索', 'pic': r'image/se/yahoo.ico'}
            ],
            [
                {'des': '腾讯视频', 'pic': r'image/v/tengxun.ico'},
                {'des': '搜狐视频', 'pic': r'image/v/sohuvideo.ico'},
                {'des': '优酷视频', 'pic': r'image/v/youku.ico'},
                {'des': '土豆视频', 'pic': r'image/v/tudou.ico'},
                {'des': 'AcFun弹幕', 'pic': r'image/v/acfun.ico'},
                {'des': '哔哩哔哩', 'pic': r'image/v/bilibili.ico'}
            ]
        ]
        for item in favorites:
            groupbox = QGroupBox()
            vlayout = QVBoxLayout(groupbox)
            vlayout.setAlignment(Qt.AlignCenter)
            for category in item:
                #toolButton 输入工具栏按钮,通常只显示图标,不显示文字
                toolButton = QToolButton()
                toolButton.setText(category['des'])
                toolButton.setIcon(QIcon(category['pic']))
                toolButton.setIconSize(QSize(64,64))
                #打开或关闭按钮选中效果True不显示
                toolButton.setAutoRaise(True)
                toolButton.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
                vlayout.addWidget(toolButton)
                name = category['des']
                toolButton.clicked.connect(self.run)
                if name =='雅虎搜索':
                    #添加项目,只能添加控件,无法添加布局
                    self.addItem(groupbox,'搜索引擎')
                elif name =='哔哩哔哩':
                    self.addItem(groupbox,'视频网站')

    def run(self):
        if self.sender().text() == '百度搜索':
            webbrowser.open('www.baidu.com')
        elif self.sender().text() == '搜狗搜索':
            webbrowser.open('www.sogou.com')
        elif self.sender().text() == '必应搜索':
            webbrowser.open(r'https://cn.bing.com/?toHttps=1&redig=68D983AFB8264741A4CCEAF0FE270880')
        elif self.sender().text() == '360搜索':
            webbrowser.open(r'https://www.so.com/')
        elif self.sender().text() == '谷歌搜索':
            webbrowser.open(r'https://www.google.cn/')
        elif self.sender().text() == '雅虎搜索':
            webbrowser.open(r'https://www.yahoo.com/')
        elif self.sender().text() == '腾讯视频':
            webbrowser.open(r'https://v.qq.com/')
        elif self.sender().text() == '搜狐视频':
            webbrowser.open(r'https://tv.sohu.com/')
        elif self.sender().text() == '优酷视频':
            webbrowser.open(r'https://www.youku.com/')
        elif self.sender().text() == '土豆视频':
            webbrowser.open(r'https://www.youku.com/')
        elif self.sender().text() == 'AcFun弹幕':
            webbrowser.open(r'https://www.acfun.cn/')
        elif self.sender().text() == '哔哩哔哩':
            webbrowser.open(r'https://www.bilibili.com/')




if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    window=Window()
    window.show()

    sys.exit(app.exec_())