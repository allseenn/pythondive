# Задание No3
# ✔ Создайте вручную кортеж содержащий элементы разных типов.
# ✔ Получите из него словарь списков, где:
# ключ — тип элемента,
# значение — список элементов данного типа.
my_tuple = ("Hello", "World", 2, 0, 2, 3, 11.30, True, False, [1,2,3], (1,2,3), {1,2,3}, {1:1, 2:2})

my_dict = {}

for i in my_tuple:
    if type(i) not in my_dict.keys():
        my_dict[type(i)] = []
        my_dict[type(i)].append(i)
    else:
        my_dict[type(i)].append(i)

print(my_dict)