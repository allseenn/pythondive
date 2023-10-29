# Доработаем класс Архив из задачи 2.
# 📌Добавьте методы представления экземпляра для программиста
# и для пользователя.

from random import randint
class Arch:
    """
    Arch - store all atrib info generated before
    digits - store digits
    stringi - stringi
    """
    digits = list()
    stringi = list()

    def __init__(self):
        self.digits.append(randint(1, 100))
        self.stringi.append(str(randint(1, 100)))

    def __str__(self):
        return 'digits: ' + ' '.join(str(i) for i in self.digits) + ' stringi: ' + ' '.join(self.stringi)

    def __repr__(self):
        return f'Arch()'


aa = Arch()
bb = Arch()
print(f'{aa = } ')
print(f'{aa}')