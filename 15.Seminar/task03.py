# Доработаем задачу 2. Сохраняйте в лог файл раздельно:
# уровень логирования, дату события, имя функции (не декоратора), аргументы вызова, результат.
import csv
from random import randint as rnd
import logging

def generate_csv_file(file_name:str='input_data.csv', rows:int=100):
    with open(file_name, 'w', newline='', encoding='utf-8') as f_csv:
        csv_write = csv.writer(f_csv, dialect='excel', quoting=csv.QUOTE_MINIMAL)
        for _ in range(rows):
            new_line = []           
            new_line.append(rnd(1, 100))
            new_line.append(rnd(0, 100))
            new_line.append(rnd(0, 100))
            csv_write.writerow(new_line)
            # logging.error(f'{new_line}')        
    return

def save_to_json(func):
    def wrapper():
        with open('input_data.csv', 'r+', newline='', encoding='utf-8') as f_csv:
            # open('results.json', 'w') as json_file:
            csv_read = csv.reader(f_csv, dialect='excel', quoting=csv.QUOTE_NONNUMERIC)                                       
            res_dic = {}
            for i, line in enumerate(csv_read):     
                a = float(line[0])
                b = float(line[1])
                c = float(line[2])
                try:                             
                    result = func(a, b, c)
                    res_dic[i] = [line, result]
                    logger.info(f'{line} = {result}')
                except ValueError as err:
                    logger.error({err})
        return

    return wrapper

@save_to_json
def find_roots(a:int or float=1, b:int or float=-4, c:int or float=4):
    d = b**2 - 4*a*c
    if d >0:
        x1 = (-b - d**0.5)/(2*a)
        x2 = (-b + d**0.5)/(2*a)
        return x1, x2
    elif d == 0:
        x = -b/(2*a)
        return x
    else:
        raise ValueError(f'Для {a}, {b}, {c} - нет действительных ')
        

if __name__ == '__main__':
    FORMAT = '{levelname:<8}, {asctime}, {name}, {msg}'
    logging.basicConfig(format=FORMAT, style='{', filename='mylog2.log', filemode='a', encoding='utf-8', level=logging.INFO)
    logger = logging.getLogger(__file__)
    generate_csv_file('input_data.csv', 101)    
    find_roots()