# AoC 2025 day 1
test_data = """L68
L30
R48
L5
R60
L55
L1
L99
R14
L82""".split("\n")

input_txt = None 

with open("input_day1.txt", "r") as f:
  input_txt = f.read()

class Password:
  def __init__(self, data):
    self.start = 50
    self.current = self.start
    self.count_zeroes = 0
    self.count_zeroes2 = 0
    self.instructions = []
    self.do_data(data)
    # self.do_instructions()
    # print(f"Password : {self.count_zeroes}")
    self.do_instructions2()
    print(f"Passwords 2 :", self.count_zeroes2)

  def do_data(self, data):
    for row in data:
      ins = {
          "instruction": row[0],
          "places": int(row[1:])
      }
      self.instructions.append(ins)

  def do_instructions(self):
    for ins in self.instructions:
      if ins["instruction"] == "L":
        self.current = (self.current + -1 * ins["places"]) % 100
      else:
        self.current = (self.current + ins["places"]) % 100
      if self.current == 0:
        self.count_zeroies += 1


  def do_instructions2(self):
      for ins in self.instructions:
          places = ins["places"]
          if ins["instruction"] == "L":
              new_position = (self.current - places) % 100
 
              full_cycles = places // 100
              remainder = places % 100
              crosses_zero = (self.current - remainder) < 0

              zero_passes = full_cycles + (1 if crosses_zero else 0)
              self.count_zeroes2 += zero_passes
              self.current = new_position

          else:
              new_position = (self.current + places) % 100

              full_cycles = places // 100
              remainder = places % 100
              crosses_zero = (self.current + remainder) >= 100

              zero_passes = full_cycles + (1 if crosses_zero else 0)
              self.count_zeroes2 += zero_passes
              self.current = new_position

# pw = Password(test_data)

pw2 = Password(input_txt.split("\n"))
