# 📌Дорабатываем класс прямоугольник из прошлого семинара.
# 📌Добавьте возможность сложения и вычитания.
# 📌При этом должен создаваться новый экземпляр прямоугольника.
# 📌Складываем и вычитаем периметры, а не длинну и ширину.
# 📌При вычитании не допускайте отрицательных значений.
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


aa = Rectangle(4)
bb = Rectangle(2)
cc = aa + bb
dd = aa - bb
print(cc.perimeter())
print(f'{ dd.width = }')