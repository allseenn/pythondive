# Задание No8 из семинара
# ✔ Создайте несколько переменных заканчивающихся и не оканчивающихся на «s».
# ✔ Напишите функцию, которая при запуске заменяет содержимое переменных
# оканчивающихся на s (кроме переменной из одной буквы s) на None.
# ✔ Значения не удаляются, а помещаются в одноимённые переменные без s на конце.

def change(var):
    for k, v in var.items():
        if not k.startswith("__") and not callable(k) and not callable(v):
            if k+"s" in var.keys():
                globals()[k] = globals()[k+"s"]
                globals()[k+"s"] = None
                


var1 = 0
var2 = 0 
var3 = 0
var1s = 1
var2s = 2
var3s= 3
s = 55

print(f"До функции change(): \n \
    var1 = {var1}, var1s = {var1s}\n \
    var2 = {var2}, var2s = {var2s}\n \
    var3 = {var3}, var3s = {var3s}\n \
    s = {s}")

change(globals())

print(f"После функции change(): \n \
    var1 = {var1}, var1s = {var1s}\n \
    var2 = {var2}, var2s = {var2s}\n \
    var3 = {var3}, var3s = {var3s}\n \
    s = {s}")
