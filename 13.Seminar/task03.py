# Создайте класс с базовым исключением и дочерние классы-исключения: 
# ошибка уровня, ошибка доступа.
class MyExption(Exception):
    pass

class LevelExetion(MyExption):
    pass

class AccessExeption(MyExption):
    pass