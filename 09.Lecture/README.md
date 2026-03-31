# Декораторы

Для понимания декораторов необходимо разобрать следующие термины:

* (лексическая) область видимости
* замыкание (функции обертки)
* функция высшего порядка

## Области видимости

Для каждой функции создается своей лексический контекст со своей внутренней и внешней областями видимости:

*x* из внешней области:

```console
>>> def func(a):
...     res = x+a
...     return res
... 
>>> x = 100
>>> print(func(7))
107
```

*x* из внутренней области:

```console
>>> def func(a):
...     x = 3
...     res = x + a
...     return res
... 
>>> x = 100
>>> print(func(7))
10
```

Внутренняя область имеет приоритет, т.к. интерпретатор использует модель LEGB — порядок поиска имени:

* L — Local: локальная область внутри текущей функции.
* E — Enclosing: области внешних функций (для вложенных функций).
* G — Global: глобальная область модуля.
* B — Built-in: встроенные имена (len, print, и т.д.).

## Замыкания

**Лексическое замыкание** (англ. closure) в программировании — функция, в теле которой присутствуют ссылки на переменные, объявленные вне тела этой функции (Enclosing) в окружающем коде и не являющиеся её параметрами.

```console
>>> def outer(x):
...     def closure(y):
...             return x+y
...     return closure
... 
>>> add10 = outer(10)
>>> print(add10(5))
15
```

Замыкание запоминает значения из своей и внешней лексических областях видимости, даже когда поток программы больше не находится в замыкании.

### Замыкание без параметров

Данный вид замыкания вызывается по цепочки без сохранения промежуточного результата (параметра) в некую переменную.

```console
>>> def add_str(a, b):
...     return a + ' ' + b
... 
>>>     
>>> print(add_str('Hello', 'world!'))
Hello world!
```

Благодаря передаче одной функции другой мы можем создавать замыкания:

```console
>>> def add_one_str(a):
...     def add_two_str(b):
...         return a + ' ' + b
...     return add_two_str
... 
>>> 
>>> print(add_one_str('Hello')('world!'))
Hello world!
```

* add_two_str - без скобок, потому что передаем, а не вызываем (не инициализируем)
* add_one_str()() - с двумя парами скобок. Где, add_one_str('Hello') возвращает функцию add_two_str и уже она вызывается и принимает аргумент во вторых скобках.

#### Замыкание с параметрами

Т.к. функции можно присваивать в переменные как объекты, поэтому присвоим возвращенное замыкание с переданным ей параметром в переменные hello и bye:

```console
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

### Замыкания изменяемых объектов


```console
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

У каждой из двух функций hello и bye оказывается свой список names. Т.е. списка всего два, а не 5 (по количеству общему вызовов bye и hello), т.к. списки names живут не в контекстах add_two_str, в контекстах add_one_str, которая была вызвана всего два раза при создании переменной hello и bye.

### Замыкания неизменяемых объектов

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

nonlocal говорит Python, что переменная не из локальной области видимости, а с уровня выше. и позволяет прозрачно в неизменяемом типе менять данные, с помощью временной переменной, которая вскоре удаляется мусорщиком.
Причем nonlocal можно использовать с неизменяемыми, так и с изменяемыми типами данных, хуже не будет.

## Функции

**Функции Python** — [это объекты первого класса](https://habr.com/ru/companies/otus/articles/725374/), также каки числа, стоки, списки и словари. Их можно присваивать переменным, хранить в структурах данных, передавать в качестве аргументов другим функциям и даже возвращать в качестве значений из других функций.

### Функция высшего порядка

**Функции высшего порядка** - функция, которая принимает другую функцию в качестве аргумента или возвращает функцию в качестве значения.

```python
print((lambda x: x*x)(5))
```

## Декораторы (обертки)

**Декоратор** — структурный шаблон проектирования, предназначенный для динамического подключения дополнительного поведения к объекту.

### Декоратор без параметров

Замыкание переданной в качестве аргумента функции внутри другой функции называется декорированием функции.

Пример с нахождением факториала:

```console
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

* **main()** принимает на вход другую функцию, тут main декоратор, которым мы декорировали функцию factorial.
* **wrapper()** принимает пару параметров *args и **kwargs, данная запись позволяет принять любое число позиционных и ключевых аргументов.
* `result = func(*args, **kwargs)` - обязательная строка внутри wrapper.
* **factorial()** вычисляет факториал для заданного числа.
* **control()** - помещается wrapper() с замкнутой внутри функций func — нашей функцией factorial()

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
... print('>>> main()')
... main()
... print('>>> Завершаю main()')
Возвращаем декоратор A
Возвращаем декоратор B
Возвращаем декоратор C
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


Декорирование происходит всегда снизу вверх от декорируемой функцции main():

1. Инетпретатор преобразует ближайший декоратор @deco_a, создавая в памяти переменную main=deco_a(main)
2. **Возвращаем декоратор A** выводится на печать перед тем, как будет возвращен wrapper_a
3. Инетпретатор преобразует следующий декоратор @deco_b, создавая в памяти переменную main=deco_b(deco_a(main))
4. **Возвращаем декоратор B** выводится на печать перед тем, как будет возвращен wrapper_b
5. Инетпретатор преобразует последний декоратор @deco_c, создавая в памяти переменную main=deco_c(deco_b(deco_a(main)))
6. **Возвращаем декоратор C** выводится на печать перед тем, как будет возвращен wrapper_c
7. **>>> main()** - вывод на печать
8. Запуск на выполнение переменной main=deco_c(deco_b(deco_a(main)))
9. **Старт декоратора C** выводится на печать, т.к. выполняется wrapper_c
10. **Запускаю wrapper_b** выводится на печать
11. Запуск на выполнение переменной main=deco_b(deco_a(main))
12. **Старт декоратора B** выводится на печать, т.к. выполняется wrapper_b
13. **Запускаю wrapper_a** выводится на печать
14. Запуск на выполнение переменной main=deco_a(main)
15. **Старт декоратора A** выводится на печать
16. Запуск на выполнение тела функции самой main(), без оберток
17. **Запускаю main** выводится на печать
18. **Старт основной функции** выводится на печать
19. **Завершение декоратора A** выводится на печать
20. **Завершение декоратора B** выводится на печать
21. **Завершение декоратора C** выводится на печать

Порядок декорирования (т.е. порядок @deco_a, @deco_b, @deco_c) может привести к разным результатам.

### Дополнительные переменные в декораторе

Аналогично замыканию переменны, списков и строк, декоратор также может замыкать их в себе.

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

Когда в словаре есть ключ, декорируемая функция не вызывается, а ответ сразу возвращается из словаря. Если же в словаре нужного ключа, то выводится фраза "Вычисляю факториал для числа n" и происходит вычисление факториала для данного числа.

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

В разделе [Дополнительные переменные декоратора] мы использовали кэширующий декоратор, который можно заменить @cache из functools.

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