# Введите ваше решение ниже
class LotteryGame:
    def __init__(self, list1, list2):
        self.list1 = list1
        self.list2 = list2

    def compare_lists(self):
        res = []
        count = 0
        for i in self.list1:
            for j in self.list2:
                if i == j:
                    res.append(i)
                    count +=1
                    break
        if len(res) == 0:
            print('Совпадающих чисел нет.')
        else:
            print(f'Совпадающие числа: {res}\nКоличество совпадающих чисел: {count}')

list1 = [3, 12, 8, 41, 7, 21, 9, 14, 5, 30]
list2 = [9, 5, 6, 12, 14, 22, 17, 41, 8, 3]

game = LotteryGame(list1, list2)
matching_numbers = game.compare_lists()

        