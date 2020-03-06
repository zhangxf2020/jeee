from PyQt5.QtWidgets import (QApplication,QWidget,QCalendarWidget,QLabel,QSlider,QGridLayout)
from PyQt5.QtCore import Qt,pyqtSignal
import sys,requests,json

class Example(QWidget):
    _signal = pyqtSignal(str,str)
    def __init__(self):
        super(Example, self).__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300,300,450,380)
        self.setWindowTitle("QCalendarWidget日历+爬虫")
        gridLayout = QGridLayout()
        self.calendar = QCalendarWidget()
        self.calendar.setGridVisible(True)
        self.lb11 = QLabel("阳历：")
        self.lb12 = QLabel("")
        self.lb21 = QLabel("阴历：")
        self.lb22 = QLabel("")
        self.lb31 = QLabel("五行：")
        self.lb32 = QLabel("")
        self.lb41 = QLabel("冲煞：")
        self.lb42 = QLabel("")
        self.lb51 = QLabel("彭祖百忌：")
        self.lb52 = QLabel("")
        self.lb61 = QLabel("吉神：")
        self.lb62 = QLabel("")
        self.lb71 = QLabel("宜：")
        self.lb72 = QLabel("")
        self.lb81 = QLabel("凶神：")
        self.lb82 = QLabel("")
        self.lb91 = QLabel("忌：")
        self.lb92 = QLabel("")
        gridLayout.addWidget(self.calendar,0,0,1,3)
        gridLayout.addWidget(self.lb11,1,0,1,1)
        gridLayout.addWidget(self.lb12,1,1,1,2)
        gridLayout.addWidget(self.lb21,2,0,1,1)
        gridLayout.addWidget(self.lb22,2,1,1,2)
        gridLayout.addWidget(self.lb31,3,0,1,1)
        gridLayout.addWidget(self.lb32,3,1,1,2)
        gridLayout.addWidget(self.lb41, 4, 0, 1, 1)
        gridLayout.addWidget(self.lb42, 4, 1, 1, 2)
        gridLayout.addWidget(self.lb51, 5, 0, 1, 1)
        gridLayout.addWidget(self.lb52, 5, 1, 1, 2)
        gridLayout.addWidget(self.lb61, 6, 0, 1, 1)
        gridLayout.addWidget(self.lb62, 6, 1, 1, 2)
        gridLayout.addWidget(self.lb71, 7, 0, 1, 1)
        gridLayout.addWidget(self.lb72, 7, 1, 1, 2)
        gridLayout.addWidget(self.lb81, 8, 0, 1, 1)
        gridLayout.addWidget(self.lb82, 8, 1, 1, 2)
        gridLayout.addWidget(self.lb91, 9, 0, 1, 1)
        gridLayout.addWidget(self.lb92, 9, 1, 1, 2)
        self.setLayout(gridLayout)

        self.calendar.selectionChanged.connect(self.mySignal)
        self._signal.connect(self.request1)

    def mySignal(self):
        self.date = self.calendar.selectedDate().toString("yyyy-MM-dd")
        self.appkey = "3f669268cbe38f049f9f20877c127bcf"
        self._signal.emit(self.appkey,self.date)

    # 日历
    def request1(self,appkey,date):
        try:
            url = "http://v.juhe.cn/laohuangli/d"
            params = {
                "key": appkey,  # 应用APPKEY(应用详细页查询)
                "date": date,  # 日期，格式2014-09-09
            }

            req = requests.get(url, params=params)#使用requests.get得到api响应的内容,返回的是requests对象
            req.encoding = 'utf8'
            content = req.text  # 得到的content是str格式，使用json.loads() 将其转为dict字典格式
            res = json.loads(content)
            if res:
                error_code = res["error_code"]
                if error_code == 0:
                    # 成功请求
                    self.lb12.setText(res["result"]["yangli"])
                    self.lb22.setText(res["result"]["yinli"])
                    self.lb32.setText(res["result"]["wuxing"])
                    self.lb42.setText(res["result"]["chongsha"])
                    self.lb52.setText(res["result"]["baiji"])
                    self.lb62.setText(res["result"]["jishen"])
                    self.lb72.setText(res["result"]["yi"])
                    self.lb82.setText(res["result"]["xiongshen"])
                    self.lb92.setText(res["result"]["ji"])
                else:
                    print("%s:%s" % (res["error_code"], res["reason"]))
            else:
                print("request api error")
        except:
            pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())

