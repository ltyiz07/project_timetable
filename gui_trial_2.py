## Ex 3-4. 툴팁 나타내기.

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtGui import QIcon


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowIcon(QIcon('lotus.png'))
        self.setWindowTitle('Time Table Maker')
        self.setGeometry(1200, 300, 500, 500)
        self.setToolTip('This is a <b>QWidget</b> widget')
        QToolTip.setFont(QFont('SansSerif', 10))

        self.btn = QPushButton('Next', self)
        self.btn.setToolTip('This is a <b>QPushButton</b> widget')
        self.btn.move(400, 460)
        self.btn.resize(self.btn.sizeHint())
        self.btn.setCheckable(True)
        # self.btn.setChecked(True)


        btn_1 = QPushButton("toggle", self)
        btn_1.move(300, 300)
        btn_1.resize(btn_1.sizeHint())
        btn_1.clicked.connect(self.review)


        self.show()

    def review(self):
        self.btn.setChecked(False)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())