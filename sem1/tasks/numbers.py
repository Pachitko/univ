from re import T


def task1():
    x = int(input())
    print(x // 10, x % 10)


def task2():
    x = int(input())
    print(f"{x % 10}{x // 10}")


def task3():
    x = int(input())
    print(x % 100)


def task4():
    x = int(input())
    print(x % 100 // 10)


def task5():
    x = int(input())
    print(x % 100 % 10 + x % 100 // 10 + x // 100)


def task6():
    x = float(input())
    print(int(x * 10) % 10)


def task7():
    year = int(input())
    print((year - 1) // 100 + 1)


def task8():
    # 0 - воскресенье
    # 6 - суббота
    day = int(input())
    offset = 4  # 1 января - четверг
    print(day % 365 + offset - 1)


def task9():
    mins = int(input())
    print(f"{mins // 60}:{mins % 60}")


def task10():
    a = int(input())
    b = int(input())
    c = int(input())

    print((a // 2 + a % 2) + (b // 2 + b % 2) + (c // 2 + c % 2))
