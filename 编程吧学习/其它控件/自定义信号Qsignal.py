from PyQt5.Qt import *
import requests,json

class Window(QWidget):
    _mysignal = pyqtSignal(str,dict)
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Qsignal实验')
        self.resize(250,250)
        self.initUI()
    def initUI(self):
        self.clw= QCalendarWidget(self)
        self._mysignal[str,dict].connect(self.fashe)
        mylayout = QGridLayout(self)
        mylayout.addWidget(self.clw,0,0,1,3)
        self.string = ['日期','阴历','五行','冲煞','拜祭','祭神','宜','凶神','忌']
        self.string1 = ['yangli','yinli','wuxing','chongsha','baiji','jishen','yi','xiongshen','ji']
        self.lb =[]
        for i in range(len(self.string)):
            self.lb.append(QLabel(self.string[i]))
        for j in range(1,len(self.lb)+1):
            mylayout.addWidget(self.lb[j-1],j,0)
        self.clw.selectionChanged.connect(self.change)
    def change(self):
        date = self.clw.selectedDate().toString('yyyy-MM-d')
        params = {'key': '3f669268cbe38f049f9f20877c127bcf'
            , 'date': date}
        url = r'http://v.juhe.cn/laohuangli/d'
        for i in range(len(self.lb)):
            self.lb[i].setText(self.string[i])
        self._mysignal.emit(url,params)

    def fashe(self,url,params):
        try:
            content1 = requests.get(url, params)
            content1.encoding = 'utf-8'
            content1 = content1.text
            content1 = json.loads(content1)
            if content1:
                if content1['error_code'] ==0:
                    for i in range(len(self.lb)):
                        len1 = len(self.lb[i].text())
                        self.lb[i].setText('{name:<{len}}:{long:}'.format(name = self.lb[i].text(),long =content1['result'][self.string1[i]],len=4-len1))
                else:
                    str1 = '{},{}'.format(content1['error_code'],content1['reason'])
                    QMessageBox.information(self,'提示',str1)
            else:
                QMessageBox.information(self,'提示','request api error')
        except:QMessageBox.information(self,'提示','request api error')




if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    window=Window()
    window.show()

    sys.exit(app.exec_())

