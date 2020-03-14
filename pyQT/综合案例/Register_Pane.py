from PyQt5.Qt import *
import sys
from Resources.register import Ui_Form

class RegisterPane(QWidget,Ui_Form):
    exit_signal = pyqtSignal()
    register_account_pwd_signal = pyqtSignal(str,str)
    def __init__(self,parent=None,*args,**kwargs):
        super(RegisterPane, self).__init__(parent,*args,**kwargs)
        self.setAttribute(Qt.WA_StyledBackground,True)
        self.setupUi(self)
        self.animation_targets =[self.about_menue_btn,self.reset_menue_btn,self.exit_menue_btn]
        self.animation_targets_pos = [target.pos() for target in self.animation_targets]
        self.about_menue_btn.move(self.main_menue_btn.pos())
        self.reset_menue_btn.move(self.main_menue_btn.pos())
        self.exit_menue_btn.move(self.main_menue_btn.pos())

    def show_hide_menue(self,checked):
        animation_group = QSequentialAnimationGroup(self)#串行组动画,一个播放完之后再播放另一个
        for idx,target in enumerate(self.animation_targets):#enumerate返回一个序列的下标和对应的元素
            animation = QPropertyAnimation()#使用属性动画,这里更改坐标
            animation.setTargetObject(target)
            animation.setPropertyName(b'pos')

            animation.setStartValue(self.main_menue_btn.pos())#因为一开始是展开的,所以一开始的坐标为按钮的坐标
            animation.setEndValue(self.animation_targets_pos[idx])#回收到菜单按钮的坐标

            animation.setDuration(200)#设置动画时长
            animation.setEasingCurve(QEasingCurve.OutBounce)#是指动画弹簧效果
            animation_group.addAnimation(animation)#往动画组内添加动画
        if checked:
            animation_group.setDirection(QAbstractAnimation.Forward)#如果是按下状态,则需要收回所以是反着执行动画
        else:
            animation_group.setDirection(QAbstractAnimation.Backward)
        animation_group.start(QAbstractAnimation.DeleteWhenStopped)


    def about_lk(self):
        QMessageBox.about(self,'综合案例','www.baiducom')
    def reset(self):
        self.account_le.clear()
        self.password_le.clear()
        self.confirm_pwd_le.clear()
    def exit_pane(self):
        self.exit_signal.emit()
    def check_register(self):
        account_txt = self.account_le.text()
        password_txt = self.password_le.text()
        if self.enable_register_btn():
            self.register_account_pwd_signal.emit(account_txt,password_txt)
        else:
            QMessageBox.information(self,'提示','两次密码输入不一致',QMessageBox.Ok,QMessageBox.Ok)
    def enable_register_btn(self):
        account_txt = self.account_le.text()
        password_txt = self.password_le.text()
        cp_txt = self.confirm_pwd_le.text()
        if len(account_txt)>0 and len(password_txt)>0 and len(cp_txt)>0 and password_txt ==\
                cp_txt:
            return True




if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = RegisterPane()
    win.exit_signal.connect(lambda :print('退出'))
    win.register_account_pwd_signal.connect(lambda x,y:print(x,y))
    win.show()
    sys.exit(app.exec_())