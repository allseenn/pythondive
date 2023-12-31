# Урок 9. Декораторы
Для решения данного домашнего задания вам необходимо воспользоваться сервисом автоматической проверки написанного кода.
Для того, чтобы успешно выполнить задание, необходимо перейти по каждой из представленных ссылок и решить все предложенные задачи. Будьте внимательны, количество попыток отправки кода на проверку ограничено! Вам дано 5 попыток на каждую задачу.
Прикреплять полученные решения не требуется. Итоговая оценка домашнего задания появится автоматически на платформе после решения всех задач. Полученная оценка не повлияет на получение итогового документа об обучении.

## Задания

### Задача 1

**Генерация случайных данных и нахождение корней квадратного уравнения**

Создайте функцию generate_csv_file(file_name, rows), которая будет генерировать по три случайны числа в каждой строке, от 100-1000 строк, и записывать их в CSV-файл. Функция принимает два аргумента:

file_name (строка) - имя файла, в который будут записаны данные.
rows(целое число) - количество строк (записей) данных, которые нужно сгенерировать.

Создайте функцию find_roots(a, b, c), которая будет находить корни квадратного уравнения вида ax^2 + bx + c = 0. Функция принимает три аргумента:

a, b, c (целые числа) - коэффициенты квадратного уравнения.

Функция возвращает:
None, если уравнение не имеет корней (дискриминант отрицателен).
Одно число, если уравнение имеет один корень (дискриминант равен нулю).
Два числа (корни), если уравнение имеет два корня (дискриминант положителен).

Создайте декоратор save_to_json(func), который будет оборачивать функцию find_roots. Декоратор выполняет следующие действия:
Читает данные из CSV-файла, переданного в аргументе функции, исходя из аргумента args[0].
Для каждой строки данных вычисляет корни квадратного уравнения с помощью функции find_roots.
Сохраняет результаты в формате JSON в файл results.json. Каждая запись JSON содержит параметры a, b, c и результаты вычислений.
Таким образом, после выполнения функций generate_csv_file и find_roots в файле results.json будет сохранена информация о параметрах и результатах вычислений для каждой строки данных из CSV-файла.

**Пример**

На входе:
```
generate_csv_file("input_data.csv", 101)
find_roots("input_data.csv")

with open("results.json", 'r') as f:
    data = json.load(f)

if 100<=len(data)<=1000:
    print(True)
else:
    print(f"Количество строк в файле не находится в диапазоне от 100 до 1000.")

print(len(data)==101)
```
На выходе:

```
True
True
```

Задача 2

**Пакет для работы с файлами 3**

Из созданных на уроке и в рамках домашнего задания функций, соберите пакет для работы с файлами.

Создайте файл __init__.py и запишите в него все функции:
save_to_json,
find_roots,
generate_csv_file.