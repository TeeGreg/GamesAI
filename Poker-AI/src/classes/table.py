# DECK
from classes.deck import Deck
# PLAYERS
from classes.player import Player

class Table:

    def __init__(self, players):
        self._players = players
        self._deck = Deck()

    def getPlayers(self):
        return [ player.getPlayer() for player in self._players ]

    def showPlayersCards(self):
        return [ {'player': player.getName(), 'hand': player.showCards()} for player in self._players ]

    def shuffleDeck(self):
        self._deck.shuffleCards()

    def showDeck(self):
        return self._deck.displayCards()

    def deckCountCards(self):
        return self._deck.cardCount()

    def distributeCards(self):
        for player in self._players:
            cards = [ self._deck.throwCard() ]
            cards.append(self._deck.throwCard())
            player.takeCards(cards)

    def returnCards(self):
        for player in self._players:
            cards = player.giveCards()
            for card in  cards:
                self._deck.getCard(card)

    def preFlop(self):
        return 1

    def playOneHand(self):
        # SHUFFLING DECK
        self.shuffleDeck()
        # INITIALIZING POT TO 0
        self.pot = 0
        # ============================================
        # TODO DEFINE PLAYER ORDER DEPENDING ON BLINDS
        # ============================================
        # DISTRIBUTING RANDOM CARDS TO PLAYERS
        self.distributeCards()
        print(self.showPlayersCards())
        # PREFLOP PHASE
        self.preFlop()
        # GIVING BACK PLAYERS CARDS TO DECK
        self.returnCards()