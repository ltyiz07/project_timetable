data_list = []
base_list = []
processed_sets = [[], [], [], [], [], [], [], [], [], []]



input_list = [0, [0, 1, 2], 0, [3, 4, 5], 0, [20, 21, 22], 1, [4, 5, 6], 1, [31, 32, 33], 1, [40, 41, 42], 2, [0, 1, 2, 20, 21, 22], 2, [10, 11, 12, 30, 31, 32], 3, [11, 12], 3, [21, 22], 3, [31, 32], 4, [23, 24, 25], 4, [44, 45, 46, 48]]

for i, d in enumerate(input_list):
    if i % 2 == 0:
        data_list.append([])
        base_list.append(d)
print(base_list)

for i, d in enumerate(input_list):
    if i % 2 == 0:
        data_list[int(i / 2)] = input_list[i + 1]

print(data_list)

data_list[0] = set((data_list[0]))
for e, i in enumerate(data_list):
    data_list[e] = set((i))

print(data_list)
for j, i in enumerate(base_list):
    processed_sets[i].append(data_list[j])
print(processed_sets)
