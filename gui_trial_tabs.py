"""
시간표 자동생성 프로그램
"""
import sys
from PyQt5.QtWidgets import QApplication, QTabWidget, QVBoxLayout
from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QSpacerItem
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QTextEdit
from PyQt5.QtWidgets import QPushButton, QRadioButton
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
        # setting tabs
        self.tab1 = QGroupBox()
        self.tab2 = QGroupBox()
        self.tab3 = QGroupBox()
        self.tabs = QTabWidget()

        self.classes_input = []     # input text from first tab 'lineEdit' to next tab 'btns_name'
        self.btns_name = []         # set by the classes_input with next push button
        self.btns_week = []         # btns for week on second window
        self.btns_time = []         # btns for time on second window
        self.btn_set = QPushButton("SET")            # SET 버튼 누를 때마다 데이터 저장
        self.initUI()               #

    def initUI(self):
        #
        # tab1 레이아웃 설정
        self.Tab1()
        # tab1 레이아웃 설정 반영
        #

        #
        # tab2 레이아웃 설정
        self.Tab2()
        # tab2 레이아웃 설정 반영
        #

        self.tabs.addTab(self.tab1, "수업 이름 설정")
        self.tabs.addTab(self.tab2, "수업 시간들 추가")
        self.tabs.addTab(self.tab3, "결과...")

        vbox = QVBoxLayout()
        vbox.addWidget(self.tabs)

        self.setLayout(vbox)

        self.setWindowTitle('QTabWidget')
        self.setWindowIcon(QIcon('lotus.png'))
        self.setGeometry(1200, 500, 500, 500)
        self.show()

    def next1_clicked(self):
        print("next1 clicked")
        for i in range(10):
            print(self.classes_input[i].text())
        for i in range(10):
            self.btns_name[i].setText(self.classes_input[i].text())
        for n in self.btns_name:
            n.setCheckable(True)
            n.toggle()
        self.tabs.setCurrentIndex(1)

    def Tab1(self):
        # setting for tab1
        layout_1 = QGridLayout()
        for i in range(10):
            layout_1.addWidget(QLabel("Class %d." % (i+1)), i, 0)
        for i in range(10):
            self.classes_input.append(QLineEdit())

        for i in range(10):
            layout_1.addWidget(self.classes_input[i], i, 1)
        btn_next = QPushButton("next")
        layout_1.addWidget(btn_next, 11, 2)
        btn_next.clicked.connect(self.next1_clicked)
        self.tab1.setLayout(layout_1)

    def Tab2(self):
        # setting for tab2
        layout_2 = QHBoxLayout()
        self.tab2.setLayout(layout_2)
        # 1. class 이름 목록
        group_1 = QGroupBox("class")
        group_11 = QVBoxLayout()
        for i in range(10):
            self.btns_name.append(QRadioButton())
            group_11.addWidget(self.btns_name[i])    # lineEdit 과 connect 하기
        group_1.setLayout(group_11)
        # class 이름 목록 설정 완료

        # 2. week 목록
        week = ("mon", "tue", "wed", "thu", "fri")
        group_2 = QGroupBox("week")
        group_22 = QVBoxLayout()
        for i in range(5):
            self.btns_week.append(QPushButton(week[i]))
            group_22.addWidget(self.btns_week[i])
        group_2.setLayout(group_22)
        # week 목록 설정 완료

        # 3. time 인풋
        time = ('1', '2', '3', '4', '5', '6', '7', '8', '9')
        group_3 = QGroupBox("time")
        group_33 = QVBoxLayout()
        for i in range(9):
            self.btns_time.append(QPushButton(time[i]))
            group_33.addWidget(self.btns_time[i])
        # SET 버튼 디자인 설정
        self.btn_set.setStyleSheet("color: red; selection-color: yellow; background-color: yellow; font: bold 14px")
        # self.btn_set.mou
        group_33.addWidget(self.btn_set)

        group_3.setLayout(group_33)

        # time 인풋 설정 완료

        layout_2.addWidget(group_1)
        layout_2.addWidget(group_2)
        layout_2.addWidget(group_3)

        self.tab2.setLayout(layout_2)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
