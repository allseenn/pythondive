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
>>> with open('biostats.csv', 'r', newline='') as f:
...     csv_file = csv.reader(f)
...     for line in csv_file:
...         print(line)
...
...     print(type(line))
...
['Name', 'Sex', 'Age', 'Height (in)', 'Weight (lbs)']
['Alex', 'M', '41', '74', '170']
['Bert', 'M', '42', '68', '166']
['Carl', 'M', '32', '70', '155']
['Dave', 'M', '39', '72', '167']
['Elly', 'F', '30', '66', '124']
['Fran', 'F', '33', '66', '115']
['Gwen', 'F', '26', '64', '121']
['Hank', 'M', '30', '71', '158']
['Ivan', 'M', '53', '72', '175']
['Jake', 'M', '32', '69', '143']
['Kate', 'F', '47', '69', '139']
['Luke', 'M', '34', '72', '163']
['Myra', 'F', '23', '62', '98']
['Neil', 'M', '36', '75', '160']
['Omar', 'M', '38', '70', '145']
['Page', 'F', '31', '67', '135']
['Quin', 'M', '29', '71', '176']
['Ruth', 'F', '28', '65', '131']
<class 'list'>
```
Важно! При работе с CSV необходимо указывать параметр newline=’’ во время открытия файла.
Кроме файлового дескриптора можно передать любой объект поддерживающий итерацию и возвращающий строки.

Поддержка разных форматов csv:
```
import csv

with open('biostats_tab.csv', 'r', newline='') as f:
    csv_file = csv.reader(f, dialect='excel-tab', quoting=csv.QUOTE_NONNUMERIC)
    for line in csv_file:
        print(line)
    print(type(line))
```

Параметры csv.reader:

- **dialect**='excel-tab' — указали диалект с табуляцией в качестве разделителя
- **quoting**=csv.QUOTE_NONNUMERIC — передали встроенную константу, указывающую функции, что числа без кавычек необходимо преобразовать к типу float.

#### csv.writer

Запись в файл

