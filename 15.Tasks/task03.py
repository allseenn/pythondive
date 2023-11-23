# Семинар 4 задача 3. Возьмите задачу о банкомате из семинара 2. 
# - Разбейте её на отдельные операции — функции.
# - Дополнительно сохраняйте все операции поступления и снятия средств в список
import logging
import argparse

parser = argparse.ArgumentParser(description='Программа банкомат', epilog="Приятного переименования")
parser.add_argument('name', metavar='N', nargs='*', help='Введите имя банка')
args = parser.parse_args()
if len(args.name) == 0:
    BANK ="ПОЛТОС & ОБЛОМИСЪ"
else:
    BANK = " ".join(args.name)

MENU = f'Банк {BANK}\n \
1. Пополнить счет\n \
2. Снять наличные\n \
3. Показать историю\n \
4. Выход'

CLS = "\033[H\033[J"

def menu():
    print(CLS)
    print(MENU)
    account["action"] = int(input("Введите номер действия: "))

def fullfil():
    print(CLS)
    print("Пополнить можно только 50-ти долларовыми купюрами!")
    volume = float(input("Введите количество купюр: "))
    if account["balance"] > 5_000_000:
        account["balance"] -= account["balance"]*0.10
    account["balance"] += volume*50
    if account["operations"]%3 == 0 and account["balance"] > 0:
        account["balance"] += account["balance"]*0.03

def withdraw():
    print(CLS)
    print("Снять можно только 50-ти долларовыми купюрами!")
    volume = float(input("Введите количество купюр: "))
    if account["balance"] > 5_000_000:
        account["balance"] -= account["balance"]*0.10
    if account["balance"] < volume*50:
        print("Не достаточно средств")
        return
    if volume*0.015 < 30:
        account["balance"] -= volume*50+30
    elif volume*0.015 >= 30 and volume*0.015 < 600:
        account["balance"] -= volume*50+volume*50*0.015
    elif volume*0.015 >= 600:
        account["balance"] -= volume*50
    if account["operations"]%3 == 0 and account["balance"] > 0:
        account["balance"] += account["balance"]*0.03

def history():
    print(CLS)
    with open("bank.log", mode="r", encoding="utf-8") as f:
        print(*f)
    input("Нажмите ввод для возврата в меню! ")

def show():
    print(CLS)
    print(f'Ваш баланс: {account["balance"]}')
    input("Нажмите ввод для возврата в меню! ")

def problem():
    print(CLS)
    print(f'{account["action"]} - нет такого действия!')
    input("Нажмите ввод для возврата в меню! ")


if __name__ == '__main__':
    FORMAT = '{levelname:<8} {asctime} {name} {msg}'
    logging.basicConfig(format=FORMAT, style='{', filename='bank.log', filemode='a', encoding='utf-8', level=logging.INFO)
    logger = logging.getLogger(__file__)

    account = { "balance":0.0, "operations":0, "action":0 }

    while(account["action"]!=4):
        match account["action"]:
            case 0:
                menu()
            case 1:
                account["operations"] += 1
                try: 
                    fullfil()
                except ValueError as e:
                    logger.error(e)
                logger.info(account.copy())
                show()
                account["action"] = 0
            case 2:
                account["operations"] += 1
                try:
                    withdraw()
                except ValueError as e:
                    logger.error(e)
                logger.info(account.copy())
                show()
                account["action"] = 0
            case 3:
                history()
                account["action"] = 0
            case _:
                problem()
                account["action"] = 0