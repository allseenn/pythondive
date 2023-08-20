# Напишите программу, которая получает целое число и 
# возвращает его шестнадцатеричное строковое представление. 
# Функцию hex используйте для проверки своего результата.
def to_hex(number):
    hex_string = ""
    while number > 0:
        match number%16:
            case 10:
                hex_string = "a" + hex_string
            case 11:
                hex_string = "b" + hex_string
            case 12:
                hex_string = "c" + hex_string
            case 13:
                hex_string = "d" + hex_string
            case 14:
                hex_string = "e" + hex_string
            case 15:
                hex_string = "f" + hex_string
            case _:
                hex_string = str(number%16) + hex_string
        number //= 16
    return "0x" + hex_string

number = int(input("Введите целое число: "))

print(to_hex(number))

print(hex(number))