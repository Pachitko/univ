import random


def printTarget(target, unguessedLetters, lives):
    letters = "".join([("\u25A0 " if c in unguessedLetters else c)
                       for c in target])
    print(f"{letters}| {lives}x\u2764")


def generateTarget(availableWords):
    return availableWords.pop() if len(availableWords) > 0 else None


def inputDifficulty():
    return int(
        input("Выберите уровень сложности: (1 - простой, 2 - средний, 3 - сложный): "))


livesPerDifficulty = [7, 5, 3]
words = ["книга", "месяц", "ручка", "шарик", "олень",
         "носок", "петь", "изысканность", "разочарование", "скатерть", "ёж"]


def yakubovich():
    lives = livesPerDifficulty[inputDifficulty() - 1]
    availableWords = words
    random.shuffle(availableWords)
    target = generateTarget(availableWords)
    hiddenLetters = set(target)
    while True:
        printTarget(target, hiddenLetters, lives)
        choice = input()
        if choice == target:
            hiddenLetters.clear()
        elif len(choice) == 1 and choice in hiddenLetters:
            hiddenLetters.remove(choice)
        else:
            lives -= 1
            print("Неправильно, вы теряете жизнь")

        if len(hiddenLetters) == 0 or lives == 0:
            if lives <= 0:
                print("Вы проиграли")
            else:
                print("Вы выиграли! Приз в студию!")

            wantToPlay = input("Хотите сыграть ещё? y/n: ")
            if wantToPlay == "y":
                target = generateTarget(availableWords)
                if target == None:
                    print("Вы отгадали все слова")
                    return
                hiddenLetters = set(target)
                lives = livesPerDifficulty[inputDifficulty() - 1]
            else:
                print("Спасибо за игру")
                return


yakubovich()
