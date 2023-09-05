# 1. Напишите функцию для транспонирования матрицы

def transpon(matrix):
    xirtam = list()
    len_x = len(max(matrix, key=len))
    for i in range(len_x):
        xirtam.append(list())
        for row in matrix:
            try:
                xirtam[i].append(row[len_x-i-1])
            except:
                xirtam[i].append(None)
    return xirtam


matrix = [[0, 0, 0],
          [1, 1, 1],
          [2, 2, 2],
          [3, 3, 3],
          [4, 4, 4]]

print(*matrix, sep="\n")
print()
print(*transpon(matrix), sep="\n")
