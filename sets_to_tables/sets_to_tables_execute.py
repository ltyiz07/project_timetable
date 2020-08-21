from sets_to_tables.sets_maker import SetMaker
# matcher_1    =>    sort_time    =>    table
# 수업 갯수 10개, 시간 9교시까지 확장

# example sets
class_input_1 = [{"mon_1", "mon_2", "mon_3"}, {"mon_4", "mon_5", "mon_6"}, {"wed_1", "wed_2", "wed_3"}]
class_input_2 = [{"mon_5", "mon_6", "mon_7"}, {"thu_2", "thu_3", "thu_4"}, {"fri_1", "fri_2", "fri_3"}]
class_input_3 = [{"mon_1", "mon_2", "mon_3", "wed_1", "wed_2", "wed_3"},
                 {"tue_1", "tue_2", "tue_3", "thu_1", "thu_2", "thu_3"}]
class_input_4 = [{"tue_2", "tue_3"}, {"wed_2", "wed_3"}, {"thu_2", "thu_3"}]
class_input_5 = [{"wed_4", "wed_5", "wed_6"}, {"fri_5", "fri_6", "fri_7", "fri_9"}]
class_input_6 = [{}]
class_input_7 = [{}]
class_input_8 = [{}]
class_input_9 = [{}]
class_input_10 = [{}]

trial = SetMaker()

trial.matcher_1(class_input_1, class_input_2)
trial.matcher_1(trial.class_set, class_input_3, trial.class_seq)
trial.matcher_1(trial.class_set, class_input_4, trial.class_seq)
trial.matcher_1(trial.class_set, class_input_5, trial.class_seq)
trial.matcher_1(trial.class_set, class_input_6, trial.class_seq)
trial.matcher_1(trial.class_set, class_input_7, trial.class_seq)
trial.matcher_1(trial.class_set, class_input_8, trial.class_seq)
trial.matcher_1(trial.class_set, class_input_9, trial.class_seq)
trial.matcher_1(trial.class_set, class_input_10, trial.class_seq)

time_sorted_list = []
for i in trial.class_set:
    time_sorted_list.append(trial.sort_with_time(i))

# 출력
# for j, i in enumerate(time_sorted_list):
#     print((j + 1), '*' * 55)
#     trial.table(i)
#     print(trial.class_seq[j])
for i in time_sorted_list:
    trial.table(i)

print('=' * 100)
# show = ""
# for i in range(10):
#     show = show + trial.lines[i] + '\n'

for i in range(len(time_sorted_list)):
    print(i + 1, '*' * 50)
    print(trial.show_list[i])
