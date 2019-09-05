# COLORS:
#   CLUBS, DIAMONDS, HEARTS, SPADES
# VALUES:
#   ACE: 1, NORMAL: 2-10, JACK: 11, QUEEN: 12, KING: 13

class Card:

    _values = {11: "J", 12: "Q", 13: "K", 14: "A"}
    _symbols = {"Clubs": "♣️", "Diamonds": "♦️", "Hearts": "♥️", "Spades": "♠️"}

    def __init__(self, color, number):
        self.color = color
        self.number = number
        self.index = 0

    def _print(self, color, number, index):
        number = self._values[number] if number > 10 else number
        style = str(index) + "." + " _______\n"
        style += '  |' + str(number) + self._symbols[color]
        if isinstance(number, int) and number > 9:
            style += '    |\n'
        else:
            style += '     |\n'
        style += "  |_______|"
        print(style)

    def get_values(self):
        return {'index': self.index, 'color': self.color, 'number': self.number}

    def set_index(self, index):
        self.index = index

    def get_index(self):
        return self.index

    def display(self):
        self._print(self.color, self.number, self.index)
        return self.get_values()
