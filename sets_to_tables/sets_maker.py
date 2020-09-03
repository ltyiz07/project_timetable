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

    def matcher(self, input_list, name_list):
        """

        :param input_list: 2차원 리스트 속의 1차원 셋 총 3차원
        :param name_list: 버튼 리스트
        :return:
        """
        # 수업 이름들 변환
        for n in name_list:
            if n.text():
                self.name_list.append(n.text())
        for n in name_list:
            self.name_list += (n,)
        for i in input_list:
            if i:
                self.matcher_1(i)

        for j, seq in enumerate(self.class_seq):
            self.name_time.append([])
            for num, v in enumerate(seq):
                for ele in input_list[num][v]:
                    self.name_time[j].append(f"{num}_{ele}")

        for one_table_set in self.name_time:
            self.time_sorted_list.append(self.sort_with_time(one_table_set))  # 리스트에 각시간별로 분류해 정리
        for i in self.time_sorted_list:  # 시간별로 정리된 시간표를 출력
            self.table(i)

    def matcher_1(self, input):
        if not self.class_set:      # input = first 일때 만 동작
            for l, set_1 in enumerate(input):
                self.class_set.append(set_1)
                self.class_seq.append([l])
            return
        # set_temp 에 self.class_set 옮기고 self.class_set 은 초기화
        set_temp = self.class_set
        # seq_temp 에 self.class_seq 옮기고 self.class_seq 은 초기화
        seq_temp = self.class_seq
        self.reset()     # self.class_set, self.class_seq 초기화
        for m, temp_set in enumerate(set_temp):
            for k, input_set in enumerate(input):
                if temp_set.isdisjoint(input_set):
                    # SET
                    unioned_set = temp_set.union(input_set)
                    self.class_set.append(unioned_set)
                    added_seq = seq_temp[m] + [k]
                    self.class_seq.append(added_seq)


if __name__ == '__main__':
    pass