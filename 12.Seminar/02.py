# Доработаем задачу 1. Создайте менеджер контекста, который при выходе сохраняет значения в JSON файл.
import json


class Fact:

    def __init__(self, k):
        self.k = k
        self.arch = []

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        with open('my_file.json', 'w', encoding='utf-8') as f:
            json.dump(self.arch, f)

    def factorial(self, num):
        res = 1
        for i in range(2, num + 1):
            res *= i
        self.arch.append({num: res})
        return self.arch[-self.k:]

    def __call__(self, n):
        return self.factorial(n)


with Fact(5) as s:
    print(s(7))
    print(s(8))
    print(s(5))
    print(s(4))
    print(s(9))
    print(s(5))
    print(s(3))