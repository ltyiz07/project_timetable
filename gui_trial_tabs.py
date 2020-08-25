import sys
from PyQt5.QtWidgets import QApplication, QTabWidget, QVBoxLayout
from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QSpacerItem
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QTextEdit
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QGroupBox

from PyQt5.QtWidgets import QBoxLayout
from PyQt5.QtWidgets import QHBoxLayout
from PyQt5.QtWidgets import QGridLayout
from PyQt5.QtWidgets import QFormLayout

from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import Qt

class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.classes_name = []
        self.initUI()

    def initUI(self):
        tab1 = QGroupBox()
        layout = QGridLayout()
        # tab1 레이아웃 설정
        for i in range(10):
            layout.addWidget(QLabel("Class %d." % (i+1)), i, 0)
        for i in range(10):
            self.classes_name.append(QLineEdit())
        for i in range(10):
            layout.addWidget(self.classes_name[i], i, 1)
        btn_next = QPushButton("next")
        layout.addWidget(btn_next, 11, 2)
        # tab1 레이아웃 설정 반영
        tab1.setLayout(layout)

        tab2 = QGroupBox()

        layout = QGridLayout()
        # tab2 레이아웃 설정
        for i in range(10):
            layout.addWidget(QPushButton(None))

        # tab2 레이아웃 설정 반영
        tab1.setLayout(layout)

        tabs = QTabWidget()
        tabs.addTab(tab1, "수업 이름 설정")
        tabs.addTab(tab2, "수업 시간들 추가")

        vbox = QVBoxLayout()
        vbox.addWidget(tabs)

        self.setLayout(vbox)

        self.setWindowTitle('QTabWidget')
        self.setWindowIcon(QIcon('lotus.png'))
        self.setGeometry(1200, 500, 500, 450)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
