from Login_Pane import LoginPane
from Register_Pane import RegisterPane
from calculator_Pane import CaculatorPlne
from PyQt5.Qt import *
import sys




if __name__ == '__main__':
    app = QApplication(sys.argv)
    login_pane = LoginPane()
    calculator_pane = CaculatorPlne()
    register_pane = RegisterPane(login_pane)
    register_pane.move(0, login_pane.height())
    register_pane.show()
    def show_register_pane():
        animation = QPropertyAnimation(register_pane)
        animation.setTargetObject(register_pane)
        animation.setPropertyName(b'pos')
        animation.setStartValue(register_pane.pos())
        animation.setEndValue(QPoint(0,0))
        animation.setDuration(1000)
        animation.setEasingCurve(QEasingCurve.OutBounce)
        animation.start(QAbstractAnimation.DeleteWhenStopped)
    def exit_register_pane():
        animation = QPropertyAnimation(register_pane)
        animation.setTargetObject(register_pane)
        animation.setPropertyName(b'pos')
        animation.setStartValue(QPoint(0, 0))
        animation.setEndValue(QPoint(login_pane.width(),0))
        animation.setDuration(1000)
        animation.setEasingCurve(QEasingCurve.InBounce)
        animation.start(QAbstractAnimation.DeleteWhenStopped)
    def check_login(account,pwd):
        if account =='23654123' and pwd =='123':
            calculator_pane.show()
            login_pane.hide()
        else:
            login_pane.show_error_animation()

    #信号连接
    login_pane.show_register_pane_signal.connect(show_register_pane)
    register_pane.exit_signal.connect(exit_register_pane)
    login_pane.check_login_signal.connect(check_login)
    login_pane.show()
    sys.exit(app.exec_())