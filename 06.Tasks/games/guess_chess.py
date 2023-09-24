# 2. Добавьте в пакет, созданный на семинаре шахматный модуль. 
# Внутри него напишите код, решающий задачу о 8 ферзях.
# Известно, что на доске 8×8 можно расставить 8 ферзей так, чтобы они не били друг друга. 
# Вам дана расстановка 8 ферзей на доске, определите, есть ли среди них пара бьющих друг друга. 
# Программа получает на вход восемь пар чисел, каждое число от 1 до 8 - координаты 8 ферзей. 
# Если ферзи не бьют друг друга верните истину, а если бьют - ложь.
def queens(*args):
    """
    Расставляет 8 ферзей на шахматной доске и проверяет их корректное размещение.
    https://en.wikipedia.org/wiki/Eight_queens_puzzle

    Аргументы:
    args (tuple): 8 Кортежей (0-7) с координатами ферзей в формате (x, y).

    Возвращает:
    bool: 
    False - хотя бы одна пара ферзей бьют друг друга (по горизонтали, вертикали или диагонали).
    True - никто из ферзей не бьют любого другого.
    """
    size = len(args)
    board =[[0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0]]

    for i, queen in enumerate(args, 1): # Перебор 8 ферзей
        x, y = queen # Получение координат каждого ферзя
        # Расстановка ферзей
        if board[y][x] == 0: # Если текущая точка (y,x) имеет значение ноль
            board[y][x] = i # Ставим i-того ферзя (ферзь№1=10)
            # пробегаем всю ось x по значению y горизонтальным лучом i-го ферзя (ферзь№1=11)
            for h in range(size): # h - horizontal
                if board[y][h] == 0 or board[y][h] == i:
                    pass
                else: return False
            # пробегаем всю ось y по значению x вертикальным лучом i-го ферзя (ферзь№1=11)
            for v in range(size): # v - vertical
                if board[v][x] == 0 or board[v][x] == i: 
                    pass
                else: return False
            # пробегаем по левой диагонали, проходящие через текущую точку
            l_start = (x-y, 0) if x-y >= 0 else (0, y-x) #  (x,y) Начало левой диагонали
            l_end = (size-1-l_start[1], size-1-l_start[0]) # (x,y) Конец левой диагонали
            while l_start != l_end:
                if board[l_start[1]][l_start[0]] == i or board[l_start[1]][l_start[0]] == 0:   
                    l_start = (l_start[0]+1, l_start[1]+1)
                else: return False 
            # r_start = (0, x+y) if (x+y) <= size-1 else 
            # r_end = (x+y, 0)
            # пробегаем по правой диагонали, проходящей через текущую точку (снизу вверх)
            r_start = (x - min(x, size-1 - y), y + min(x, size-1 - y))
            r_end = (x + min(size-1 - x, y), y - min(size-1 - x, y))
            while r_start != r_end:
                if board[r_start[1]][r_start[0]] == i or board[r_start[1]][r_start[0]] == 0:
                    r_start = (r_start[0] + 1, r_start[1] - 1)
                else:
                    return False

        else:
            return False

    return True

# 8. Напишите функцию в шахматный модуль. 
# Используйте генератор случайных чисел для случайной расстановки ферзей в задаче выше. 
# Проверяйте различный случайные варианты и выведите 4 успешных расстановки.

# def positions(variants, size=8) -> list:
#     variants_list = list()
#     maxi = int("77777777", 8)
#     mini = int("11111111", 8)
#     for i in range(mini, maxi):
#         oc = oct(i)
#         variant = [(int(oc[2],8), 0), (int(oc[3],8), 1), (int(oc[4],8), 2), (int(oc[5],8), 3), 
#         (int(oc[6],8), 4), (int(oc[7],8), 5), (int(oc[8],8), 6), (int(oc[9],8), 7)]
#         # print(*variant)
#         if queens(*variant):
#             variants_list.append(variant)
#         # if variants == len(variants_list):
            
#     return variants_list 

def oc(dec_num):
    if dec_num == 0:
        return '0'  # Обработка случая, когда входное число равно 0
    oc_dig = []  # Создаем список для хранения цифр восьмеричного числа
    while dec_num > 0:
        remainder = dec_num % 8  # Остаток от деления на 8
        oc_dig.insert(0, str(remainder))  # Добавляем остаток в начало списка
        dec_num = dec_num // 8  # Целая часть от деления на 8
    return ''.join(oc_dig)  # Преобразуем список в строку

def positions(variants, board_size=8) -> list:
    variants_list = list()
    maxi = board_size**board_size
    mini = int("11111111", 8)
    for i in range(mini, maxi):
        q0 = (int(oc(i)[0],8), 0)
        q1 = (int(oc(i)[1],8), 1)
        q2 = (int(oc(i)[2],8), 2)
        q3 = (int(oc(i)[3],8), 3)
        q4 = (int(oc(i)[4],8), 4)
        q5 = (int(oc(i)[5],8), 5)
        q6 = (int(oc(i)[6],8), 6)
        q7 = (int(oc(i)[7],8), 7)
        if queens(q0, q1, q2, q3, q4, q5, q6, q7):
            variants_list.append([q0, q1, q2, q3, q4, q5, q6, q7])
        if len(variants_list) == variants:  # Check if the desired number of solutions is reached
            break
    return variants_list


if __name__ == "__main__":

    #print(queens((0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7)))
    # print(queens((4, 0), (1, 1), (3, 2), (6, 3), (2, 4), (7, 5), (5, 6), (0, 7)))
    print(queens((5,0),(3,1),(6,2),(0,3),(7,4),(1,5),(4,6),(2,7)))
 
    


