# 1. Класс Rectangle - работа с прямоугольниками doctest

Возьмите задачу Rectangle с прошлых семинаров. Напишите тесты для этой задачи.

Используйте модуль doctest.

Тесты:

test_width: Тестирование инициализации ширины. Созданы прямоугольники r1 с шириной 5 и r4 с отрицательной шириной (-2). Убедимся, что r1.width корректно установлен на 5, а создание r4 вызывает исключение NegativeValueError.

test_height: Тестирование инициализации ширины и высоты. Созданы прямоугольники r2 с шириной 3 и высотой 4. Проверяем, что r2.width равно 3 и r2.height равно 4.

test_perimeter: Тестирование вычисления периметра. Создан прямоугольник r1 с шириной 5 и проверяем, что r1.perimeter() возвращает 20. Также создан прямоугольник r2 с шириной 3 и высотой 4 и проверяем, что r2.perimeter() возвращает 14.

test_area: Тестирование вычисления площади. Создан прямоугольник r1 с шириной 5 и проверяем, что r1.area() возвращает 25. Также создан прямоугольник r2 с шириной 3 и высотой 4 и проверяем, что r2.area() возвращает 12.

test_addition: Тестирование операции сложения. Созданы прямоугольники r1 с шириной 5 и r2 с шириной 3 и высотой 4. Выполняем операцию сложения r1 + r2 и проверяем, что полученный прямоугольник r3 имеет правильные значения ширины и высоты (8 и 6.0 соответственно).

test_subtraction: Тестирование операции вычитания. Созданы прямоугольники r1 с шириной 5 и r2 с шириной 3 и высотой 4. Выполняем операцию вычитания r1 - r2 и проверяем, что полученный прямоугольник r3 имеет правильные значения ширины и высоты (2 и 2.0 соответственно).

**Запускать тесты не надо, автотест это сделает сам:**

```
__file__ = None
doctest.testmod(extraglobs={'__file__': __file__})

```

**Шаблон с автотеста:**
```
# Введите ваше решение ниже

# Введите ваше решение ниже
class Rectangle:
    """
    Класс, представляющий прямоугольник.

    Атрибуты:
    - width (int): ширина прямоугольника
    - height (int): высота прямоугольника

    Методы:
    - perimeter(): вычисляет периметр прямоугольника
    - area(): вычисляет площадь прямоугольника
    - __add__(other): определяет операцию сложения двух прямоугольников
    - __sub__(other): определяет операцию вычитания одного прямоугольника из другого
    - __lt__(other): определяет операцию "меньше" для двух прямоугольников
    - __eq__(other): определяет операцию "равно" для двух прямоугольников
    - __le__(other): определяет операцию "меньше или равно" для двух прямоугольников
    - __str__(): возвращает строковое представление прямоугольника
    - __repr__(): возвращает строковое представление прямоугольника, которое может быть использовано для создания нового объекта
    """

    def __init__(self, width, height=None):
        self.width = width
        if height is None:
            self.height = width
        else:
            self.height = height

    def perimeter(self):
        """
        Вычисляет периметр прямоугольника.

        Возвращает:
        - int: периметр прямоугольника
        """
        return 2 * (self.width + self.height)

    def area(self):
        """
        Вычисляет площадь прямоугольника.

        Возвращает:
        - int: площадь прямоугольника
        """
        return self.width * self.height

    def __add__(self, other):
        """
        Определяет операцию сложения двух прямоугольников.

        Аргументы:
        - other (Rectangle): второй прямоугольник

        Возвращает:
        - Rectangle: новый прямоугольник, полученный путем сложения двух исходных прямоугольников
        """
        width = self.width + other.width
        perimeter = self.perimeter() + other.perimeter()
        height = perimeter // 2 - width
        return Rectangle(width, height)

    def __sub__(self, other):
        """
        Определяет операцию вычитания одного прямоугольника из другого.

        Аргументы:
        - other (Rectangle): вычитаемый прямоугольник

        Возвращает:
        - Rectangle: новый прямоугольник, полученный путем вычитания вычитаемого прямоугольника из исходного
        """
        if self.perimeter() < other.perimeter():
            self, other = other, self
        width = abs(self.width - other.width)
        perimeter = self.perimeter() - other.perimeter()
        height = perimeter // 2 - width
        return Rectangle(width, height)

    def __lt__(self, other):
        """
        Определяет операцию "меньше" для двух прямоугольников.

        Аргументы:
        - other (Rectangle): второй прямоугольник

        Возвращает:
        - bool: True, если площадь первого прямоугольника меньше площади второго, иначе False
        """
        return self.area() < other.area()

    def __eq__(self, other):
        """
        Определяет операцию "равно" для двух прямоугольников.

        Аргументы:
        - other (Rectangle): второй прямоугольник

        Возвращает:
        - bool: True, если площади равны, иначе False
        """
        return self.area() == other.area()

    def __le__(self, other):
        """
        Определяет операцию "меньше или равно" для двух прямоугольников.

        Аргументы:
        - other (Rectangle): второй прямоугольник

        Возвращает:
        - bool: True, если площадь первого прямоугольника меньше или равна площади второго, иначе False
        """
        return self.area() <= other.area()

    def __str__(self):
        """
        Возвращает строковое представление прямоугольника.

        Возвращает:
        - str: строковое представление прямоугольника
        """
        return f"Прямоугольник со сторонами {self.width} и {self.height}"

    def __repr__(self):
        """
        Возвращает строковое представление прямоугольника, которое может быть использовано для создания нового объекта.

        Возвращает:
        - str: строковое представление прямоугольника
        """
        return f"Rectangle({self.width}, {self.height})"
```

# 2. Rectangle тесты unittest

Возьмите код из прошлой задачи "Класс Rectangle".

Напишите к ней тесты, используя unittest и лежать в class TestRectangle(unittest.TestCase)

Тесты:

test_width: Тестирование инициализации ширины. Создайте прямоугольник с шириной 5 и убедитесь, что атрибут width корректно установлен на 5.

test_height: Тестирование инициализации ширины и высоты. Создайте прямоугольник с шириной 3 и высотой 4 и убедитесь, что атрибут height корректно установлен на 4.

test_perimeter: Тестирование вычисления периметра. Создайте прямоугольник с шириной 5 и вычислите его периметр. Убедитесь, что результат равен 20.

test_area: Тестирование вычисления площади. Создайте прямоугольник с шириной 3 и высотой 4 и вычислите его площадь. Убедитесь, что результат равен 12.

test_addition: Тестирование операции сложения. Создайте два прямоугольника: один с шириной 5, другой с шириной 3 и высотой 4. Выполните операцию сложения r1 + r2 и убедитесь, что полученный прямоугольник имеет правильные значения ширины и высоты (8 и 6.0 соответственно).

test_subtraction: Тестирование операции вычитания. Создайте два прямоугольника: один с шириной 10, другой с шириной 3 и высотой 4. Выполните операцию вычитания r1 - r2 и убедитесь, что полученный прямоугольник имеет правильные значения ширины и высоты (7 и 6.0 соответственно).

test_negative_width: Тестирование инициализации отрицательной ширины. Попробуйте создать прямоугольник с отрицательной шириной (-5) и убедитесь, что это вызывает исключение NegativeValueError.

test_negative_height: Тестирование инициализации отрицательной высоты. Попробуйте создать прямоугольник с шириной 5 и отрицательной высотой (-4) и убедитесь, что это вызывает исключение NegativeValueError.

test_set_width: Тестирование изменения ширины. Создайте прямоугольник с шириной 5 и измените его ширину на 10. Убедитесь, что атрибут width корректно изменяется на 10.

test_set_negative_width: Тестирование изменения отрицательной ширины. Создайте прямоугольник с шириной 5 и попробуйте изменить его ширину на отрицательное значение (-10). Убедитесь, что это вызывает исключение NegativeValueError.

test_set_height: Тестирование изменения высоты. Создайте прямоугольник с шириной 3 и высотой 4 и измените его высоту на 6. Убедитесь, что атрибут height корректно изменяется на 6.

test_set_negative_height: Тестирование изменения отрицательной высоты. Создайте прямоугольник с шириной 3 и высотой 4 и попробуйте изменить его высоту на отрицательное значение (-6). Убедитесь, что это вызывает исключение NegativeValueError.

test_subtraction_negative_result: Тестирование операции вычитания с отрицательным результатом. Создайте два прямоугольника: один с шириной 3 и высотой 4, другой с шириной 10. Попробуйте выполнить операцию вычитания r1 - r2 и убедитесь, что это вызывает исключение NegativeValueError.

test_subtraction_same_perimeter: Тестирование операции вычитания с прямоугольниками одинакового периметра. Создайте два прямоугольника: один с шириной 5, другой с шириной 4 и высотой 3. Выполните операцию вычитания r1 - r2 и убедитесь, что полученный прямоугольник имеет правильные значения ширины и высоты (1 и 1.0 соответственно).

Используйте модуль unittest для запуска тестов. Все тесты должны выполняться успешно и не вызывать ошибок.

**Запускать тесты не надо, автотест это сделает сам:**

```
unittest.main()
```

**На выходе после автоматической обрезки информации в тестах вы должны получить:**

```
FAILED (failures=1)
```

**Шаблон с автотеста:**
```
import unittest

class NegativeValueError(ValueError):
    pass

class Rectangle:

    def __init__(self, width, height=None):
        if width <= 0:
            raise NegativeValueError(f'Ширина должна быть положительной, а не {width}')
        self._width = width
        if height is None:
            self._height = width
        else:
            if height <= 0:
                raise NegativeValueError(f'Высота должна быть положительной, а не {height}')
            self._height = height

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        if value > 0:
            self._width = value
        else:
            raise NegativeValueError(f'Ширина должна быть положительной, а не {value}')

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        if value > 0:
            self._height = value
        else:
            raise NegativeValueError(f'Высота должна быть положительной, а не {value}')

    def perimeter(self):
        return 2 * (self._width + self._height)

    def area(self):
        return self._width * self._height

    def __add__(self, other):
        width = self._width + other._width
        perimeter = self.perimeter() + other.perimeter()
        height = perimeter / 2 - width
        return Rectangle(width, height)

    def __sub__(self, other):
        if self.perimeter() < other.perimeter():
            self, other = other, self
        width = abs(self._width - other._width)
        perimeter = self.perimeter() - other.perimeter()
        height = perimeter / 2 - width
        return Rectangle(width, height)

# Введите ваше решение ниже
```

# 3. Управление информацией о сотрудниках и их возрасте doctest

Возьмите код из прошлой задачи "Управление информацией о сотрудниках и их возрасте".

Ваша задача - написать набор тестов для класса Employee с использованием модуля doctest, чтобы убедиться, что он работает правильно.

Тесты:

test_employee_full_name: Тестирование метода full_name(). Создайте объект Employee с фамилией "Ivanov", именем "Ivan", отчеством "Ivanovich" и возрастом 30. Убедитесь, что метод full_name() возвращает правильное полное имя в формате "Ivanov Ivan Ivanovich".

test_employee_birthday: Тестирование метода birthday(). Создайте объект Employee с фамилией "Ivanov", именем "Ivan", отчеством "Ivanovich" и возрастом 30. Вызовите метод birthday() и убедитесь, что возраст увеличился на 1 и стал равным 31.

test_employee_raise_salary: Тестирование метода raise_salary(). Создайте объект Employee с фамилией "Ivanov", именем "Ivan", отчеством "Ivanovich", возрастом 30, должностью "manager" и зарплатой 50000. Вызовите метод raise_salary(10) и убедитесь, что зарплата увеличилась на 10% и стала равной 55000.0.

test_employee_str: Тестирование метода __str__(). Создайте объект Employee с фамилией "Ivanov", именем "Ivan", отчеством "Ivanovich", возрастом 30, должностью "manager" и зарплатой 50000. Убедитесь, что метод __str__() возвращает правильную строку в формате "Ivanov Ivan Ivanovich (Manager)".

test_employee_last_name_title: Тестирование атрибута last_name. Создайте объект Employee с фамилией "ivanov" (в нижнем регистре), именем "ivan" (в нижнем регистре), отчеством "ivanovich" (в нижнем регистре), возрастом 30, должностью "manager" и зарплатой 50000. Убедитесь, что атрибут last_name возвращается в верхнем регистре, то есть "Ivanov".

**Запускать тесты не надо, автотест это сделает сам:**

```
__file__ = None
doctest.testmod(extraglobs={'__file__': __file__})
```

**Шаблон с автотеста:**
```
import doctest

class Person:

    def __init__(self, last_name: str, first_name: str, patronymic: str, age: int):
        self.last_name = last_name.title()
        self.first_name = first_name.title()
        self.patronymic = patronymic.title()
        self._age = age

    def full_name(self):
        return f'{self.last_name} {self.first_name} {self.patronymic}'

    def birthday(self):
        self._age += 1

    def get_age(self):
        return self._age


class Employee(Person):
    
    def __init__(self, last_name: str, first_name: str, patronymic: str, age: int, position: str, salary: float):
        super().__init__(last_name, first_name, patronymic, age)
        self.position = position.title()
        self.salary = salary

    def raise_salary(self, percent: float):
        self.salary *= (1 + percent / 100)

    def __str__(self):
        return f'{self.full_name()} ({self.position})'


# Введите ваше решение ниже
```

# 4. Управление информацией о сотрудниках и их возрасте unittest

Возьмите код из прошлой задачи "Управление информацией о сотрудниках и их возрасте".

Ваша задача - написать набор тестов для класса Employee, чтобы убедиться, что он работает правильно.

Тесты должны быть написаны с использованием модуля unittest и лежать в class TestEmployee(unittest.TestCase).

Тесты:

test_employee_full_name: Тестирование метода full_name(). Создайте объект Employee с фамилией "Ivanov", именем "Ivan", отчеством "Ivanovich" и убедитесь, что метод full_name() возвращает правильное полное имя в формате "Ivanov Ivan Ivanovich".

test_employee_birthday: Тестирование метода birthday(). Создайте объект Employee с возрастом 30, вызовите метод birthday() и убедитесь, что возраст увеличился на 1 и стал равным 31.

test_employee_raise_salary: Тестирование метода raise_salary(). Создайте объект Employee с зарплатой 50000, вызовите метод raise_salary(10) и убедитесь, что зарплата увеличилась на 10% и стала равной 55000.0.

test_employee_str: Тестирование метода __str__(). Создайте объект Employee с данными: фамилия "Ivanov", имя "Ivan", отчество "Ivanovich", возраст 30, должность "manager" и зарплата 50000. Убедитесь, что метод __str__() возвращает правильную строку в формате "Ivanov Ivan Ivanovich (Manager)".

test_employee_last_name_title: Тестирование атрибута last_name. Создайте объект Employee с фамилией "Ivanov" и убедитесь, что атрибут last_name не возвращает в верхнем регистре "Ivan".

Тесты должны проходить успешно и не вызывать ошибок.

**Запускать тесты не надо, автотест это сделает сам:**

```
unittest.main()
```

**На выходе после автоматической обрезки информации в тестах вы должны получить:**

```
FAILED (failures=1)
```

**Шаблон с автотеста:**

```
# Введите ваше решение ниже
import unittest

class Person:

    def __init__(self, last_name: str, first_name: str, patronymic: str, age: int):
        self.last_name = last_name.title()
        self.first_name = first_name.title()
        self.patronymic = patronymic.title()
        self._age = age

    def full_name(self):
        return f'{self.last_name} {self.first_name} {self.patronymic}'

    def birthday(self):
        self._age += 1

    def get_age(self):
        return self._age

class Employee(Person):

    def __init__(self, last_name: str, first_name: str, patronymic: str, age: int, position: str, salary: float):
        super().__init__(last_name, first_name, patronymic, age)
        self.position = position.title()
        self.salary = salary

    def raise_salary(self, percent: float):
        self.salary *= (1 + percent / 100)

    def __str__(self):
        return f'{self.full_name()} ({self.position})'
```

# 5. Класс Rectangle - работа с прямоугольниками Pytest

Вам предоставлен код на Python из предыдущих задач, который содержит два класса: Rectangle и NegativeValueError.

Ваша задача - написать набор тестов для класса Rectangle, чтобы убедиться, что он работает правильно и обрабатывает некорректные значения.

Тесты должны быть написаны с использованием модуля pytest.

*Тесты необходимо написать именно в этом порядке!

Тесты:

test_width: Тестирование инициализации ширины. Создайте объект Rectangle с шириной 5 и убедитесь, что ширина установлена правильно.

test_height: Тестирование инициализации ширины и высоты. Создайте объект Rectangle с шириной 3 и высотой 4 и убедитесь, что высота установлена правильно.

test_perimeter: Тестирование вычисления периметра. Создайте объект Rectangle с шириной 5 и вычислите его периметр (должен быть равен 20).

test_area: Тестирование вычисления площади. Создайте объект Rectangle с шириной 3 и высотой 4 и вычислите его площадь (должна быть равна 12).

test_addition: Тестирование операции сложения двух прямоугольников. Создайте два объекта Rectangle с ширинами 5 и 3, и высотами 1 и 4 соответственно. Произведите операцию сложения и убедитесь, что полученный прямоугольник имеет правильные значения ширины и высоты.

test_negative_width: Тестирование инициализации отрицательной ширины. Попробуйте создать объект Rectangle с отрицательной шириной (-5) и убедитесь, что это вызывает исключение NegativeValueError.

test_negative_height: Тестирование инициализации отрицательной высоты. Попробуйте создать объект Rectangle с шириной 5 и отрицательной высотой (-4) и убедитесь, что это вызывает исключение NegativeValueError.

test_set_width: Тестирование изменения ширины. Создайте объект Rectangle с шириной 5 и измените его ширину на 10. Убедитесь, что ширина изменена правильно.

test_set_negative_width: Тестирование изменения отрицательной ширины. Создайте объект Rectangle с шириной 5 и попробуйте изменить его ширину на отрицательное значение (-10). Убедитесь, что это вызывает исключение NegativeValueError.

test_set_height: Тестирование изменения высоты. Создайте объект Rectangle с шириной 3 и высотой 4 и измените его высоту на 6. Убедитесь, что высота изменена правильно.

test_set_negative_height: Тестирование изменения отрицательной высоты. Создайте объект Rectangle с шириной 3 и высотой 4 и попробуйте изменить его высоту на отрицательное значение (-6). Убедитесь, что это вызывает исключение NegativeValueError.

test_subtraction: Тестирование операции вычитания двух прямоугольников. Создайте два объекта Rectangle с ширинами 10 и 3, и высотами 1 и 4 соответственно. Произведите операцию вычитания и убедитесь, что полученный прямоугольник имеет правильные значения ширины и высоты.

test_subtraction_negative_result: Тестирование операции вычитания с отрицательным результатом. Создайте два объекта Rectangle с ширинами 3 и 10, и высотами 4 и 1 соответственно. Попробуйте выполнить операцию вычитания и убедитесь, что это вызывает исключение NegativeValueError.

test_subtraction_same_perimeter: Тестирование операции вычитания с одинаковым периметром. Создайте два объекта Rectangle с ширинами 5 и 4, и высотами 1 и 3 соответственно. Произведите операцию вычитания и убедитесь, что полученный прямоугольник имеет правильные значения ширины и высоты.

**Запускать тесты не надо, автотест это сделает сам:** 

```
# Запускаем pytest.main() с нужными параметрами
pytest.main(["--no-header", '-q', "--durations=0", new_filename])
```

**На выходе после автоматической обрезки информации в тестах вы должны получить:**

```
....F.......FF                                                           [100%]
```

**Шаблон с автотеста:**

```
import pytest

class NegativeValueError(ValueError):
    pass


class Rectangle:
    def __init__(self, width, height=None):
        if width <= 0:
            raise NegativeValueError(f'Ширина должна быть положительной, а не {width}')
        self._width = width
        if height is None:
            self._height = width
        else:
            if height <= 0:
                raise NegativeValueError(f'Высота должна быть положительной, а не {height}')
            self._height = height

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        if value > 0:
            self._width = value
        else:
            raise NegativeValueError(f'Ширина должна быть положительной, а не {value}')

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        if value > 0:
            self._height = value
        else:
            raise NegativeValueError(f'Высота должна быть положительной, а не {value}')

    def perimeter(self):
        return 2 * (self._width + self._height)

    def area(self):
        return self._width * self._height

    def __add__(self, other):
        width = self._width + other._width
        perimeter = self.perimeter() + other.perimeter()
        height = perimeter / 2 - width
        return Rectangle(width, height)

    def __sub__(self, other):
        if self.perimeter() < other.perimeter():
            self, other = other, self
        width = abs(self._width - other._width)
        perimeter = self.perimeter() - other.perimeter()
        height = perimeter / 2 - width
        return Rectangle(width, height)

# Введите ваше решение ниже
```

# 6. Управление информацией о сотрудниках и их возрасте pytest

У вас есть два класса: Person и Employee из предыдущих задач.

Необходимо написать тесты с использованием модуля pytest и лежать в class TestEmployee.

*Тесты необходимо написать именно в этом порядке!

Тесты:

test_employee_full_name: Тестирование метода full_name(). Создайте объект Employee с фамилией "Ivanov", именем "Ivan", отчеством "Ivanovich" и убедитесь, что метод full_name() возвращает правильное полное имя в формате "Ivanov Ivan Ivanovich".

test_employee_birthday: Тестирование метода birthday(). Создайте объект Employee с возрастом 30, вызовите метод birthday() и убедитесь, что возраст увеличился на 1 и стал равным 31.

test_employee_raise_salary: Тестирование метода raise_salary(). Создайте объект Employee с зарплатой 50000, вызовите метод raise_salary(10) и убедитесь, что зарплата увеличилась на 10% и стала равной 55000.0.

test_employee_str: Тестирование метода __str__(). Создайте объект Employee с данными: фамилия "Ivanov", имя "Ivan", отчество "Ivanovich", возраст 30, должность "manager" и зарплата 50000. Убедитесь, что метод __str__() возвращает правильную строку в формате "Ivanov Ivan Ivanovich (Manager)".

test_employee_last_name_title: Тестирование атрибута last_name. Создайте объект Employee с фамилией "Ivanov" и убедитесь, что атрибут last_nameвозвращается в верхнем регистре, то есть "Ivanov".

**Запускать тесты не надо, автотест это сделает сам:**

```
# Запускаем pytest.main() с нужными параметрами
    pytest.main(["--no-header", '-q', "--durations=0", new_filename])
```

**На выходе после автоматической обрезки информации в тестах вы должны получить:**

```
..F..                                                                    [100%]
```

**Шаблон с автотеста:**

```
import pytest

class Person:
    def __init__(self, last_name: str, first_name: str, patronymic: str, age: int):
        self.last_name = last_name.title()
        self.first_name = first_name.title()
        self.patronymic = patronymic.title()
        self._age = age

    def full_name(self):
        return f'{self.last_name} {self.first_name} {self.patronymic}'

    def birthday(self):
        self._age += 1

    def get_age(self):
        return self._age

class Employee(Person):
    def __init__(self, last_name: str, first_name: str, patronymic: str, age: int, position: str, salary: float):
        super().__init__(last_name, first_name, patronymic, age)
        self.position = position.title()
        self.salary = salary

    def raise_salary(self, percent: float):
        self.salary *= (1 + percent / 100)

    def __str__(self):
        return f'{self.full_name()} ({self.position})'

# Введите ваше решение ниже
```

