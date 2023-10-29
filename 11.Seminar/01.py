# 📌Создайте класс Моя Строка, где:
# 📌будут доступны все возможности str
# 📌дополнительно хранятся имя автора строки и время создания (time.time)
import time
class MyStr(str):
    def __new__(cls, stringi, author):
        instance = super().__new__(cls, stringi)
        instance.name = author
        instance.time = time.ctime()
        return instance

    def __str__(self):
        return self + " " + self.name + " " + self.time


ss = MyStr("Hello world", "Slava")

print(ss.upper())