# COLORS:
#   CLUBS, DIAMONDS, HEARTS, SPADES
# VALUES:
#   ACE: 1, NORMAL: 2-10 ,JACK: 11, QUEEN: 12, KING: 13

class Card:

    def __init__(self, color, number):
        self.color = color
        self.number = number

    def getValues(self):
        return {'color': self.color, 'number': self.number}