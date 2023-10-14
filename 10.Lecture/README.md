# ООП

## Основы ООП

**Объектно-ориентированное программирование** (сокр. ООП) — методология программирования, основанная на представлении программы в виде совокупности взаимодействующих объектов, каждый из которых является экземпляром определённого класса, а классы образуют иерархию наследования.

В Python всё объект. 
Объекты строятся на основе классов.
Объекты также называют экземплярами класса. 
В следующем коде создается экземпляр класса (объект) list с помощью функции list()

```
>>> data = list((1, 2, 3))
>>> print(f'{data = }, {type(data) = }, {type(list) = }')
data = [1, 2, 3], type(data) = <class 'list'>, type(list) = <class 'type'>

```
Тип функции list — type, т.е. класса типа данных пайтон. 
Привычные функции list(), tuple(), dict(), set() int(), str(), etc являются классами.
Пайтон специально разрабатывался как язык ООП имеющий функциональный стиль

### Классы

**Класс** — универсальный, комплексный тип данных, состоящий из тематически единого набора «полей» (переменных более элементарных типов) и «методов» (функций для работы с этими полями), то есть он является моделью информационной сущности с внутренним и внешним интерфейсами для оперирования своим содержимым (значениями полей).

Python имеет несколько областей видимости:
- Локальные переменные функции 
- Переменные и функции внутри модулей.
- Переменные (поля) и функции (методы) внутри класса

Для обращение к атрибутам модулей используется импорт и точечная нотация:

```
import random
import supermodule

result1 = random.randint(1, 10)
result2 = supermodule.randint(42)
```

Класс Python это ещё один способ создать локальную область видимости, поместив в неё переменные и функции класса.

Разные модули могут содержать одноимённые функции и переменные, что не будет вызывать ошибок, т.к. пространство имён разграничивает их по областям видимости, используя тоже точечную нотацию как и модули, но имеют еще одно преимущество - классы позволяют создавать экземпляры. У каждого экземпляра будет своя область видимости.

Создадим для игрушки класс Person:

```
>>> class Person:
...     pass
... 
```

- **class** - указывает на создание нового класса
- **Person** - имя класса в стиле кэмел кейс или TitleCase,
- **:** - обязательное двоеточие
- **pass** - тело класса записывается с отступами относительно его определения


Определение класса записывается в начале файла, после импортов и констант уровня модуля. До и после класса оставляют по две пустых строки

### Экземпляры класса

Для создания экземпляра класса необходимо выполнить операцию присваивания вызвав класс(). Точно так же как в примере со функцией list():

```
>>> class Person:
...     max_up = 3
... 
>>> 
>>> p1 = Person()
>>> print(p1.max_up)
3
```

Переменная p1 является экземпляром класса Person. Мы можем обращаться в переменным класса из экземпляра

Класс это прототип (чертеж), а его экземпляр это серийный объект, созданный на основе чертежа.

Класс — такой же объект, как и экземпляр. С ним так же можно взаимодействовать. Поэтому он не просто чертёж на бумаге:

```
print(Person.max_up)
```

### Атрибуты класса и экземпляров

Переменная max_up - атрибут (свойство, поле) класса. Свойства (атрибуты, поля) позволяют хранить значения и переходят ко всем экземплярам класса:

```
>>> class Person:
...     max_up = 3
... 
>>> 
>>> p1 = Person()
>>> p2 = Person()
>>> print(f'{Person.max_up = }, {p1.max_up = }, {p2.max_up = }')
Person.max_up = 3, p1.max_up = 3, p2.max_up = 3
>>> p1.max_up = 12
>>> print(f'{Person.max_up = }, {p1.max_up = }, {p2.max_up = }')
Person.max_up = 3, p1.max_up = 12, p2.max_up = 3
>>> Person.max_up = 42
>>> print(f'{Person.max_up = }, {p1.max_up = }, {p2.max_up = }')
Person.max_up = 42, p1.max_up = 12, p2.max_up = 42
```

### Динамическая структура класса

Класс и экземпляр являются динамическими объектами. Мы можем добавлять атрибуты в процессе работы, а не только в момент создания класса:

```
>>> class Person:
...     max_up = 3
... 
>>>     
>>> p1 = Person()
>>> p2 = Person()
>>> Person.level = 1
>>> print(f'{Person.level = }, {p1.level = }, {p2.level = }')
Person.level = 1, p1.level = 1, p2.level = 1
>>> p1.health = 100
>>> print(f'{Person.health = }, {p1.health = }, {p2.health = }')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: type object 'Person' has no attribute 'health'
>>> print(f'{p1.health = }, {p2.health = }')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'Person' object has no attribute 'health'
>>> print(f'{p1.health = }')
p1.health = 100

```
Добавление свойства level для класса позволяет обращаться к нему и из экземпляров.
Когда же мы добавляем свойство health для экземпляра p1, получаем ошибку AttributeError. Ни класс, ни экземпляр p2 не могут получить доступ к данному атрибуту.

Возможность динамически изменять класс может быть использована как аналог работы со словарями dict:

```
>>> class Person:
...     pass
... 
>>> 
>>> p1 = Person()
>>> p1.level = 1
>>> p1.health = 100
>>> dict_p1 = {}
>>> dict_p1['level'] = 1
>>> dict_p1['health'] = 100
>>> print(f'{p1.health = }')
p1.health = 100
>>> print(f'{dict_p1["health"] = }')
dict_p1["health"] = 100
```

Если в словаре мы указываем строковой ключ в квадратных скобках, в экземпляре достаточно точечной нотации без лишних скобок и кавычек.

### Конструктор экземпляра

При создании класса обычно используют функцию конструктор __init__():

```
>>> class Person:
...     max_up = 3
...     def __init__(self):
...         self.level = 1
...         self.health = 100
... 
>>> 
>>> p1 = Person()
>>> p2 = Person()
>>> print(f'{p1.max_up = }, {p1.level = }, {p1.health = }')
p1.max_up = 3, p1.level = 1, p1.health = 100
>>> print(f'{p2.max_up = }, {p2.level = }, {p2.health = }')
p2.max_up = 3, p2.level = 1, p2.health = 100
>>> print(f'{Person.max_up = }, {Person.level = }, {Person.health = }')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: type object 'Person' has no attribute 'level'
>>> Person.level = 100
>>> print(f'{Person.level = }, {p1.level = }, {p2.level = }')
Person.level = 100, p1.level = 1, p2.level = 1
```

Внутри функции заданы две переменные level и health. Это атрибуты экземпляров. Любой экземпляр получает заранее присвоенные значения. При этом сам класс не имеет доступа к заданным атрибутам.

Также при попытке определить свойства level у класса мы не меняем значения экземпляров. Это разные объекты, находящиеся в разных локальных областях видимости.

#### Параметр self

Имя self не является зарезервированным. Вместо него можно использовать любое. Но соглашение о написании кода требует писать self. Так ваш код поймут другие разработчики, а IDE верно его проанализируют. В некоторых языках при написании кода используется запись this.name.

```
def __init__(self):
    self.level = 1
    self.health = 100
```

**self** является указателем на тот экземпляр класса, к которому происходит обращение. Например для p1 это p1.level = 1. Какое бы имя вы не дали экземпляру, self подставляет его на своё место.


#### Передача аргументов в экземпляр

При создании экземпляра можно передать значения в конструктор и тем самым добавить свойства, характерные для конкретного экземпляра.

```
>>> class Person:
...     max_up = 3
...     def __init__(self, name, race='unknown'):
...         self.name = name
...         self.race = race
...         self.level = 1
...         self.health = 100
... 
>>> 
>>> p1 = Person('Сильвана', 'Эльф')
>>> p2 = Person('Иван', 'Человек')
>>> p3 = Person('Грогу')
>>> print(f'{p1.name = }, {p1.race = }')
p1.name = 'Сильвана', p1.race = 'Эльф'
>>> print(f'{p2.name = }, {p2.race = }')
p2.name = 'Иван', p2.race = 'Человек'
>>> print(f'{p3.name = }, {p3.race = }')
p3.name = 'Грогу', p3.race = 'unknown'
```

У __init__() определено три параметра. При этом первый параметр всегда self и он не учитывается при передаче аргументов. Вызывая класс ожидаются два параметра, при этом второй имеет значение по умолчанию. За исключением self логика такая же как и при создании обычной функции.

### Методы класса

Функция внутри класса называется методом. При обращение к методу используют круглые скобки:

```
>>> class Person:
...     max_up = 3
...     def __init__(self, name, race='unknown'):
...         self.name = name
...         self.race = race
...         self.level = 1
...         self.health = 100
...         
...     def level_up(self):
...         self.level += 1
... 
>>>         
>>> p1 = Person('Сильвана', 'Эльф')
>>> p2 = Person('Иван', 'Человек')
>>> p3 = Person('Грогу')
>>> print(f'{p1.level = }, {p2.level = }, {p3.level = }')
p1.level = 1, p2.level = 1, p3.level = 1
>>> p3.level_up()
>>> p1.level_up()
>>> p3.level_up()
>>> print(f'{p1.level = }, {p2.level = }, {p3.level = }')
p1.level = 2, p2.level = 1, p3.level = 3
```

Между методами класса оставляется по одной пустой строке до и после. В модуле до и после функции оставляют по две   пустые строки.

Можно передавать в метод аргументы и даже экземпляр класса:

```
>>> class Person:
...     max_up = 3
...     def __init__(self, name, race='unknown'):
...         self.name = name
...         self.race = race
...         self.level = 1
...         self.health = 100
...     def level_up(self):
...         self.level += 1
...     def change_health(self, other, quantity):
...         self.health += quantity
...         other.health -= quantity
... 
>>> 
>>> p1 = Person('Сильвана', 'Эльф')
>>> p2 = Person('Иван', 'Человек')
>>> p3 = Person('Грогу')
>>> print(f'{p1.health = }, {p2.health = }, {p3.health = }')
p1.health = 100, p2.health = 100, p3.health = 100
>>> p1.change_health(p2, 10)
>>> print(f'{p1.health = }, {p2.health = }, {p3.health = }')
p1.health = 110, p2.health = 90, p3.health = 100

```
Метод change_health принимает ещё один экземпляр и количество здоровья. Атрибут меняется у экземпляра, вызвавшего метод и у второго, переданного экземпляра. Чаще всего для указания на другой экземпляр того же класса используют параметр other в имени метода. Соответственно записи other.name аналогичны self.name, но изменяют другой, переданный экземпляр класса.

## 2. Инкапсуляция

**Инкапсуляция** — свойство системы, позволяющее объединить данные и методы, работающие с ними, в классе.

Инкапсуляция нужна одним разработчикам для сокрытия от других разработчиков и самих себя свойств и методов класса. В Python нет строгой инкапсуляции как в ряде других языков.


### Модификаторы доступа

В классическом ООП выделяют следующие модификаторы доступа:

- public — публичный доступ, т.е. возможность обратиться к свойству или методу из любого другого класса и экземпляра
- protected — защищённый доступ, позволяющий обращаться к свойствам и методам из класса и из классов наследников.
- private — приватный доступ, т.е. отсутсвие возможности обратиться к свойству или методы из другого класса или экземпляра.

В Python по умолчанию все свойства и методы публичные

### _ защищенный доступ

```
>>> class Person:
...     max_up = 3
...     _max_level = 80
...     def __init__(self, name, race='unknown', speed=100):
...         self.name = name
...         self.race = race
...         self.level = 1
...         self.health = 100
...         self._speed = speed
...     def _check_level(self):
...         return self.level < self._max_level
...     def level_up(self):
...         if self._check_level():
...             self.level += 1
...     def change_health(self, other, quantity):
...         self.health += quantity
...         other.health -= quantity
... 
>>> 
>>> p1 = Person('Сильвана', 'Эльф', 120)
>>> p2 = Person('Иван', 'Человек')
>>> p3 = Person('Грогу', speed=60)
>>> print(f'{p1._max_level = }')
p1._max_level = 80
>>> print(f'{p2._speed = }')
p2._speed = 100
>>> p2._speed = 150
>>> print(f'{p2._speed = }')
p2._speed = 150
>>> p3.level_up()
>>> print(f'{p3.level = }')
p3.level = 2
>>> p3.level = 80
>>> p3.level_up()
>>> print(f'{p3.level = }')
p3.level = 80
```

Переменная уровня класса _max_level и переменная уровня экземпляра _speed говорят другим разработчикам, что они защищены. Так мы просим их не использовать. Однако мы сможем обратиться к ним через точечную нотацию. И даже изменить, если очень захотим. Скорее всего IDE будет указывать на неверные действия с подобными переменными.
Аналогично метод _check_level говорит о том, что он защищён. Метод нужен классу для проверки достижения максимального уровня персонажа и не должен использоваться напрямую вне класса. А вот его вызов из метода level_up считается нормальным поведением.

### __ Приватный доступ

Переменная с двумя подчёркиваниями в начале не может иметь более одного подчёркивания в конце имени.
Двойное подчёркивание до и после имени — магическая переменная Python. Подобно __init__ такие имена зарезервированы для особых действий.

```
>>> class Person:
...     __max_up = 3
...     _max_level = 80
...     def __init__(self, name, race='unknown', speed=100):
...         self.name = name
...         self.race = race
...         self.level = 1
...         self.health = 100
...         self._speed = speed
...         self.up = 3
...     def _check_level(self):
...         return self.level < self._max_level
...     def level_up(self):
...         if self._check_level():
...             self.level += 1
...     def change_health(self, other, quantity):
...         self.health += quantity
...         other.health -= quantity
...     def add_up(self):
...         self.up += 1
...         self.up = min(self.up, self.__max_up)
...         
... 
>>> p1 = Person('Сильвана', 'Эльф', 120)
>>> print(f'{p1.up = }')
p1.up = 3
>>> p1.up = 1
>>> print(f'{p1.up = }')
p1.up = 1
>>> for _ in range(5):
...     p1.add_up()
...     print(f'{p1.up = }')
... 
p1.up = 2
p1.up = 3
p1.up = 3
p1.up = 3
p1.up = 3
>>> print(p1.__max_up)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'Person' object has no attribute '__max_up'
>>> print(Person.__max_up)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: type object 'Person' has no attribute '__max_up'
```

**__max_up** доступна внутри класса и его экземпляров. Если обратиться к такому свойству напрямую, получаем ошибку доступа к
атрибуту. Аналогичные ошибки будут и при обращении к методу, начинающемуся с двух подчёркиваний.

### Доступ к приватным переменным

Приватная переменная __max_up не исчезает за пределами класса. Срабатывает механизм модификации имени. В общем случае он превращает переменную
__name в переменныю _classname__name:

```
class Person:
    __max_up = 3
...
print(f'{p1._Person__max_up = }')
```

В нашем примере переменная __max_up превратилась в _Person__max_up. Обратите внимание на заглавную P в имени, ведь Python является регистрозависимым языком.

## 3. Наследование

**Наследование** — свойство системы, позволяющее описать новый класс на основе уже существующего с частично или полностью заимствованной функциональностью. Класс, от которого производится наследование, называется базовым, родительским или суперклассом. Новый класс — потомком, наследником, дочерним или производным классом.


В Python все объекты являются наследниками класса **object**

Т.е запись вида:
```
class Person:
    pass
```
Аналогична виду:
```
class Person(object):
    pass
```

Создадим класс героя на основе класса персонажа:

```
>>> class Person:
...     __max_up = 3
...     _max_level = 80
...     def __init__(self, name, race='unknown', speed=100):
...         self.name = name
...         self.race = race
...         self.level = 1
...         self.health = 100
...         self._speed = speed
...         self.up = 3
...     def _check_level(self):
...         return self.level < self._max_level
...     def level_up(self):
...         if self._check_level():
...             self.level += 1
...     def change_health(self, other, quantity):
...         self.health += quantity
...         other.health -= quantity
...     def add_up(self):
...         self.up += 1
...         self.up = min(self.up, self.__max_up)
... 
>>> 
>>> class Hero(Person):
...     def __init__(self, power, *args, **kwargs):
...         self.power = power
...         super().__init__(*args, **kwargs)
... 
>>>         
>>> p1 = Hero('archery', 'Сильвана', 'Эльф', 120)
>>> print(f'{p1.name = }, {p1.up = }, {p1.power = }')
p1.name = 'Сильвана', p1.up = 3, p1.power = 'archery'
```

Cоздаём класс Hero и указываем в скобках класс Person. 
Герой - дочерний класс для персонажа. Мы хотим добавить герою свойство power и прописываем его в методе инициализации. 
Далее вызываем метод super().__init__, т.е. метод инициализации родительского класса. Без такого вызова не будут созданы атрибуты родительского
класса.

### Переопределение методов

При наследовании мы можем использовать в дочернем классе все общедоступные свойства и методы родительского класса. Кроме того можно создать свои. И если имена будут совпадать, произойдёт переопределение. Будут браться значения дочернего класса.

```
>>> class Hero(Person):
...     def __init__(self, power, *args, **kwargs):
...         self.power = power
...         super().__init__(*args, **kwargs)
...     def change_health(self, other, quantity):
...         self.health += quantity * 2
...         other.health -= quantity * 2
...     def add_many_up(self):
...         self.up += 1
...         self.up = min(self.up, self._Person__max_up * 2)
... 
>>>         
>>> p1 = Hero('archery', 'Сильвана', 'Эльф', 120)
>>> p2 = Person('Маг', 'Тролль')
>>> print(f'{p1.health = }, {p2.health = }')
p1.health = 100, p2.health = 100
>>> p1.change_health(p2, 10)
>>> print(f'{p1.health = }, {p2.health = }')
p1.health = 120, p2.health = 80
>>> p2.change_health(p1, 10)
>>> print(f'{p1.health = }, {p2.health = }')
p1.health = 110, p2.health = 90
>>> p1.add_many_up()
>>> print(f'{p1.up = }')
p1.up = 4
```

В примере создан метод change_health с дополнительным множителем. Он срабатывает у героя. Но при вызове метода у экземпляра класса Person
срабатывает старый метод. В методе add_many_ups для обхода инкапсуляции используем запись self._Person__max_up. Экземпляр обращается к приватному атрибуту родительского класса, напрямую указав его.

### Множественное наследование

Класс может быть наследником сразу двух и более классов. В некоторых языках множественное наследование недоступно по причине усложнения кода. Например наследуя класс существо от классов птицы и рыбы позволит создать летающую рыбу или плавающую птицу.

```
>>> class Person:
...     __max_up = 3
...     _max_level = 80
...     def __init__(self, name, race='unknown', speed=100):
...         self.name = name
...         self.race = race
...         self.level = 1
...         self.health = 100
...         self._speed = speed
...         self.up = 3
...     def _check_level(self):
...         return self.level < self._max_level
...     def level_up(self):
...         if self._check_level():
...             self.level += 1
...     def change_health(self, other, quantity):
...         self.health += quantity
...         other.health -= quantity
...     def add_up(self):
...         self.up += 1
...         self.up = min(self.up, self.__max_up)
... 
>>> 
>>> class Address:
...     def __init__(self, country, city, street):
...         self.country = country or ''
...         self.city = city or ''
...         self.street = street or ''
...     def say_address(self):
...         return f'Адрес героя: {self.country}, {self.city}, {self.street}'
... 
>>> 
>>> class Weapon:
...     def __init__(self, left_hand, right_hand):
...         self.left_hand = left_hand or 'Клинок'
...         self.right_hand = right_hand or 'Лук'
... 
>>> 
>>> class Hero(Person, Address, Weapon):
...     def __init__(self, power, name=None, race=None, speed=None,country=None, city=None, street=None, left_hand=None, right_hand=None):
...         self.power = power
...         Person.__init__(self, name, race, speed)
...         Address.__init__(self, country, city, street)
...         Weapon.__init__(self, left_hand, right_hand)
...     def change_health(self, other, quantity):
...         self.health += quantity * 2
...         other.health -= quantity * 2
...     def add_many_ups(self):
...         self.up += 1
...         self.up = min(self.up, self._Person__max_up * 2)
... 
>>> 
>>> p1 = Hero('archery', 'Сильвана', 'Эльф', 120,
... country='Эльфляндия', street='Ночного эльфа',
... left_hand='Стрела')
>>> print(f'{p1.say_address()}')
Адрес героя: Эльфляндия, , Ночного эльфа
>>> print(f'{p1.right_hand = }, {p1.left_hand = }')
p1.right_hand = 'Лук', p1.left_hand = 'Стрела'
```

Мы создали классы Address и Weapon. Добавив их к нашему герою, получаем сочетание атрибутов и методов всех перечисленных классов. При
простых реализациях наследования достаточно функции super(). В отличие от вышестоящего примера, не стоит усложнять код до того состояния, когда внутренние механизмы не справляются с наследованием.

### MRO

**MRO** — method resolution order (порядок разрешения методов). Относится этот порядок не только к методам, но и ко всем атрибутам
класса. Это внутренний механизм, определяющий порядок наследования.

```
>>> class A:
...     def __init__(self):
...         print('Init class A')
...         self.data_a = 'A'
... 
>>> 
>>> class B:
...     def __init__(self):
...         print('Init class B')
...         self.data_b = 'B'
... 
>>> 
>>> class C:
...     def __init__(self):
...         print('Init class C')
...         self.data_c = 'C'
... 
>>> 
>>> class D:
...     def __init__(self):
...         print('Init class D')
...         self.data_d = 'D'
... 
>>> 
>>> class X1(A, C):
...     def __init__(self):
...         print('Init class X1')
...         super().__init__()
... 
>>> 
>>> class X2(B, D):
...     def __init__(self):
...         print('Init class X2')
...         super().__init__()
... 
>>> 
>>> class X3(A, D):
...     def __init__(self):
...         print('Init class X3')
...         super().__init__()
... 
>>> 
>>> class Z(X1, X2, X3):
...     def __init__(self):
...         print('Init class Z')
...         super().__init__()
... 
>>> 
>>> print(*Z.mro(), sep='\n')
<class '__main__.Z'>
<class '__main__.X1'>
<class '__main__.X2'>
<class '__main__.B'>
<class '__main__.X3'>
<class '__main__.A'>
<class '__main__.C'>
<class '__main__.D'>
<class 'object'>
```

1. Четыре класса A, B, C, D не имеют родительского класса. Точнее они наследуются от прародителя object. У каждого из классов есть по параметру.
2. Далее три класса X имеют по два родительских класса.
3. В финале класс Z наследуется от трёх классов X.

У каждого класса добавили текстовый вывод при вызове методу __init__. Также функция super, вызывает инициализацию родительского класса:

<img src=pics/mro.png>

У каждого класса есть метод mro, который вычисляет порядок наследования. Он отвечает за инициализацию каждого класса один раз в порядке слева направо и по старшинству, т.е. родитель не может быть инициализирован раньше дочернего класа.

- В первую очередь отрабатывает инициализация самого класса.
- Далее начинаем двигаться слева направо по списку родительских классов: X1, X2
- Следующим будет класс B. Почему он, а не X3? Класс B является родительским только для класса X2. Так мы не нарушаем порядок слева направо и старшинство.
- Следующим инициализируется X3, последний из родительских классов у Z.
- Далее идёт инициализация класса A. Он родитель для X1 и X3. Следовательно
его инициализация была невозможна раньше дочерних классов.
- Классы С и D инициализируются последними, они правее A, B и С в списке
родительских классов у “иксов”.
- Класс object всегда инициализируется в последнюю очередь.

Добавим несколько строк кода и посмотрим на результат:
```
>>> z = Z()
Init class Z
Init class X1
Init class X2
Init class B
>>> print(f'{z.data_b = }')
z.data_b = 'B'
>>> print(f'{z.data_a = }')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'Z' object has no attribute 'data_a'. Did you mean: 'data_b'?
```
Вызов метода __init__ остановился на классе B. Мы не дописали ему вызов super, считая что он и так не имеет наследников. В результате аргумент data_a не был создан в экземпляре класса z. Попробуем описать классу A дополнительный метод.

Попробуем описать классу A дополнительный метод:
```
class A:
    def __init__(self):
        print('Init class A')
        self.data_a = 'A'
    def say(self):
        print('Текст')
        print(self.data_b)
...


z = Z()
z.say(
```
Вызов метода say из класса A отработал без ошибок. Мы нашли его двигаясь по
цепочке линеаризации. При этом метод даже смог обратиться к свойству другого
класса. Связано это с тем, что мы работаем из экземпляра класса Z и он собрал в
себя аргументы и методы наследуемых классов.
Не стоит из родительских классов обращаться к аргументам и
методам дочерних классов или классов того же уровня наследования.

- Полиморфизм — свойство системы, позволяющее использовать объекты с одинаковым интерфейсом без информации о типе и внутренней структуре объекта.