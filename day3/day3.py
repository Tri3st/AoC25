# AoC25 code day3 part 1
test_data = """987654321111111
811111111111119
234234234234278
818181911112111""".split("\n")

input_text = None

with open("input_day3.txt", "r") as f:
  input_text = f.readlines()


class Jolt:
    self __init__(self, index, value):
        self.index = index
        self.value = value



class Battery:
    def __init__(self, line):
        self.battery = [Jolt(i, int(x)) for i,x in enumerate(line)]

    def get_highest_2(self):
        for jolt in self.battery:
            if 
