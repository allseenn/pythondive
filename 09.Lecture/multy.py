def deco_a(func):
    def wrapper_a():
        print(f'Вошли в обертку {func.__name__}') 
        res = func() 
        print(f'Вышли зи обертки {func.__name__}')  
        return res 

    print(f'Обернули функцию {func.__name__} в декоратор deco_a') 
    return wrapper_a

def deco_b(func):
    def wrapper_b():
        print(f'Вошли в обертку {func.__name__}') 
        res = func()
        print(f'Вышли из обертки {func.__name__}') 
        return res  

    print(f'Обернули функцию {func.__name__} в декоратор deco_b')  
    return wrapper_b

# @deco_b  # Сахар
# @deco_a  # Сахар
def main():
    print('Старт основной функции') 

main = deco_b(deco_a(main)) # Без сахара, равносильно с сахаром
# main()  

def cache(func):
    _cache_dict = {}
    def wrapper(*args):
        if args not in _cache_dict:
            _cache_dict[args] = func(*args)
        return _cache_dict[args]
    return wrapper


@cache
def factorial(n):
    print(f'Вычисляю факториал для числа {n}')
    f = 1
    for i in range(2, n + 1):
        f *= i
    return f


print(f'{factorial(10) = }')
print(f'{factorial(15) = }')
print(f'{factorial(10) = }')
print(f'{factorial(20) = }')
print(f'{factorial(10) = }')
print(f'{factorial(20) = }')

