from sets_to_tables.sets_maker import SetMaker
# matcher_1    =>    sort_time    =>    table
# 수업 갯수 10개, 시간 9교시까지 확장

# example sets
class_input = []
for i in range(10):
    class_input.append([])

class_input[0] = [{"mon_1", "mon_2", "mon_3"}, {"mon_4", "mon_5", "mon_6"}, {"wed_1", "wed_2", "wed_3"}]
class_input[1] = [{"mon_5", "mon_6", "mon_7"}, {"thu_2", "thu_3", "thu_4"}, {"fri_1", "fri_2", "fri_3"}]
class_input[2] = [{"mon_1", "mon_2", "mon_3", "wed_1", "wed_2", "wed_3"},
                  {"tue_1", "tue_2", "tue_3", "thu_1", "thu_2", "thu_3"}]
class_input[3] = [{"tue_2", "tue_3"}, {"wed_2", "wed_3"}, {"thu_2", "thu_3"}]
class_input[4] = [{"wed_4", "wed_5", "wed_6"}, {"fri_5", "fri_6", "fri_7", "fri_9"}]
class_input[5] = []
class_input[6] = []
class_input[7] = []
class_input[8] = []
class_input[9] = []


trial = SetMaker()
trial.matcher(class_input)

for i in trial.class_set:
    trial.time_sorted_list.append(trial.sort_with_time(i))

for i in trial.time_sorted_list:
    trial.table(i)

print('=' * 100)

for j, i in enumerate(trial.time_sorted_list):
    print(j + 1, '*' * 50)
    trial.table(i)
    print(trial.class_seq[j])
