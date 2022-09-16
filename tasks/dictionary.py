import sys

from extensions import readInt


def task1():
    words = input().split()
    d = dict()
    for w in words:
        if (w not in d):
            d[w] = 0

        print(d[w], end=' ')
        d[w] += 1

    print()


def task2():
    N = readInt()
    d = dict()
    for _ in range(N):
        words = input().split()
        d[words[0]] = words[1]
        d[words[1]] = words[0]

    print(d[input()])


def task3():
    N = readInt()
    d = dict()

    for _ in range(N):
        parts = input().split()
        d[parts[0]] = \
            d[parts[0]] + int(parts[1]) if parts[0] in d else int(parts[1])

    for k in sorted(d.keys()):
        print(f"{k} {d[k]}")


def task4():
    N = readInt()
    d = dict()
    maxCount = -1

    for _ in range(N):
        words = input().split()
        for w in words:
            d[w] = d[w] + 1 if w in d else 1
            maxCount = max(maxCount, d[w])

    candidates = []

    for k, v in d.items():
        if (v == maxCount):
            candidates.append(k)

    print(sorted(candidates)[0])


def task5():
    opToChar = {
        "read": "R",
        "write": "W",
        "execute": "X"
    }

    d = dict()

    for _ in range(readInt()):
        parts = input().split()
        if (len(parts) > 1):
            d[parts[0]] = "".join(parts[1:])

    for _ in range(readInt()):
        parts = input().split()
        if (opToChar[parts[0]] in d[parts[1]]):
            print("OK")
        else:
            print("Denied")


def task6():
    d = dict()
    for _ in range(readInt()):
        parts = input().split()
        for city in parts[1:]:
            d[city] = parts[0]

    for _ in range(readInt()):
        print(d[input()])


def task7():
    d = dict()
    for _ in range(readInt()):
        words = input().split()
        for w in words:
            d[w] = (d[w][0] + 1, w) if w in d else (1, w)

    for v in sorted(d.values(), reverse=True):
        print(v[1], v[0])


if (len(sys.argv) > 1):
    eval(f"task{sys.argv[1]}()")
