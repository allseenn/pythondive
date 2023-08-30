# def no_mutable(a: int) -> int:
#     a += 4
#     return a

# a = 0

# print(f'function returns {no_mutable(a)}')
# print(f'without function {a}')
def school_print(**kwargs):
    for key, value in kwargs.items():
        print(f'По предмету "{key}" получена оценка {value}')
    


school_print(chimestry=5, phisics=4, math=5, fitness=5)