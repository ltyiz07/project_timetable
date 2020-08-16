# ex)수업풀 input : """# 1. 공학_1(월1~3), 공학_2(월4~6), 공학_3(수1~3)
# 2. 수학_1(월5~7), 수학_2(목2~4), 수학_3(금1~3)
# 3. 실험_1(월1~3, 수1~3), 실험_2(화1~3, 목1~3)
# 4. 코딩_1(화2~3), 코딩_2(수2~3), 코딩_3(목2~3)
# 5. 물리_1(수4~6), 물리_2(금5~7)
# """

# 결과 변수 너무 많음 제한이나 추가 옵션 추가 필!
import time
engineering = [{"mon_1", "mon_2", "mon_3"}, {"mon_4", "mon_5", "mon_6"}, {"wed_1", "wed_2", "wed_3"}]
mathematic = [{"mon_5", "mon_6", "mon_7"}, {"thu_2", "thu_3", "thu_4"}, {"fri_1", "fri_2", "fri_3"}]
experiment = [{"mon_1", "mon_2", "mon_3", "wed_1", "wed_2", "wed_3"},
              {"tue_1", "tue_2", "tue_3", "thu_1", "thu_2", "thu_3"}]
coding = [{"tue_2", "tue_3"}, {"wed_2", "wed_3"}, {"thu_2", "thu_3"}]
physics = [{"wed_4", "wed_5", "wed_6"}, {"fri_5", "fri_6", "fri_7"}]
all_classses = [engineering, mathematic, experiment, coding, physics]

classlist = []
sequances = []
for num_eng, j in enumerate(engineering):
    for num_math, i in enumerate(mathematic):
        if j.isdisjoint(i):
            eng_math = j.union(i)
            for num_exp, k in enumerate(experiment):
                if eng_math.isdisjoint(k):
                    eng_math_exp = eng_math.union(k)
                    for num_cod, m in enumerate(coding):
                        if eng_math_exp.isdisjoint(m):
                            eng_math_exp_cod = eng_math_exp.union(m)
                            for num_phy, n in enumerate(physics):
                                if eng_math_exp_cod.isdisjoint(n):
                                    eng_math_exp_cod_phy = eng_math_exp_cod.union(n)
                                    classlist.append(eng_math_exp_cod_phy)
                                    sequances = [num_eng, num_math, num_exp, num_cod, num_phy]
                                    print(sequances)


print(len(classlist), classlist)

print('=' * 50)
for i in range(len(classlist)):
    print(i + 1, classlist[i])
