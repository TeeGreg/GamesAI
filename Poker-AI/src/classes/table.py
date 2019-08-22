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

    def showPlayersCards(self, mode="console"):
        if mode == "console":
            return [ {'player': player.getName(), 'hand': player.showCards("console")} for player in self._players ]
        for player in self._players:
            print(player.getName() + ':')
            player.showCards("graphic")
        return ""

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

    def PlayersAreOk(self):
        leader = 0
        for player in self._players:
            state = player.getState()
            if state >= 0 and leader == 0:
                leader = state
            elif state >= 0 and state != leader:
                return 0
        return 1

    def PlayersReturnHighest(self):
        leader = 0
        for player in self._players:
            state = player.getState()
            if state >= 0 and state > leader:
                leader = state
        return leader

    def playersAction(self, state, highBlind=0):
        while True:
            for player in self._players:
                if highBlind > 0:
                    action = player.action(state, highBlind)
                    highBlind = 0
                else:
                    action = player.action(state, self.PlayersReturnHighest())
                if action > 0:
                    self.pot += action
                if self.PlayersAreOk():
                    return

    def preFlop(self):
        print("====PREFLOP====")
        print("= Pot:", str(self.pot) + "💰", "=\n")
        # TODO BLINDS
        self.playersAction("preflop", 50)
        print("\n= Pot:", str(self.pot) + "💰", "=")
        print("======END======")

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
        print(self.showPlayersCards("graphic"))
        # PREFLOP PHASE
        self.preFlop()
        # GIVING BACK PLAYERS CARDS TO DECK
        self.returnCards()
