from entities.board import Board
from entities.player import Player
from entities.humanPlayer import HumanPlayer
from entities.pcPlayer import PcPlayer

# Сущность игры


class Game:
    # Занять клетку, True - клетка успешно занята, False - клетка уже была занята
    def selectCell(self, board: Board, index: int, player: Player) -> bool:
        if board.isCellSelected(index):
            return False

        board.selectCell(index, player)
        return True

    # Проверка победы игрока
    def setWonIfWon(self, player: Player, game_board: Board):
        if game_board.checkWinByPlayer(player):
            player.setWon()

    # Ход игрока
    def playerTurn(self, player: Player, game_board: Board):
        print(f"What is {player.getPlayerName()}'s move? (1-9)")
        cellIndex = player.getSelectedCellIndex()
        while not self.selectCell(game_board, int(cellIndex), player):
            if isinstance(player, HumanPlayer):
                print("This cell already taken! Choose another!")
            cellIndex = player.getSelectedCellIndex()
        if isinstance(player, PcPlayer):
            print(cellIndex)
        game_board.printBoard()
        self.setWonIfWon(player, game_board)

    # Игровая механика
    def start(self):
        pveOrPvp = input("PVE or PVP? (1 - PVE, 2 - PVP): ")

        player1 = HumanPlayer(1, 'O', 'player1')
        activePlayerIndex = player1.getIndex()

        if int(pveOrPvp) == 1:
            player2 = PcPlayer(2, 'X', 'pcName')
        else:
            player2 = HumanPlayer(2, 'X', 'player2')

        board = Board()

        counter = 9

        print("Welcome to tic-tac-toe!")
        board.printBoard()

        while (not player1.isWon()) and (not player2.isWon()) and (counter > 0):
            if player1.getIndex() == activePlayerIndex:
                self.playerTurn(player1, board)
                activePlayerIndex = player2.getIndex()
            else:
                self.playerTurn(player2, board)
                activePlayerIndex = player1.getIndex()

            counter = counter - 1

        if player1.isWon():
            print(f"{player1.getPlayerName()} has won the game!")
        elif player2.isWon():
            print(f"{player2.getPlayerName()} has won the game!")
        else:
            print("Draw!")

        print("Thanks for playing!")


Game().start()
