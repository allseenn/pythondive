# Добавьте в модуль с загадками функцию, которая хранит словарь списков. 
# Ключ словаря - загадка, значение - список с отгадками. 
# Функция в цикле вызывает загадывающую функцию, чтобы передать ей все свои загадки.

import task05

def multy_quiz(my_quit):
    ATTEMP = 3
    for key, value  in my_quit.items():
        print('Вопрос: ', end=' ' )
        task05.quiz(key, value, ATTEMP)



my_dic = {'ex1':['ans1', 'ans2', 'ans3'], 'ex2':['ans4','ans5', 'ans6'], 'ex3':['ans7','ans8', 'ans9']}        

multy_quiz(my_dic)