# Задание No8
# ✔ Три друга взяли вещи в поход. Сформируйте
# словарь, где ключ — имя друга, а значение —
# кортеж вещей. Ответьте на вопросы:
# ✔ Какие вещи взяли все три друга
# ✔ Какие вещи уникальны, есть только у одного друга
# ✔ Какие вещи есть у всех друзей кроме одного
# и имя того, у кого данная вещь отсутствует
# ✔ Для решения используйте операции
# с множествами. Код должен расширяться
# на любое большее количество друзей.
team = {}

while True:
    friend = input("Put friend name, or Enter to stop: ")
    if friend == "":
        break
    team[friend] = tuple(input(f"Enter {friend}'s items, comma is separator: ").split(", "))

## Without SET()
# print("1. Team items: ")
# for i in team:
#     print(f"  {i} takes: {', '.join(team[i])}")

union_set = set()
for i in team:
    union_set = union_set.union(set(team[i]))
print(f"1. Team items: {', '.join(union_set)}")

## Without SET()
# unique_list = []
# for i in team:
#     for j in team[i]:
#         if j in unique_list:
#             unique_list.remove(j)
#         else:
#             unique_list.append(j)

# print(f"2. Unique items: {', '.join(unique_list)}") 

unique_set = set()
for i in team:
    unique_set ^= set(team[i])
print(f"2. Unique items: {', '.join(unique_set)}")

team_set = set()
for i in team:
    team_set = team_set.union(set(team[i]))
print("3. Poor friends:")
for i in team:
    check_set = team_set - set(team[i])
    if len(check_set) > 0:
        print(f"  {i} not have: {', '.join(check_set)}")