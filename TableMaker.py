"""
시간표 자동생성 프로그램
"""
import os
import sys
from PyQt5.QtWidgets import QTabWidget, QVBoxLayout
from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QIcon
from PyQt5.QtGui import QStandardItem
from PyQt5.QtGui import QStandardItemModel
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QPushButton, QRadioButton
from PyQt5.QtWidgets import QGroupBox
from PyQt5.QtWidgets import QStackedWidget
from PyQt5.QtWidgets import QListView
from PyQt5.QtWidgets import QMessageBox

from PyQt5.QtWidgets import QGridLayout

from PyQt5.QtWidgets import QApplication
from sets_to_tables.sets_maker import SetMaker


class Data(QWidget):
    def __init__(self):
        super().__init__()
        self.unify_time = []
        self.data_list = []         # 시간들의 셋들을 저장함
        self.table_making = SetMaker()


class MyApp(Data):
    def __init__(self):
        super().__init__()
        # setting tabs
        self.tab1 = QGroupBox()
        self.tab2 = QGroupBox()
        self.tab3 = QGroupBox()
        self.tabs = QTabWidget()

        self.stack = QStackedWidget(self)

        # tab3 setting
        self.btn_show = QPushButton("show")
        self.tab3_group_11 = QVBoxLayout()
        self.tab3_group_22 = QVBoxLayout()
        self.stack2 = QStackedWidget(self)

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
        # tab3 레이아웃 설정
        self.Tab3()
        # tab3 레이아웃 설정 반영
        #

        self.tabs.addTab(self.tab1, "수업 이름 설정")
        self.tabs.addTab(self.tab2, "수업 시간들 추가")
        self.tabs.addTab(self.tab3, "시간표")            # tab3 추가

        vbox = QVBoxLayout()
        vbox.addWidget(self.tabs)

        self.setLayout(vbox)

        self.setWindowTitle('Timetable Maker')
        self.setWindowIcon(QIcon('lotus.png'))
        self.setGeometry(1200, 500, 500, 500)
        self.show()

    def next1_clicked(self):
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
        self.tabs.tabBarClicked.connect(self.next1_clicked)
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
            self.btns_name[i].clicked.connect(self.class_name_clicked)
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

    def class_name_clicked(self):
        for t in range(50):
            self.unify_time[t].setChecked(False)
        self.set_color_blue()

    def Tab3(self):
        # tab3 outfit
        layout_3 = QGridLayout()

        group_1 = QGroupBox("Options")
        group_1.setLayout(self.tab3_group_11)
        layout_3.addWidget(group_1, 0, 0, 1, 1)
        group_1.setMaximumSize(400, 2000)

        group_2 = QGroupBox("Table")
        group_2.setLayout(self.tab3_group_22)
        layout_3.addWidget(self.stack2, 0, 1, 1, 3)

        save = QPushButton("SAVE")
        info = QPushButton("info")

        self.btn_show.clicked.connect(self.btn_show_clicked)
        save.clicked.connect(self.save_clicked)
        info.clicked.connect(self.info_clicked)

        layout_3.addWidget(self.btn_show, 1, 0)
        layout_3.addWidget(save, 1, 3)
        layout_3.addWidget(info, 1, 2)
        self.tab3.setLayout(layout_3)

    def save_clicked(self):
        view_index = self.view.currentIndex()
        index = view_index.row()
        text_write = []
        class_info = ""
        for i, j in enumerate(self.table_making.class_seq[index]):
            temp_dialog_message = ""
            for k in self.sets_list[i][j]:
                temp_num_week = int(k) // 10
                temp_num_time = int(k) % 10
                temp_dialog_message += f"{self.week[temp_num_week]}_{temp_num_time + 1}, "
            class_info += "{0} ---> {1} \n".format(str(self.classes_input[i].text()), temp_dialog_message)
        indexed_table_list = self.table_making.lines[index * 11:index * 11 + 11]
        for line in indexed_table_list:
            text_write.append(str(line) + '\n')
        with open(f"..\\option{index + 1}.txt", 'w') as f:
            for one_line in text_write:
                f.write(one_line)
            f.write('\n')
            f.write(class_info)
            f.write('\n')
            f.write("(set font to 'D2CODING' or any monospaced font)")

    def tab3_show(self):
        self.view = QListView(self)
        self.model = QStandardItemModel()
        option_length = len(self.table_making.class_set)
        for option in range(option_length):
            self.model.appendRow(QStandardItem("option%d" % (option + 1)))
            table = QGroupBox("table%d" % (option + 1))
            table_box = QVBoxLayout()
            for i in self.table_making.lines[option * 11:(option * 11 + 11)]:
                label = QLabel(i, self)
                label.setFont(QFont('D2CODING'))
                table_box.addWidget(label)
            table.setLayout(table_box)
            self.stack2.addWidget(table)
        self.view.setModel(self.model)
        self.tab3_group_11.addWidget(self.view)
        self.view.clicked.connect(self.slot_clicked_item)

    def slot_clicked_item(self, index):
        self.stack2.setCurrentIndex(index.row())

    def info_clicked(self):
        view_index = self.view.currentIndex()
        index = view_index.row()
        title = "option%d" % (index + 1)
        message = ""
        for i, j in enumerate(self.table_making.class_seq[index]):
            temp_dialog_message = ""
            for k in self.sets_list[i][j]:
                temp_num_week = int(k) // 10
                temp_num_time = int(k) % 10
                temp_dialog_message += f"{self.week[temp_num_week]}_{temp_num_time + 1}, "
            message += "{0} ---> {1} \n".format(str(self.classes_input[i].text()), temp_dialog_message)
        QMessageBox.information(self, title, message)


class Disk(MyApp):
    def __init__(self):
        super().__init__()
        self.input_time_data = []
        self.sets_list = [[], [], [], [], [], [], [], [], [], []]

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

        self.set_color_blue()

        for c in self.unify_time:
            c.clicked.connect(self.set_color_green)

        self.stack.addWidget(self.mon)
        self.stack.addWidget(self.tue)
        self.stack.addWidget(self.wed)
        self.stack.addWidget(self.thu)
        self.stack.addWidget(self.fri)
        self.stack.setMaximumSize(150, 450)

    def set_color_blue(self):
        self.mon.setStyleSheet("background-color: #4d79ff;")
        self.tue.setStyleSheet("background-color: #4d79ff;")
        self.wed.setStyleSheet("background-color: #4d79ff;")
        self.thu.setStyleSheet("background-color: #4d79ff;")
        self.fri.setStyleSheet("background-color: #4d79ff;")

    def set_color_green(self):
        self.mon.setStyleSheet("background-color: #70db70;")
        self.tue.setStyleSheet("background-color: #70db70;")
        self.wed.setStyleSheet("background-color: #70db70;")
        self.thu.setStyleSheet("background-color: #70db70;")
        self.fri.setStyleSheet("background-color: #70db70;")

    def set_clicked(self):
        self.set_color_blue()
        for i in range(10):
            if self.btns_name[i].isChecked():
                name_index = i
                break
        temp_set = set(())
        for u in range(50):
            if self.unify_time[u].isChecked():
                btn_index = str(u)
                temp_set.add(btn_index.zfill(2))
        self.sets_list[name_index].append(temp_set)
        # reset buttons
        for t in range(50):
            self.unify_time[t].setChecked(False)

    def btn_show_clicked(self):
        """
        data processing

        :return:
        """
        self.btn_show.setEnabled(False)
        self.table_making.matcher(self.sets_list, self.classes_input)
        self.tab3_show()


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
        """
        날짜 클릭되면 스택 반환.
        :return:
        """
        for j in range(5):
            if self.btns_week[j].isChecked():
                week_value = j
                break
        self.stack.setCurrentIndex(week_value)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Disk()
    sys.exit(app.exec_())
