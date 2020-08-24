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


class SecondWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.btn_class_1 = QPushButton(None)
        self.btn_class_2 = QPushButton(None)
        self.btn_class_3 = QPushButton(None)
        self.btn_class_4 = QPushButton(None)
        self.btn_class_5 = QPushButton(None)
        self.btn_class_6 = QPushButton(None)
        self.btn_class_7 = QPushButton(None)
        self.btn_class_8 = QPushButton(None)
        self.btn_class_9 = QPushButton(None)
        self.btn_class_10 = QPushButton(None)
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
        layout.addWidget(self.btn_class_1)
        layout.addWidget(self.btn_class_2)
        layout.addWidget(self.btn_class_3)
        layout.addWidget(self.btn_class_4)
        layout.addWidget(self.btn_class_5)
        layout.addWidget(self.btn_class_6)
        layout.addWidget(self.btn_class_7)
        layout.addWidget(self.btn_class_8)
        layout.addWidget(self.btn_class_9)
        layout.addWidget(self.btn_class_10)
        grp_1.setLayout(layout)

        # 두 번째 그룹 QGridLayout
        grp_2 = QGroupBox("Day")
        layout_base.addWidget(grp_2)
        layout = QGridLayout()
        layout.addWidget(QPushButton("mon"))
        layout.addWidget(QPushButton("tue"))
        layout.addWidget(QPushButton("wed"))
        layout.addWidget(QPushButton("thu"))
        layout.addWidget(QPushButton("fri"))
        grp_2.setLayout(layout)

        # 세 번째 그룹 QFormLaytout
        grp_3 = QGroupBox("QFormLaytout")
        layout_base.addWidget(grp_3)
        layout = QGridLayout()
        layout.addWidget(QPushButton("1교시"))
        layout.addWidget(QPushButton("2교시"))
        layout.addWidget(QPushButton("3교시"))
        layout.addWidget(QPushButton("4교시"))
        layout.addWidget(QPushButton("5교시"))
        layout.addWidget(QPushButton("6교시"))
        layout.addWidget(QPushButton("7교시"))
        layout.addWidget(QPushButton("8교시"))
        layout.addWidget(QPushButton("9교시"))
        grp_3.setLayout(layout)

        next_2 = QPushButton("next", self)
        layout_base.addWidget(next_2)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = SecondWindow()
    form.show()
    exit(app.exec_())
