# 1. В модуль с проверкой даты добавьте возможность запуска в терминале с передачей даты на проверку.

import calendar as cal
from sys import argv

def check_date(argv: tuple) -> bool:
    day, month, year = argv[1].split(".")
    if int(year) > 10000:
        return False
    if int(month) > 12:
        return False
    days_in_month = cal.monthrange(int(year), int(month))[1]
    if int(day) > days_in_month:
        return False

    return True

if __name__ == "__main__":
    print(check_date(argv))