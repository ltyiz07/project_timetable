class TimeTable:
    def __init__(self):
        self.dash = "    -    "
        self.new_line = "\n"
        self.sharp = "    #    "

    def generate(self):
        with open("table.txt", 'w') as f:
            first_line = "    mon      tue      wed      thu      fri  \n"
            f.write(first_line)
            for i in range(7):
                time_stamp = str(i + 1)
                f.write(time_stamp)
                for j in range(5):
                    f.write(self.dash)
                f.write(self.new_line)

    def label(self, all_set):
        for set in all_set:
            pass

test = TimeTable()
test.generate()