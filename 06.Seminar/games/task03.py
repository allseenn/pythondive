# Улучшаем задачу 2. 
# Добавьте возможность запуска функции “угадайки” из модуля в командной строке терминала. 
# Строка должна принимать от 1 до 3 аргументов: параметры вызова функции. 
# Для преобразования строковых аргументов командной строки в числовые параметры 
# используйте генераторное выражение.

import random as rnd
from sys import argv

def lotery(a, b, c):
    temp = rnd.randint(a, b)
    count = 0
    while count < c:
        num = int(input('Введите число:  '))
        if num == temp:
            return True
        elif num < temp:
            print('Больше')
        else:
            print('Меньше')
        count += 1
    return False



print(argv)

x_gen = (int(i) for i in argv[1:])

print(lotery(*x_gen))