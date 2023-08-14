# name = 'Slava'
# age = None
# a = 42
# print(id(a))
# a = 'Hello world!'
# print(id(a))
# a = 3.14 / 3
# print(id(a))

# print(name, age, a, 456, 'text', sep=' (=^.^=) ', end='#')
# print('Any text')

# res=input('Print your text: ')
# print('You write:', res)

# ADULT = 18
# age = int(input('How old are you?: '))
# how_old = ADULT - age
# print(how_old, 'Till your adults')


# pwd  = 'text'
# res = input("input you pass: ")
# if res == pwd:
#     print("Access granted")
#     my_math = int(input('2 + 2 = '))
#     if 2+2 == my_math:
#         print('you are in right world')
#     else:
#         print("you are in wrong world")
# else:    
#     print("Access denied")
# print("Exit")

# year = int(input('year: '))
# if year % 4 != 0:
#     print("simple")
# elif year % 100 == 0:
#     if year % 400 == 0:
#         print ("leap")
#     else: 
#         print("simple")
# else:
#     print("leap")

## Ленивый If 
# 1. если хотя бы один OR то вернется сразу истина
# 2. если получили ложь перед AND - сразу вернет ложь
# year = int(input('year: '))
# if year % 4 !=0 or year % 100 == 0 and year % 400 !=0:
#     print("simple")
# else:
#     print("leap")

# data = [0, 1, 1, 2, 3, 5, 8, 13, 21]
# num = int(input("enter number: "))
# if num not in data:
#     print("Leonardo is sad")

## ternary operator if
# my_math = int(input("2 + 2 = "))
# print('Yes' if 2+2 == my_math else "No")

## Syntax sugar
# num = float(input("input number: "))
# count = 0
# while count < num:
#     print(count)
#     count += 2

# num = float(input("input number: "))
# STEP = 2
# limit  = num - STEP
# count = -STEP
# while count < limit:
#     count += STEP
#     if count % 12 == 0:
#         continue
#     print(count)

# while True: - бесконечный цикл.

# min_limit = 0
# max_limit = 10
# count = 3
# num = None

# while count > 0:
#     print("Attempt", count)
#     count -= 1

#     print ("Enter num between", min_limit, max_limit)
#     num = float(input())
#     if num < min_limit or num > max_limit:
#         print("False")
#     else:
#         break

# else:
#     print("All attempts empty")
#     quit()
# print("your number is", num)



# data = [0, 1, 1, 2, 3, 5, 8, 13, 21]
# for item in data:
#     print(item)

## range (stop), range(start, stop), range(start, stop, step) for use i j k
# num = int(input('enter num: '))
# for i in range (0, num, 2):
#     print(i)

## enumerate warning - animal and animalS
# animals = ['cat', 'dog', 'wolf', 'rate', 'dragon']
# for i, animal in enumerate(animals, start=1):
#     print(i, animal)

data = 0
while data < 100:
    data += 3
    if data % 19 == 0:
        continue
    data += 1
    if data % 40 == 0:
        break
else:
    data += 5

print(data)