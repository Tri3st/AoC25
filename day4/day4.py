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
                
    def find_neighbors(self, col, row):
        count = 0

        # upper-left
        if row - 1 >= 0 and col - 1 >= 0 and self.grid[row - 1][col - 1] == "@":
            count += 1
        # upper
        if row - 1 >= 0 and self.grid[row - 1][col] == "@":
            count += 1
        # upper-right
        if row - 1 >= 0 and col + 1 < self.dimcol and self.grid[row - 1][col + 1] == "@":
            count += 1
        # left
        if col - 1 >= 0 and self.grid[row][col - 1] == "@":
            count += 1
        # right
        if col + 1 < self.dimcol and self.grid[row][col + 1] == "@":
            count += 1
        # lower-left
        if row + 1 < self.dimrow and col - 1 >= 0 and self.grid[row + 1][col - 1] == "@":
            count += 1
        # lower
        if row + 1 < self.dimrow and self.grid[row + 1][col] == "@":
            count += 1
        # lower-right
        if row + 1 < self.dimrow and col + 1 < self.dimcol and self.grid[row + 1][col + 1] == "@":
            count += 1

        return count

    def count_3s(self):
        count_3s = 0
        for col in range(self.dimcol):
            for row in range(self.dimrow):
                if self.grid[row][col] == "@" and self.find_neighbors(col, row) < 4:
                    count_3s += 1
        return count_3s

    
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

m1 = Matrix(input_text)
print(m1)
print(m1.count_3s())

