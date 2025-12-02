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

with open("/content/input_day1.txt.txt", "r") as f:
  input_txt = f.read()

class Password:
  def __init__(self, data):
    self.start = 50
    self.current = self.start
    self.count_zeroes = 0
    self.count_zeroes2 = 0
    self.instructions = []
    self.do_data(data)
    print(self.instructions)
    # self.do_instructions()
    print(f"Password : {self.count_zeroes}")
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
      print(f"current: {self.current} -> ins : {ins}")
      if ins["instruction"] == "L":
        self.current = (self.current + -1 * ins["places"]) % 100
      else:
        self.current = (self.current + ins["places"]) % 100
      print(f"new current: {self.current}")
      if self.current == 0:
        self.count_zeroes += 1

  def do_instructions2(self):
    for ins in self.instructions:
        print(f"current: {self.current} -> ins : {ins}")
        
        places = ins["places"]
        if ins["instruction"] == "L":
            # Naar links (negatief)
            new_position = (self.current - places) % 100
            
            # Bepaal hoeveel keer 0 gepasseerd is
            # Bijvoorbeeld: van 5 naar 2 - 8 plaatsen → 5 - 8 = -3 %100 = 97
            # aantal rondes = (places - current + 99) // 100
            delta = self.current - new_position
            if delta < 0:
                delta += 100
            zero_passes = (places - delta) // 100 + 1 if places >= 100 else 1 if self.current < new_position else 0
            
            # Voor eenvoudiger: aantal keer dat we 0 overschrijden is (places + current) // 100 bij rechts en (places - current + 99) // 100 bij links, maar dit kan soms verwarrend zijn
            # Hier pakken we het simpel:
            zero_passes = (places + (100 - self.current) - 1) // 100 + 1 if places >= 100 else 1 if new_position > self.current else 0
            
            self.count_zeroes2 += zero_passes
            
            self.current = new_position
            
        else:
            # Naar rechts (positief)
            new_position = (self.current + places) % 100
            
            # Bereken hoeveel keer 0 gepasseerd
            zero_passes = (self.current + places) // 100
            
            self.count_zeroes2 += zero_passes
            self.current = new_position
        
        print(f"new current: {self.current}, zeroes counted: {self.count_zeroes2}")
        
        # Als we precies op 0 komen, tel eeen extra
        if self.current == 0:
            self.count_zeroes2 += 1 
  
# pw = Password(test_data)

pw2 = Password(input_txt.split("\n"))
