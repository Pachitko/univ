from player import Player

""" Сущность клетки игры, с состоянием занятости игроком """
class Cell:

    """ Инициализация """
    def __init__(self, index = 1):
        self.owner = None
        self.index = index

    def getSymbol(self):
        if self.owner is None:
            return " "
        
        return self.owner.getSymbol()
    
    """ Занята ли клетка? """
    def isSelected(self):
        return self.owner is not None

    """ Занята ли клетка игроком? """
    def isSelectedBy(self, player: Player):
        if self.owner is None:
            return False
        return self.owner.getIndex() == player.getIndex()

    """ Получение индекса клетки """
    def getIndex(self):
        return self.index

    """ Занять клетку игроком"""
    def select(self, player: Player):
        self.owner = player
