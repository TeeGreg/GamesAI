class Informations:

    RED = "\033[1;38;5;124m"
    GREEN = "\033[1;38;5;47m"
    BLUE = "\033[1;38;5;38m"
    ERROR = "\033[1;38;5;63m"
    THINKING = "\033[1;38;5;226m"
    NONE = "\033[0m"

    def _message(self, state, message):
        if state == "warning":
            print(self.RED + message + self.NONE)
        elif state == "success":
            print(self.GREEN + message + self.NONE)
        elif state == "error":
            print(self.ERROR + message + self.NONE)
        elif state == "blue":
            print(self.BLUE + message + self.NONE)

    def available_actions(self):
        self._message(
            "error",
            "→ I can bet an amount, follow, check, fold and all-in by typing the corresponding command in the console!",
        )

    def display_current_chips(self, amount):
        self._message("success", "Current chips: " + str(amount) + "💰")

    def display_current_bet(self, amount):
        self._message("warning", "To play: " + str(amount) + "💰")

    def chips_missing(self):
        self._message("error", "→ I don't have enough chips!")

    def more_chips(self, amount):
        self._message(
            "error",
            "→ If i want to play, i must bet at least " + str(amount) + " chips!",
        )

    def bet_amount(self):
        self._message("error", "→ I must specify an amount of chips if i want to bet!")

    def action_error(self):
        self._message(
            "error",
            "→ Sorry there is an error with this action, contact the support: support@support.com",
        )

    def invalid_check(self):
        self._message("error", "→ No, i can't check now!")

    def switch_infos(self):
        self._message(
            "error",
            "→ I can choose cards i want to replace, just by typing their index in the console",
        )
        self._message("error", "→ Ooops, i must not forget to write 'done' after")

    def invalid_action(self):
        self._message("error", "→ No, i can't do that!")

    def my_bet(self, bet):
        self._message("blue", "Current bet: " + str(bet) + "💰")

    def invalid_card(self):
        self._message(
            "error",
            "→ This card does not exists! I must choose an index between 1 and 5",
        )

    def no_changes(self):
        self._message("error", "→ Ok then no changes, perfect hand")

    def new_hand(self):
        self._message("error", "→ Here is my new hand")

    def thinking(self):
        value = ""
        try:
            print(self.THINKING + "→ ", end="")
            value = input()
        finally:
            print(self.NONE, end="")
        return value
