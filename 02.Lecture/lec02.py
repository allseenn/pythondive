# a = 5
# print(type(a), id(a))
# a = "hello world"
# print(type(a), id(a))
# a = 42.0 * 3.141592 / 2.71828
# print(type(a), id(a))

# data = 3.14
# print(isinstance(data, (float, complex, int)))

# num = 2 + 2 * 2
# digit = 36 // 6
# print(type(num), type(digit))
# print(num == digit)
# print(num is digit)

# a = 5
# print(a, id(a))
# a += 1
# print(a, id(a))

# txt = 'Hello world!'
# txt[5] = '_'

# txt = 'Hello world!'
# print(txt, id(txt))
# txt = txt.replace(' ', '_')
# print(txt, id(txt))

# a = c = 2
# b = 3
# print(a, id(a), b, id(b), c, id(c))
# a = b + c
# print(a, id(a), b, id(b), c, id(c))

x = 42
y = 'text'
z = 3.1415
print(hash(x), hash(y), hash(z))
my_list = [x, y, z]
print(hash(my_list)) # получим ошибку, т.к. list изменяемый