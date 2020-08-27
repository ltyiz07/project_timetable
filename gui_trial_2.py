## Ex 3-4. 툴팁 나타내기.

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtGui import *


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()


    def initUI(self):
        self.button_group = QButtonGroup()
        self.setWindowIcon(QIcon('lotus.png'))
        self.setWindowTitle('Time Table Maker')
        self.setGeometry(1200, 300, 500, 500)
        self.setToolTip('This is a <b>QWidget</b> widget')
        QToolTip.setFont(QFont('SansSerif', 10))


        self.btn_3 = QPushButton()
        self.button_group.addButton(self.btn_3, 1)


        self.btn = QPushButton('Next_2', self)
        self.button_group.addButton(self.btn, 2)
        # self.button_group.addButton(self.btn, 1)
        self.btn.setToolTip('This is a <b>QPushButton</b> widget')
        self.btn.move(400, 460)
        self.btn.resize(self.btn.sizeHint())
        self.btn.setCheckable(True)

        self.btn_1 = QPushButton('Next_3', self)
        self.button_group.addButton(self.btn_1, 3)
        self.btn_1.setToolTip('This is a <b>QPushButton</b> widget')
        self.btn_1.move(250, 460)
        self.btn_1.resize(self.btn.sizeHint())
        self.btn_1.setCheckable(True)
        # self.btn.setChecked(True)

        self.btn_2 = QPushButton("what?")

        # self.QtWidgets.QButtonGroup.addButton(btn, [id=1])

        btn_0 = QPushButton("toggle", self)
        btn_0.move(300, 300)
        btn_0.resize(btn_0.sizeHint())
        btn_0.clicked.connect(self.review)
        self.button_group.setExclusive(False)

        self.show()

    def review(self):
        print(self.button_group.checkedButton())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())