import sys
from PyQt5.QtWidgets import QApplication,QWidget

app=QApplication(sys.argv)
w=QWidget()
w.resize(250,500)
w.move(300,300)
w.show()
sys.exit(app.exec_())