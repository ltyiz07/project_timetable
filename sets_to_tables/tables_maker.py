# tables_maker   파일명
# 상속에대한 위계를 반대로 부여했으면 더 좋았을듯...

class Sort:

    """
    set_trial 에서 출력한 data 를 table 에 올려줌
    """
    def __init__(self):
        # lines 리스트 내부의 리스트 갯수: 첫째줄 + N교시 = 10
        # 10 교시 위해 한줄 더 추가하기
        self.lines = []
        self.show = ""
        self.time_sorted_list = []
        self.show_list = []
        self.class_seq = []
        self.class_set = []
        self.time_sorted_list = []
        self.name_time = []
        self.input_list = []
        self.name_list = []

    def reset(self):
        self.class_seq = []
        self.class_set = []

    def sort_with_time(self, set_1):
        """

        :param set_1:
        :return:
        """
        list_time = []
        for j in range(10):
            list_time.append([])

        for i in set_1:
            if int(i[2:]) % 10 == 0:
                list_time[0].append(i)
        for i in set_1:
            if int(i[2:]) % 10 == 1:
                list_time[1].append(i)
        for i in set_1:
            if int(i[2:]) % 10 == 2:
                list_time[2].append(i)
        for i in set_1:
            if int(i[2:]) % 10 == 3:
                list_time[3].append(i)
        for i in set_1:
            if int(i[2:]) % 10 == 4:
                list_time[4].append(i)
        for i in set_1:
            if int(i[2:]) % 10 == 5:
                list_time[5].append(i)
        for i in set_1:
            if int(i[2:]) % 10 == 6:
                list_time[6].append(i)
        for i in set_1:
            if int(i[2:]) % 10 == 7:
                list_time[7].append(i)
        for i in set_1:
            if int(i[2:]) % 10 == 8:
                list_time[8].append(i)
        for i in set_1:
            if int(i[2:]) % 10 == 9:
                list_time[9].append(i)
        return list_time

    def table(self, set_3):
        """
                2차원 리스트의 수업시간표를 받아서 테이블을 만들어줌.
                :param set_3: 하나의 시간표 (2차원 리스트)
                :return: ...
                """
        # 한글 시간표 출력
        if ord('가') <= ord(self.name_list[0][0]) <= ord('힣'):
            dash = "{0:^12}".format('-')
            first_line = "     {0:^12}{1:^12}{2:^12}{3:^12}{4:^12}".format('mon', 'tue', 'wed', 'thu', 'fri')
            self.lines.append(str(first_line))
            for j in range(10):
                a, b, c, d, e = dash, dash, dash, dash, dash
                for i in set_3[j]:
                    length = len(self.name_list[int(i[0])][:5])
                    print(length)
                    x = 12 - (2 * length)
                    if int(i[2:]) // 10 == 0:
                        a = f"{self.name_list[int(i[0])][:5]}"
                    if int(i[2:]) // 10 == 1:
                        b = f"{self.name_list[int(i[0])][:5]}"
                    if int(i[2:]) // 10 == 2:
                        c = f"{self.name_list[int(i[0])][:5]}"
                    if int(i[2:]) // 10 == 3:
                        d = f"{self.name_list[int(i[0])][:5]}"
                    if int(i[2:]) // 10 == 4:
                        e = f"{self.name_list[int(i[0])][:5]}"
                class_line = "({0:^3}){1:^x}{2:^x}{3:^x}{4:^x}{5:^x}".format(j + 1, a, b, c, d, e)
                self.lines.append(str(class_line))
            for i in range(11):
                self.show += str(self.lines[i]) + '\n'
        # 영어시간표 출력
        elif ord('a') <= ord(self.name_list[0][0].lower()) <= ord('z'):
            dash = "{0:^11}".format('-')
            first_line = "     {0:^11}{1:^11}{2:^11}{3:^11}{4:^11}".format('mon', 'tue', 'wed', 'thu', 'fri')
            self.lines.append(str(first_line))
            for j in range(10):
                a, b, c, d, e = dash, dash, dash, dash, dash
                for i in set_3[j]:
                    if int(i[2:]) // 10 == 0:
                        a = f"{self.name_list[int(i[0])][:7]}"
                    if int(i[2:]) // 10 == 1:
                        b = f"{self.name_list[int(i[0])][:7]}"
                    if int(i[2:]) // 10 == 2:
                        c = f"{self.name_list[int(i[0])][:7]}"
                    if int(i[2:]) // 10 == 3:
                        d = f"{self.name_list[int(i[0])][:7]}"
                    if int(i[2:]) // 10 == 4:
                        e = f"{self.name_list[int(i[0])][:7]}"
                class_line = "({0:^3}){1:^11}{2:^11}{3:^11}{4:^11}{5:^11}".format(j + 1, a, b, c, d, e)
                self.lines.append(str(class_line))
            for i in range(11):
                self.show += str(self.lines[i]) + '\n'

        show = ""
        for i in range(10):
            show += str(self.lines[i]) + '\n'
        self.show_list.append(show)     #


if __name__ == '__main__':
    pass
