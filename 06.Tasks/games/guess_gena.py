# 3. Напишите функцию в шахматный модуль. 
# Используйте генератор случайных чисел для случайной расстановки ферзей в задаче выше. 
# Проверяйте различный случайные  варианты и выведите 4 успешных расстановки.
import random

def is_attacking(x1, y1, x2, y2):
    # Проверяем, бьют ли ферзи друг друга по вертикали, горизонтали или диагоналям
    return x1 == x2 or y1 == y2 or abs(x1 - x2) == abs(y1 - y2)

def generate_random_queen_arrangement():
    # Генерируем случайную расстановку ферзей
    queens = [(x, y) for x in range(8) for y in range(8)]
    random.shuffle(queens)
    return queens

def check_queen_arrangement(arrangement):
    # Проверяем, бьют ли ферзи друг друга в данной расстановке
    for i in range(8):
        for j in range(i + 1, 8):
            x1, y1 = arrangement[i]
            x2, y2 = arrangement[j]
            if is_attacking(x1, y1, x2, y2):
                return False
    return True

successful_arrangements = []

# Генерируем и проверяем случайные расстановки ферзей
while len(successful_arrangements) < 4:
    arrangement = generate_random_queen_arrangement()
    if check_queen_arrangement(arrangement):
        successful_arrangements.append(arrangement)

# Выводим 4 успешные расстановки
for i, arrangement in enumerate(successful_arrangements, 1):
    print(f"Successful Arrangement {i}:")
    for x, y in arrangement:
        row = ["." if (x, y) != (qx, qy) else "Q" for qx, qy in arrangement]
        print(" ".join(row))
    print()
