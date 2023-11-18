# Создайте функцию, которая удаляет из текста все символы кроме букв латинского алфавита и пробелов.
# Возвращается строка в нижнем регистре.
def func_clear_text(text: str) -> str:
    new_text = ''
    for letter in text:
        if 97 <= ord(letter) <= 122 or 65 <= ord(letter) <= 90 or letter == ' ':
            new_text +=letter
    return new_text.lower()


text = 'фывфыв Hello world 123'
print(func_clear_text(text))



