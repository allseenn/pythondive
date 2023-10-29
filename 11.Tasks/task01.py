import datetime

class MyStr(str):
        
    def __new__(cls, value, author):
        instance = super().__new__(cls, value)
        instance.value = value
        instance.author = author
        instance.time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M')
        return instance
    
    def __str__(self):
        return f'{self.value} (Автор: {self.author}, Время создания: {self.time})'
    
    def __repr__(self):
        return f"MyStr('{self.value}', '{self.author}')"
    

my_string = MyStr("Мама мыла раму", "Маршак")
print(my_string)
print(repr(my_string))
