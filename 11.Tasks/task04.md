Не все тесты пройдены, есть ошибки :(


Количество затраченных попыток: 1

Время выполнения: 0.247871 сек

Общая статистика
Всего тестов: 1. Пройдено: 0. Не пройдено: 1.

Подробную информацию по каждому тесту смотрите ниже.
___________________

Тест 1
Тест не пройден ✗

Формулировка:
* Итоговый код для проверки. Иногда добавляем что-то от себя :)

```
import warnings

warnings.filterwarnings('ignore')

# Введите ваше решение ниже


class Matrix:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.data = [[0 for _ in range(cols)] for _ in range(rows)]

    def __str__(self):
        string = ""
        for row in self.data:
            string += " ".join(map(str, row)) + '\n'
        return string

    def __repr__(self):
        return f"Matrix({self.rows}, {self.cols})"
    
    def __eq__(self, other):
        if self.rows != other.rows: return False
        if self.cols != other.cols: return False
        for i in range(self.rows):
            for j in range(self.cols):
                if self.data[i][j] != other.data[i][j]: return False
        return True
    
    def __add__(self, other):
        if self.rows != other.rows: return False
        if self.cols != other.cols: return False
        big = [[0 for _ in range(self.cols)] for _ in range(self.rows)]
        for i in range(self.rows):
            for j in range(self.cols):
                big[i][j] = self.data[i][j] + other.data[i][j]
        return big

    def __mul__(self, other):
        if self.cols != other.rows: return False
        result = Matrix(self.rows, other.cols)

        for i in range(self.rows):
            for j in range(other.cols):
                for k in range(self.cols):
                    result.data[i][j] += self.data[i][k] * other.data[k][j]

        return result


#При отправке кода на Выполнение раскомментируйте строку ниже, чтобы задать значения аргументов и вызвать функцию

#При отправке решения на Проверку закомментируйте эту строку обратно - система автоматически подставит разные значения аргументов и вызовет функцию для проверки

#matrix1 = Matrix(2, 3)
#matrix1.data = [[1, 2, 3], [4, 5, 6]]

#matrix2 = Matrix(2, 3)
#matrix2.data = [[7, 8, 9], [10, 11, 12]]

# Выводим матрицы
#print(matrix1)

#print(matrix2) 


# Создаем матрицы
matrix1 = Matrix(2, 3)
matrix1.data = [[1, 2, 3], [4, 5, 6]]

matrix2 = Matrix(2, 3)
matrix2.data = [[7, 8, 9], [10, 11, 12]]

# Выводим матрицы
print(matrix1)

print(matrix2)

# Сравниваем матрицы
print(matrix1 == matrix2)

# Выполняем операцию сложения матриц
matrix_sum = matrix1 + matrix2
print(matrix_sum)

# Выполняем операцию умножения матриц
matrix3 = Matrix(3, 2)
matrix3.data = [[1, 2], [3, 4], [5, 6]]

matrix4 = Matrix(2, 2)
matrix4.data = [[7, 8], [9, 10]]

result = matrix3 * matrix4
print(result)
```

# Создаем матрицы
matrix1 = Matrix(2, 3)
matrix1.data = [[1, 2, 3], [4, 5, 6]]

matrix2 = Matrix(2, 3)
matrix2.data = [[7, 8, 9], [10, 11, 12]]

# Выводим матрицы
print(matrix1)

print(matrix2)

# Сравниваем матрицы
print(matrix1 == matrix2)

# Выполняем операцию сложения матриц
matrix_sum = matrix1 + matrix2
print(matrix_sum)

import warnings

warnings.filterwarnings('ignore')

# Введите ваше решение ниже


class Matrix:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.data = [[0 for _ in range(cols)] for _ in range(rows)]

    def __str__(self):
        string = ""
        for row in self.data:
            string += " ".join(map(str, row)) + '\n'
        return string

    def __repr__(self):
        return f"Matrix({self.rows}, {self.cols})"
    
    def __eq__(self, other):
        if self.rows != other.rows: return False
        if self.cols != other.cols: return False
        for i in range(self.rows):
            for j in range(self.cols):
                if self.data[i][j] != other.data[i][j]: return False
        return True
    
    def __add__(self, other):
        if self.rows != other.rows: return False
        if self.cols != other.cols: return False
        big = [[0 for _ in range(self.cols)] for _ in range(self.rows)]
        for i in range(self.rows):
            for j in range(self.cols):
                big[i][j] = self.data[i][j] + other.data[i][j]
        return big

    def __mul__(self, other):
        if self.cols != other.rows: return False
        result = Matrix(self.rows, other.cols)

        for i in range(self.rows):
            for j in range(other.cols):
                for k in range(self.cols):
                    result.data[i][j] += self.data[i][k] * other.data[k][j]

        return result


#При отправке кода на Выполнение раскомментируйте строку ниже, чтобы задать значения аргументов и вызвать функцию

#При отправке решения на Проверку закомментируйте эту строку обратно - система автоматически подставит разные значения аргументов и вызовет функцию для проверки

#matrix1 = Matrix(2, 3)
#matrix1.data = [[1, 2, 3], [4, 5, 6]]

#matrix2 = Matrix(2, 3)
#matrix2.data = [[7, 8, 9], [10, 11, 12]]

# Выводим матрицы
#print(matrix1)

#print(matrix2) 

________________
# Создаем матрицы
matrix1 = Matrix(2, 3)
matrix1.data = [[1, 2, 3], [4, 5, 6]]

matrix2 = Matrix(2, 3)
matrix2.data = [[7, 8, 9], [10, 11, 12]]

# Выводим матрицы
print(matrix1)

print(matrix2)

# Сравниваем матрицы
print(matrix1 == matrix2)

# Выполняем операцию сложения матриц
matrix_sum = matrix1 + matrix2
print(matrix_sum)

# Выполняем операцию умножения матриц
matrix3 = Matrix(3, 2)
matrix3.data = [[1, 2], [3, 4], [5, 6]]

matrix4 = Matrix(2, 2)
matrix4.data = [[7, 8], [9, 10]]

result = matrix3 * matrix4
print(result)
________________________

Ожидаемый ответ:

1 2 3
4 5 6
7 8 9
10 11 12
False
8 10 12
14 16 18
25 28
57 64
89 100

Ваш ответ:

1 2 3
4 5 6

7 8 9
10 11 12

False
[[8, 10, 12], [14, 16, 18]]
25 28
57 64
89 100