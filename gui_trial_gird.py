
import sys

from gui_trial_grid2 import SecondWindow

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
    # 첫번째 화면
    def __init__(self):
        super().__init__()
        self.SetClasses()

    def SetClasses(self):
        self.setWindowTitle("First Class - Set Class")
        self.setFixedWidth(640)
        self.setFixedHeight(480)

        layout_base = QBoxLayout(QBoxLayout.TopToBottom, self)
        self.setLayout(layout_base)

        # 수업 갯수 목록 라벨
        grp_1 = QGroupBox("수업 목록")
        layout_base.addWidget(grp_1)
        layout = QGridLayout()
        layout.addWidget(QLabel("Class 1."), 0, 0)
        layout.addWidget(QLabel("Class 2. "), 1, 0)
        layout.addWidget(QLabel("Class 3. "), 2, 0)
        layout.addWidget(QLabel("Class 4. "), 3, 0)
        layout.addWidget(QLabel("Class 5. "), 4, 0)
        layout.addWidget(QLabel("Class 6. "), 5, 0)
        layout.addWidget(QLabel("Class 7. "), 6, 0)
        layout.addWidget(QLabel("Class 8. "), 7, 0)
        layout.addWidget(QLabel("Class 9. "), 8, 0)
        layout.addWidget(QLabel("Class 10. "), 9, 0)

        # 수업 이름들 선언
        self.class_1 = QLineEdit()
        self.class_2 = QLineEdit()
        self.class_3 = QLineEdit()
        self.class_4 = QLineEdit()
        self.class_5 = QLineEdit()
        self.class_6 = QLineEdit()
        self.class_7 = QLineEdit()
        self.class_8 = QLineEdit()
        self.class_9 = QLineEdit()
        self.class_10 = QLineEdit()

        # 수업 이름들 인풋 연결...
        # self.class_1.textChanged.connect(self.text_edited)
        # self.class_2.
        # self.class_3
        # self.class_4
        # self.class_5
        # self.class_6
        # self.class_7
        # self.class_8
        # self.class_9
        # self.class_10

        # 수업 이름 인풋들 배치
        layout.addWidget(self.class_1, 0, 1)
        layout.addWidget(self.class_2, 1, 1)
        layout.addWidget(self.class_3, 2, 1)
        layout.addWidget(self.class_4, 3, 1)
        layout.addWidget(self.class_5, 4, 1)
        layout.addWidget(self.class_6, 5, 1)
        layout.addWidget(self.class_7, 6, 1)
        layout.addWidget(self.class_8, 7, 1)
        layout.addWidget(self.class_9, 8, 1)
        layout.addWidget(self.class_10, 9, 1)
        grp_1.setLayout(layout)

        # 첫번째 화면 next 버튼
        next_1 = QPushButton("next", self)
        next_1.clicked.connect(self.firstnext_1Clicked)
        layout_base.addWidget(next_1)

    # def text_edited(self, text):
    #     self.btn_class_1.setText(text)
    #     self.btn_class_1.adjustSize()

    def firstnext_1Clicked(self):
        # 다음 클래스 실행 버튼클릭
        second_window = SecondWindow()
        second_window.show()
        self.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = Form()
    form.show()
    exit(app.exec_())
