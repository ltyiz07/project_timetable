first = [{"a_1", "a_2", "a_3"}, {"a_4", "a_5", "a_6"}, {"c_1", "c_2", "c_3"}]
second = [{"a_5", "a_6", "a_7"}, {"d_2", "d_3", "d_4"}, {"e_1", "e_2", "e_3"}]
third = [{"a_1", "a_2", "a_3", "c_1", "c_2", "c_3"},
         {"b_1", "b_2", "b_3", "d_1", "d_2", "d_3"}]
fourth = [{"b_2", "b_3"}, {"c_2", "c_3"}, {"d_2", "d_3"}]
fifth = [{"c_4", "c_5", "c_6"}, {"e_5", "e_6", "e_7"}]

# set_trial.py 의 결과와 동일함
# sequence 알아낼 방법 찾기


class SetMaker:
    def __init__(self):
        self.class_seq = []
        self.class_set = []

    def matcher(self, before, after):
        self.__init__()
        for i, class_set1 in enumerate(before):
            for j, class_set2 in enumerate(after):
                if class_set1.isdisjoint(class_set2):
                    added_class = class_set1.union(class_set2)
                    added_seq = seq[i].append(j)
                    self.class_set.append(added_class)
                    self.class_seq.append(added_seq)



if __name__ == '__main__':
    first = [{"mon_1", "mon_2", "mon_3"}, {"mon_4", "mon_5", "mon_6"}, {"wed_1", "wed_2", "wed_3"}]
    second = [{"mon_5", "mon_6", "mon_7"}, {"thu_2", "thu_3", "thu_4"}, {"fri_1", "fri_2", "fri_3"}]
    third = [{"mon_1", "mon_2", "mon_3", "wed_1", "wed_2", "wed_3"},
             {"tue_1", "tue_2", "tue_3", "thu_1", "thu_2", "thu_3"}]
    fourth = [{"tue_2", "tue_3"}, {"wed_2", "wed_3"}, {"thu_2", "thu_3"}]
    fifth = [{"wed_4", "wed_5", "wed_6"}, {"fri_5", "fri_6", "fri_7"}]
    class_list = [first, second, third, fourth, fifth]

    test_1 = SetMaker()
    test_1.matcher(first, second, seq = [])
    print(test_1.class_set)
    print(test_1.class_seq)
    # test_1.matcher(test_1.class_set, third)
    # test_1.matcher(test_1.class_set, fourth)
    # test_1.matcher(test_1.class_set, fifth)
