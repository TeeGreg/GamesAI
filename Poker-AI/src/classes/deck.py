import random

from classes.card import Card

# COLORS:
#   CLUBS, DIAMONDS, HEARTS, SPADES
# VALUES:
#   ACE: 1, NORMAL: 2-10, JACK: 11, QUEEN: 12, KING: 13


class Deck:
    def _create_color(self, color):
        for i in range(2, 14):
            self._deck.append(Card(color, i))
        return self

    def __init__(self):
        self._deck = []
        self._create_color("Clubs")._create_color("Diamonds")\
        ._create_color("Hearts")._create_color("Spades")

    def shuffle_cards(self):
        random.shuffle(self._deck)
        return self._deck

    def display_cards(self):
        return [card.get_values() for card in self._deck]

    def card_count(self):
        return len(self._deck)

    def throw_card(self):
        choice = random.choice(self._deck)
        self._deck.remove(choice)
        return choice

    def get_card(self, card):
        self._deck.append(card)
        return card
