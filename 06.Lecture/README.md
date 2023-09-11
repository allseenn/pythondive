# Модули

## import

**Модуль** — это файл, содержащий определения и операторы Python. Во время исполнения модуль представлен соответствующим объектом, атрибутами которого являются объявления, присутствующие в файле и объекты импортированные в этот модуль откуда-либо. Часто имя модуля заканчивается расширением
.py. При импорте расширение не указывается.

```
>>> import sys
>>> print(sys)
<module 'sys' (built-in)>
>>> print(sys.builtin_module_names)
('_abc', '_ast', '_bisect', '_blake2', '_codecs', '_collections', '_csv', '_datetime', '_elementtree', '_functools', '_heapq', '_imp', '_io', '_locale', '_md5', '_operator', '_pickle', '_posixsubprocess', '_random', '_sha1', '_sha256', '_sha3', '_sha512', '_signal', '_socket', '_sre', '_stat', '_statistics', '_string', '_struct', '_symtable', '_thread', '_tracemalloc', '_warnings', '_weakref', 'array', 'atexit', 'binascii', 'builtins', 'cmath', 'errno', 'faulthandler', 'fcntl', 'gc', 'grp', 'itertools', 'marshal', 'math', 'posix', 'pwd', 'pyexpat', 'select', 'spwd', 'sys', 'syslog', 'time', 'unicodedata', 'xxsubtype', 'zlib')
>>> print(*sys.path, sep='\n')

/usr/lib/python310.zip
/usr/lib/python3.10
/usr/lib/python3.10/lib-dynload
/home/User/.local/lib/python3.10/site-packages
/usr/local/lib/python3.10/dist-packages
/usr/lib/python3/dist-packages
```

- В первую очередь проверяется список встроенных модулей, который хранится в sys.builtin_module_names. Если имя модуля не найдено, проверка ведётся в каталогах файловой системы, которые перечислены в sys.path.
- В результате импорта имя sys было добавлено в глобальную область видимости. 
- Для того, чтобы получить доступ к переменным, функциям, классам и т.п. используется точечная нотация: имя_модуля<точка>имя_объекта.
- При импорте нескольких модулей каждый указывается с новой строки.

### from и as
```
>>> from sys import builtin_module_names, path
>>> print(builtin_module_names)
('_abc', '_ast', '_bisect', '_blake2', '_codecs', '_collections', '_csv', '_datetime', '_elementtree', '_functools', '_heapq', '_imp', '_io', '_locale', '_md5', '_operator', '_pickle', '_posixsubprocess', '_random', '_sha1', '_sha256', '_sha3', '_sha512', '_signal', '_socket', '_sre', '_stat', '_statistics', '_string', '_struct', '_symtable', '_thread', '_tracemalloc', '_warnings', '_weakref', 'array', 'atexit', 'binascii', 'builtins', 'cmath', 'errno', 'faulthandler', 'fcntl', 'gc', 'grp', 'itertools', 'marshal', 'math', 'posix', 'pwd', 'pyexpat', 'select', 'spwd', 'sys', 'syslog', 'time', 'unicodedata', 'xxsubtype', 'zlib')
>>> print(*path, sep='\n')

/usr/lib/python310.zip
/usr/lib/python3.10
/usr/lib/python3.10/lib-dynload
/home/Rostislav/.local/lib/python3.10/site-packages
/usr/local/lib/python3.10/dist-packages
/usr/lib/python3/dist-packages
```

Конструкция from import допускает перечисление импортируемых имён объектов через запятую в одной строке. После from всегда указывается один модуль.

```
from sys import builtin_module_names as bmn, path as p
```

### import * (со свездой)

Чтобы импортировать все глобальные объекты за исключением тех, чьи имена начинаются с символа подчёркивания.
```
from имя_модуля import *
```

Файл  **super_module.py**
```
from random import randint

SIZE = 100
_secret = 'qwerty'
__top_secret = '1q2w3e4r5t6y'
def func(a: int, b: int) -> str:
    z = f'В диапазоне от {a} до {b} получаем случайно {randint(a, b)}'
    return z

result = func(1, 6)
```
В модуле есть следующие объекты:
● глобальная функция randint
● глобальная константа SIZE
● глобальная защищенная переменная _secret
● глобальная приватная переменная __top_secret
● глобальная функция func
● локальные параметры функции a и b
● локальная переменная функции z
● глобальная переменная result

Если название объекта (переменной, функции и т.п.) начинается с символа подчёркивания, объект становится защищённым. Если имя начинается с двух подчёркиваний, объект становится приватным. Использование стиля from module import * зачастую приводит к неожиданным результатам

Файл **main.py**
```
from super_module import *

SIZE = 49.5

print(f'{SIZE = }\n{result = }')
print(f'{z = }') # NameError: name 'z' is not defined
print(f'{_secret = }') # NameError: name '_secret' defined
print(f'{func(100, 200) = }\n{randint(10, 20) = }')

def func(a: int, b: int) -> int:
    return a + b

print(f'{func(100, 200) = }')
```
При попытке обратиться к локальной и защищённой переменным получаем ошибки. Они не были импортированы “звёздочкой”.

Значения из модуля super_module.py затертые новыми из main.py:
- SIZE
- func()

#### __all__

Применяется для импорта списка объектов из модуля и модулей из пакета.


Файл **super_module.py**

```
from random import randint

__all__ = ['func', '_secret']

SIZE = 100
_secret = 'qwerty'
__top_secret = '1q2w3e4r5t6y'
def func(a: int, b: int) -> str:
z = f'В диапазоне от {a} до {b} получили {randint(a, b)}'
    return z

result = func(1, 6)
```

Переменной __all__ присваивается список имён объектов. В основной модуль попадут глобальные переменные указанные в списке имена независимо от того являются они публичными, защищёнными или приватными. Если указать в списке имя локального объекта, то получим ошибку.

## Модули

Виды модулей:

- встроенные модули,
- установленные внешние модули,
- свои модули (созданные разработчиком)
- модуль в составе пакета,
- сгруппированная коллекция модулей.

### Встроенные модули (Стандартная библиотека)

Импорт модулей стандартной библиотеки (далее батареек) пишется в начале файла, до импорта внешних и своих модулей.

Свойства "батареек":
1. Стандартная библиотека устанавливается вместе с интерпретатором
2. Батарейки достаточно импортировать
3. Множество задач можно решить с помощью батареек
4. Существуют старые батарейки, которые уже не работают, потому что делались давно под старые стандарты.

### Свои модули

Стандартная структура модуля следующая:
● документация по модулю в виде многострочного комментария (три пары
двойных кавычек),
● импорт необходимых пакетов, модулей, классов, функций и т.п. объектов,
● определение констант уровня модуля,
● создание классов модуля при ООП подходе,
● создание функций модуля,
● определение переменных модуля,
● покрытие тестами, если оно не вынесено в отдельный пакет,
● main код.

#### Первый учебный модуль **base_math.py**

```
"""Four basic mathematical operations.

Addition, subtraction, multiplication and division as functions.
"""

_START_SUM = 0
_START_MULT = 1
_BEGINNING = 0
_CONTINUATION = 1

def add(*args):
    res = _START_SUM
    for item in args:
        res += item
    return res

def sub(*args):
    res = args[_BEGINNING]
    for item in args[_CONTINUATION:]:
        res -= item
    return res

def mul(*args):
    res = _START_MULT
    for item in args:
        res *= item
    return res

def div(*args):
    res = args[_BEGINNING]
    for item in args[_CONTINUATION:]:
        res /= item
    return res

print(f'{add(2, 4) = }')
print(f'{add(2, 4, 6, 8) = }')
print(f'{sub(10, 2) = }')
print(f'{mul(2, 2, 2, 2, 2) = }')
print(f'{div(-100, 5, -2) = }')
```

#### __name__ == '__main__'

Файл **main.py**
```
import base_math

x = base_math.mul # Плохой приём
y = base_math._START_MULT # Очень плохой приём
z = base_math.sub(73, 42)
print(x(2, 3))
print(y)
print(z)
```

При запуске main.py наблюдаем вывод “принтов” из файла base_math.py раньше наших расчётов в “мейне”, т.к. команда import запускает импортируемый модуль на исполнение. Чтобы избежать лишнего вывода и расхода памяти, нужно перед каждым блоком печати в модуле поставить проверку на то, что текущий файл основным __main__ т.е. запускается самостоятельно, а не импортируется.

```
if __name__ == '__main__':
    print(f'{add(2, 4) = }')
```

# Пакеты

**Пакет** — это набор взаимосвязанных модулей, предназначенных для решения задач определенного класса некоторой предметной области. Пакеты — это способ структурирования пространства имен модулей Python с помощью «точечных имен модулей». Пакет представляет собой папку, в которой содержатся модули и другие пакеты и обязательный файл __init__.py, отвечающий за инициализацию пакета.

#### Второй учебный модуль **advanced_math.py**

Расширим наш первый учебный модуль, еще одним для научных операций

```
"""Two advanced mathematical operations.

Integer division and exponentiation."""

__all__ = ['div', 'exp']
_BEGINNING = 0
_CONTINUATION = 1

def div(*args):
    res = args[_BEGINNING]
    for item in args[_CONTINUATION:]:
        res //= item
    return res

def exp(*args):
    res = args[_BEGINNING]
    for item in args[_CONTINUATION:]:
        res **= item
    return res

if __name__ == '__main__':
    print(f'{div(42, 4) = }')
    print(f'{exp(2, 4, 6, 8) = }')
```

## Объединение модулей в пакет

В Python любая директория с файлом __init__.py автоматически становится пакетом:

- Создаём директорию mathematical
- Переносим в неё директорию файлы учебных модулей: base_math,py и advanced_math.py
- Создаём в каталоге пустой файл __init__.py. 

### Разница между модулем и пакетом

Пакет — директория с __init__.py файлом и другими py файлами — модулями. В Python любой пакет является одновременно и модулем. Это означает, что пакет можно импортировать в проект как и модуль. Так же это означает, что пакет может хранить в себе другие пакеты — директории с “инит” файлом. Глубина вложенности не ограничена.

### __init__.py
Внутри __init__.py можно прописать код, который будет выполняться при
импорте пакета. Можно добавить переменную __all__ с именами всех модулей пакета.

```
__all__ = ['base_math', 'advanced_math']
```

При добавлении или удалении модулей в пакет нужно изменять список __all__

## Варианты импорта

Указываем всю цепочку через точечную нотацию: имя пакета, имя модуля, имя объекта

```
import mathematical

x = mathematical.base_math.div(12, 5)
```

Для сокращения объема импортируемого кода указывают только нужные модули или объекты модуля (функции, переменные, константы и т.д.) через точечную нотацию

```
from mathematical import base_math as bm
from mathematical.advanced_math import exp

x = bm.div(12, 5)
z = exp(2, 3)
```

Импорт в другой модуль того же пакета можно осуществить через относительный импорт:

```
from .. import other_module1
from ..other_package import other_module2
```

Модуль, который является основным в вашем проекте должен использовать только абсолютные имена пакетов и модулей. Связано это с тем, что у запускаемого модуля в переменной __name__ хранится значение “__main__”, а не имя модуля.

## Пример стандартных модулей

### Модуль sys

Относится к группе служебных. Обеспечивает доступ к некоторым переменным, используемым или поддерживаемым интерпретатором, а также к функциям, тесно взаимодействующим с интерпретатором:

#### argv
Переменная argv содержит список. В нулевой ячейке имя запускаемого скрипта. В последующих ячейках переданные значения.

```
from sys import argv
print(argv)
```
Запуск скрипта из командной строки:
```
python script.py -d 42 -s "Hello world!" -k 100
```
Вывод
```
['script.py', '-d', '42', '-s', 'Hello world!', '-k', '100']
```

#### random

Генераторы псевдослучайных чисел модуля не должны использоваться в целях безопасности. Для обеспечения безопасности или криптографии необходимо использовать модуль secrets

Для управления состоянием используют следующие функции:
●
seed(a=None, version=2) — инициализирует генератор. Если значение a не указано, для инициализации используется текущее время ПК. Версия 2 используется со времён Python 3.2 как основная. 
● getstate() — возвращает объект с текущим состоянием генератора.
● setstate(state) — устанавливает новое состоянии генератора, принимая на вход объект, возвращаемый функцией getstate.

Полезные функции генерации чисел:

- randint(a, b) — генерация случайного целого числа в диапазоне от a включительно до b включительно — [a, b].
- uniform(a, b) — генерация случайного вещественного числа в диапазоне от a до b. Правая граница может как входить, так и не входить в возвращаемый диапазон. Зависит от способа округления.
- choice(seq) — возвращает случайный элемент из непустой последовательности.
- randrange(stop) или randrange(start, stop[, step]) работает как вложение функции range в функцию choice, т.е.choice(range(start, stop, step)). Возвращает случайное число от start до stop с шагом step.
- shuffle(x) — перемешивает случайным образом изменяемую последовательность in place, т.е. не создавая новую.
- sample(population, k, *, counts=None) — выбирает k уникальных элементов из последовательности population и возвращает их в новой последовательности. Параметр counts позволяет указать количество повторов элемента.

Все описанные функции представлены в листинге ниже:
```
import random as rnd

START = -100
STOP = 1_000
STEP = 10
data = [2, 4, 6, 8, 42, 73]

print(rnd.random())
rnd.seed(42)
state = rnd.getstate()
print(rnd.random())
rnd.setstate(state)
print(rnd.random())
print(rnd.randint(START, STOP))
print(rnd.uniform(START, STOP))
print(rnd.choice(data))
print(rnd.randrange(START, STOP, STEP))
print(data)
rnd.shuffle(data)
print(data)
print(rnd.sample(data, 2))
print(rnd.sample(data, 2, counts=[1, 1, 1, 1, 1, 100]))
```