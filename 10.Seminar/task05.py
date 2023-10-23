# Создайте три (или более) отдельных классов животных. Например рыбы, птицы и т.п. 
# У каждого класса должны быть как общие свойства, например имя, так и специфичные для класса. 
# Для каждого класса создайте метод, выводящий информацию специфичную для данного класса.
# Доработайте задачу 5. 
# Вынесите общие свойства и методы классов в класс Животное. 
# Остальные классы наследуйте от него. 
# Убедитесь, что в созданные ранее классы внесены правки.
class Animal:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    def my_print(self):
        return (f'{self.name} {self.age} {self.weight}')

class Cat(Animal):
    def __init__(self, name, age, weight, breed):
        super().__init__(name, age, weight)
        self.breed = breed

    def my_print(self):
        return (f'{super().my_print()} {self.breed}')
        
class Birth(Animal):
    def __init__(self, name, age, weight, len_wings):
        super().__init__(name, age, weight)
        self.len_wings = len_wings

    def my_print(self):
        return (f'{super().my_print()} {self.len_wings}')
    
cat1 = Cat('Barsik', 4, 8, 'Siamsk')
birth1 = Birth('Chizhik', 2, 15, 2)

print(cat1.my_print())
print(birth1.my_print())