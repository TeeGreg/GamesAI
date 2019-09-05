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


    def get_values(self):
        return {'index': self.index, 'color': self.color, 'number': self.number}

    def set_index(self, index):
        self.index = index

    def get_index(self):
        return self.index

    def display(self):
        print(self)
        return self.get_values()

    def __str__(self):
        number = self._values[self.number] if self.number > 10 else self.number
        style = str(self.index) + "." + " _______\n"
        style += '  |' + str(number) + self._symbols[self.color]
        if isinstance(number, int) and number > 9:
            style += '    |\n'
        else:
            style += '     |\n'
        style += "  |_______|"
        return style

    def __repr__(self):
        return str(self.get_values())

    def __eq__(self, other):
        return self.number == other.number

    def __ne__(self, other):
        return self.number != other.number

    def __lt__(self, other):
        return self.number < other.number

    def __le__(self, other):
        return self.number <= other.number

    def __gt__(self, other):
        return self.number > other.number

    def __ge__(self, other):
        return self.number >= other.number
