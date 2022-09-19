from Player import Player
from config import STILL

# Class que representa o jogador na instruction screen
class PlayerInstru(Player):

    # Construtor da classe pai
    def __init__(self, player_sheet):
        super().__init__(player_sheet)
        self.default = STILL