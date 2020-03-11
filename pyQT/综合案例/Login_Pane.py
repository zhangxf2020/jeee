from PyQt5.Qt import *
import sys
from Resources.login import Ui_Form

class LoginPane(QWidget,Ui_Form):
    show_register_pane_signal = pyqtSignal()
    check_login_signal = pyqtSignal(str,str)

    def __init__(self,parent=None,*args,**kwargs):
        super(LoginPane, self).__init__(parent,*args,**kwargs)
        self.setAttribute(Qt.WA_StyledBackground,True)
        self.setupUi(self)
        movie = QMovie(':/login/images/login_top_bg.gif')
        movie.setScaledSize(QSize(self.width(),180))#设置动态图片的尺寸
        self.login_top_bg_label.setMovie(movie)
        movie.start()
    def show_register_pane(self):
        self.show_register_pane_signal.emit()
    def open_qq_link(self):
        link = r'http://shang.qq.com/wpa/qunwpa?idkey=aa9b59ea6a8c8796037b10d606a3b5256b6bd3763a45165fa0c88ed64bf067bf'
        QDesktopServices.openUrl(QUrl(link))#打开一个网页
    def enable_login_btn(self):
        account = self.account_cb.currentText()
        pwd = self.pwd_le.text()
        if len(account)>0 and len(pwd)>0:
            self.login_btn.setEnabled(True)
        else:
            self.login_btn.setEnabled(False)
    def check_login(self):
        account = self.account_cb.currentText()
        pwd = self.pwd_le.text()
        self.check_login_signal.emit(account,pwd)
    def auto_login(self,checked):
        if checked:
            self.remember_pwd_cb.setChecked(True)
    def remember_pwd(self,checked):
        if not checked:
            self.auto_login_cb.setChecked(False)

    def show_error_animation(self):
        animation = QPropertyAnimation(self)
        animation.setTargetObject(self.login_bottom)
        animation.setPropertyName(b'pos')
        animation.setKeyValueAt(0,self.login_bottom.pos())
        animation.setKeyValueAt(0.2,self.login_bottom.pos()+QPoint(15,0))
        animation.setKeyValueAt(0.5,self.login_bottom.pos())
        animation.setKeyValueAt(0.7,self.login_bottom.pos()+QPoint(-15,0))
        animation.setKeyValueAt(1,self.login_bottom.pos())
        animation.setLoopCount(3)
        animation.setDuration(150)
        animation.start(QAbstractAnimation.DeleteWhenStopped)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = LoginPane()
    win.show()
    sys.exit(app.exec_())