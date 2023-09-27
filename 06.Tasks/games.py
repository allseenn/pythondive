# Создайте пакет с всеми модулями, которые вы создали за время занятия. 
# Добавьте в __init__ пакета имена модулей внутри дандер __all__. 
# В модулях создайте дандер __all__ и укажите только те функции, 
# которые могут верно работать за пределами модуля.
import time
from games.guess_chess import positions


arrangements_to_find = 4
mode = 1
start_time = time.time()
arrangements = positions(arrangements_to_find, mode)
end_time = time.time()
print(*arrangements, sep='\n')
print(f"За {end_time-start_time} секунд, найдено {len(arrangements)} расстановки")