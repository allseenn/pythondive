# Доработаем задачи 3 и 4. Создайте класс проекта, который имеет следующие методы: 
# загрузка данных (функция из задания 4)
# вход в систему - требует указать имя и id пользователя. Для проверки наличия пользователя в множестве используйте магический метод проверки на равенство пользователей. Если такого пользователя нет, вызывайте исключение доступа. А если пользователь есть, получите его уровень из множества пользователей.
# добавление пользователя. Если уровень пользователя меньше, чем ваш уровень, вызывайте исключение уровня доступа.
from sem13_task3 import LevelExetion, AccessExeption

import json


class User:
    def __init__(self, name, level, user_id):
        self.name = name
        self.level = level
        self.user_id = user_id
    
    def __repr__(self) -> str:
        return f'User({self.name}, {self.level}, {self.user_id})'
    
    def __eq__(self, other):
        if self.name == other.name and self.user_id == other.user_id:
            return True
        else:
            return False
        
    def __hash__(self) -> int:
        return hash((self.name, self.user_id))
 

class ProjectUser:
    def __init__(self):
        self.users = set()
        self.user = None


    def my_json(self):
        with open('new_file.json', 'r', encoding='utf=8') as f:
            my_dict = json.load(f)      

        for level, value in my_dict.items():
            for user_id, user_name in value.items():
                new_user = User(user_name, level, user_id)
                self.users.add(new_user)
        return f'{self.users}'
    
    def login_2_sys(self, name, user_id):
        local_user = User(name, None, user_id)
        if local_user in self.users:
            # self.user = local_user
            for user in self.users:
                if user == local_user:
                    self.user = user
        else:
            raise AccessExeption
  
    def add_user(self, name, level, user_id):

        if self.user is not None and self.user.level < level:
            self.users.add(User(name, level, user_id))
        else:
            raise LevelExetion
     
        
p1 = ProjectUser()
p1.my_json()
p1.login_2_sys('Ann', '12')
p1.add_user('Pit', '0', 10)
print(p1.user)
print(p1.users)