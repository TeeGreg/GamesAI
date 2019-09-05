from card import Card

COMBOS = ("Quint Flush", "Square", "Full", "Flush", "Quint", "Brelan", "Double Pair", "Pair", "High")

class Hand():


    def __init__(self, cards):
        self.cards = sorted(cards, reverse=True)

    def __eq__(self, other):
        return COMBOS.index(self.eval_combo()) == COMBOS.index(other.eval_combo()) and self.compare_same_combo(other)

    def __ne__(self, other):
        return COMBOS.index(self.eval_combo()) != COMBOS.index(other.eval_combo()) or not self.compare_same_combo(other)

    def __lt__(self, other):
        return COMBOS.index(self.eval_combo()) > COMBOS.index(other.eval_combo()) or \
        COMBOS.index(self.eval_combo()) == COMBOS.index(other.eval_combo()) and self.compare_same_combo(other) < 0

    def __le__(self, other):
        return COMBOS.index(self.eval_combo()) > COMBOS.index(other.eval_combo()) or \
        COMBOS.index(self.eval_combo()) == COMBOS.index(other.eval_combo()) and self.compare_same_combo(other) <= 0

    def __gt__(self, other):
        return COMBOS.index(self.eval_combo()) < COMBOS.index(other.eval_combo()) or \
        COMBOS.index(self.eval_combo()) == COMBOS.index(other.eval_combo()) and self.compare_same_combo(other) > 0

    def __ge__(self, other):
        return COMBOS.index(self.eval_combo()) < COMBOS.index(other.eval_combo()) or \
        COMBOS.index(self.eval_combo()) == COMBOS.index(other.eval_combo()) and self.compare_same_combo(other) >= 0

    def __repr__(self):
        return str(self.cards)

    def __str__(self):
        return "\n".join(str(c) for c in self.cards)

    def is_quint_flush(self):
        if self.is_quint() and self.is_flush():
            return "Quint Flush"
        return None

    def is_square(self):
        if self.cards[0].number == self.cards[1].number == self.cards[2].number == self.cards[3].number or\
              self.cards[1].number == self.cards[2].number == self.cards[3].number == self.cards[4].number:
            return "Square"
        return None

    def is_full(self):
        if self.cards[0].number == self.cards[1].number and self.cards[2].number == self.cards[3].number == self.cards[4].number or\
              self.cards[0].number == self.cards[1].number == self.cards[2].number and self.cards[3].number == self.cards[4].number:
            return "Full"
        return None

    def is_flush(self):
        if self.cards[0].color == self.cards[1].color == self.cards[2].color == self.cards[3].color == self.cards[4].color:
            return "Flush"
        return None

    def is_quint(self):
        if self.cards[0].number == self.cards[1].number + 1 == self.cards[2].number + 2 == self.cards[3].number + 3 == self.cards[4].number + 4:
            return "Quint"
        if self.cards[1].number - 4 == self.cards[2].number - 3 == self.cards[3].number - 2 == self.cards[4].number - 1 == self.cards[0].number - 13 == 1:
            return "Quint"
        return None

    def is_brelan(self):
        if self.cards[0].number == self.cards[1].number == self.cards[2].number or\
         self.cards[1].number == self.cards[2].number == self.cards[3].number or\
         self.cards[2].number == self.cards[3].number == self.cards[4].number:
            return "Brelan"
        return None

    def is_double_pair(self):
        if self.cards[0].number == self.cards[1].number and self.cards[2].number == self.cards[3].number or\
         self.cards[1].number == self.cards[2].number and self.cards[3].number == self.cards[4].number or\
         self.cards[0].number == self.cards[1].number and self.cards[3].number == self.cards[4].number:
            return "Double Pair"
        return None

    def is_pair(self):
        if self.cards[0].number == self.cards[1].number or self.cards[2].number == self.cards[3].number or\
         self.cards[1].number == self.cards[2].number or self.cards[3].number == self.cards[4].number:
            return "Pair"
        return None

    def eval_combo(self):
        order = (self.is_quint_flush, self.is_square, self.is_full, self.is_flush, self.is_quint, self.is_brelan, self.is_double_pair, self.is_pair)
        for a_combo in order:
            whatsthat = a_combo()
            if whatsthat:
                return whatsthat
        return "High"

    def compare_same_combo(self, other):
        for card1, card2 in zip(self.cards, other.cards):
            if card1.number > card2.number:
                return 1
            if card2.number > card1.number:
                return -1
        return 0

# COLORS:
#   Clubs, Diamonds, Hearts, Spades
# VALUES:
#   ACE: 1, NORMAL: 2-10, JACK: 11, QUEEN: 12, KING: 13
def test():
    hand1 = (Card("Hearts", 14),Card("Hearts", 2),Card("Hearts", 3),Card("Hearts", 4),Card("Hearts", 5),)
    hand2 = (Card("Clubs", 14),Card("Diamonds", 14),Card("Spades", 14),Card("Hearts", 14),Card("Hearts", 5),)
    hand2bis = (Card("Clubs", 14),Card("Diamonds", 14),Card("Spades", 14),Card("Spades", 5),Card("Hearts", 5),)
    hand3 = (Card("Hearts", 14),Card("Hearts", 2),Card("Hearts", 8),Card("Hearts", 4),Card("Hearts", 5),)
    hand4 = (Card("Clubs", 14),Card("Hearts", 2),Card("Hearts", 3),Card("Hearts", 4),Card("Hearts", 5),)
    hand5 = (Card("Clubs", 14),Card("Diamonds", 14),Card("Spades", 14),Card("Spades", 8),Card("Hearts", 5),)
    hand6 = (Card("Clubs", 14),Card("Diamonds", 14),Card("Spades", 8),Card("Spades", 5),Card("Hearts", 5),)
    hand7 = (Card("Clubs", 14),Card("Diamonds", 14),Card("Spades", 8),Card("Spades", 5),Card("Hearts", 3),)
    handy1 = Hand(hand1)
    print(handy1)
    print(handy1.eval_combo())
    handy2 = Hand(hand2)
    print(handy2)
    print(handy2.eval_combo())
    handy2b = Hand(hand2bis)
    print(handy2b)
    print(handy2b.eval_combo())
    handy3 = Hand(hand3)
    print(handy3)
    print(handy3.eval_combo())
    handy4 = Hand(hand4)
    print(handy4)
    print(handy4.eval_combo())
    handy5 = Hand(hand5)
    print(handy5)
    print(handy5.eval_combo())
    handy6 = Hand(hand6)
    print(handy6)
    print(handy6.eval_combo())
    handy7 = Hand(hand7)
    print(handy7)
    print(handy7.eval_combo())

    print(handy1 > handy2 > handy2b > handy3 > handy4 > handy5 > handy6 > handy7)

if __name__ == '__main__':
    test()
