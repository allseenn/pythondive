# Задание No1
# 📌 Создайте класс окружность.
# 📌 Класс должен принимать радиус окружности при создании
# экземпляра.
# 📌 У класса должно быть два метода, возвращающие длину
# окружности и её площадь
from math import pi

class Okr:
    def __init__(self, rad=1):
        self.rad = rad

    def circle(self):
        return 2 * pi * self.rad

    def square(self):
        return pi * self.rad**2


o = Okr(4)
print(round(o.circle(), 2))
print(round(o.square(), 2))

