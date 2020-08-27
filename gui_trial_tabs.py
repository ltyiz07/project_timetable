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
from PyQt5.QtWidgets import QStackedWidget

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

        self.stack = QStackedWidget(self)

        self.week = ("mon", "tue", "wed", "thu", "fri")

        self.classes_input = []     # input text from first tab 'lineEdit' to next tab 'btns_name'
        self.btns_name = []         # QRadioButton, set by the classes_input with next push button
        self.btns_week = []         # QRadioButton for week on second window
        self.btns_time = []         # QPushButton for time on second window
        self.btn_set = QPushButton("SET")            # SET 버튼 누를 때마다 데이터 저장
        self.initUI()               #

    def initUI(self):
        #
        # tab1 레이아웃 설정
        self.Tab1()
        # tab1 레이아웃 설정 반영
        #

        #
        # stack 에 요일들 추가
        self.set_stack()

        #
        # tab2 레이아웃 설정
        self.Tab2()
        # tab2 레이아웃 설정 반영
        #

        self.tabs.addTab(self.tab1, "수업 이름 설정")
        self.tabs.addTab(self.tab2, "수업 시간들 추가")
        self.tabs.addTab(self.tab3, "결과...")            # tab3 추가

        vbox = QVBoxLayout()
        vbox.addWidget(self.tabs)

        self.setLayout(vbox)

        self.setWindowTitle('Timetable Maker')
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
        btn_next = QPushButton("&next")
        layout_1.addWidget(btn_next, 11, 2)
        btn_next.clicked.connect(self.next1_clicked)
        self.tab1.setLayout(layout_1)

    def Tab2(self):
        # setting for tab2
        layout_2 = QGridLayout()
        self.tab2.setLayout(layout_2)
        # 1. class 이름 목록
        group_1 = QGroupBox("class")
        group_11 = QVBoxLayout()
        for i in range(10):
            self.btns_name.append(QRadioButton())
            group_11.addWidget(self.btns_name[i])    # lineEdit 과 connect 하기
            self.btns_name[i].clicked.connect(self.RadioChanged)
        group_1.setLayout(group_11)
        # class 이름 목록 설정 완료

        # 2. week 목록
        week = ("mon", "tue", "wed", "thu", "fri")
        group_2 = QGroupBox("week")
        group_22 = QVBoxLayout()
        for i in range(5):
            self.btns_week.append(QRadioButton(week[i]))
            group_22.addWidget(self.btns_week[i])
        group_2.setLayout(group_22)

        layout_2.addWidget(group_1, 0, 0)
        layout_2.addWidget(group_2, 0, 1)
        layout_2.addWidget(self.stack, 0, 2)

        btn_set = QPushButton("SET")
        btn_set.setStyleSheet("color: red; selection-color: yellow; background-color: yellow; font: bold 14px")
        layout_2.addWidget(btn_set, 1, 2)
        btn_set.clicked.connect(self.set_clicked)

        self.tab2.setLayout(layout_2)

    def set_stack(self):
        self.mon = QGroupBox('monday')
        self.mon_box = QVBoxLayout()
        self.monday()           # 이동해서 세팅
        self.mon.setLayout(self.mon_box)

        self.tue = QWidget()
        tuesday = QGridLayout()
        self.tue.setLayout(tuesday)
        self.wed = QWidget()
        self.thu = QWidget()
        self.fri = QWidget()

        self.stack.addWidget(self.mon)
        self.stack.addWidget(self.tue)
        self.stack.addWidget(self.wed)
        self.stack.addWidget(self.thu)
        self.stack.addWidget(self.fri)
        self.stack.setMaximumSize(150, 450)
        self.stack.setCurrentIndex(0)

    def set_clicked(self):
        for i in range(10):
            if self.btns_name[i].isChecked():
                name_value = i
                break
        for j in range(5):
            if self.btns_week[j].isChecked():
                week_value = j
                break

        print(name_value, "    ", week_value, "    ")

    def RadioChanged(self):
        pass
        # for i in range(9):
        #     self.btns_time[i].setChecked(False)

    def monday(self):
        for j, i in enumerate(self.week):
            self.btns_week.append(QRadioButton(i))
            self.mon_box.addWidget(self.btns_week[j])

    def tuesday(self):
        pass

    def wedenesday(self):
        pass

    def thursday(self):
        pass

    def friday(self):
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
