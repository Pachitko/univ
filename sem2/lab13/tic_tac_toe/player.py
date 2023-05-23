from abc import ABC, abstractmethod

# Базовый класс игрока
class Player(ABC):

    # Инициализация игрока
    def __init__(self, index, symbol, playerName="playerName"):
        self.index = index
        self.symbol = symbol
        self.won = False
        self.playerName = playerName

    def getSymbol(self):
        return self.symbol
    
    def getIndex(self):
        return self.index

    # Победил ли игрок?
    def isWon(self) -> bool:
        return self.won

    # Игрок победил
    def setWon(self):
        self.won = True

    # Метод получения имени игрока
    def getPlayerName(self):
        return self.playerName

    @abstractmethod
    def getSelectedCellIndex(self):
        pass
