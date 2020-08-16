class Sort:
    def __init__(self):
        self.list_time = []
    def sort_time(self, set):
        for j in range(7):
            self.list_time.append([])
        for i in set:
            if i[4] == '1':
                self.list_time[0].append(i)
        for i in set:
            if i[4] == '2':
                self.list_time[1].append(i)
        for i in set:
            if i[4] == '3':\

                self.list_time[2].append(i)
        for i in set:
            if i[4] == '4':
                self.list_time[3].append(i)
        for i in set:
            if i[4] == '5':
                self.list_time[4].append(i)
        for i in set:
            if i[4] == '6':
                self.list_time[5].append(i)
        for i in set:
            if i[4] == '7':
                self.list_time[6].append(i)
        return self.list_time
if __name__ == '__main__':
    set = {'thu_2', 'wed_2', 'mon_2', 'tue_1', 'tue_3', 'mon_3', 'tue_2', 'thu_3', 'wed_3', 'wed_6', 'wed_5', 'wed_4',
           'mon_6', 'mon_1', 'thu_1', 'mon_7', 'mon_5'}

    test = Sort()
    test.sort_time(set)
    print(test.list_time)




# with open("table_2", 'w') as f:
#     sharp = "    #   "
#     new_line = "\n"
#     for i in range(7):
#         for j in range(5):
#             f.write(sharp)
#         f.write(new_line)