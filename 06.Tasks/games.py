# Создайте пакет с всеми модулями, которые вы создали за время занятия. 
# Добавьте в __init__ пакета имена модулей внутри дандер __all__. 
# В модулях создайте дандер __all__ и укажите только те функции, 
# которые могут верно работать за пределами модуля.

from games.store_guess import multy_quiz, my_dic

multy_quiz(my_dic)