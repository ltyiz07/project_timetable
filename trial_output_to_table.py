from sets_to_tables.sets_maker import SetMaker

data_sets = [[{0, 1, 2}, {3, 4, 5}, {20, 21, 22}], [{4, 5, 6}, {32, 33, 31}, {40, 41, 42}], [{0, 1, 2, 20, 21, 22}, {32, 10, 11, 12, 30, 31}], [{11, 12}, {21, 22}, {32, 31}], [{24, 25, 23}, {48, 44, 45, 46}], [], [], [], [], []]
class_name = ["first", "second", "third", "fourth", "fifth"]
trial = SetMaker()
trial.matcher(data_sets)
print("#########################################################################")

print(trial.class_seq)
message = ""
week = 'mon', 'tue', 'wed', 'thu', 'fri'
temp_list = []
# for i, d in enumerate(data_sets):
#     for j, n in enumerate(data_sets[i]):
#         for k in data_sets[i][j]:
#             print(k)
#             temp_num_week = k // 10
#             temp_num_time = k % 10
#             temp_word = f"{week[temp_num_week]}_{temp_num_time + 1}"
#             print(temp_word)

for i, j in enumerate(trial.class_seq[0]):
    temp_dialog_message = ""
    for k in data_sets[i][j]:
        temp_num_week = k // 10
        temp_num_time = k % 10
        temp_dialog_message += f"{week[temp_num_week]}_{temp_num_time + 1} "
    message += f"{class_name[i]}: {temp_dialog_message}\n"

print(message)
