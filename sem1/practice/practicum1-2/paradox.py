import random


def monty_hall(N):
    correct1, correct2 = 0, 0

    for _ in range(N):
        prize = random.randrange(1, 4)
        choice1, choice2 = random.randrange(1, 4), random.randrange(1, 4)

        if (choice1 == prize):
            correct1 += 1
        if (choice2 == prize):
            correct2 += 1
        else:
            choices = [1, 2, 3]
            choices.remove(choice2)
            choice2 = choices[random.randrange(0, 2)]
            if (choice2 == prize):
                correct2 += 1

    return correct2/N


def birthday(N):
    daysInMonth = 28
    daysInYear = daysInMonth * 12

    matched = 0
    for _ in range(N):
        birthdays = [random.randrange(1, daysInYear) for _ in range(23)]
        s = set()
        for b in birthdays:
            if b in s:
                matched += 1
                break
            s.add(b)
        # if (len(s) != len(birthdays)):
        #     matched += 1

    return matched / N
