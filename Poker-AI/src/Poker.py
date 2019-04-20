from classes.table import Table
from classes.player import Player

if __name__ == '__main__':
    players = [Player("Patrick", 1), Player("Moundir", 2)]
    table = Table(players)
    table.playOneHand()