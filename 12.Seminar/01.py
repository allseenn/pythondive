# Создайте класс-функцию, который считает факториал числа при
# вызове экземпляра.
# Экземпляр должен запоминать последние k значений.
# Параметр k передаётся при создании экземпляра.
# Добавьте метод для просмотра ранее вызываемых значений и
# их факториалов.
class Fact:
    def __init__(self, k):
        self.k = k
        self.arch = []

    def factorial(self, num):
        res = 1
        for i in range(2, num + 1):
            res *= i
        self.arch.append({num: res})
        return self.arch[-self.k:]

    def __call__(self, n):
        return self.factorial(n)


s = Fact(3)
print(s(7))
print(s(8))
print(s(5))
print(s(4))
print(s(9))
print(s(5))
print(s(3))