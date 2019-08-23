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

    def availableActions(self):
        self._message("error", '→ I can bet an amount, follow, check, fold and all-in by typing the corresponding command in the console!')

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

    def switchInfos(self):
        self._message("error", "→ I can choose cards i want to replace, just by typing their index in the console")
        self._message("error", "→ Ooops, i must not forget to write 'done' after")

    def invalidAction(self):
        self._message("error", "→ No, i can't do that!")

    def myBet(self, bet):
        self._message("blue", "Current bet: " + str(bet) + "💰")

    def invalidCard(self):
        self._message("error", "→ This card does not exists! I must choose an index between 1 and 5")

    def noChanges(self):
        self._message("error", "→ Ok then no changes, perfect hand")

    def newHand(self):
        self._message("error", "→ Here is my new hand")

    def thinking(self):
        value = ''
        try:
            print(self.THINKING + '→ ', end="")
            value = input()
        finally:
            print(self.NONE, end="")
        return value
