# Сериализация
● Сериализация — это процесс преобразования объекта в поток байтов для
сохранения или передачи в память, базу данных или файл.
● Десериализация — восстановление объектов из байт, сохранение которых
было произведено ранее. Процедура выгрузки «зафиксированной»
информации пользователем
## 1. JSON

JSON (JavaScript Object Notation) — это популярный формат текстовых данных, который используется для обмена данными в современных веб- и мобильных приложениях? для хранения неструктурированных данных в файлах журналов или базах данных NoSQL.

### Формат JSON
JSON похож на словарь питона.

Листинг import json:
```
{
    "id": 2,
    "name": "Ervin Howell",
    "username": "Antonette",
    "email": [
        "Shanna@melissa.tv",
        "antonette@howel.com"
        ],
    "address": {
        "street": "Victor Plains",
        "suite": "Suite 879",
        "city": "Wisokyburgh",
        "zipcode": "90566-7771",
        "geo": {
            "lat": "-43.9509",
            "lng": "-34.4618"
        }
        },
    "phone": "010-692-6593 x09125",
    "website": "anastasia.net",
    "company": {
        "name": "Deckow-Crist",
        "catchPhrase": "Proactive didactic contingency",
        "bs": "synergize scalable supply-chains"
        }
    }
```
Но при конвертации данные могут оказаться другими

<table>
<tr><th>Python</th><th>JSON</th><th>Python</th></tr>
<tr><td>dict</td><td>object</td><td>dict</td></tr>
<tr><td>list, tuple</td><td>array</td><td>list</td></tr>
<tr><td>str</td><td>string</td><td>str</td></tr>
<tr><td>int</td><td>number (int)</td><td>int</td></tr>
<tr><td>float</td><td>number (real)</td><td>float</td></tr>
<tr><td>True</td><td>true</td><td>True</td></tr>
<tr><td>False</td><td>false</td><td>False</td></tr>
<tr><td>None</td><td>null</td><td>None</td></tr>
</table>

Внимание: из tuple при конвертации из конвертации получится list
Для хранения нескольких JSON объектов, в Python используют list. 
Для хранения нескольких JSON объектов, в JSON используют array.

### Модуль JSON
В библиотеке есть стандартный модуль
import json 

#### JSON to Python

##### json.load
**Загрузка из файла user.json**:
```
>>> import json
>>> with open('user.json', 'r', encoding='utf-8') as f:
...     json_file = json.load(f)
... 
>>> print(f'{type(json_file) = }\n{json_file = }')
type(json_file) = <class 'dict'>
json_file = {'id': 2, 'name': 'Ervin Howell', 'username': 'Antonette', 'email': ['Shanna@melissa.tv', 'antonette@howel.com'], 'address': {'street': 'Victor Plains', 'suite': 'Suite 879', 'city': 'Wisokyburgh', 'zipcode': '90566-7771', 'geo': {'lat': '-43.9509', 'lng': '-34.4618'}}, 'phone': '010-692-6593 x09125', 'website': 'anastasia.net', 'company': {'name': 'Deckow-Crist', 'catchPhrase': 'Proactive didactic contingency', 'bs': 'synergize scalable supply-chains'}}
>>> print(f'{json_file["name"] = }')
json_file["name"] = 'Ervin Howell'
>>> print(f'{json_file["address"]["geo"] = }')
json_file["address"]["geo"] = {'lat': '-43.9509', 'lng': '-34.4618'}
>>> print(f'{json_file["email"] = }')
json_file["email"] = ['Shanna@melissa.tv', 'antonette@howel.com']
```

##### json.loads()
**Загрузка из строковой переменной:**

```
>>> import json
>>> json_text = """
... [
... {
... "userId": 1,
... "id": 9,
... "title": "nesciunt iure omnis dolorem tempora et accusantium",
... "body": "consectetur animi nesciunt iure dolore"
... },
... {
... "userId": 1,
... "id": 10,
... "title": "optio molestias id quia eum",
... "body": "quo et expedita modi cum officia vel magni"
... },
... {
... "userId": 2,
... "id": 11,
... "title": "et ea vero quia laudantium autem",
... "body": "delectus reiciendis molestiae occaecati non minima eveniet qui voluptatibus"
... },
... {
... "userId": 2,
... "id": 12,
... "title": "in quibusdam tempore odit est dolorem",
... "body": "praesentium quia et ea odit et ea voluptas et"
... }
... ]"""
>>>
>>> print(f'{type(json_text) = }\n{json_text = }')
type(json_text) = <class 'str'>
json_text = '\n[\n{\n"userId": 1,\n"id": 9,\n"title": "nesciunt iure omnis dolorem tempora et accusantium",\n"body": "consectetur animi nesciunt iure dolore"\n},\n{\n"userId": 1,\n"id": 10,\n"title": "optio molestias id quia eum",\n"body": "quo et expedita modi cum officia vel magni"\n},\n{\n"userId": 2,\n"id": 11,\n"title": "et ea vero quia laudantium autem",\n"body": "delectus reiciendis molestiae occaecati non minima eveniet qui voluptatibus"\n},\n{\n"userId": 2,\n"id": 12,\n"title": "in quibusdam tempore odit est dolorem",\n"body": "praesentium quia et ea odit et ea voluptas et"\n}\n]'
>>> json_list = json.loads(json_text)
>>> print(f'{type(json_list) = }\t{len(json_list) = }\n{json_list =}')
type(json_list) = <class 'list'>        len(json_list) = 4
json_list =[{'userId': 1, 'id': 9, 'title': 'nesciunt iure omnis dolorem tempora et accusantium', 'body': 'consectetur animi nesciunt iure dolore'}, {'userId': 1, 'id': 10, 'title': 'optio molestias id quia eum', 'body': 'quo et expedita modi cum officia vel magni'}, {'userId': 2, 'id': 11, 'title': 'et ea vero quia laudantium autem', 'body': 'delectus reiciendis molestiae occaecati non minima eveniet qui voluptatibus'}, {'userId': 2, 'id': 12, 'title': 'in quibusdam tempore odit est dolorem', 'body': 'praesentium quia et ea odit et ea voluptas et'}]
```
#### Python to JSON

##### json.dump

```
>>> import json
>>> 
>>> my_dict = {
...     "first_name": "Джон",
...     "last_name": "Смит",
...         "hobbies": ["кузнечное дело", "программирование", "путешествия"],
...     "age": 35,
...     "children": [
...         {
...         "first_name": "Алиса",
...         "age": 5
...         },
...         {
...         "first_name": "Маруся",
...         "age": 3
...         }
...     ]
... }
>>>
>>> print(f'{type(my_dict) = }\n{my_dict = }')
type(my_dict) = <class 'dict'>
my_dict = {'first_name': 'Джон', 'last_name': 'Смит', 'hobbies': ['кузнечное дело', 'программирование', 'путешествия'], 'age': 35, 'children': [{'first_name': 'Алиса', 'age': 5}, {'first_name': 'Маруся', 'age': 3}]}       
>>> with open("new_user.json", "w") as f:
...     json.dump(my_dict, f)
... 
```

В файл запишется информацию преобразующия русские символы на коды.
Что бы этого избежать нужно параметр ensure_ascii выключить.

```
with open('new_user.json', 'w', encoding='utf-8') as f:
    json.dump(my_dict, f, ensure_ascii=False)
```
##### json.dumps

```
>>> import json
>>> my_dict = {
...     "first_name": "Джон",
...     "last_name": "Смит",
...         "hobbies": ["кузнечное дело", "программирование", "путешествия"],
...     "age": 35,
...     "children": [
...         {
...         "first_name": "Алиса",
...         "age": 5
...         },
...         {
...         "first_name": "Маруся",
...         "age": 3
...         }
...     ]
... }
>>>
>>> dict_to_json_text = json.dumps(my_dict)
>>> print(f'{type(dict_to_json_text) = }\n{dict_to_json_text = }')
type(dict_to_json_text) = <class 'str'>
dict_to_json_text = '{"first_name": "\\u0414\\u0436\\u043e\\u043d", "last_name": "\\u0421\\u043c\\u0438\\u0442", "hobbies": ["\\u043a\\u0443\\u0437\\u043d\\u0435\\u0447\\u043d\\u043e\\u0435 \\u0434\\u0435\\u043b\\u043e", "\\u043f\\u0440\\u043e\\u0433\\u0440\\u0430\\u043c\\u043c\\u0438\\u0440\\u043e\\u0432\\u0430\\u043d\\u0438\\u0435", "\\u043f\\u0443\\u0442\\u0435\\u0448\\u0435\\u0441\\u0442\\u0432\\u0438\\u044f"], "age": 35, "children": [{"first_name": "\\u0410\\u043b\\u0438\\u0441\\u0430", "age": 5}, {"first_name": "\\u041c\\u0430\\u0440\\u0443\\u0441\\u044f", "age": 3}]}'
```

##### Параметры методов dump и dumps

- **indent** отвечает за форматирование с отступами. Теперь JSON выводится не в одну строку, а в несколько. Читать стало удобнее, но размер увеличился.
- **separators** принимает на вход кортеж из двух строковых элементов.
*Первый* — символ разделитель элементов. По умолчанию это запятая и пробел. 
*Второй* — разделитель ключа и значения. По умолчанию это двоеточие и пробел. Передав запятую и двоеточие без пробела JSON стал компактнее.
**sort_keys** отвечает за сортировку ключей по алфавиту. Нужна сортировка или нет, решать только вам.

```
>>> res = json.dumps(my_dict, indent=2, separators=(',', ':'), sort_keys=True)
>>> res
'{\n  "age":35,\n  "children":[\n    {\n      "age":5,\n      "first_name":"\\u0410\\u043b\\u0438\\u0441\\u0430"\n    },\n    {\n      "age":3,\n      "first_name":"\\u041c\\u0430\\u0440\\u0443\\u0441\\u044f"\n    }\n  ],\n  "first_name":"\\u0414\\u0436\\u043e\\u043d",\n  "hobbies":[\n    "\\u043a\\u0443\\u0437\\u043d\\u0435\\u0447\\u043d\\u043e\\u0435 \\u0434\\u0435\\u043b\\u043e",\n    "\\u043f\\u0440\\u043e\\u0433\\u0440\\u0430\\u043c\\u043c\\u0438\\u0440\\u043e\\u0432\\u0430\\u043d\\u0438\\u0435",\n    "\\u043f\\u0443\\u0442\\u0435\\u0448\\u0435\\u0441\\u0442\\u0432\\u0438\\u044f"\n  ],\n  "last_name":"\\u0421\\u043c\\u0438\\u0442"\n}'
```
## CSV

CSV (от англ. Comma-Separated Values — значения, разделённые запятыми)

### Формат CSV
Формат не до конца стандартизирован. Например запятая как символ разделитель может являться частью текста. Чтобы не учитывать такие запятые, можно использовать кавычки. Но тогда кавычки не могут быть частью строки. Кроме того десятичная запятая используется для записи вещественных чисел в некоторых странах.

### Модуль CSV
import csv

#### csv.reader

Чтение из файла
```
>>> import csv
>>> with open('biostats_tab.csv', 'r', newline='') as f:
...     csv_file = csv.reader(f, dialect='excel-tab', quoting=csv.QUOTE_NONNUMERIC)
...     for line in csv_file:
...         print(line)
...     print(type(line))
...
... 
['Name', 'Sex', 'Age', 'Height(in)', 'Weight(lbs)']
['Alex', 'M', 41.0, 74.0, 170.0]
['Bert', 'M', 42.0, 68.0, 166.0]
['Carl', 'M', 32.0, 70.0, 155.0]
['Dave', 'M', 39.0, 72.0, 167.0]
['Elly', 'F', 30.0, 66.0, 124.0]
['Fran', 'F', 33.0, 66.0, 115.0]
['Gwen', 'F', 26.0, 64.0, 121.0]
['Hank', 'M', 30.0, 71.0, 158.0]
['Ivan', 'M', 53.0, 72.0, 175.0]
['Jake', 'M', 32.0, 69.0, 143.0]
['Kate', 'F', 47.0, 69.0, 139.0]
['Luke', 'M', 34.0, 72.0, 163.0]
['Myra', 'F', 23.0, 62.0, 98.0]
['Neil', 'M', 36.0, 75.0, 160.0]
['Omar', 'M', 38.0, 70.0, 145.0]
['Page', 'F', 31.0, 67.0, 135.0]
['Quin', 'M', 29.0, 71.0, 176.0]
['Ruth', 'F', 28.0, 65.0, 131.0]
<class 'list'>
```
- Важно! При работе с CSV необходимо указывать внутри open() параметр newline=''.
Кроме файлового дескриптора можно передать любой объект поддерживающий итерацию и возвращающий строки.
- **dialect**='excel-tab' — указали диалект с табуляцией в качестве разделителя
- **quoting**=csv.QUOTE_NONNUMERIC — передали встроенную константу, указывающую функции, что числа без кавычек необходимо преобразовать к типу float.

#### csv.writer

Запись в файл:

```
>>> import csv
>>> 
>>> with (open('biostats_tab.csv', 'r', newline='') as f_read, open('new_biostats.csv', 'w', newline='',encoding='utf-8') as f_write):
...     csv_read = csv.reader(f_read, dialect='excel-tab', quoting=csv.QUOTE_NONNUMERIC)
...     csv_write = csv.writer(f_write, dialect='excel', delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
...     all_data = []
...     for i, line in enumerate(csv_read):
...         if i == 0:
...             csv_write.writerow(line)
...         else:
...             line[2] += 1
...             for j in range(2, 4 + 1):
...                 line[j] = int(line[j])
...             all_data.append(line)
...     csv_write.writerows(all_data)
... 
43
```
Данные в файл не записываются пока у возвращённого объекта не будет вызван метод writerow для записи одной строки или writerows для нескольких.

1. Используя менеджер контекста with открыли два файла. Из первого читаем
информацию, а второй создаём для записи.
2. Функция reader возвращает объект csv_read для чтения как в пример выше.
3. Функция writer возвращает объект csv_write для записи. Мы указали:
- a. диалект “excel”
- b. в качестве разделителя столбцов будем использовать пробел
- c. если символ разделитель (пробел) есть в данных, экранируем их вертикальной чертой
- d. символ экранирования используем по минимум, только там где он необходим для разрешения конфликта с разделителем
4. В цикле читаем все строки из исходного файл. При этом строку с заголовком
сразу записываем методом writerow.
5. Для остальных строк увеличиваем возраст на единицу, преобразуем
вещественные числа в целые и сохраняем список в матрицу all_data
6. Одним запросом writerows(all_data) сохраняем матрицу в файл.

#### Класс csv.DictReader

##### restval
Если передать “лишний” ключ count, ему присвоится значение из параметра restval:
```
>>> import csv
>>> 
>>> with open('biostats_tab.csv', 'r', newline='') as f:
...     csv_file = csv.DictReader(f, fieldnames=["name", "sex", "age", "height", "weight", "office"], restkey="new", restval="Main Office", dialect='excel-tab', quoting=csv.QUOTE_NONNUMERIC)
...     for line in csv_file:
...         print(f'{line = }')
...         print(f'{line["name"] = }\t{line["age"] = }')
...
line = {'name': 'Name', 'sex': 'Sex', 'age': 'Age', 'height': 'Height (in)', 'weight': 'Weight (lbs)', 'office': 'Main Office'}
line["name"] = 'Name'   line["age"] = 'Age'
line = {'name': 'Alex', 'sex': 'M', 'age': 41.0, 'height': 74.0, 'weight': 170.0, 'office': 'Main Office'}     
line["name"] = 'Alex'   line["age"] = 41.0
line = {'name': 'Bert', 'sex': 'M', 'age': 42.0, 'height': 68.0, 'weight': 166.0, 'office': 'Main Office'}     
line["name"] = 'Bert'   line["age"] = 42.0
line = {'name': 'Carl', 'sex': 'M', 'age': 32.0, 'height': 70.0, 'weight': 155.0, 'office': 'Main Office'}     
line["name"] = 'Carl'   line["age"] = 32.0
line = {'name': 'Dave', 'sex': 'M', 'age': 39.0, 'height': 72.0, 'weight': 167.0, 'office': 'Main Office'}     
line["name"] = 'Dave'   line["age"] = 39.0
line = {'name': 'Elly', 'sex': 'F', 'age': 30.0, 'height': 66.0, 'weight': 124.0, 'office': 'Main Office'}     
line["name"] = 'Elly'   line["age"] = 30.0
line = {'name': 'Fran', 'sex': 'F', 'age': 33.0, 'height': 66.0, 'weight': 115.0, 'office': 'Main Office'}     
line["name"] = 'Fran'   line["age"] = 33.0
line = {'name': 'Gwen', 'sex': 'F', 'age': 26.0, 'height': 64.0, 'weight': 121.0, 'office': 'Main Office'}     
line["name"] = 'Gwen'   line["age"] = 26.0
line = {'name': 'Hank', 'sex': 'M', 'age': 30.0, 'height': 71.0, 'weight': 158.0, 'office': 'Main Office'}     
line["name"] = 'Hank'   line["age"] = 30.0
line = {'name': 'Ivan', 'sex': 'M', 'age': 53.0, 'height': 72.0, 'weight': 175.0, 'office': 'Main Office'}     
line["name"] = 'Ivan'   line["age"] = 53.0
line = {'name': 'Jake', 'sex': 'M', 'age': 32.0, 'height': 69.0, 'weight': 143.0, 'office': 'Main Office'}     
line["name"] = 'Jake'   line["age"] = 32.0
line = {'name': 'Kate', 'sex': 'F', 'age': 47.0, 'height': 69.0, 'weight': 139.0, 'office': 'Main Office'}     
line["name"] = 'Kate'   line["age"] = 47.0
line = {'name': 'Luke', 'sex': 'M', 'age': 34.0, 'height': 72.0, 'weight': 163.0, 'office': 'Main Office'}     
line["name"] = 'Luke'   line["age"] = 34.0
line = {'name': 'Myra', 'sex': 'F', 'age': 23.0, 'height': 62.0, 'weight': 98.0, 'office': 'Main Office'}      
line["name"] = 'Myra'   line["age"] = 23.0
line = {'name': 'Neil', 'sex': 'M', 'age': 36.0, 'height': 75.0, 'weight': 160.0, 'office': 'Main Office'}     
line["name"] = 'Neil'   line["age"] = 36.0
line = {'name': 'Omar', 'sex': 'M', 'age': 38.0, 'height': 70.0, 'weight': 145.0, 'office': 'Main Office'}     
line["name"] = 'Omar'   line["age"] = 38.0
line = {'name': 'Page', 'sex': 'F', 'age': 31.0, 'height': 67.0, 'weight': 135.0, 'office': 'Main Office'}     
line["name"] = 'Page'   line["age"] = 31.0
line = {'name': 'Quin', 'sex': 'M', 'age': 29.0, 'height': 71.0, 'weight': 176.0, 'office': 'Main Office'}     
line["name"] = 'Quin'   line["age"] = 29.0
line = {'name': 'Ruth', 'sex': 'F', 'age': 28.0, 'height': 65.0, 'weight': 131.0, 'office': 'Main Office'}     
line["name"] = 'Ruth'   line["age"] = 28.0
```
##### restkey
Если ключей меньше, чем столбцов, нужен параметр restkey. Все столбцы без ключа сохраняются как элементы списка в restkey:
```
>>> import csv
>>> 
>>> with open('biostats_tab.csv', 'r', newline='') as f:
...     csv_file = csv.DictReader(f, fieldnames=["name", "sex", "age", ], restkey="new", restval="Main Office",dialect='excel-tab', quoting=csv.QUOTE_NONNUMERIC)
...     for line in csv_file:
...         print(f'{line = }')
...         print(f'{line["name"] = }\t{line["age"] = }')
...
line = {'name': 'Name', 'sex': 'Sex', 'age': 'Age', 'new': ['Height (in)', 'Weight (lbs)']}
line["name"] = 'Name'   line["age"] = 'Age'
line = {'name': 'Alex', 'sex': 'M', 'age': 41.0, 'new': [74.0, 170.0]}
line["name"] = 'Alex'   line["age"] = 41.0
line = {'name': 'Bert', 'sex': 'M', 'age': 42.0, 'new': [68.0, 166.0]}
line["name"] = 'Bert'   line["age"] = 42.0
line = {'name': 'Carl', 'sex': 'M', 'age': 32.0, 'new': [70.0, 155.0]}
line["name"] = 'Carl'   line["age"] = 32.0
line = {'name': 'Dave', 'sex': 'M', 'age': 39.0, 'new': [72.0, 167.0]}
line["name"] = 'Dave'   line["age"] = 39.0
line = {'name': 'Elly', 'sex': 'F', 'age': 30.0, 'new': [66.0, 124.0]}
line["name"] = 'Elly'   line["age"] = 30.0
line = {'name': 'Fran', 'sex': 'F', 'age': 33.0, 'new': [66.0, 115.0]}
line["name"] = 'Fran'   line["age"] = 33.0
line = {'name': 'Gwen', 'sex': 'F', 'age': 26.0, 'new': [64.0, 121.0]}
line["name"] = 'Gwen'   line["age"] = 26.0
line = {'name': 'Hank', 'sex': 'M', 'age': 30.0, 'new': [71.0, 158.0]}
line["name"] = 'Hank'   line["age"] = 30.0
line = {'name': 'Ivan', 'sex': 'M', 'age': 53.0, 'new': [72.0, 175.0]}
line["name"] = 'Ivan'   line["age"] = 53.0
line = {'name': 'Jake', 'sex': 'M', 'age': 32.0, 'new': [69.0, 143.0]}
line["name"] = 'Jake'   line["age"] = 32.0
line = {'name': 'Kate', 'sex': 'F', 'age': 47.0, 'new': [69.0, 139.0]}
line["name"] = 'Kate'   line["age"] = 47.0
line = {'name': 'Luke', 'sex': 'M', 'age': 34.0, 'new': [72.0, 163.0]}
line["name"] = 'Luke'   line["age"] = 34.0
line = {'name': 'Myra', 'sex': 'F', 'age': 23.0, 'new': [62.0, 98.0]}
line["name"] = 'Myra'   line["age"] = 23.0
line = {'name': 'Neil', 'sex': 'M', 'age': 36.0, 'new': [75.0, 160.0]}
line["name"] = 'Neil'   line["age"] = 36.0
line = {'name': 'Omar', 'sex': 'M', 'age': 38.0, 'new': [70.0, 145.0]}
line["name"] = 'Omar'   line["age"] = 38.0
line = {'name': 'Page', 'sex': 'F', 'age': 31.0, 'new': [67.0, 135.0]}
line["name"] = 'Page'   line["age"] = 31.0
line = {'name': 'Quin', 'sex': 'M', 'age': 29.0, 'new': [71.0, 176.0]}
line["name"] = 'Quin'   line["age"] = 29.0
line = {'name': 'Ruth', 'sex': 'F', 'age': 28.0, 'new': [65.0, 131.0]}
line["name"] = 'Ruth'   line["age"] = 28.0
```
#### Класс csv.DictWriter

```
>>> import csv                       
>>> from typing import Iterator
>>> with (open('biostats_tab.csv', 'r', newline='') as f_read, open('biostats_new.csv', 'w', newline='', encoding='utf-8') as f_write):
...     csv_read: Iterator[dict] = csv.DictReader(f_read, fieldnames=["name", "sex", "age", "height", "weight", "office"], restval="Main Office", dialect='excel-tab', quoting=csv.QUOTE_NONNUMERIC)
...     csv_write = csv.DictWriter(f_write, fieldnames=["id", "name", "office", "sex", "age", "height", "weight"], dialect='excel-tab', quoting=csv.QUOTE_ALL)
...     csv_write.writeheader()
...     all_data = []
...     for i, dict_row in enumerate(csv_read):
...         if i != 0:
...             dict_row['id'] = i
...             dict_row['age'] += 1
...             all_data.append(dict_row)
...     csv_write.writerows(all_data)
...
52
```
Класс DictWriter получил список полей для записи, где добавлено новое поле id. В качестве диалекта выбран excel с табуляцией. В параметре quoting указали, что все значения стоит заключать в кавычки.
Новый для нас метод writeheader сохранил первую строку с заголовками в том порядке, в котором мы их перечислили в параметре fieldnames. Далее мы работаем с элементами словаря и формируем список словарей для одноразовой записи в файл.
Важно! Обратите внимание на импорт объекта Iterator из модуля typing. При написании кода IDE подсвечивала возможные ошибки, так как не понимала что за объект csv_read. Запись csv_read: Iterator[dict] = … сообщает, что мы используем объект итератор, который возвращает словари. После уточнения типа IDE исключила подсветку “ошибок”.

```
import csv
>>> with open('quest.csv', 'w', newline='', encoding='utf-8') as f_write:
...     csv_write = csv.DictWriter(f_write, fieldnames=["number", "name", "data"], restval='Hello world!',dialect='excel', delimiter='#', quotechar='=', quoting=csv.QUOTE_NONNUMERIC)
...     csv_write.writeheader()
...     dict_row = {}
...     for i in range(10):
...         dict_row['number'] = i
...         dict_row['name'] = str(i)
...         csv_write.writerow(dict_row)
... 
24
22
22
22
22
22
22
22
22
22
22
```

## 3. Pickle
Python предлагает модуль pickle для сериализации и десериализации своих структур в поток байт
Важно! Не используйте pickle с набором байт, которые вы не знаете. 
```
>>> import pickle
>>> res = pickle.loads(b"cos\nsystem\n(S'echo Hello world!'\ntR.")
Hello world!
>>> print(res)
0
```
Модуль pickle имеет несколько протоколов, не совместимых с более старыми версиями. Версия №4 является дефолтной начиная с python 3.8.

### Структуры данных pickle
● None, True и False;
● int, float, complex;
● str, bytes, bytearrays;
● tuple, list, set, dict если они содержат объекты, обрабатываемые pickle;
● встроенные функции и функции созданные разработчиком и доступные из
верхнего уровня модуля, кроме lambda функций;
● классы доступные из верхнего уровня модуля;
● экземпляры классов, если pickle смог обработать их дандер __dict__ или
результат вызова метода __getstate__().

### pickle.dumps
dumps() преобразует структуру (словарь) в строку байт:
```
>>> import pickle
>>> 
>>> my_dict = {
...     "first_name": "Джон",
...     "last_name": "Смит",
...         "hobbies": ["кузнечное дело", "программирование", "путешествия"],
...     "age": 35,
...     "children": [
...         {
...         "first_name": "Алиса",
...         "age": 5
...         },
...         {
...         "first_name": "Маруся",
...         "age": 3
...         }
...     ]
... }
>>> print(my_dict)
{'first_name': 'Джон', 'last_name': 'Смит', 'hobbies': ['кузнечное дело', 'программирование', 'путешествия'], 'age': 35, 'children': [{'first_name': 'Алиса', 'age': 5}, {'first_name': 'Маруся', 'age': 3}]}
>>> res = pickle.dumps(my_dict, protocol=pickle.DEFAULT_PROTOCOL)
>>> print(f'{res = }')
res = b'\x80\x04\x95\xe3\x00\x00\x00\x00\x00\x00\x00}\x94(\x8c\nfirst_name\x94\x8c\x08\xd0\x94\xd0\xb6\xd0\xbe\xd0\xbd\x94\x8c\tlast_name\x94\x8c\x08\xd0\xa1\xd0\xbc\xd0\xb8\xd1\x82\x94\x8c\x07hobbies\x94]\x94(\x8c\x1b\xd0\xba\xd1\x83\xd0\xb7\xd0\xbd\xd0\xb5\xd1\x87\xd0\xbd\xd0\xbe\xd0\xb5 \xd0\xb4\xd0\xb5\xd0\xbb\xd0\xbe\x94\x8c \xd0\xbf\xd1\x80\xd0\xbe\xd0\xb3\xd1\x80\xd0\xb0\xd0\xbc\xd0\xbc\xd0\xb8\xd1\x80\xd0\xbe\xd0\xb2\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb5\x94\x8c\x16\xd0\xbf\xd1\x83\xd1\x82\xd0\xb5\xd1\x88\xd0\xb5\xd1\x81\xd1\x82\xd0\xb2\xd0\xb8\xd1\x8f\x94e\x8c\x03age\x94K#\x8c\x08children\x94]\x94(}\x94(h\x01\x8c\n\xd0\x90\xd0\xbb\xd0\xb8\xd1\x81\xd0\xb0\x94h\nK\x05u}\x94(h\x01\x8c\x0c\xd0\x9c\xd0\xb0\xd1\x80\xd1\x83\xd1\x81\xd1\x8f\x94h\nK\x03ueu.'
```

Попробуем сохранить объекты, неподдерживаемые JSON в бинарный файл.

```
>>> import pickle
>>> def func(a, b, c):
...     return a + b + c
...
>>> my_dict = {"numbers": [42, 4.1415, 7+3j], "functions": (func, sum, max), "others": {True, False, 'Hello world!'},}
>>> with open('my_dict.pickle', 'wb') as f:
...     pickle.dump(my_dict, f)
...
... 
```
Функция, как структура данных, сохранена в бинарном файле my_dict.pickle

#### picle.loads
Загрузим данные из файла my_dict.pikle, который создали ранее.

```
>>> import pickle                
>>> 
>>> def func(a, b, c):
...     return a * b * c
...
>>> with open('my_dict.pickle', 'rb') as f:
...     new_dict = pickle.load(f)
...
>>> print(f'{new_dict = }')
new_dict = {'numbers': [42, 4.1415, (7+3j)], 'functions': (<function func at 0x000001EB30A53E20>, <built-in function sum>, <built-in function max>), 'others': {False, True, 'Hello world!'}}
>>> print(f'{new_dict["functions"][0](2, 3, 4) = }')
new_dict["functions"][0](2, 3, 4) = 24
```

Привызове функции func, которая лежит в нулевой ячейке кортежа по ключу functions мы получили не сумму трёх чисел, а произведение. В файле, где произведена десериализация есть функция func, которая умножает числа. Модуль pickle указал в словаре её, а не исходную. Более того, если бы функции с нужным именем не было, десериализация завершилась бы ошибкой.