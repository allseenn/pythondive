# 3. Создайте функцию генератор чисел Фибоначчи (см. Википедию).

n = int(input('Введите длину ряда: '))

def factorial(n):
    number = 1
    for i in range(1, n + 1):
        number *= i
        yield number

for i, num in enumerate(factorial(n), start=1):
    print(f'{i}! = {num}')