from set_trial_3 import SetMaker

first = [{"mon_1", "mon_2", "mon_3"}, {"mon_4", "mon_5", "mon_6"}, {"wed_1", "wed_2", "wed_3"}]
second = [{"mon_5", "mon_6", "mon_7"}, {"thu_2", "thu_3", "thu_4"}, {"fri_1", "fri_2", "fri_3"}]
third = [{"mon_1", "mon_2", "mon_3", "wed_1", "wed_2", "wed_3"},
         {"tue_1", "tue_2", "tue_3", "thu_1", "thu_2", "thu_3"}]
fourth = [{"tue_2", "tue_3"}, {"wed_2", "wed_3"}, {"thu_2", "thu_3"}]
fifth = [{"wed_4", "wed_5", "wed_6"}, {"fri_5", "fri_6", "fri_7"}]


trial = SetMaker()

trial.matcher_1(first, second)
trial.matcher_1(trial.class_set, second)
trial.matcher_1(trial.class_set, third)
trial.matcher_1(trial.class_set, fourth)
trial.matcher_1(trial.class_set, fifth)
print(trial.class_set)

trial.sort_time(trial.class_set[0])44141
