        self.button_1 = QPushButton('buton', self)
        self.button_1.setCheckable(True)
        # self.button_1.toggled()
        self.button_1.clicked.connect(self.checked_1)
    def checked_1(self):
        print(self.button_1.isChecked())
# Time Table Maker
 
gui input
 
My first project solo.

듣고싶은 수업별로 시간표 셋들을 추가하면 조합가능한 모든 수업시간표들을 보여주는 프로그램



connect 로 QLineEdit 연결시키기

리스트 만든후 인풋 단어들 리스트에 추가?

알고리즘 import 한후 gui 에서 바로 사용?

## trial_1 두개의 클래스 이용해서 윈도우 새로 생성
gui_trial_grid ==>> 첫번째 윈도우 클래스에서 수업 이름 받고 이를 매개값으로
두번째 클래스에 전달.

## trial_2 TAB을 사용하여 하나의 클래스, 윈도우에 구성
두번째 탭 pushbottone들에 토글 반영하기, set button 추가하기
set button 누를 때마다 값 반영, pushbotton 토글 초기화.

두번째 탭 수업 이름들 라디오로 바꾸고 첫번째 탭에서 입력한 만큼만
만들어 보여주기...

## trial_3 QStackedWidget 을 사용하여 구성...<= 이방법이 가장 깔끔할듯...

