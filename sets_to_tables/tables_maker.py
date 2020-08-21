# tables_maker   파일명
# 상속에대한 위계를 반대로 부여했으면 더 좋았을듯...

class Sort:

    """
    set_trial 에서 출력한 data 를 table 에 올려줌
    """
    def __init__(self):
        # lines 리스트 내부의 리스트 갯수: 첫째줄 + N교시 = 10
        self.lines = [[], [], [], [], [], [], [], [], [], []]
        self.show = ""
        self.show_list = []

    def sort_with_time(self, set_1):
        """

        :param set_1:
        :return:
        """
        list_time = []
        for j in range(11):
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
        for i in set_1:
            if i[4] == '8':
                list_time[7].append(i)
        for i in set_1:
            if i[4] == '9':
                list_time[8].append(i)
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
        for j in range(9):
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
            self.lines[0] = str(first_line)
            self.lines[j + 1] = str(class_line)
        for i in range(10):
            self.show += str(self.lines[i]) + '\n'

        show = ""
        for i in range(10):
            show += str(self.lines[i]) + '\n'
        self.show_list.append(show)
        # print(self.lines)       # indexing 가능


if __name__ == '__main__':
    pass
