# Напишите код, который запрашивает число и сообщает является ли оно простым или составным.
# Используйте правило для проверки: «Число является простым, если делится нацело только на единицу
# и на себя». Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч.
limitations = True
number = 0

while(limitations):
    number = int(input("Введите неотрицательное целое число меньше 100 тысяч: "))
    if  number < 0 or number > 99999:
        limitations = True
    else:
        limitations = False 

for i in range(2, number):
    if not(number%i):
        print("Составное число!")
        exit()
        
print("Простое число!")