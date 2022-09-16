def task1():
    x = int(input())

    i = 2
    while (x % i != 0):
        i += 1

    print(i)


def task2():
    x = int(input())

    i = 1
    while (pow(2, i + 1) < x):
        i += 1
    print(i, pow(2, i))


def task3():
    X = float(input())
    Y = float(input())
    step = X * 0.1

    days = 2
    while (X + step < Y):
        X += step
        step = X * 0.1
        days += 1

    print(days)


def task4():
    count = 0
    number = int(input())
    while (True):
        prev = number
        number = int(input())

        if (number == 0):
            break
        else:
            if (number > prev):
                count += 1

        prev = number

    print(count)


def task5():
    x = int(input())
    i = 1
    print(1)
    while (pow(i + 1, 2) <= x):
        print(pow(i + 1, 2))
        i += 1


def task6():
    N = int(input())
    if (N == 1):
        print(1)
        return

    prev = 1
    cur = 1
    pos = 2
    while (cur < N):
        prev, cur = cur, cur + prev
        pos += 1

    print(pos if cur == N else -1)


def task7():
    N = int(input())

    prev = 1
    cur = 1
    pos = 2
    while (pos < N):
        prev, cur = cur, cur + prev
        pos += 1

    print(cur)


def task8():
    prev = int(input())
    count = 1
    maxCount = 1
    while (prev != 0):
        n = int(input())
        if (n == 0):
            break

        if (n == prev):
            count += 1
            maxCount = max(maxCount, count)
        else:
            count = 1

        prev = n

    print(maxCount)
