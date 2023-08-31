# ? Напишите функцию, которая принимает строку текста.
# Вывести функцией каждое слово с новой строки.
# ? Строки нумеруются начиная с единицы.
# ? Слова выводятся отсортированными согласно кодировки Unicode.
# ? Текст выравнивается по правому краю так, чтобы у самого
# длинного слова был один пробел между ним и номером строки.
def my_func_str(f_str):
    my_list = sorted(f_str.split())
    max_len_word = len(max(my_list))
    for i, item in enumerate(my_list, start=1):
        print(f'{i:} {item:>{max_len_word}}')
    return None


my_str = 'Hello Worldddd Able'
my_func_str(my_str)