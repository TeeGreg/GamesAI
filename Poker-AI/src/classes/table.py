# DECK
from classes.deck import Deck

# PLAYERS
# from classes.player import Player


class Table:
    def __init__(self, players, blind):
        self._players = players
        self._blind = blind
        self._deck = Deck()
        self.pot = 0

    def get_players(self):
        return [player.get_player() for player in self._players]

    def show_players_cards(self, mode="console"):
        if mode == "console":
            return [
                {"player": player.get_name(), "hand": player.show_cards("console")}
                for player in self._players
            ]
        for player in self._players:
            print(player.get_name() + ":")
            player.show_cards("graphic")
        return ""

    def shuffle_deck(self):
        self._deck.shuffle_cards()

    def show_deck(self):
        return self._deck.display_cards()

    def deck_count_cards(self):
        return self._deck.card_count()

    def distribute_cards(self):
        for player in self._players:
            cards = [self._deck.throw_card()]
            for _ in range(4):
                cards.append(self._deck.throw_card())
            player.take_cards(cards)

    def return_cards(self):
        for player in self._players:
            cards = player.give_cards()
            for card in cards:
                self._deck.get_card(card)

    def are_player_ok(self):
        leader = 0
        for player in self._players:
            state = player.get_state()
            if state >= 0 and leader == 0:
                leader = state
            elif state >= 0 and state != leader:
                return 0
        return 1

    def highest_player(self):
        leader = 0
        for player in self._players:
            state = player.get_state()
            if state >= 0 and state > leader:
                leader = state
        return leader

    def _pot_informations(self):
        print("- Pot:", str(self.pot) + "💰", "-")

    def players_action(self, state, high_blind=0):
        while True:
            for player in self._players:
                self._pot_informations()
                if high_blind > 0:
                    action = player.action(state, high_blind)
                    high_blind = 0
                else:
                    action = player.action(state, self.highest_player())
                if action > 0:
                    self.pot += action
                if self.are_player_ok():
                    return

    def _phase_begin_informations(self, phase):
        print("====" + phase + "====")
        if phase == "PREFLOP":
            for player in self._players:
                print(player.get_name() + ": " + str(player.get_chips()) + "💰")
            self._pot_informations()
            print("===============")

    def _phase_end_informations(self, phase):
        print("\n= Pot:", str(self.pot) + "💰", "=")

    def pre_flop(self, blind):
        self._phase_begin_informations("PREFLOP")
        # TODO BLINDS
        self.players_action("preflop", blind)
        self._phase_end_informations("PREFLOP")

    def switch_phase(self):
        self._phase_begin_informations("SWITCH PHASE")
        for player in self._players:
            player.replace(self._deck)

    def reveal_phase(self):
        self._phase_begin_informations("REVEAL")
        self.players_action("reveal")
        # WINNER ?

    def play_one_hand(self):
        # SHUFFLING DECK
        self.shuffle_deck()
        # INITIALIZING POT TO 0
        self.pot = 0
        # ============================================ #
        # TODO DEFINE PLAYER ORDER DEPENDING ON BLINDS #
        # ============================================ #
        # DISTRIBUTING RANDOM CARDS TO PLAYERS
        self.distribute_cards()
        # PREFLOP PHASE
        self.pre_flop(self._blind)
        # CHANGE CARDS PHASE
        self.switch_phase()
        # LAST PHASE WHERE CARDS ARE REVEALED
        self.reveal_phase()
        # GIVING BACK PLAYERS CARDS TO DECK
        self.return_cards()
        print("======END======")
