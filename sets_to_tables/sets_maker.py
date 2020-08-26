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
        self.time_sorted_list = []

    def matcher_1(self, input):
        if not self.class_set:      # input = first 일때 만 동작
            for l, set_1 in enumerate(input):
                self.class_set.append(set_1)
                self.class_seq.append([l])
            return
        elif input == [{}]:
            return

        # set_temp 에 self.class_set 옮기고 self.class_set 은 초기화
        set_temp = self.class_set

        # seq_temp 에 self.class_seq 옮기고 self.class_seq 은 초기화
        seq_temp = self.class_seq
        self.__init__()     # self.class_set, self.class_seq 초기화
        for m, class_set1 in enumerate(set_temp):
            for k, class_set2 in enumerate(input):
                if class_set1.isdisjoint(class_set2):
                    # SET
                    unioned_set = class_set1.union(class_set2)
                    self.class_set.append(unioned_set)
                    added_seq = seq_temp[m] + [k]
                    self.class_seq.append(added_seq)


if __name__ == '__main__':
    from sets_to_tables.tables_maker import Sort

    first = [{"mon_1", "mon_2", "mon_3"}, {"mon_4", "mon_5", "mon_6"}, {"wed_1", "wed_2", "wed_3"}]
    second = [{"mon_5", "mon_6", "mon_7"}, {"thu_2", "thu_3", "thu_4"}, {"fri_1", "fri_2", "fri_3"}]
    third = [{"mon_1", "mon_2", "mon_3", "wed_1", "wed_2", "wed_3"},
             {"tue_1", "tue_2", "tue_3", "thu_1", "thu_2", "thu_3"}]
    fourth = [{"tue_2", "tue_3"}, {"wed_2", "wed_3"}, {"thu_2", "thu_3"}]
    fifth = [{"wed_4", "wed_5", "wed_6"}, {"fri_5", "fri_6", "fri_7", "fri_9"}]

    test_1 = SetMaker()

# 다섯번 실행해줘야함... 앞으로 수정하기
    test_1.matcher_1(first)
    test_1.matcher_1(second)
    test_1.matcher_1(third)
    test_1.matcher_1(fourth)
    test_1.matcher_1(fifth)

    for j, i in enumerate(test_1.class_set):
        print(i)
        print(test_1.class_seq[j])    # 수업 시퀀스
        test_1.time_sorted_list.append(test_1.sort_with_time(i))    # 리스트에 각시간별로 분류해 정리
    print('=' * 100)

    for j, i in enumerate(test_1.time_sorted_list):    # 시간별로 정리된 시간표를 출력
        print(j + 1, '*' * 50)
        test_1.table(i)
        print(test_1.class_seq[j])
    #
    # for i in range(len(time_sorted_list)):
    #     print(i + 1, '*' * 50)
    #     print(test_1.show_list[i])

