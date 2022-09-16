def task1():
    x = int(input())
    if (x % 2 == 0):
        print("Чёт")
    else:
        print("Нечёт")


def task2():
    x = int(input())
    y = int(input())
    if (x < y):
        print(x)
    else:
        print(y)


def task3():
    number = int(input())
    if (number > 0):
        print(1)
    elif (number == 0):
        print(0)
    else:
        print(-1)


def task4():
    number = int(input())
    if (number > 99 or number < -99):
        print("Да")
    else:
        print("Нет")


def task5():
    number1 = int(input())
    number2 = int(input())
    if (number1 > 0 or number2 > 0):
        print("Да")
    else:
        print("Нет")


def task6():
    x = int(input())

    if (x // 100 < x // 10 % 10 < x % 10):
        print('Yes')
    else:
        print("No")


def task7():
    x = int(input())

    if (x // 1000 == x % 10 and x // 100 % 10 == x // 10 % 10):
        print("Yes")
    else:
        print("No")


def task8():
    x = int(input())
    if (x == 2):
        print('28')
    elif (x in [1, 3, 5, 7, 8, 10, 12]):  # a lot of ifs
        print("31")
    else:
        print('30')


def task9():
    x1, x2, x3 = int(input()), int(input()), int(input())
    if (x1 == x2 == x3):
        print("3")
    elif (x1 == x2 or x2 == x3 or x1 == x3):
        print("2")
    else:
        print("0")


def task10():
    x = int(input())
    y = int(input())

    if ((x+y) % 2 == 0):
        print("Черная")
    else:
        print("Белая")


def task11():
    x1 = int(input())
    y1 = int(input())

    x2 = int(input())
    y2 = int(input())

    if ((x1+y1) % 2 == (x2+y2) % 2):
        print("Да")
    else:
        print("Нет")


def task12():
    m = int(input())
    d = int(input())
    curYear = 2022

    months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if (d == months[m-1]):
        if (m == 12):
            print(f"1-1-{curYear+1}")
        else:
            print(f"1-{m + 1}-{curYear}")
    else:
        print(f"{d+1}-{m}-{curYear}")
