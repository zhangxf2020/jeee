# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'register.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(500, 450)
        Form.setMinimumSize(QtCore.QSize(500, 450))
        Form.setMaximumSize(QtCore.QSize(500, 450))
        Form.setStyleSheet("QWidget#Form{\n"
"border-image: url(:/register/images/register_background.jpg);}")
        self.main_menue_btn = QtWidgets.QPushButton(Form)
        self.main_menue_btn.setGeometry(QtCore.QRect(10, 20, 40, 40))
        self.main_menue_btn.setStyleSheet("QPushButton {\n"
"    border-radius:20px;\n"
"    color:white;\n"
"    background-color:rgb(103, 167, 193);\n"
"    border:2px solid rgb(186, 229, 240)\n"
"        \n"
"}\n"
"QPushButton:hover {\n"
"    \n"
"    border:3px double rgb(2, 255, 120)\n"
"        \n"
"}\n"
"QPushButton:checked {\n"
"    \n"
"    background-color:rgb(20, 212, 255);\n"
"        \n"
"}")
        self.main_menue_btn.setCheckable(True)
        self.main_menue_btn.setChecked(False)
        self.main_menue_btn.setObjectName("main_menue_btn")
        self.about_menue_btn = QtWidgets.QPushButton(Form)
        self.about_menue_btn.setGeometry(QtCore.QRect(79, 3, 40, 40))
        self.about_menue_btn.setStyleSheet("QPushButton {\n"
"    border-radius:20px;\n"
"    color:white;\n"
"    background-color:rgb(103, 167, 193);\n"
"    border:2px solid rgb(186, 229, 240)\n"
"        \n"
"}\n"
"QPushButton:hover {\n"
"    \n"
"    border:3px double rgb(2, 255, 120)\n"
"        \n"
"}\n"
"QPushButton:checked {\n"
"    \n"
"    background-color:rgb(20, 212, 255);\n"
"        \n"
"}")
        self.about_menue_btn.setCheckable(False)
        self.about_menue_btn.setObjectName("about_menue_btn")
        self.reset_menue_btn = QtWidgets.QPushButton(Form)
        self.reset_menue_btn.setGeometry(QtCore.QRect(65, 59, 40, 40))
        self.reset_menue_btn.setStyleSheet("QPushButton {\n"
"    border-radius:20px;\n"
"    color:white;\n"
"    background-color:rgb(103, 167, 193);\n"
"    border:2px solid rgb(186, 229, 240)\n"
"        \n"
"}\n"
"QPushButton:hover {\n"
"    \n"
"    border:3px double rgb(2, 255, 120)\n"
"        \n"
"}\n"
"QPushButton:checked {\n"
"    \n"
"    background-color:rgb(20, 212, 255);\n"
"        \n"
"}")
        self.reset_menue_btn.setCheckable(False)
        self.reset_menue_btn.setObjectName("reset_menue_btn")
        self.exit_menue_btn = QtWidgets.QPushButton(Form)
        self.exit_menue_btn.setGeometry(QtCore.QRect(6, 84, 40, 40))
        self.exit_menue_btn.setStyleSheet("QPushButton {\n"
"    border-radius:20px;\n"
"    color:white;\n"
"    background-color:rgb(103, 167, 193);\n"
"    border:2px solid rgb(186, 229, 240)\n"
"        \n"
"}\n"
"QPushButton:hover {\n"
"    \n"
"    border:3px double rgb(2, 255, 120)\n"
"        \n"
"}\n"
"QPushButton:checked {\n"
"    \n"
"    background-color:rgb(20, 212, 255);\n"
"        \n"
"}")
        self.exit_menue_btn.setCheckable(False)
        self.exit_menue_btn.setObjectName("exit_menue_btn")
        self.layoutWidget = QtWidgets.QWidget(Form)
        self.layoutWidget.setGeometry(QtCore.QRect(200, 230, 231, 207))
        self.layoutWidget.setObjectName("layoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.layoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setVerticalSpacing(15)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setStyleSheet("color:rgb(255, 85, 0);\n"
"\n"
"font: 12pt \"楷体\";")
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.account_le = QtWidgets.QLineEdit(self.layoutWidget)
        self.account_le.setMinimumSize(QtCore.QSize(0, 30))
        self.account_le.setStyleSheet("background-color:transparent;\n"
"color:rgb(243, 243, 243);\n"
"border:None;\n"
"border-bottom:1px solid lightgray;")
        self.account_le.setText("")
        self.account_le.setClearButtonEnabled(True)
        self.account_le.setObjectName("account_le")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.account_le)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setStyleSheet("color:rgb(255, 85, 0);\n"
"\n"
"font: 12pt \"楷体\";")
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.password_le = QtWidgets.QLineEdit(self.layoutWidget)
        self.password_le.setMinimumSize(QtCore.QSize(0, 30))
        self.password_le.setStyleSheet("background-color:transparent;\n"
"color:rgb(243, 243, 243);\n"
"border:None;\n"
"border-bottom:1px solid lightgray;")
        self.password_le.setClearButtonEnabled(True)
        self.password_le.setObjectName("password_le")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.password_le)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        self.label_3.setStyleSheet("color:rgb(255, 85, 0);\n"
"\n"
"font: 12pt \"楷体\";")
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.confirm_pwd_le = QtWidgets.QLineEdit(self.layoutWidget)
        self.confirm_pwd_le.setMinimumSize(QtCore.QSize(0, 30))
        self.confirm_pwd_le.setStyleSheet("background-color:transparent;\n"
"color:rgb(243, 243, 243);\n"
"border:None;\n"
"border-bottom:1px solid lightgray;")
        self.confirm_pwd_le.setClearButtonEnabled(True)
        self.confirm_pwd_le.setObjectName("confirm_pwd_le")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.confirm_pwd_le)
        self.pushButton = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setMinimumSize(QtCore.QSize(0, 40))
        self.pushButton.setStyleSheet("QPushButton {\n"
"background-color: rgb(255, 170, 127);\n"
"    color:rgb(14, 131, 174);\n"
"    border-radius:10px\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgb(255, 192, 167);\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgb(195, 130, 97);\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.SpanningRole, self.pushButton)
        self.layoutWidget.raise_()
        self.about_menue_btn.raise_()
        self.reset_menue_btn.raise_()
        self.exit_menue_btn.raise_()
        self.main_menue_btn.raise_()

        self.retranslateUi(Form)
        self.main_menue_btn.clicked['bool'].connect(Form.show_hide_menue)
        self.about_menue_btn.clicked.connect(Form.about_lk)
        self.reset_menue_btn.clicked.connect(Form.reset)
        self.exit_menue_btn.clicked.connect(Form.exit_pane)
        self.pushButton.clicked.connect(Form.check_register)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.main_menue_btn.setText(_translate("Form", "菜单"))
        self.about_menue_btn.setText(_translate("Form", "关于"))
        self.reset_menue_btn.setText(_translate("Form", "重置"))
        self.exit_menue_btn.setText(_translate("Form", "退出"))
        self.label.setText(_translate("Form", "账    号:"))
        self.label_2.setText(_translate("Form", "密    码:"))
        self.label_3.setText(_translate("Form", "确认密码:"))
        self.pushButton.setText(_translate("Form", "注册"))
import images_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
