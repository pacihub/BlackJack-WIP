import random
from card import Card


class Deck:
    def __init__(self):
        self.cards = []
        self.create_deck()
        self.shuffle()

# creates a deck of cards
    def create_deck(self):
        for suit in range(4):           # 4 suits
            for card in range(1, 14):   # 13 cards each suit
                new_card = Card(suit, card)
                self.cards.append(new_card)

    def shuffle(self):
        random.shuffle(self.cards)

# deal cards either to player or dealer
    def deal(self, num_cards):
        dealt_cards = []

# start dealing from the top of the deck. Treating end of the list as top of the deck
        for idx in range(num_cards):
            # we will treat the end of the list as the top of the deck
            top_card = self.cards.pop()
            dealt_cards.append(top_card)

        return dealt_cards