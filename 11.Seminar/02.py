# 📌Создайте класс Архив, который хранит пару свойств. Например, число и строку.
# 📌При нового экземпляра класса, старые данные из ранее созданных экземпляров сохраняются в пару списков-
# архивов list-архивы также являются свойствами экземпляра
from random import randint
class Arch:
    digits = list()
    stringi = list()
    def __init__(self):
        self.digits.append(randint(1,100))
        self.stringi.append(str(randint(1,100)))

aa = Arch()
bb = Arch()
cc = Arch()
print(cc.digits, cc.stringi)
