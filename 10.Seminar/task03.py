# Напишите класс для хранения информации о человеке: ФИО, возраст и т.п. на ваш выбор. 
# У класса должны быть методы birthday для увеличения возраста на год, 
# full_name для вывода полного ФИО и т.п. на ваш выбор. 
# Убедитесь, что свойство возраст недоступно для прямого изменения, но есть возможность получить текущий возраст.
class Person:

    def __init__(self, name, surname, father_name, age, sex):
        self._age = age
        self.name = name
        self.surname = surname
        self.father_name = father_name
        self.sex = sex

    def birthday(self):
        self._age += 1

    def full_name(self):
        return (f'ФИО = {self.surname} {self.name} {self.father_name} Пол = {self.sex} Возраст ={self._age}')
    
p1 = Person('Иван', 'Ivanov', 'Ivanovich', 30, 'M')
p2 = Person('Maria', 'Sergeevna', 'Sergeeva', 20, 'F')
print(p1.full_name())
p1.birthday()
print(p1.full_name())
print(p2.full_name())