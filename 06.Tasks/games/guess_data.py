# Задача 7:
# Создайте модуль и напишите в нём функцию, которая получает на вход дату в формате DD.MM.YYYY
# Функция возвращает истину, если дата может существовать или ложь, если такая дата невозможна.
# Для простоты договоримся, что год может быть в диапазоне [1, 9999]. 
# Весь период (1 января 1 года - 31 декабря 9999 года) действует Григорианский календарь. 
# Проверку года на високосность вынести в отдельную защищённую функцию
import calendar as cal

def check_date(date: str) -> bool:
    year = int(date.split(".")[2])
    month = int(date.split(".")[1])
    day = int(date.split(".")[0])
    if year > 10000:
        return False
    if month > 12:
        return False
    days_in_month = cal.monthrange(year, month)[1]
    if day > days_in_month:
        return False

    return True

        
print(check_date("31.12.9999"))