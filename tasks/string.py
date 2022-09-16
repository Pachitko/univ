def task1():
    print(input().count(' ') + 1)


def task2():
    strs = input().split(' ')
    print(strs[1], strs[0])


def task3():
    s = input()
    parts = s.split('f')
    if (len(parts) == 1):
        print(-1)
    elif (len(parts) == 2):
        print(len(parts[0]))
    else:
        print(f"{len(parts[0])} {len(s)-len(parts[-1]) - 1}")


def task4():
    s = input()
    print(s.replace('1', 'one'))


def task5():
    email = input()
    print(email.replace('@', ''))