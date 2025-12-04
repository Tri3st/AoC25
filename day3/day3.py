# AoC25 code day3 part 1
test_data = """987654321111111
811111111111119
234234234234278
818181911112111""".split("\n")

input_text = None

with open("input_day3.txt", "r") as f:
  input_text = f.read().split("\n")



class Jolt:
    def __init__(self, index, value):
        self.value = value
        self.index = index
  
    def is_bigger_than(self, jolt):
        if self.value > jolt.value:
            return True
        return False 


class Battery:
    def __init__(self, line):
        self.battery = [Jolt(i, int(x)) for i,x in enumerate(line)]
        self.joltage = self.get_highest_2()

    def get_highest_2(self):
        lst = self.battery.copy()
        highest = -1
        for i in range(len(lst)):
            for j in range(i+1, len(lst)):
                if int(f"{lst[i].value}{lst[j].value}") > highest:
                    highest = int(f"{lst[i].value}{lst[j].value}")
        return highest

    def get_highest_12(self):
        pass
      
    def __str__(self):
        return "".join([str(x.value) for x in self.battery])

class Batteries:
    def __init__(self,data):
        print(data)
        self.batteries = [Battery(x) for x in data]
        self.joltages = [b.joltage for b in self.batteries]
        self.total_sum = sum(self.joltages)

    def __str__(self):
        result = ""
        for i in range(len(self.batteries)):
            result += f"{i} {self.batteries[i]} -> jolt: {self.batteries[i].joltage}\n"
        return result

bs = Batteries(input_text)
print(bs)
print(bs.total_sum)

