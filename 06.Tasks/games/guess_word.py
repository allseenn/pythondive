# Создайте модуль с функцией внутри. 
# Функция получает на вход загадку, список с возможными вариантами отгадок и количество попыток на угадывание.
# Программа возвращает номер попытки, с которой была отгадана загадка или ноль, если попытки исчерпаны.
def quiz(my_str, my_solve, my_try):
    print(my_str)
    count = 0
    while count < my_try:
        answer = input('Введите ответ ')
        if answer in my_solve:
            print(f'Угадал {answer}')
            return count + 1
        count += 1
    return 0           

my_quiz = 'Зимой и летом одним цветом'

if __name__ == '__main__':
    print(quiz(my_quiz, ['елка', 'ель', 'сосна'], 3))