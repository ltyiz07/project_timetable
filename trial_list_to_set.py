data_list = []
base_list = []

processed_sets = [[], [], [], [], [], [], [], [], [], []]



input_list = [0, [0, 1, 2], 0, [3, 4, 5], 0, [20, 21, 22], 1, [4, 5, 6], 1, [31, 32, 33], 1, [40, 41, 42], 2, [0, 1, 2, 20, 21, 22], 2, [10, 11, 12, 30, 31, 32], 3, [11, 12], 3, [21, 22], 3, [31, 32], 4, [23, 24, 25], 4, [44, 45, 46, 48]]

print(input_list)

# 짝수는 각각의 수업 번호
# 홀수는 수업 시간들 셋으로 분리
# 각각 base_list, data_list
for i, d in enumerate(input_list):
    if not(i % 2):
        data_list.append([])
        base_list.append(d)
        data_list[int(i / 2)] = input_list[i + 1]

print(base_list)
print(data_list)

# data_list 2차원 리스트를 리스트 에서 셋으로 변환함
for e, i in enumerate(data_list):
    data_list[e] = set(i)
print(data_list)

# 각각의 셋들을 base_list 에따라 수업 이름별로 나눔
for j, i in enumerate(base_list):
    processed_sets[i].append(data_list[j])
print(processed_sets)
