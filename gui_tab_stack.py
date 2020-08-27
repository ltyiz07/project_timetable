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
      self.initUI()

  def initUI(self):

      self.setWindowTitle('Timetable Maker')
      self.setWindowIcon(QIcon('lotus.png'))
      self.setGeometry(1200, 500, 500, 450)
      self.show()

class Tab(MyApp):
    def __init__(self):
        super().__init__()
        self.init()
        self.input_lectures = []
        self.radio_btn_lectures = []
        self.radio_btn_weeks = []
        self.push_btn_times = []

    def init(self):
        self.tab1 = QGroupBox()
        layout_tab1 = QGridLayout()

        self.tab1.setLayout(layout_tab1)
        self.tab2 = QGroupBox()
        self.tab3 = QGroupBox()
        self.tabs = QTabWidget()
        self.tabs.addTab(self.tab1, '수업 이름')
        self.tabs.addTab(self.tab2, '수업 시간')
        self.tabs.addTab(self.tab3, '결과...')
        vbox = QVBoxLayout()
        vbox.addWidget(self.tabs)
        self.setLayout(vbox)

# class Tab_1(QWidget):
#     def __init__(self):
#         self.layout(QGridLayout)


if __name__ == '__main__':
  app = QApplication(sys.argv)
  ex = Tab()
  sys.exit(app.exec_())
