# Задание No4
# ✔ Создайте вручную список с повторяющимися элементами.
# ✔ Удалите из него все элементы, которые встречаются дважды.
my_list = [1,1,1,2,3,4,5,5,5,6,6,7]

for i in my_list:
    if my_list.count(i) == 2:
        my_list.remove(i)
        my_list.remove(i)

print(my_list)