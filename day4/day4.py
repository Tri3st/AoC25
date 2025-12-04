test_data = """..xx.xx@x.
x@@.@.@.@@
@@@@@.x.@@
@.@@@@..@.
x@.@@@@.@x
.@@@@@@@.@
.@.@.@.@@@
x.@@@.@@@@
.@@@@@@@@.
x.x.@@@.x.""".split("\n")

input_text = None

with open("input_day4.txt", "r") as f:
  input_text = f.read().split("\n")

class Paper:
    def __init__(self):
        self.matrix = i
