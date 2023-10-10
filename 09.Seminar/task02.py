# Дорабатываем задачу 1. 
# Превратите внешнюю функцию в декоратор. 
# Он должен проверять входят ли переданные в функцию-угадайку числа в диапазоны [1, 100] и [1, 10]. 
# Если не входят, вызывать функцию со случайными числами из диапазонов.
def my_fun(enigma: int, num_try: int):
        # for _ in range(num_try):
    print(enigma)
    enigma = 25
    def new_fun():
        for _ in range(num_try):
            my_answer = int(input('Введите число:  '))
            if my_answer > enigma:
                print('Меньше')
            elif my_answer < enigma:
                print('Больше')
            else:
                print('Верно')
                break
    return new_fun
    


if __name__ == '__main__':

    hello = my_fun(30, 7)
    # print(hello)
    hello()