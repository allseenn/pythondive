# Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь,
# где ключ — значение переданного аргумента, а значение — имя аргумента. Если ключ не хешируем,
# используйте его строковое представление.

def dict_revers(**kwargs):
    my_dict = dict()
    for name, value in kwargs.items():
        if isinstance(value, (dict, list)):
            my_dict[str(value)] = name
        else:
            my_dict[value] = name
    return my_dict

res = dict_revers(ints=5, floats=0.4, strings = "Hello", lists=[1, 2, 3], sets=(1, 2, 3), dicts = {1:10, 2:20, 3:30} )
print(res)
