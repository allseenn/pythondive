# Задание No7
# ✔ Пользователь вводит строку текста.
# ✔ Подсчитайте сколько раз встречается
# каждая буква в строке без использования
# метода count и с ним.
# ✔ Результат сохраните в словаре, где ключ —
# символ, а значение — частота встречи
# символа в строке.
# ✔ Обратите внимание на порядок ключей.
# Объясните почему они совпадают
# или не совпадают в ваших решениях.
my_string = input("Enter any text: ")

no_count_dict = {}
for i in my_string:
    no_count_dict[i] = no_count_dict[i]+1 if i in no_count_dict else 1 

print(no_count_dict)

count_dict = {}
for i in set(my_string):
    count_dict[i] = my_string.count(i)

print(count_dict)

