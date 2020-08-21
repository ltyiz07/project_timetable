# set_trial_3
"""
set_trial.py 의 결과와 동일함
sequence 알아낼 방법 찾기 ==>> 해결함
sequence 알아내는 과정에서 함수기능 지저분해짐 통일시키는 방법찾기 ==>> 해결함
"""
from sets_to_tables.tables_maker import Sort

class SetMaker(Sort):
    def __init__(self):
        super().__init__()
        self.class_seq = []
        self.class_set = []

    def matcher_1(self, before, after, seq=[]):
        self.__init__() # 불러올때마다 초기화
        for k, class_set1 in enumerate(before):
            for m, class_set2 in enumerate(after):
                if class_set1.isdisjoint(class_set2):
                    # SET
                    added_class = class_set1.union(class_set2)
                    self.class_set.append(added_class)
                    # SEQUENCE
                    if not seq:
                        added_seq = [k, m]
                        self.class_seq.append(added_seq)
                    else:
                        added_seq = seq[k] + [m]
                        self.class_seq.append(added_seq)


if __name__ == '__main__':
    from sets_to_tables.tables_maker import Sort

    first = [{"mon_1", "mon_2", "mon_3"}, {"mon_4", "mon_5", "mon_6"}, {"wed_1", "wed_2", "wed_3"}]
    second = [{"mon_5", "mon_6", "mon_7"}, {"thu_2", "thu_3", "thu_4"}, {"fri_1", "fri_2", "fri_3"}]
    third = [{"mon_1", "mon_2", "mon_3", "wed_1", "wed_2", "wed_3"},
             {"tue_1", "tue_2", "tue_3", "thu_1", "thu_2", "thu_3"}]
    fourth = [{"tue_2", "tue_3"}, {"wed_2", "wed_3"}, {"thu_2", "thu_3"}]
    fifth = [{"wed_4", "wed_5", "wed_6"}, {"fri_5", "fri_6", "fri_7"}]

# 다섯번 실행해줘야함... 앞으로 수정하기
    test_1 = SetMaker()
    test_1.matcher_1(first, second)
    test_1.matcher_1(test_1.class_set, third, test_1.class_seq)
    test_1.matcher_1(test_1.class_set, fourth, test_1.class_seq)
    test_1.matcher_1(test_1.class_set, fifth, test_1.class_seq)
    print('=' * 100)

    trial_1 = Sort()
    time_sorted_list = []
    for j, i in enumerate(test_1.class_set):
        print(test_1.class_seq[j])    # 수업 시퀀스
        print(i)
        time_sorted_list.append(trial_1.sort_time(i))    # 리스트에 각시간별로 분류해 정리
    print('=' * 100)


    for i in time_sorted_list:    # 시간별로 정리된 시간표를 출력
        trial_1.table(i)