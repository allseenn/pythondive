# Задание № 2
# Пользователь вводит данные. Сделайте проверку данных
# и преобразуйте если возможно в один из вариантов ниже:
# ✔ Целое положительное число
# ✔ Вещественное положительное или отрицательное число
# ✔ Строку в нижнем регистре, если в строке есть
# хотя бы одна заглавная буква
# ✔ Строку в нижнем регистре в остальных случаях
data = str(input("Enter data: "))

if data.isdigit():
    conv = int(data)
elif data.replace("-","").replace(".","").replace(",","").isdigit():
    conv = float(data)
elif data.__contains__(r'\p{Lu}'):
    conv = data.lower()
else:
    conv = data.lower()

print(conv, type(conv))