class Sort:
    def __init__(self):
        pass

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
        list_time = list_time
        return list_time

    def sort_week(self, set_2):
        """
        2차원 리스트 의 수업시간표를 받아서 이를 요일순으로 정렬해준다.
        :param set_2: 하나의 시간표 (2차원 리스트)
        :return:
        """
        # 5 times iterating
        # 'i' is one of the class set
        pass
    def table(self, set_3):
        """
        2차원 리스트의 수업시간표를 받아서 테이블을 만들어줌.
        :param set_3: 하나의 시간표 (2차원 리스트)
        :return: 시간표
        """
        dash = "{0:^11}".format('-')
        first_line = "   {0:^11}{1:^11}{2:^11}{3:^11}{4:^11}".format('mon', 'tue', 'wed', 'thu', 'fri')
        print(first_line)
        for j in range(len(set_3)):
            a, b, c, d, e = dash, dash, dash, dash, dash
            for i in range(len(set_3[j])):
                if set_3[j][i][0:3] == 'mon':
                    a = "{0:^11}".format(i)
        print(a)

            # class_line_1 = "(1){0:^11}{1:^11}{2:^11}{3:^11}{4:^11}".format(a, b, c, d, e)




if __name__ == '__main__':
    set = {'thu_2', 'wed_2', 'mon_2', 'tue_1', 'tue_3', 'mon_3', 'tue_2', 'thu_3', 'wed_3', 'wed_6', 'wed_5', 'wed_4',
           'mon_6', 'mon_1', 'thu_1', 'mon_7', 'mon_5'}

    test = Sort()
    print(test.sort_time(set))
    test.table([['thu_1', 'fri_1', 'tue_1'], ['tue_2', 'wed_2', 'fri_2', 'thu_2'], ['thu_3', 'fri_3', 'tue_3', 'wed_3'], ['mon_4'], ['fri_5', 'mon_5'], ['fri_6', 'mon_6'], ['fri_7']])




# with open("table_2", 'w') as f:
#     sharp = "    #   "
#     new_line = "\n"
#     for i in range(7):
#         for j in range(5):
#             f.write(sharp)
#         f.write(new_line)