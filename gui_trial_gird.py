
import sys

from PyQt5.QtWidgets import QWidget
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

class Form(QWidget):
    def __init__(self):
        super().__init__()
        self.classes_name = []
        self.SetClasses()

    def SetClasses(self):
        self.setWindowTitle("First Class - Set Class")
        self.setFixedWidth(640)
        self.setFixedHeight(480)

        layout_base = QBoxLayout(QBoxLayout.TopToBottom, self)
        self.setLayout(layout_base)

        grp_1 = QGroupBox("수업 목록")
        layout_base.addWidget(grp_1)
        layout = QGridLayout()

        for i in range(10):
            layout.addWidget(QLabel("Class %d." % (i + 1)), i, 0)

        for i in range(10):
            self.classes_name.append(QLineEdit())

        for i in range(10):
            layout.addWidget(self.classes_name[i], i, 1)

        grp_1.setLayout(layout)

        next_1 = QPushButton("next", self)
        next_1.clicked.connect(self.firstnext_1Clicked)
        layout_base.addWidget(next_1)

    def firstnext_1Clicked(self):
        self.sec = SecondWindow(self.classes_name)
        self.sec.show()
        self.close()


class SecondWindow(QWidget):
    def __init__(self, classes_list):
        super().__init__()
        self.working_days = ["mon", "tue", "wed", "thu", "fri"]
        self.classes_list = classes_list
        self.SetTime()

    def SetTime(self):
        self.setWindowTitle("Second Window - Set Time")
        self.setFixedWidth(640)
        self.setFixedHeight(480)

        layout_base = QBoxLayout(QBoxLayout.LeftToRight, self)
        self.setLayout(layout_base)

        # 첫 번째 그룹 QBoxLayout
        grp_1 = QGroupBox("Class Name")
        layout_base.addWidget(grp_1)
        layout = QGridLayout()

        for i in range(10):
            layout.addWidget(QPushButton(self.classes_list[i].text()))
        grp_1.setLayout(layout)

        # 두 번째 그룹 QGridLayout
        grp_2 = QGroupBox("Day")
        layout_base.addWidget(grp_2)
        layout = QGridLayout()
        #
        for i in range(5):
            layout.addWidget(QPushButton(self.working_days[i]))
        grp_2.setLayout(layout)

        # 세 번째 그룹 QFormLaytout
        grp_3 = QGroupBox("QFormLaytout")
        layout_base.addWidget(grp_3)
        layout = QGridLayout()

        for i in range(10):
            layout.addWidget(QPushButton("%d교시" % (i+1)))
        grp_3.setLayout(layout)

        next_1 = QPushButton("next_1", self)
        layout_base.addWidget(next_1)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = Form()
    form.show()
    exit(app.exec_())

