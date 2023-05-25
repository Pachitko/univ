from cell import Cell
from player import Player

""" Доска с клетками """
class Board:

    """ Метод инициализации обЪекта доски """
    def __init__(self):
        self.cells = list()
        for i in range(1, 10):
            self.cells.append(Cell(i))

    """ Получить клетку по индексу """
    def getCell(self, index: int) -> Cell:
        return next(filter(lambda cell: cell.getIndex() == index, self.cells))

    """ Занята ли клетка? """
    def isCellSelected(self, index: int):
        return self.getCell(index).isSelected()

    """ Занять клетку """
    def selectCell(self, cellIndex, player: Player):
        self.getCell(cellIndex).select(player)

    """ Проверить победу игрока по его индексу """
    def checkWinByPlayer(self, player: Player) -> bool:
        return (self.checkTriples([[1, 2, 3], [1, 4, 7], [1, 5, 9], [4, 5, 6], [2, 5, 8], [3, 6, 9], [3, 5, 7]], player))

    """ Проверка трёх в ряд """
    def checkTriples(self, triples: list[list[int]], player: Player) -> bool:
        result = False
        for triple in triples:
            result |= self.checkTriple(triple, player)

        return result

    def checkTriple(self, triple: list[int], player: Player) -> bool:
        for index in triple:
            if (not self.getCell(index).isSelectedBy(player)) or not self.isCellSelected(index):
                return False
        return True

    """ Распечатать доску """
    def printBoard(self):
        self.printRow(list(range(1, 4)))
        print("-+-+-")
        self.printRow(list(range(4, 7)))
        print("-+-+-")
        self.printRow(list(range(7, 10)))

    """ Распечатать строку поля """
    def printRow(self, indexes: list):
        print(self.getCell(indexes[0]).getSymbol(), end="|")
        print(self.getCell(indexes[1]).getSymbol(), end="|")
        print(self.getCell(indexes[2]).getSymbol(
        ), end=f" {indexes[0]} {indexes[1]} {indexes[2]}\n")
