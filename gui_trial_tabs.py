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
            self.classes_name[i] = QLineEdit()

            # self.classes_name[i].textChanged.connect(self.btn_change)
        for i in range(10):
            layout.addWidget(self.classes_name[i], i, 1)
        btn_next = QPushButton("next")
        layout.addWidget(btn_next, 11, 2)
        btn_next.clicked.connect(self.next1_clicked)
        tab1.setLayout(layout)
        # tab1 레이아웃 설정 반영
        #

        #
        # tab2 레이아웃 설정
        tab2 = QGroupBox("tab2")
        layout = QHBoxLayout()
        tab2.setLayout(layout)

        # 1. class 이름 목록
        group_1 = QGroupBox("class")
        group_11 = QVBoxLayout()
        for i in range(10):
            group_11.addWidget(QPushButton(self.classes_name[i].text()))    # lineEdit 과 connect 하기
        group_1.setLayout(group_11)
        # class 이름 목록 설정 완료

        # 2. week 목록
        group_2 = QGroupBox("week")

        # week 목록 설정 완료

        # 3. time 인풋
        group_3 = QGroupBox("time")

        # time 인풋 설정 완료

        layout.addWidget(group_1)
        layout.addWidget(group_2)
        layout.addWidget(group_3)

        tab1.setLayout(layout)
        # tab2 레이아웃 설정 반영

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

    def next1_clicked(self):
        print("next1 clicked")
        for i in range(10):
            self.classes_name[i].setText(self.classes_name[i].text())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
