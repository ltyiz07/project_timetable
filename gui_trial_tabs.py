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
from sets_to_tables.sets_maker import SetMaker

class Data(QWidget):
    def __init__(self):
        super().__init__()
        self.unify_time = []
        self.data_list = []         # 시간들의 셋들을 저장함
        self.base_list = []         # data_list 내의 시간들의 셋들에대한 인덱스정보
        # 각각의 data_list 의 셋들을 base_list 인덱스에 따라 수업별로 정리한정보
        self.processed_sets = [[], [], [], [], [], [], [], [], [], []]




class MyApp(Data):
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

        #
        ## tab3 레이아웃 설정
        self.Tab3()
        ## tab3 레이아웃 설정 반영
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
        # 1. class 이름 목록
        group_1 = QGroupBox("class")
        group_11 = QVBoxLayout()
        for i in range(10):
            self.btns_name.append(QRadioButton())
            group_11.addWidget(self.btns_name[i])    # lineEdit 과 connect 하기
            self.btns_name[i].clicked.connect(self.week_clicked)
        group_1.setLayout(group_11)
        # class 이름 목록 설정 완료

        # 2. week 목록
        week = ("mon", "tue", "wed", "thu", "fri")
        group_2 = QGroupBox("week")
        group_22 = QVBoxLayout()
        for i in range(5):
            self.btns_week.append(QRadioButton(week[i]))
            group_22.addWidget(self.btns_week[i])
            self.btns_week[i].clicked.connect(self.week_changed)
        group_2.setLayout(group_22)

        layout_2.addWidget(group_1, 0, 0)
        layout_2.addWidget(group_2, 0, 1)
        layout_2.addWidget(self.stack, 0, 2)

        btn_set = QPushButton("SET")
        btn_set.setStyleSheet("color: red; selection-color: yellow; background-color: yellow; font: bold 14px")
        layout_2.addWidget(btn_set, 1, 2)
        btn_set.clicked.connect(self.set_clicked)

        self.tab2.setLayout(layout_2)

    def Tab3(self):
        layout_3 = QGridLayout()
        group_1 = QGroupBox("Table")
        group_11 = QVBoxLayout()
        group_1.setLayout(group_11)
        layout_3.addWidget(group_1, 0, 0, 1, 3)

        show = QPushButton("show")
        before = QPushButton("<-before")
        after = QPushButton("after->")

        show.clicked.connect(self.show_clicked)
        before.clicked.connect(self.before_clicked)
        after.clicked.connect(self.after_clicked)

        layout_3.addWidget(show, 1, 0)
        layout_3.addWidget(before, 1, 1)
        layout_3.addWidget(after, 1, 2)
        self.tab3.setLayout(layout_3)
        # for i in range(10):
        #     layout_1.addWidget(self.classes_input[i], i, 1)
        # btn_next = QPushButton("&next")
        # layout_1.addWidget(btn_next, 11, 2)
        # btn_next.clicked.connect(self.next1_clicked)
        # self.tab1.setLayout(layout_1)

    def week_clicked(self):
        for t in range(50):
            self.unify_time[t].setChecked(False)

    def before_clicked(self):
        pass

    def after_clicked(self):
        pass


class Disk(MyApp):
    def __init__(self):
        super().__init__()
        self.input_time_data = []

    def set_stack(self):
        # 월요일
        self.mon = QGroupBox('월요일')
        self.mon_box = QVBoxLayout()
        self.monday()           # 이동해서 세팅
        self.mon.setLayout(self.mon_box)
        # 화요일
        self.tue = QGroupBox('화요일')
        self.tue_box = QVBoxLayout()
        self.tuesday()
        self.tue.setLayout(self.tue_box)
        # 수요일
        self.wed = QGroupBox('수요일')
        self.wed_box = QVBoxLayout()
        self.wednesday()
        self.wed.setLayout(self.wed_box)
        # 목요일
        self.thu = QGroupBox('목요일')
        self.thu_box = QVBoxLayout()
        self.thursday()
        self.thu.setLayout(self.thu_box)
        # 금요일
        self.fri = QGroupBox('금요일')
        self.fri_box = QVBoxLayout()
        self.friday()
        self.fri.setLayout(self.fri_box)


        self.stack.addWidget(self.mon)
        self.stack.addWidget(self.tue)
        self.stack.addWidget(self.wed)
        self.stack.addWidget(self.thu)
        self.stack.addWidget(self.fri)
        self.stack.setMaximumSize(150, 450)

    def set_clicked(self):
        temp_time_data = []
        for i in range(10):
            if self.btns_name[i].isChecked():
                name_value = i
                break
        for j in range(5):
            if self.btns_week[j].isChecked():
                week_value = j
                break
        for u in range(50):
            if self.unify_time[u].isChecked():
                temp_time_data.append(u)
        self.input_time_data.append(name_value)
        self.input_time_data.append(temp_time_data)

        for t in range(50):
            self.unify_time[t].setChecked(False)
        print("name_value: ", name_value, "week_value: ", week_value)

    def show_clicked(self):
        """
        data processing

        :return:
        """
        print(self.input_time_data)
        for n, d in enumerate(self.input_time_data):
            if not(n % 2):
                self.data_list.append([])
                self.base_list.append(d)
                self.data_list[int(n / 2)] = self.input_time_data[n + 1]
        print(self.base_list)
        print(self.data_list)

        for e, i in enumerate(self.data_list):
            self.data_list[e] = set(i)
        print(self.data_list)

        for j, i in enumerate(self.base_list):
            self.processed_sets[i].append(self.data_list[j])
        print(self.processed_sets)

    def monday(self):
        for i in range(0, 10):
            self.unify_time.append(QPushButton('%d교시' % (i+1)))
            self.mon_box.addWidget(self.unify_time[i])
            self.unify_time[i].setCheckable(True)

    def tuesday(self):
        for i in range(10, 20):
            self.unify_time.append(QPushButton('%d교시' % (i - 9)))
            self.tue_box.addWidget(self.unify_time[i])
            self.unify_time[i].setCheckable(True)

    def wednesday(self):
        for i in range(20, 30):
            self.unify_time.append(QPushButton('%d교시' % (i - 19)))
            self.wed_box.addWidget(self.unify_time[i])
            self.unify_time[i].setCheckable(True)

    def thursday(self):
        for i in range(30, 40):
            self.unify_time.append(QPushButton('%d교시' % (i - 29)))
            self.thu_box.addWidget(self.unify_time[i])
            self.unify_time[i].setCheckable(True)

    def friday(self):
        for i in range(40, 50):
            self.unify_time.append(QPushButton('%d교시' % (i - 39)))
            self.fri_box.addWidget(self.unify_time[i])
            self.unify_time[i].setCheckable(True)

    def week_changed(self):
        for j in range(5):
            if self.btns_week[j].isChecked():
                week_value = j
                break
        self.stack.setCurrentIndex(week_value)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Disk()
    sys.exit(app.exec_())
