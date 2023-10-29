# Добавьте к задачам 1 и 2 строки документации для классов.
import time
from random import randint
class MyStr(str):
    """
    Add to str() two attribute:
    author - string with name of authoer
    time - time of object creation
    __str__ - string of all attribute for print
    """
    def __new__(cls, stringi, author):
        instance = super().__new__(cls, stringi)
        instance.name = author
        instance.time = time.ctime()
        return instance

    def __str__(self):
        """
        overided str() method
        :return: string of attrubutes, such main string, name of author and creation time
        """
        return self + " " + self.name + " " + self.time


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

help(Arch)
help(MyStr)