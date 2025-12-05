# AoC25 code day3 part 1
test_data = """3-5
10-14
16-20
12-18

1
5
8
11
17
32""".split("\n\n")

input_text = None

with open("input_day5.txt", "r") as f:
  input_text = f.read().split("\n\n")


class Product:
    def __init__(self, value) -> None:
        self.value = value
        self.checked = False
        self.fresh = None

    def is_in_range(self, product_range):
        in_range = self.value >= product_range.min and self.value <= product_range.max
        if in_range:
            product_range.checked = True
        return in_range 

    def check_range(self, product_range):
        self.fresh = self.is_in_range(product_range)
        self.checked = True   

    def __str__(self) -> str:
        return f"{self.value} {'fresh' if self.fresh else 'rotten'} {'V' if self.checked else 'X'}"

class ProdRange:
    def __init__(self, min, max):
        self.min = min
        self.max = max
        self.checked = False

    def is_in_range(self, product: Product):
        in_range = product.value >= self.min and product.value <= self.max
        if in_range:
            self.checked = True
        return in_range
    
    def __str__(self) -> str:
        return f"{self.min}-{self.max} ({'V' if self.checked else 'X'})"

class Storage:
    def __init__(self, data) -> None:
       self.products = []
       self.ranges = []
       self.count_fresh = 0
       self.new_count_fresh = 0
       self.process_data(data[0].split("\n"), data[1].split("\n"))
       self.count_fresh_products()
       self.new_count_fresh_products()

    def process_data(self, ranges, products):
        for r in ranges:
            self.ranges.append(ProdRange(int(r.split("-")[0]), int(r.split("-")[1])))
        for p in products:
            self.products.append(Product(int(p)))

    def count_fresh_products(self):
        for p in self.products:
            p.checked = True
            for r in self.ranges:
                if r.is_in_range(p):
                    p.fresh = True
        for p in self.products:
            if p.fresh:
                self.count_fresh += 1
        
    def new_count_fresh_products(self):
        for r in self.ranges:
            if r.checked == True:
                self.new_count_fresh += r.max - r.min + 1


    def __str__(self) -> str:
        result = "Ranges:\n"
        for r in self.ranges:
            result += f"{r}\n"
        result += "\nProducts:\n"
        for p in self.products:
            result += f"{p}\n"
        result += f"# of fresh products: {self.count_fresh}\n"
        result += f"NEW # of fresh products: {self.new_count_fresh}\n"
        return result
        
st = Storage(input_text)
print(st)
