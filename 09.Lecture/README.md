# Декораторы

## Замыкания

- **Замыкание** (англ. closure) в программировании — функция первого класса, в теле которой присутствуют ссылки на переменные, объявленные вне тела этой функции в окружающем коде и не являющиеся её параметрами.

**Функция первого класса** - это функция, которая была создана с целью передачи другим функциям. Он выполняет одну конкретную задачу, не имеет побочных эффектов и не предназначен для прямого вызова, а скорее для использования «другими функциями».

### Области видимости

```
>>> def func(a):
...     x = 3
...     res = x + a
...     return res
... 
>>> x = 100
>>> print(func(7))
10
```

### Функция высшего порядка

#### Замыкание функции без заданного параметра

```
>>> def add_str(a, b):
...     return a + ' ' + b
... 
>>>     
>>> print(add_str('Hello', 'world!'))
Hello world!
```

Благодаря передаче одной функции другой мы можем создавать замыкания:

```
>>> def add_one_str(a):
...     def add_two_str(b):
...         return a + ' ' + b
...     return add_two_str
... 
>>> 
>>> print(add_one_str('Hello')('world!'))
Hello world!
```
- add_two_str - без скобок, потому что передаем, а не вызываем (не инициализируем)
- add_one_str()() - с двумя парами скобок. Где, add_one_str('Hello') возвращает функцию add_two_str и уже она вызывается и принимает аргумент во вторых скобках.

#### Замыкаем функцию с заданными параметрами

Функции можно присваивать в переменные как объекты:

```
>>> def add_one_str(a):
...     def add_two_str(b):
...         return a + ' ' + b
...     return add_two_str
... 
>>> 
>>> hello = add_one_str('Hello')
>>> bye = add_one_str('Good bye')
>>> print(hello('world!'))
Hello world!
>>> print(hello('friend!'))
Hello friend!
>>> print(bye('wonderful world!'))
Good bye wonderful world!
>>> print(f'{type(add_one_str) = }, {add_one_str.__name__ = }, {id(add_one_str) = }')
type(add_one_str) = <class 'function'>, add_one_str.__name__ = 'add_one_str', id(add_one_str) = 139933281816704
>>> print(f'{type(hello) = }, {hello.__name__ = }, {id(hello) = }')
type(hello) = <class 'function'>, hello.__name__ = 'add_two_str', id(hello) = 139933281777472
>>> print(f'{type(bye) = }, {bye.__name__ = }, {id(bye) = }')
type(bye) = <class 'function'>, bye.__name__ = 'add_two_str', id(bye) = 139933281816544
```

В переменные hello и bye поместили результат работы функции add_one_str с разными аргументами

Вызывая переменные как функции с параметрами, объединяем строки передавая по одному параметру функции. 

Получаем замыкание функций с параметрами. 

Замкнутый (первый) параметр остается неизменным, при вызове функций (переменных) со вторым параметром.

В конце 2 принта содержат переменные, где type показывает, что переменные являются функцией, причем одной и той же, но с разным параметром, т.е. разными объектами, о чем говорят разные адреса в памяти.

### Изменяемые замыкания

Замыкания с изменяемыми типами данных (объектами):

```
>>> def add_one_str(a):
...     names = []
...     def add_two_str(b):
...         names.append(b)
...         return a + ', ' + ', '.join(names)
...     return add_two_str
... 
>>> 
>>> hello = add_one_str('Hello')
>>> bye = add_one_str('Good bye')
>>> print(hello('Alex'))
Hello, Alex
>>> print(hello('Karina'))
Hello, Alex, Karina
>>> print(bye('Alina'))
Good bye, Alina
>>> print(hello('John'))
Hello, Alex, Karina, John
>>> print(bye('Neo'))
Good bye, Alina, Neo
```

У каждой из двух функций hello и bye оказывается свой список names.

### Неизменяемые замыкания

Замыкания с неизменяемыми типами данных (объектами):

```
>>> def add_one_str(a):
...     text = ''
...     def add_two_str(b):
...         nonlocal text
...         text += ', ' + b
...         return a + text
...     return add_two_str
... 
>>>     
>>> hello = add_one_str('Hello')
>>> bye = add_one_str('Good bye')
>>> print(hello('Alex'))
Hello, Alex
>>> print(hello('Karina'))
Hello, Alex, Karina
>>> print(bye('Alina'))
Good bye, Alina
>>> print(hello('John'))
Hello, Alex, Karina, John
>>> print(bye('Neo'))
Good bye, Alina, Neo
```

Без nonlocal text была бы получена ошибка UnboundLocalError. 

nonlocal делает переменную видимой на уровень выше. и позволяет прозрачно в неизменяем типе менять данные, с помощью временной переменной, которая вскоре удаляется мусорщиком.

## Декораторы (обертки)

- **Декоратор** — структурный шаблон проектирования, предназначенный для динамического подключения дополнительного поведения к объекту.

### Простой декоратор (без параметров)

Замыкание переданной в качестве аргумента функции внутри другой функции называется декорированием функции.

Пример с нахождением факториала:

```
>>> import time
>>> 
>>> def main(func):
...     def wrapper(*args, **kwargs):
...         print(f'Запуск функции {func.__name__} в {time.time()}')
...         result = func(*args, **kwargs)
...         print(f'Результат функции {func.__name__}: {result}')
...         print(f'Завершение функции {func.__name__} в {time.time()}')
...         return result
...     return wrapper
... 
>>> 
>>> def factorial(n):
...     f = 1
...     for i in range(2, n + 1):
...         f *= i
...     return f
... 
>>> 
>>> print(f'{factorial(100) = }')
factorial(100) = 93326215443944152681699238856266700490715968264381621468592963895217599993229915608941463976156518286253697920827223758251185210916864000000000000000000000000
>>> control = main(factorial)
>>> print(f'{control.__name__ = }')
control.__name__ = 'wrapper'
>>> print(f'{control(100) = }')
Запуск функции factorial в 1696529274.2231383
Результат функции factorial: 93326215443944152681699238856266700490715968264381621468592963895217599993229915608941463976156518286253697920827223758251185210916864000000000000000000000000
Завершение функции factorial в 1696529274.2233374
control(100) = 93326215443944152681699238856266700490715968264381621468592963895217599993229915608941463976156518286253697920827223758251185210916864000000000000000000000000
```

- **main()** принимает на вход другую функцию, тут main декоратор, которым мы декорировали функцию factorial.
- **wrapper()** принимает пару параметров *args и **kwargs, данная запись позволяет принять любое число позиционных
и ключевых аргументов.
- __result = func(*args, **kwargs)__ - обязательная строка внутри wrapper.
- **factorial()** вычисляет факториал для заданного числа.
- **control()** - помещается wrapper() с замкнутой внутри функций func — нашей функцией factorial()

### @ (Синтаксический сахар)

**@** - более элегантная возможность создания декораторов, пишется непосредственно над определением функции или метода:

```
>>> import time
>>> 
>>> def main(func):
...     def wrapper(*args, **kwargs):
...         start = time.time()
...         func(*args, **kwargs)
...         end = time.time()
...         return end - start
...     return wrapper
... 
>>> @main
... def factorial(n):
...     f = 1
...     for i in range(2, n + 1):
...         f *= i
...     return f
... 
>>> print(factorial(1_000_000))
351.9936227798462
```

-**@main** - можно обойтись без присваивания control = main(factorial) и еще нескольких строк кода. Также сохранено старое имя функции factorial(). Функция декоратор должна быть определена раньше, чем использована, иначе получим ошибку NameError.

Понять где функция, замыкание или присвоение сложно. Если используется @, то сразу ясно что используется декоратор.

### Множественное декорирование

```
>>> def deco_a(func):
...     def wrapper_a(*args, **kwargs):
...         print('Старт декоратора A')
...         print(f'Запускаю {func.__name__}')
...         res = func(*args, **kwargs)
...         print(f'Завершение декоратора A')
...         return res
...     print('Возвращаем декоратор A')
...     return wrapper_a
... 
>>> 
>>> def deco_b(func):
...     def wrapper_b(*args, **kwargs):
...         print('Старт декоратора B')
...         print(f'Запускаю {func.__name__}')
...         res = func(*args, **kwargs)
...         print(f'Завершение декоратора B')
...         return res
...     print('Возвращаем декоратор B')
...     return wrapper_b
... 
>>> 
>>> def deco_c(func):
...     def wrapper_c(*args, **kwargs):
...         print('Старт декоратора C')
...         print(f'Запускаю {func.__name__}')
...         res = func(*args, **kwargs)
...         print(f'Завершение декоратора C')
...         return res
...     print('Возвращаем декоратор C')
...     return wrapper_c
... 
>>> @deco_c
... @deco_b
... @deco_a
... def main():
...     print('Старт основной функции')
... 
Возвращаем декоратор A
Возвращаем декоратор B
Возвращаем декоратор C
>>> 
>>> main()
Старт декоратора C
Запускаю wrapper_b
Старт декоратора B
Запускаю wrapper_a
Старт декоратора A
Запускаю main
Старт основной функции
Завершение декоратора A
Завершение декоратора B
Завершение декоратора C
```

Порядок декорирования (т.е. порядок @deco_a, @deco_b, @deco_c) может привести к разным результатам.

### Дополнительные замыкания 

Пример кэширующего декоратора со словарным замыканием (переменная _cache_dict)

```
>>> def cache(func):
...     _cache_dict = {}
...     def wrapper(*args):
...         if args not in _cache_dict:
...             _cache_dict[args] = func(*args)
...         return _cache_dict[args]
...     return wrapper
...
>>>
>>> @cache
... def factorial(n):
...     print(f'Вычисляю факториал для числа {n}')
...     f = 1
...     for i in range(2, n + 1):
...         f *= i
...     return f
...
>>>
>>> print(f'{factorial(10) = }')
Вычисляю факториал для числа 10
factorial(10) = 3628800
>>> print(f'{factorial(15) = }')
Вычисляю факториал для числа 15
factorial(15) = 1307674368000
>>> print(f'{factorial(10) = }')
factorial(10) = 3628800
>>> print(f'{factorial(20) = }')
Вычисляю факториал для числа 20
factorial(20) = 2432902008176640000
>>> print(f'{factorial(10) = }')
factorial(10) = 3628800
>>> print(f'{factorial(20) = }')
factorial(20) = 2432902008176640000
```

Когда в словаре есть ключ, декорируемая функция не вызывается, а ответ сразу возвращается из словаря.

Важно! Тут **kwargs не используется т.к. у нас уже есть словарь.

### Декоратор с параметрами

Тройная вложенность позволяет передавать параметры декоратору. Например с помощью функции первого порядка count() мы передали параметр 10, что бы он в обертке играл роль счетчика:

```
import time

def count(num = 1):
    def deco(func):
        def wrapper(*args, **kwargs):
            time_for_count = []
            result = None
            for _ in range(num):
                start = time.perf_counter()
                result = func(*args, **kwargs)
                stop = time.perf_counter()
                time_for_count.append(stop - start)
            print(f'Результаты замеров {time_for_count}')
            return result
        return wrapper
    return deco


@count(10)
def factorial(n):
    f = 1
    for i in range(2, n + 1):
        f *= i
    return f

    
print(f'{factorial(1000) = }')
print(f'{factorial(1000) = }')

```

## functools

Дополнительные возможности декорирования предоставляет модуль functools декоратор.
### @wraps

Добавим строку документации в функцию factorial из прошлого кода

```
import time

def count(num = 1):
    def deco(func):
        def wrapper(*args, **kwargs):
            time_for_count = []
            result = None
            for _ in range(num):
                start = time.perf_counter()
                result = func(*args, **kwargs)
                stop = time.perf_counter()
                time_for_count.append(stop - start)
            print(f'Результаты замеров {time_for_count}')
            return result
        return wrapper
    return deco


@count(10)
def factorial(n):
    """Returns the factorial of the number n."""
    f = 1
    for i in range(2, n + 1):
        f *= i
    return f

    
print(f'{factorial(1000) = }')
print(f'{factorial.__name__ = }')
help(factorial)

```

Но получаем не справку а вывод функции wrapper

```
...
>>> print(f'{factorial.__name__ = }')
factorial.__name__ = 'wrapper'
>>> help(factorial)
Help on function wrapper in module __main__:

wrapper(*args, **kwargs)
```

Чтобы исправить ситуацию, воспользуемся декоратором wraps из functools.

```
import time
from functools import wraps

def count(num = 1):
    def deco(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            time_for_count = []
            result = None
            for _ in range(num):
                start = time.perf_counter()
                result = func(*args, **kwargs)
                stop = time.perf_counter()
                time_for_count.append(stop - start)
            print(f'Результаты замеров {time_for_count}')
            return result
        return wrapper
    return deco


@count(10)
def factorial(n):
    """Returns the factorial of the number n."""
    f = 1
    for i in range(2, n + 1):
        f *= i
    return f

    
print(f'{factorial(1000) = }')
print(f'{factorial.__name__ = }')
help(factorial)

```

Декоратор @wraps добавляется к функции wrapper, т.е. к самой глубоко вложенной функции. В качестве аргумента wraps должен получить параметр декларируемой функции. Теперь factorial возвращает свои название и строку документации.

```
...
>>> print(f'{factorial.__name__ = }')
factorial.__name__ = 'factorial'
>>> help(factorial)
Help on function factorial in module __main__:

factorial(n)
    Returns the factorial of the number n.

```

### @cache

В разделе [Дополнительные замыкания] мы использовали кэширующий декоратор, который можно заменить @cache из functools.

```
>>> from functools import cache
>>>
>>> @cache
... def factorial(n):
...     print(f'Вычисляю факториал для числа {n}')
...     f = 1
...     for i in range(2, n + 1):
...         f *= i
...     return f
...
>>>
>>> print(f'{factorial(10) = }')
Вычисляю факториал для числа 10
factorial(10) = 3628800
>>> print(f'{factorial(15) = }')
Вычисляю факториал для числа 15
factorial(15) = 1307674368000
>>> print(f'{factorial(10) = }')
factorial(10) = 3628800
>>> print(f'{factorial(20) = }')
Вычисляю факториал для числа 20
factorial(20) = 2432902008176640000
>>> print(f'{factorial(10) = }')
factorial(10) = 3628800
>>> print(f'{factorial(20) = }')
factorial(20) = 2432902008176640000
```

Запись стала короче. Первые вызовы запускают функцию. Повторный вызов с уже передававшимся аргументом обрабатывается декоратором cache.