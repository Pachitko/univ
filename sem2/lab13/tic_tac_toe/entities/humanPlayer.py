from player import Player

""" Игрок-человек """
class HumanPlayer(Player):

    """ Получение индекса выбранной клетки для игрока-человека """
    def getSelectedCellIndex(self) -> int:
        cellIndex = input()

        while not cellIndex.isdigit():
            print("Must be digit!")
            cellIndex = input("")
        return int(cellIndex)
