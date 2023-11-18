# ООП. Финал


## 1. Класс как функция

```
>>> class Number:
...     def __init__(self, num):
...         self.num = num
...
>>>
>>> n = Number(42)
>>> print(f'{callable(Number) = }')
callable(Number) = True
>>> print(f'{callable(n)= }')
callable(n)= False
```

- callable() функция, показывающая является ли ее аргумент объектом или нет.
- Number - это класс, который можно вызвать как функцию
- n - экземпляр класса, его вызвать нельзя

###  __call__

```
>>> from collections import defaultdict
>>> class Storage:
...     def __init__(self):
...         self.storage = defaultdict(list)
...     def __str__(self):
...         txt = '\n'.join((f'{k}: {v}' for k, v in self.storage.items()))
...         return f'Объекты хранилища по типам:\n{txt}'
...     def __call__(self, value):
...         self.storage[type(value)].append(value)
...         return f'К типу {type(value)} добавлен {value}'
...
...
>>> s = Storage()
>>> print(s(42))
К типу <class 'int'> добавлен 42
>>> print(s(1.22))
К типу <class 'float'> добавлен 1.22
>>> print(s(72))
К типу <class 'int'> добавлен 72
>>> print(s('Hello world!'))
К типу <class 'str'> добавлен Hello world!
>>> print(s(0))
К типу <class 'int'> добавлен 0
>>> print(s)
Объекты хранилища по типам:
<class 'int'>: [42, 72, 0]
<class 'float'>: [1.22]
<class 'str'>: ['Hello world!']
```

__call__ - метод, который позволяет вызывать один и тот же экземпляр класса, реализуем технологию мемоизации.

## 2. Итераторы

С помощью функции all() можно проверить является ли объект переданный в качестве аргумента итерируемым

```
>>> class Fibonacci:
...     def __init__(self, start, stop):
...         self.start = start
...         self.stop = stop
...         self.first = 0
...         self.second = 1
...
>>>
>>> all(Fibonacci(20, 100))
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'Fibonacci' object is not iterable
```

Как и ожидалось объект не итерируемый

###  __iter__ __next__

Любая итерация представляет из себя последовательный вызов функции next() с итератором в качестве аргумента.
Для возврата  значения необходимо определить дандер метод __next__:

```
>>> class Fibonacci:
...     def __init__(self, start, stop):
...         self.start = start
...         self.stop = stop
...         self.first = 0
...         self.second = 1
...     def __iter__(self):
...         return self
...     def __next__(self):
...         while self.first < self.stop:
...             self.first, self.second = self.second, self.first + self.second
...             if self.start <= self.first < self.stop:
...                 return self.first
...         raise StopIteration
...
>>>
>>> fib = Fibonacci(20, 100)
>>> for num in fib:
...     print(num)
...
21
34
55
89
```
Обязательным условием для завершения итерации является вызов ошибки StopIteration

## 3. with

**Дескриптор** — это атрибут объекта со “связанным поведением”, то есть такой
атрибут, при доступе к которому его поведение переопределяется методом
протокола дескриптора. Эти методы __get__, __set__ и __delete__. Если хотя
бы один из этих методов определен в объекте , то можно сказать что этот
метод дескриптор.