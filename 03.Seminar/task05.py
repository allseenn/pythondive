# Задание No5
# ✔ Создайте вручную список с повторяющимися целыми числами.
# ✔ Сформируйте список с порядковыми номерами
# нечётных элементов исходного списка.
# ✔ Нумерация начинается с единицы.
my_list = [1,1,1,2,3,4,5,5,5,6,6,7]

odd_indexes = []

for k,i in enumerate(my_list, 1):
    if i % 2:
        odd_indexes.append(k)

print(odd_indexes)