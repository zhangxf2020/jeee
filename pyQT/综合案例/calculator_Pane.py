from PyQt5.Qt import *
import sys
from Resources.caculator import Ui_Form

class Caculator(QObject):
    def __init__(self,parent):
        super().__init__(parent)
        self.key_models = []
        self.flag = False
        self.endstr =''
    def parse_key_model(self,key_model):
        try:
            if key_model['role'] == 'clear':
                self.key_models =[]
                self.flag =False
                return '0.0'
            if key_model['role'] == 'caculate':
                if self.flag:
                    self.key_models[-1]['title'] += self.endstr
                    return str(eval(self.key_models[-1]['title']))
                if len(self.key_models) !=0 and self.key_models[-1]['role'] != 'operator':
                    str1 = ''
                    self.endstr = self.key_models[-2]['title']+self.key_models[-1]['title']
                    for model in self.key_models:
                        str1 +=model['title']
                    str1 =eval(str1)
                    self.key_models[0]['title'] =str(str1)
                    self.key_models = self.key_models[0:1]
                    self.flag = True
                    return str(str1)
            if key_model['role'] == 'num':
                if self.flag and self.key_models[-1]['role'] =='num':
                    self.key_models =[]
                    self.flag = False
                if len(self.key_models) == 0:
                    if key_model['title'] != '+/-' and key_model['title'] != '%' and key_model['title'] != '.':
                        self.key_models.append(key_model)
                        return key_model['title']
                    elif key_model['title'] =='.':
                        self.key_models.append(key_model)
                        self.key_models[-1]['title'] = '0.'
                        return self.key_models[-1]['title']

                else:
                    if self.key_models[-1]['role'] != 'operator':
                        if key_model['title'] == '+/-':
                            self.key_models[-1]['title'] = str(float(self.key_models[-1]['title'])*-1)
                            return self.key_models[-1]['title']
                        elif key_model['title'] == '%':
                            self.key_models[-1]['title'] = str(float(self.key_models[-1]['title']) /100)
                            return self.key_models[-1]['title']
                        elif key_model['title'] != '.' and self.key_models[-1]['title'] =='0':
                            self.key_models[-1]['title'] = key_model['title']
                            return self.key_models[-1]['title']
                        elif key_model['title'] =='.':
                            if '.' in self.key_models[-1]['title']:
                                return self.key_models[-1]['title']
                            else:
                                self.key_models[-1]['title'] += key_model['title']
                                return self.key_models[-1]['title']
                        else:
                            if self.key_models[-1]['role'] == 'num':
                                self.key_models[-1]['title'] += key_model['title']
                                return self.key_models[-1]['title']
                    else:
                        self.key_models.append(key_model)
                        return self.key_models[-1]['title']
            if key_model['role'] == 'operator':
                self.flag = False
                if len(self.key_models) ==0:
                    return None
                if self.key_models[-1]['role'] != 'operator':
                    if len(self.key_models)>2:
                        self.key_models[0]['title'] = str(eval(self.key_models[0]['title']+self.key_models[1]['title']+self.key_models[2]['title']))
                        self.key_models = self.key_models[0:1]
                        self.key_models.append(key_model)
                    else:self.key_models.append(key_model)
                    return self.key_models[0]['title']

                else:
                    self.key_models[-1]['title'] = key_model['title']
                    return self.key_models[0]['title']
        finally:
            print(self.key_models)



class CaculatorPlne(QWidget,Ui_Form):
    def __init__(self,parent=None,*args,**kwargs):
        super(CaculatorPlne, self).__init__(parent,*args,**kwargs)
        self.setAttribute(Qt.WA_StyledBackground,True)
        self.setupUi(self)
        self.caculator = Caculator(self)
    def get_key(self,title ,role):
        self.lineEdit.setText(self.caculator.parse_key_model({'title':title,'role':role}))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = CaculatorPlne()
    win.show()
    sys.exit(app.exec_())