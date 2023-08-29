# Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения. 
# Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность. 
# Достаточно вернуть один допустимый вариант. *Верните все возможные варианты комплектации рюкзака.

items_dict = {
    "Фонарь": 0.5,
    "Нож": 0.1,
    "Аптечка": 0.5,
    "Веревка": 1.0,
    "Спички": 0.03,
    "Зажигалка": 0.2,
    "Палатка": 5.0,
    "Сгущенка": 0.5,
    "Тушенка": 0.5,
    "Пшенка": 1.0,
    "Перловка": 1.0,
    "Гречка": 1.0,
    "Рис": 1.0,
    "Топор": 1.0,
    "Ружье": 5.0,
    "Патроны": 0.5,
    "Спальник": 1,
    "Рация": 0.5,
    "Компас": 0.3,
    "Смартфон": 0.5,
    "Карта": 0.1
}

total_wight = sum(items_dict.values())
max_weight = float(input(f"Задайте МАКСимальный вес вещей, но не более {total_wight} кг: "))
min_weight = float(input("Задайте МИНИмальный вес вещей, кг: "))

bag_weight = 0
bag = []
for i in items_dict:
    if bag_weight + items_dict[i] > max_weight:
        break
    elif bag_weight + items_dict[i] == max_weight:
        bag_weight += items_dict[i]
        bag.append(i)
    else:
        bag_weight += items_dict[i]
        bag.append(i)
print("Любой вариант:", bag)

print("Исполнение звездного задания (*):")

items_quantity = len(items_dict)
counter = 0
permutations = 2**items_quantity
no_0b = 2
index_dict = list(items_dict.keys())
value_dict = list(items_dict.values())

for i in range(permutations):
    items_variant = bin(i)[no_0b:].zfill(items_quantity)
    variant = list()
    bag_weight = 0
    for k,j in enumerate(items_variant):
        if j == "1":
            bag_weight += value_dict[k]
    if min_weight < bag_weight <= max_weight:
        for k,j in enumerate(items_variant):
            if j == "1":
                variant.append(index_dict[k])
    if len(variant) > 0:
        counter += 1
        print(f"{counter}. {', '.join(variant)} = {bag_weight:.2f} кг.")
    
print(f"Итого: {counter} вариант. из {items_quantity} шт. вещей весом от {min_weight} до {max_weight} кг.")

