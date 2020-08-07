# ex)수업풀 input : """
# 1. 공학_1(월1~3), 공학_2(월4~6), 공학_3(수1~3)
# 2. 수학_1(월5~7), 수학_2(목2~4), 수학_3(금1~3)
# 3. 실험_1(월1~3, 수1~3), 실험_2(화1~3, 목1~3)
# 4. 코딩_1(화2~3), 코딩_2(수2~3), 코딩_3(목2~3)
# 5. 물리_1(수4~6), 물리_2(금5~7)
# """

engineering = [{"mon_1", "mon_2", "mon_3"}, {"mon_4", "mon_5", "mon_6"}, {"wed_1", "wed_2", "wed_3"}]
mathematic = [{"mon_5", "mon_6", "mon_7"}, {"thu_2", "thu_3", "thu_4"}, {"fri_1", "fri_2", "fri_3"}]
experiment = [{"mon_1", "mon_2", "mon_3", "wed_1", "wed_2", "wed_3"},
              {"tue_1", "tue_2", "tue_3", "thu_1", "thu_2", "thu_3"}]
coding = [{"tue_2", "tue_3"}, {"wed_2", "wed_3"}, {"thu_2", "thu_3"}]
physics = [{"wed_4", "wed_5", "wed_6"}, {"fri_5", "fri_6", "fri_7"}]

for i in mathematic:
    if engineering[0].isdisjoint(i):
        print(i)