class Sort:
    """
    set_trial 에서 출력한 data 를 table 에 올려줌
    """
    def __init__(self):
        self.lines = [[],[],[],[],[],[],[]]

    def sort_time(self, set_1):
        """

        :param set_1:
        :return:
        """
        list_time = []
        for j in range(7):
            list_time.append([])
        for i in set_1:
            if i[4] == '1':
                list_time[0].append(i)
        for i in set_1:
            if i[4] == '2':
                list_time[1].append(i)
        for i in set_1:
            if i[4] == '3':
                list_time[2].append(i)
        for i in set_1:
            if i[4] == '4':
                list_time[3].append(i)
        for i in set_1:
            if i[4] == '5':
                list_time[4].append(i)
        for i in set_1:
            if i[4] == '6':
                list_time[5].append(i)
        for i in set_1:
            if i[4] == '7':
                list_time[6].append(i)
        return list_time

    def table(self, set_3):
        """
                2차원 리스트의 수업시간표를 받아서 테이블을 만들어줌.
                :param set_3: 하나의 시간표 (2차원 리스트)
                :return: ...
                """
        dash = "{0:^11}".format('-')
        first_line = "   {0:^11}{1:^11}{2:^11}{3:^11}{4:^11}".format('mon', 'tue', 'wed', 'thu', 'fri')
        print(first_line)
        for j in range(7):
            a, b, c, d, e = dash, dash, dash, dash, dash
            for i in range(len(set_3[j])):
                if set_3[j][i][0:3] == 'mon':
                    a = "{0:^11}".format(set_3[j][i])
                if set_3[j][i][0:3] == 'tue':
                    b = "{0:^11}".format(set_3[j][i])
                if set_3[j][i][0:3] == 'wed':
                    c = "{0:^11}".format(set_3[j][i])
                if set_3[j][i][0:3] == 'thu':
                    d = "{0:^11}".format(set_3[j][i])
                if set_3[j][i][0:3] == 'fri':
                    e = "{0:^11}".format(set_3[j][i])
            class_line = "({0}){1:^11}{2:^11}{3:^11}{4:^11}{5:^11}".format(j + 1, a, b, c, d, e)
            print(class_line)
            self.lines[j] = class_line
        print(self.lines)       # indexing 가능


if __name__ == '__main__':
    set_1 = {'thu_2', 'wed_2', 'mon_2', 'tue_1', 'tue_3', 'mon_3', 'tue_2', 'thu_3', 'wed_3', 'wed_6', 'wed_5', 'wed_4',
           'mon_6', 'mon_1', 'thu_1', 'mon_7', 'mon_5'}

    test = Sort()
    print(test.sort_time(set_1))
    test.table([['thu_1', 'fri_1', 'tue_1'], ['tue_2', 'wed_2', 'fri_2', 'thu_2'], ['thu_3', 'fri_3', 'tue_3', 'wed_3'], ['mon_4'], ['fri_5', 'mon_5'], ['fri_6', 'mon_6'], ['fri_7']])
