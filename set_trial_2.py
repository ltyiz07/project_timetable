# ex)수업풀 input : """
# 1. 공학_1(월1~3), 공학_2(월4~6), 공학_3(수1~3)
# 2. 수학_1(월5~7), 수학_2(목2~4), 수학_3(금1~3)
# 3. 실험_1(월1~3, 수1~3), 실험_2(화1~3, 목1~3)
# 4. 코딩_1(화2~3), 코딩_2(수2~3), 코딩_3(목2~3)
# 5. 물리_1(수4~6), 물리_2(금5~7)
# """

# 결과 변수 너무 많음 제한이나 추가 옵션 추가 필!
pick_1 = [{"mon_1", "mon_2", "mon_3"}, {"mon_4", "mon_5", "mon_6"}, {"wed_1", "wed_2", "wed_3"}]
pick_2 = [{"mon_5", "mon_6", "mon_7"}, {"thu_2", "thu_3", "thu_4"}, {"fri_1", "fri_2", "fri_3"}]
pick_3 = [{"mon_1", "mon_2", "mon_3", "wed_1", "wed_2", "wed_3"},
          {"tue_1", "tue_2", "tue_3", "thu_1", "thu_2", "thu_3"}]
pick_4 = [{"tue_2", "tue_3"}, {"wed_2", "wed_3"}, {"thu_2", "thu_3"}]
pick_5 = [{"wed_4", "wed_5", "wed_6"}, {"fri_5", "fri_6", "fri_7"}]

classlist = []
sequances = []
class_union = {}
for num_eng, j in enumerate(pick_1):
    class_union.clear()
    print("first", class_union)
    for num_math, i in enumerate(pick_2):
        if j.isdisjoint(i):
            class_union = j.union(i)
            print("second", num_eng, num_math, class_union)
        for num_exp, k in enumerate(pick_3):
            if class_union.isdisjoint(k):
                class_union = class_union.union(k)
                for num_cod, m in enumerate(pick_4):
                    if class_union.isdisjoint(m):
                        class_union = class_union.union(m)
                        for num_phy, n in enumerate(pick_5):
                            if class_union.isdisjoint(n):
                                class_union = class_union.union(n)
                                classlist.append(class_union)
                                sequances = [num_eng, num_math, num_exp, num_cod, num_phy]
                                print(sequances)


print(len(classlist), classlist)
print('=' * 50)
for i in range(len(classlist)):
    print(i + 1, classlist[i])