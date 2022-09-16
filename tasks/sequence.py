from extensions import readSeq
import sys


def task1():
    seq = readSeq()
    for n in seq:
        if (n % 2 == 1):
            print(n, end=' ')


def task2():
    seq = readSeq()
    for i, n in enumerate(seq):
        if (i == 0):
            continue
        if (n > seq[i - 1]):
            print(n, end=' ')
    print()


def task3():
    seq = readSeq()
    for i, n in enumerate(seq):
        if (i % 2 == 1):
            print(n, seq[i-1], end=' ')

    if (len(seq) % 2 == 1):
        print(seq[-1])

    print()


def task4():
    seq = readSeq()
    max, maxIdx = seq[0], 0
    min, minIdx = seq[0], 0

    for i, n in enumerate(seq):
        if (n > max):
            max = n
            maxIdx = i
        elif (n < min):
            min = n
            minIdx = i

    seq[maxIdx], seq[minIdx] = seq[minIdx], seq[maxIdx]
    print(seq)


def task5():
    seq1 = readSeq()
    seq2 = readSeq()

    count = 0
    for n1 in seq1:
        for n2 in seq2:
            if (n1 == n2):
                count += 1

    print(count)


def task6():
    seq1 = readSeq()
    seq2 = readSeq()

    seq1.sort()
    seq2.sort()

    for n1 in seq1:
        for n2 in seq2:
            if (n1 == n2):
                print(n1, end=' ')
            elif (n2 > n1):
                break

    print()


def task7():
    seq = readSeq()

    for i, n in enumerate(seq):
        seen = False
        for i in range(i - 1, 0, -1):
            if (seq[i] == n):
                print("YES")
                seen = True
                break

        if (seen == False):
            print("NO")


def task8():
    s = input()

    print(s[2])
    print(s[-1])
    print(s[:5])
    print(s[:-2])
    [(print(n, end='') if i % 2 == 0 else 0) for i, n in enumerate(s)]
    print()
    [(print(n, end='') if i % 2 == 1 else 0) for i, n in enumerate(s)]
    print()
    print(s[::-1])
    [(print(n, end='') if i % 2 == 0 else 0) for i, n in enumerate(s[::-1])]
    print()


def task9():
    s = input()
    mid = len(s) // 2 + len(s) % 2
    print(f'{s[mid:]}{s[:mid]}')


def task10():
    s = input()

    leftIdx = s.index('h')
    rightIdx = s[::-1].index('h')

    print(f'{s[:leftIdx]}{s[(len(s) - rightIdx):]}')


def task11():
    s = input()

    leftIdx = s.index('h')
    rightIdx = s[::-1].index('h')

    print(
        f'{s[:leftIdx]}{s[(len(s) - rightIdx - 1):(leftIdx - 1):-1]}{s[(len(s) - rightIdx):]}')


def task12():
    s = input()

    leftIdx = s.index('h')
    rightIdx = s[::-1].index('h')
    x = s[leftIdx + 1:len(s)-rightIdx - 1].replace('h', 'H')
    print(f'{s[:leftIdx + 1]}{x}{s[len(s) - rightIdx - 1:]}')


if (len(sys.argv) > 1):
    eval(f"task{sys.argv[1]}()")
