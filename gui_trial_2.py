## Ex 3-4. 툴팁 나타내기.

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QToolTip
from PyQt5.QtGui import QFont
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

        btn = QPushButton('Next', self)
        btn.setToolTip('This is a <b>QPushButton</b> widget')
        btn.move(400, 460)
        btn.resize(btn.sizeHint())
        btn.clicked.connect(QCoreApplication.instance().quit)

        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())