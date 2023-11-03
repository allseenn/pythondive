Не все тесты пройдены, есть ошибки :(


Количество затраченных попыток: 1

Время выполнения: 0.497543 сек

**Общая статистика**

Всего тестов: 2. Пройдено: 0. Не пройдено: 2.

Подробную информацию по каждому тесту смотрите ниже.

____________

**Тест 1**
Тест не пройден ✗

Формулировка:
* Итоговый код для проверки. Иногда добавляем что-то от себя :)

```
import warnings

warnings.filterwarnings('ignore')

# Введите ваше решение ниже

class Archive:
    """
    Класс, представляющий архив текстовых и числовых записей.

    Атрибуты:
    - archive_text (list): список архивированных текстовых записей.
    - archive_number (list): список архивированных числовых записей.
    - text (str): текущая текстовая запись для добавления в архив.
    - number (int или float): текущая числовая запись для добавления в архив.
    """

    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.archive_text = []
            cls._instance.archive_number = []
        return cls._instance

    def __init__(self, text, number):
        self._instance.text = text
        self._instance.number = number
        self._instance.archive_text.append(text)
        self._instance.archive_number.append(number)

    def __str__(self):
        return f'Text is {self._instance.text} and number is {self._instance.number}. Also {self._instance.archive_text} and {self._instance.archive_number}'

    def __repr__(self):
        return f'Archive("{self._instance.text}", {self._instance.number})'




#При отправке кода на Выполнение раскомментируйте строку ниже, чтобы задать значения аргументов и вызвать функцию

#При отправке решения на Проверку закомментируйте эту строку обратно - система автоматически подставит разные значения аргументов и вызовет функцию для проверки

#archive1 = Archive("Запись 1", 42)
#archive2 = Archive("Запись 2", 3.14) 


archive1 = Archive("First Text", 1)

print(archive1)

archive2 = Archive("Second Text", 2)

print(archive2)

archive3 = Archive("Third Text", 3)

print(archive1)
print(archive3)
```
**Ожидаемый ответ:**

Text is First Text and number is 1. Also [] and []
Text is Second Text and number is 2. Also ['First Text'] and [1]
Text is Third Text and number is 3. Also ['First Text', 'Second Text'] and [1, 2]
Text is Third Text and number is 3. Also ['First Text', 'Second Text'] and [1, 2]

Ваш ответ:

Text is First Text and number is 1. Also ['First Text'] and [1]
Text is Second Text and number is 2. Also ['First Text', 'Second Text'] and [1, 2]
Text is Third Text and number is 3. Also ['First Text', 'Second Text', 'Third Text'] and [1, 2, 3]
Text is Third Text and number is 3. Also ['First Text', 'Second Text', 'Third Text'] and [1, 2, 3]
______________

Тест 2
Тест не пройден ✗

Формулировка:

* Итоговый код для проверки. Иногда добавляем что-то от себя :)

```
import warnings

warnings.filterwarnings('ignore')

# Введите ваше решение ниже

class Archive:
    """
    Класс, представляющий архив текстовых и числовых записей.

    Атрибуты:
    - archive_text (list): список архивированных текстовых записей.
    - archive_number (list): список архивированных числовых записей.
    - text (str): текущая текстовая запись для добавления в архив.
    - number (int или float): текущая числовая запись для добавления в архив.
    """

    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.archive_text = []
            cls._instance.archive_number = []
        return cls._instance

    def __init__(self, text, number):
        self._instance.text = text
        self._instance.number = number
        self._instance.archive_text.append(text)
        self._instance.archive_number.append(number)

    def __str__(self):
        return f'Text is {self._instance.text} and number is {self._instance.number}. Also {self._instance.archive_text} and {self._instance.archive_number}'

    def __repr__(self):
        return f'Archive("{self._instance.text}", {self._instance.number})'




#При отправке кода на Выполнение раскомментируйте строку ниже, чтобы задать значения аргументов и вызвать функцию

#При отправке решения на Проверку закомментируйте эту строку обратно - система автоматически подставит разные значения аргументов и вызовет функцию для проверки

#archive1 = Archive("Запись 1", 42)
#archive2 = Archive("Запись 2", 3.14) 


archive1 = Archive("First Text", 1)
archive2 = Archive("Second Text", 2)
archive3 = Archive("Third Text", 3)
print(archive1.archive_text)  # Выведет: ['First Text', 'Third Text']
print(archive1.archive_number)  # Выведет: [1, 3]
print(archive2.archive_text)  # Выведет: ['First Text', 'Second Text']
print(archive2.archive_number)
```
__________

Ожидаемый ответ:

['First Text', 'Second Text']
[1, 2]
['First Text', 'Second Text']
[1, 2]

Ваш ответ:

['First Text', 'Second Text', 'Third Text']
[1, 2, 3]
['First Text', 'Second Text', 'Third Text']
[1, 2, 3]