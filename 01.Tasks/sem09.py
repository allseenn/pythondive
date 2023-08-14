# Выведите в консоль таблицу умножения от 2х2 до 9х10 как на школьной тетрадке.

for k in range(0, 5, 4):
    for i in range(2, 11):
        for j in range(2+k, 6+k):
            print(f"{j} X {i} = {(j)*i}", end="\t\t")
            if j==5+k: print()
    print()

    