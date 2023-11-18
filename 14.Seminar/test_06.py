# На семинаре 13 был создан проект по работе с пользователями (имя, id, уровень). 
# Напишите 3-7 тестов pytest для данного проекта.
# Используйте фикстуры.
import json
import pytest
class MyExption(Exception):
    pass

class LevelExetion(MyExption):
    pass

class AccessExeption(MyExption):
    pass

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
        

        
@pytest.fixture     
def data():
    user1 = User("John", "10", 1)
    user2 = User("John", "10", 1)
    return user1, user2

def test_eq(data):
    user1, user2 = data
    assert user1 == user2

@pytest.fixture
def data_project():
    project = ProjectUser()
    project.my_json()
    print(project.users)
    return project

def test_auth(data_project):
    user10 = User("Ann", "1", "12")
    print(user10)
    data_project.login_2_sys("Ann", "12")
    print(data_project.login_2_sys("Ann", "12"))
    assert data_project.user == user10

if __name__ == "__main__":
    pytest.main([f'{__file__}', '-v'])
