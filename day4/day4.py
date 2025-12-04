# AoC25 code day3 part 1
test_data = """..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@.""".split("\n")

input_text = None

with open("input_day4.txt", "r") as f:
  input_text = f.read().split("\n")

class Matrix:
    def __init__(self, data):
        self.dimrow = len(data[0])
        self.dimcol = len(data)
        self.grid = [["." for _ in range(self.dimcol)] for _ in range(self.dimrow)]
        self.init_grid(data)

    def init_grid(self, data):
        for col, line in enumerate(data):
            for row, c in enumerate(line):
                if c == "@":
                    self.grid[row][col] = "@"
                
    def find_neighbors(self, row, col):
        count_neig = 0
        
    
    def __str__(self):
        result = ""
        for col in range(self.dimcol):
            for row in range(self.dimrow):
                result += self.grid[row][col]
            result += "\n"
        return result        

class Paper:
    def __init__(self):
        pass

m1 = Matrix(test_data)
print(m1)

