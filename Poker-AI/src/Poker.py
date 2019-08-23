from classes.table import Table
from classes.player import HumanPlayer

if __name__ == '__main__':
    players = [HumanPlayer("Patrick", 1, 1000), HumanPlayer("Moundir", 2, 1000)]
    table = Table(players, 50)
    table.playOneHand()
