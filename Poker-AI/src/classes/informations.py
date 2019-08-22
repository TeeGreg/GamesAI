class Informations:

    RED = "\033[1;38;5;124m"
    GREEN = "\033[1;38;5;47m"
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

    def availableActions(self):
        print('[bet, follow, check, fold, all-in]')

    def displayCurrentChips(self, amount):
        self._message("success", "Current chips: " + str(amount) + "💰")

    def displayCurrentBet(self, amount):
        self._message("warning", "To play: " + str(amount) + "💰")

    def chipsMissing(self):
        self._message("error", "→ I don't have enough chips!")

    def moreChips(self, amount):
        self._message("error", "→ If i want to play, i must bet at least " + str(amount) + " chips!")

    def betAmount(self):
        self._message("error", "→ I must specify an amount of chips if i want to bet!")

    def actionError(self):
        self._message("error", "→ Sorry there is an error with this action, contact the support: support@support.com")

    def invalidCheck(self):
        self._message("error", "→ No, i can't check now!")

    def invalidAction(self):
        self._message("error", "→ No, i can't do that!")

    def thinking(self):
        value = ''
        try:
            print(self.THINKING + '→ ', end="")
            value = input()
        finally:
            print(self.NONE, end="")
        return value
