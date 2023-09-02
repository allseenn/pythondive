# Основы пайтона (Basics of python)

Windows
```
python --version
```
Unix
```
python3 --version
```

## Виртуальное окружение

Виртуальное окружение созданное в одной ОС нельзя скопировать в другую ОС
### Создание окружения

```
mkdir project
cd project
python3 -m venv venv
```

Windows
```
venv\Scripts\activate
```

для Linux и MacOS
```
source venv/bin/activate
```

## Выход из окружения

```
deactivate
```

## PIP

### Установка пакета pip

```
pip install requests
```

### Вывод списка установленных пакетов pip

```
pip freeze
```

### Сохранение списка пакетов в файл requirements.txt

```
pip freeze > requirements.txt
```

### Установка зависимостей

```
pip install -r requirements.txt
```

## Интерпретатор python

### Символ _ повтор вывода

```
>>> 2+2
4
>>> _
4

```

### Написание сложного кода

После цикла или ветвления отступы ставим 4-мя пробелами

```
>>> a = 2
>>> b = 6
>>> while a < b:
...     print(a)
...     a+=1
... 
2
3
4
5
```

После цикла или ветвления два раза Enter

### Выход из интерпретатора

```
exit()
```
или

```
quit()
```

## Документация

### PEP-8 Python Style. (руководство по стилю)

- отступы в один пробел вокруг математических знаков "=", "*" и др
- имена переменных на английском строчными snake_case
- не использовать транслит
- первая буква переменной это буква или _, не должно быть цифры
- не использвать антипаттерн "магические числа" - числе у которых сложно найти объяснений в коде
- 4 отступа вместо фигурных скобок
- строки кода не должна превышать 120 символов
- последняя строка в файле должны быть пустой (одна)
- во вложенных циклах используются переменные i, j, k

PEP-257 (оформление документации/комментариев)


## Переменные 

В Python всё объект. Числа, строки, массивы и даже функции и классы являются объектом. Переменная в Python является указателем на объект.

Python является языком со строгой динамической типизацией. Это означает что тип объекта изменить невозможно он строго задаётся при создании объекта. При этом переменные могут ссылаться на объекты разных типов.

```
>>> a = 5
>>> a = "hello world"
>>> a = 42.0 * 3.141592 / 2.71828
>>> a
48.5405712435805
```

## Константы 
Констант нет - есть договоренность писать их капслоком

```
>>> MAX_COUNT = 1000
>>> ZERO = 0
>>> DATA_AFTER_DELETE = 'No data'
>>> DAY = 60 * 60 * 24
```

### True, False, None

True, False, None - это тоже константы

### Функция id()

возвращает адрес объекта в оперативной памяти

```
>>> print(id(a))
140004143929776
>>> a = 42.0 * 3.141592 / 2.71828
>>> print(id(a))
140004144147984
```

### Списко ключевых слов keyword.kwlist

Запрещено использовать в качестве имён переменных:

False, None, True, and, as, assert, async, await, break, case, class, continue, def, del, elif, else, except, finally, for, from, global, if, import, in, is, lambda, match, nonlocal, not, or, pass, raise, return, try, while, with, yield.

## Ввод и вывод

### Ввод

```
>>> name = input('Ваше имя: ')
Ваше имя: Slava
>>> name
'Slava'

```

### Вывод

```
print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)
```

```
>>> print(42)
42
>>> print(1, 2, 3, 4)
1 2 3 4
>>> print('Hello', ',', 'world', '!')
Hello , world !
```

## Ветвление

### if
```
>>> pwd = 'text'
>>> res = input('Input password: ')
Input password: if res == pwd:
>>> print('Доступ разрешён')
Доступ разрешён
```

### else

```
pwd = 'text'
res = input('Input password: ')
if res == pwd:
    print('Доступ разрешён')
    print('Но будьте осторожны')
else:
    print('Доступ запрещён')
    print('Работа завершена')
```

### elif

```
color = input('Твой любимый цвет: ')
if color == 'красный':
    print('Любитель яркого')
elif color == 'зелёный':
    print('Ты не охотник?')
elif color == 'синий':
    print('Ха, классика!')
else:
    print('Тебя не понять')
```

### match и case

```
color = input('Твой любимый цвет: ')
match color:
    case 'красный' | 'оранжевый':
        print('Любитель яркого')
    case 'зелёный':
        print('Ты не охотник?')
    case 'синий' | 'голубой':
        print('Ха, классика!')
    case _:
        print('Тебя не понять')
```

### or, and, not

● and — логическое умножение «И»;
● or — логическое сложение «ИЛИ»;
● not — логическое отрицание «НЕ».

```
if year % 4 != 0 or year % 100 == 0 and year % 400 != 0:
    print("Обычный")
else:
    print("Високосный")
```

### Ленивый if
Если в логическом выражении есть оператор or и первое значение то есть левое вернуло истину, дальнейшая проверка не происходит, возвращается True. Если в логическом выражении есть оператор and и левая половина вернула ложь, то возвращается False без проверки правой половины выражения.

### in
```
data = [0, 1, 1, 2, 3, 5, 8, 13, 21]
num = int(input('Введи число: '))
if num in data:
    print('Леонардо передаёт привет!')
```

### Тернарный if

```
my_math = int(input('2 + 2 = '))
print('Верно!' if 2 + 2 == my_math else 'Вы уверены?')
```

## Циклы

### while

Цикл while является циклом с предусловием

```
num = float(input('Введите число: '))
count = 0
while count < num:
    print(count)
    count += 2
```

### Синтаксический сахар
```
num = num + 1
num += 1
```

### Возврат в начало continue

```
num = float(input('Введите число: '))
STEP = 2
limit = num - STEP
count = -STEP
while count < limit:
    count += STEP
    if count % 12 == 0:
        continue
    print(count)
```

### Завершение цикла break

Конструкция while True: создаёт бесконечный цикл, где нужно завершение break

```
min_limit = 0
max_limit = 10
while True:
    print('Введи число между', min_limit, 'и', max_limit, '? ')
    num = float(input())
    if num < min_limit or num > max_limit:
        print('Неверно')
    else:
        break
print('Было введено число ' + str(num))
```

### else в цикле 

else может применятся не только к ветвлениям, но и к циклам

```
min_limit = 0
max_limit = 10
count = 3
while count > 0:
    print('Попытка ' + str(count))
    count -= 1
    num = float(input('Введи число между ' + str(min_limit) + ' и ' + str(max_limit) + ': '))
    if num < min_limit or num > max_limit:
        print('Неверно')
    else:
        break
else:
    print('Исчерпаны все попытки. Сожалею.')
    quit()
print('Было введено число ' + str(num))
```

Функция quit() аналог exit()

### итератор for in

```
data = [0, 1, 1, 2, 3, 5, 8, 13, 21]
for item in data:
    print(item)
```

### функция range()

range(start, stop, step)

```
num = int(input('Введите число: '))
for i in range(0, num, 2):
    print(i)
```

Аргументами функции range() должны быть целые числа, int()

### функция enumerate()

```
animals = ['cat', 'dog', 'wolf', 'rat', 'dragon']
for i, animal in enumerate(animals, start=1):
    print(i, animal)
```