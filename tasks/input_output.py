from re import S
from traceback import print_tb


def task1():
    print(int(input()) + int(input()) + int(input()))


def task2():
    print(1/2 * int(input()) * int(input()))


def task3():
    print("Привет, ", input(), "!")


def task4():
    x = int(input())
    print(f"Следующее число для числа {x}: {x + 1}")
    print(f"Предыдущее число для числа {x}: {x - 1}")


def task5():
    N = int(input())
    K = int(input())
    print(f"Яблок у студентов: {K // N }, в корзине: {K % N}")


def task6():
    s = int(input())
    s = s % (60*60*24)
    print(s / 60 // 60, s / 60)


def task7():
    s1 = int(input()) * 60 * 60 + int(input()) * 60 + int(input())
    s2 = int(input()) * 60 * 60 + int(input()) * 60 + int(input())
    print(s2 - s1)
