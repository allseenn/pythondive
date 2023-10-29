# Доработайте прошлую задачу.
# Добавьте сравнение прямоугольников по площади
# Должны работать все шесть операций сравнения

class Rectangle():
    def __init__(self, len_rec, width=None):
        self.len_rec = len_rec
        if width is None:
            self.width = len_rec
        else:
            self.width = width
    def perimeter(self):
        return 2 * (self.len_rec + self.width)
    def square(self):
        return self.len_rec * self.width
    def __add__(self, other):
        perimeter = self.perimeter() + other.perimeter()
        return Rectangle(perimeter/4)
    def __sub__(self, other):
        perimeter = abs(self.perimeter() - other.perimeter())
        return Rectangle(perimeter/4)
    def __eq__(self, other):
        return self.perimeter() == other.perimeter()

    def __lt__(self, other):
        return self.perimeter() < other.perimeter()



aa = Rectangle(4)
bb = Rectangle(2)
cc = aa + bb
dd = aa - bb
print(f'{cc.perimeter()} < {dd.perimeter()}')
print(cc > dd)

