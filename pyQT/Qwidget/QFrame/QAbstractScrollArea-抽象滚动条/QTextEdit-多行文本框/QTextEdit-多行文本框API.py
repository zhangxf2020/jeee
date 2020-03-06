from PyQt5.Qt import *


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('QTextEdit-多行文本框API')
        self.resize(500,500)
        self.initUI()
    def initUI(self):
        self.te=QTextEdit('xxx',self)
        self.te.move(20,50)
        self.te.resize(300,300)
        self.btn=QPushButton('测试',self)
        self.btn.move(20,20)
        self.btn.clicked.connect(self.text_insert)
        # self.设置占位文本()
        # self.普通设置()
        # self.文本光标设置()
    def 设置占位文本(self):
        self.te.setPlainText('请输入您的个人简介:')
        self.te.selectAll()
        self.te.setFocus()
    def 普通设置(self):
        #普通文本设置
        self.te.setPlainText('</h1>远看山有色</h1>')
        self.te.insertPlainText('</h1>远看山有色</h1>')
        #富文本设置
        self.te.setHtml('<h1>远看山有色</h1>')
        self.te.insertHtml('<h2>远看山有色</h2>')
    #使用文本光标设置
    def text_insert(self):
        #插入表格
        tc = self.te.textCursor()
        ttf=QTextTableFormat()
        #设置对其方式
        ttf.setAlignment(Qt.AlignRight)
        #设置表格内间距(距离实际内容)
        ttf.setCellPadding(1)
        #设置表格外间距(距离边框)
        ttf.setCellSpacing(2)

        tc.insertTable(3,4,ttf)


        return None
        #插入图片
        tc=self.te.textCursor()
        tif=QTextImageFormat()
        tif.setName('xxx.png')
        tif.setWidth(50)
        tif.setHeight(50)
        tc.insertImage(tif)
        return None
        #插入文本
        # QTextCursor
        # QTextCharFormat
        #创建文本光标格式对象
        tcf=QTextCharFormat()
        #设置鼠标提示
        tcf.setToolTip('爪哇')
        tcf.setFontFamily('楷体')
        tcf.setFontPointSize(20)
        #获取到对象的文本光标对象
        tc=self.te.textCursor()
        #对文本光标对象插入带有文本格式的内容(内容,内容格式(文本光标格式对象))
        tc.insertText('这里是插入的文本内容',tcf)
        #插入html字符串
        tc.insertHtml("<a href='www.baidu.com'> 谢谢 </a>")


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    window=Window()
    window.show()

    sys.exit(app.exec_())


