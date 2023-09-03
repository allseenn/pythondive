# 1. Напишите функцию для транспонирования матрицы
import sys


def transpon(matrix):
    length = len(matrix) - 1
    for i in matrix[length]:
        for j in matrix:
            print(j[length], end=" ")
        length -= 1
        print()

matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

transpon(matrix)
