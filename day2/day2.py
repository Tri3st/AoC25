# AoC 2025 day 1
test_data = """11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"""

input_txt = None

with open("/content/input_day2.txt", "r") as f:
  input_txt = f.read()


class GiftSequence:
  def __init__(self, low, high):
    if low > high:
      low, high = high, low
    self.lo = low
    self.hi = high
    self.nums = [x for x in range(self.lo, self.hi + 1)]
    self.invalids = []
    self.calculate_rng()

  def calculate_rng(self):
    for num in self.nums:
      if self.calculate_invalid_ids(num):
        self.invalids.append(num)

  def calculate_invalid_ids(self, num):
    num_str = str(num)
    length = len(num_str)
    # We want to check if the string consists of exactly 2 repetitions of a substring
    if length % 2 != 0:
        # Length must be even to be exactly two repetitions
        return False
    half = length // 2
    pattern = num_str[:half]
    if pattern * 2 == num_str:
        return True
    return False

  def get_invalids(self):
    return self.invalids

  def __str__(self):
    return f"{self.invalids}"

class GiftIDs:
  def __init__(self, data):
    self.invalid_ids = []
    self.rngs = []
    self.process_input(data)
    self.check_invalid_ids()

  def process_input(self, input_txt):
    lines = input_txt.split(",")
    for line in lines:
      rng = line.split("-")
      gs = GiftSequence(int(rng[0]), int(rng[1]))
      self.rngs.append(gs)

  def check_invalid_ids(self):
    for rng in self.rngs:
      # print(rng)
      new_rng = rng.get_invalids()
      if new_rng:
        # print(f"Found invalids in range {rng} -> {new_rng}")
        self.invalid_ids.extend(new_rng)
  
  def get_sum(self):
    return sum(self.check_invalid_ids)