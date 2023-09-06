# 1. Напишите функцию для транспонирования матрицы

def transpose(matrix, method="left"):
    num_rows = len(matrix)
    num_cols = max(len(row) for row in matrix)
    transposed = [[None] * num_rows for _ in range(num_cols)]
    match method:
        case "right":
            for i in range(num_rows):
                for j in range(len(matrix[i])):
                    transposed[j][-i-1] = matrix[i][j]
            return transposed
        case "left":
            for i in range(num_rows):
                for j in range(len(matrix[i])):
                    transposed[-j-1][i] = matrix[i][j]
            return transposed
        case "roll":
            return matrix[::-1]
        case "mirror":
            return [row[::-1] for row in matrix]
    return ["Значения второго аргумента функции:", "right", "left", "roll", "mirror"]


matrix = [[100, 200, 300, 400, 500],
          [101, 202, 303, 404, 505],
          [110, 220, 330, 440],
          [111, 222, 333, 444, 555, 666]]

print("Исходная матрица:")
print(*matrix, sep="\n")

print("\nТранспонирование по часовой стрелке:")
print(*transpose(matrix, "right"), sep="\n")

print("\nТранспонирование против стрелки:")
print(*transpose(matrix, "left"), sep="\n")

print("\nЗеркальное транспонирование:")
print(*transpose(matrix, "mirror"), sep="\n")

print("\nПереворот матрицы:")
print(*transpose(matrix, "roll"), sep="\n")