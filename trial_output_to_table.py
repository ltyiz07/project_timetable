from sets_to_tables.sets_maker import SetMaker

data_sets = [[{0, 1, 2}, {3, 4, 5}, {20, 21, 22}], [{4, 5, 6}, {32, 33, 31}, {40, 41, 42}], [{0, 1, 2, 20, 21, 22}, {32, 10, 11, 12, 30, 31}], [{11, 12}, {21, 22}, {32, 31}], [{24, 25, 23}, {48, 44, 45, 46}], [], [], [], [], []]

trial = SetMaker()
trial.matcher(data_sets)
print("#########################################################################")
for l in trial.lines:
    print(l)
print(len(trial.lines))