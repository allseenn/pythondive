# Создайте пакет с всеми модулями, которые вы создали за время занятия. 
# Добавьте в __init__ пакета имена модулей внутри дандер __all__. 
# В модулях создайте дандер __all__ и укажите только те функции, 
# которые могут верно работать за пределами модуля.
import time
from games.guess_chess import positions

start_time = time.time()
arrangements_to_find = 100
mode = 2
arrangements = positions(arrangements_to_find, mode)
print(*arrangements, sep='\n')
end_time = time.time()
print(f"За {end_time-start_time} секунд, найдено {len(arrangements)} расстановки")