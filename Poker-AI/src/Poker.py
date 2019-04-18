from classes.deck import Deck

if __name__ == '__main__':
    deck = Deck()
    print("Threw:", deck.throw())
    print(deck.getRemaining())