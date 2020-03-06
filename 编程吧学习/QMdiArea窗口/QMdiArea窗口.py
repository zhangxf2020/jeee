from PyQt5.Qt import *
import sys,random
class Card(QLabel):
    Card = {"2": r'./res/pokercards/2.png',
            "3": r'./res/pokercards/3.png',
            "4": r'./res/pokercards/4.png',
            "5": r'./res/pokercards/5.png',
            "6": r'./res/pokercards/6.png',
            "7": r'./res/pokercards/7.png',
            "8": r'./res/pokercards/8.png',
            "9": r'./res/pokercards/9.png',
            "10": r'./res/pokercards/10.png',
            "a": r'./res/pokercards/a.png',
            "j": r'./res/pokercards/j.png',
            "joker": r'./res/pokercards/joker.png',
            "k": r'./res/pokercards/k.png',
            "q": r'./res/pokercards/q.png',
            }
    def __init__(self,num):
        super(Card, self).__init__(num)
        self.setPixmap(QPixmap(self.Card[num]))

class My_Win(QMainWindow):

    def __init__(self):
        super(My_Win, self).__init__()
        self.setWindowTitle('QMdiArea窗口')
        self.setGeometry(0,0,1920,1080)
        self.initui()
    def initui(self):
        self.mid = QMdiArea()
        self.setCentralWidget(self.mid)
        sendOnecardAct = QAction(QIcon(r'./res/sendOnecard.ico'),'发一张牌',self)
        sendOnecardAct.triggered.connect(self.sendOnecard)
        sendFivecardsAct = QAction(QIcon('./res/sendFivecard.ico'), '随机5张牌', self)
        sendFivecardsAct.triggered.connect(self.sendFivecards)
        clearcardAct = QAction(QIcon('./res/clear.ico'), '清除牌', self)
        clearcardAct.triggered.connect(self.clearCards)
        foldcardAct = QAction(QIcon('./res/fold.ico'), '收牌', self)
        foldcardAct.triggered.connect(self.foldCards)
        toolbar = self.addToolBar('工具栏')
        toolbar.addAction(sendOnecardAct)
        toolbar.addAction(sendFivecardsAct)
        toolbar.addAction(clearcardAct)
        toolbar.addAction(foldcardAct)
        toolbar.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

    def sendOnecard(self):
        randomflag = self.randomsend(1)
        subcard = QMdiSubWindow()
        subcard.setWidget(Card(randomflag))
        self.mid.addSubWindow(subcard)
        subcard.setWindowFlags(Qt.WindowMinimizeButtonHint)
        subcard.resize(150, 200)
        subcard.show()
    def sendFivecards(self):
        randomflag = self.randomsend(5)
        for item in randomflag:
            subcard = QMdiSubWindow()
            subcard.setWidget(Card(item))
            self.mid.addSubWindow(subcard)
            subcard.setWindowFlags(Qt.WindowMinimizeButtonHint)
            subcard.resize(150, 200)
            subcard.show()
    def clearCards(self):
        self.mid.closeAllSubWindows()
    def foldCards(self):
        self.mid.cascadeSubWindows()
    def randomsend(self,num):
        cardlist = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "a", "j", "joker", "k", "q"]
        if num ==1:
            return random.choice(cardlist)
        elif num ==5:
            return random.sample(cardlist,5)
if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = My_Win()
    win.show()
    sys.exit(app.exec_())