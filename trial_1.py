from set_trial_3 import SetMaker
# matcher_1    =>    sort_time    =>    table


first = [{"mon_1", "mon_2", "mon_3"}, {"mon_4", "mon_5", "mon_6"}, {"wed_1", "wed_2", "wed_3"}]
second = [{"mon_5", "mon_6", "mon_7"}, {"thu_2", "thu_3", "thu_4"}, {"fri_1", "fri_2", "fri_3"}]
third = [{"mon_1", "mon_2", "mon_3", "wed_1", "wed_2", "wed_3"},
         {"tue_1", "tue_2", "tue_3", "thu_1", "thu_2", "thu_3"}]
fourth = [{"tue_2", "tue_3"}, {"wed_2", "wed_3"}, {"thu_2", "thu_3"}]
fifth = [{"wed_4", "wed_5", "wed_6"}, {"fri_5", "fri_6", "fri_7"}]


trial = SetMaker()

trial.matcher_1(first, second)
trial.matcher_1(trial.class_set, third, trial.class_seq)
trial.matcher_1(trial.class_set, fourth, trial.class_seq)
trial.matcher_1(trial.class_set, fifth, trial.class_seq)
for i in trial.class_set:
    print(i)

time_sorted_list = []
for i in trial.class_set:
    time_sorted_list.append(trial.sort_time(i))

for j, i in enumerate(time_sorted_list):
    print((j + 1), '*' * 55)
    trial.table(i)
