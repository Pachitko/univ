from player import Player
import random

# Игрок-компьютер
class PcPlayer(Player):

    # Случайный выбор клетки
    def getSelectedCellIndex(self):
        cell_number = random.randint(1, 9)
        return cell_number
