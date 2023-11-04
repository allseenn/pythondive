# Создайте функцию, которая запрашивает числовые данные от
# пользователя до тех пор, пока он не введёт целое или
# вещественное число.
# Обрабатывайте не числовые данные как исключения.
def get(text):
    while True:
        my_text = input(text)
        try:
            num = int(my_text)
            break
        except ValueError as e:
            try:
                num = float(my_text)
                break
            except ValueError as e:
                print(f'Ваш ввод привёл к ошибке ValueError: {e}\n' f'Попробуйте снова')
                
    return num

number = get('Введите целый делитель: ')
print(f'100 / {number} = {100 / number}')