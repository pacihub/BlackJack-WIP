from deck import Deck
from hand import Hand


class Game:
    MIN_BET = 10

    # initialize by taking a player and a dealer
    def __init__(self, player, dealer):
        self.player = player
        self.dealer = dealer
        self.bet = None
        self.deck = Deck()

    def place_bet(self):
        while True:
            bet = float(input("Place your bet: "))
            if bet > self.player.balance:
                print("You do not have enough cash.")
            elif bet < self.MIN_BET:
                print(f"The minimum bet is ${self.MIN_BET}.")
            else:
                self.bet = bet
                self.player.balance -= bet
                break

        ...

        # work in progress