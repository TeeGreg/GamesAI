from classes.informations import Informations


class Player:
    def __init__(self, name, position, chips):
        self.name = name.lower()
        self.position = position
        self._hand = []
        self._brain = Informations()
        self.chips = chips
        # CALL, RAISE, FOLD
        # NUM , NUM  , -1
        self.state = 0

    def get_name(self):
        return self.name

    def get_state(self):
        return self.state

    def get_chips(self):
        return self.chips

    def get_player(self):
        return {"name": self.name, "position": self.position}

    def take_cards(self, cards):
        i = 1
        for card in cards:
            card.set_index(i)
            self._hand.append(card)
            i += 1

    def take_card_from_deck(self, deck, index=0):
        card = deck.throw_card()
        card.set_index(index)
        self._hand.append(card)

    def show_cards(self, mode="console"):
        if mode == "console":
            return [card.get_values() for card in self._hand]
        return [card.display() for card in self._hand]

    def give_cards(self):
        ret = [card for card in self._hand]
        self._hand = []
        return ret

    def give_selected_cards(self, deck, indexes):
        cards = []
        for card in self._hand[:]:
            if card.get_index() in indexes:
                cards.append(card)
                self._hand.remove(card)
                deck.get_card(card, "side")
        return cards

    def play(self, play):
        if 0 <= play <= self.chips:
            self.state += play
            self.chips -= play
            return play
        return -1


class AIPlayer(Player):
    def new_hand(self, thrown):
        print("____New HAND____")
        self.show_cards("graphic")

    def select_cards(self):
        print("No selected AI")

    def replace(self, deck):
        print("=", self.get_name(), "=")
        self.show_cards("graphic")
        ret = self.select_cards()
        return ret

class HumanPlayer(Player):
    def select_cards(self):
        choices = []
        while True:
            string = self._brain.thinking()
            if string.lower() == "done":
                break
            if string.isdigit() and int(string) > 0 and int(string) < 6:
                choices.append(int(string))
            else:
                self._brain.invalid_card()
        return choices

    def new_hand(self, thrown):
        if thrown:
            self._brain.new_hand()
            self.show_cards("graphic")
        else:
            self._brain.no_changes()

    def replace(self, deck):
        print("=", self.get_name(), "=")
        self.show_cards("graphic")
        self._brain.switch_infos()
        ret = self.select_cards()
        return ret

    def action(self, phase, highest):
        print("=", self.get_name(), phase, "=")
        self.show_cards("graphic")
        self._brain.display_current_chips(self.chips)
        self._brain.my_bet(self.state)
        call = highest - self.state
        self._brain.display_current_bet(call)
        self._brain.available_actions()
        while True:
            action = self._brain.thinking()
            if "bet" in action.lower():
                try:
                    amount = int(action.split(" ")[1])
                    if amount >= call:
                        if self.play(amount) != -1:
                            return amount
                        self._brain.chips_missing()
                    else:
                        self._brain.more_chips(call)
                except Exception:
                    self._brain.bet_amount()
            elif "follow" in action.lower():
                if self.play(call) != -1:
                    return call
                self._brain.more_chips(call)
            elif "check" in action.lower():
                if call == 0:
                    return call
                self._brain.invalid_check()
            elif "fold" in action.lower():
                self.state = -1
                return -1
            elif "all-in" in action.lower():
                max_chips = self.chips
                if self.play(max_chips) != -1:
                    return max_chips
                self._brain.action_error()
            else:
                self._brain.invalid_action()
