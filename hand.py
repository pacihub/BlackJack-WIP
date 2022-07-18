class Hand:
    def __init__(self, cards):
        self.cards = cards

    # calculate hand value per the rules
    def get_value(self):
        # hand value without aces
        value = 0
        aces = 0

        for card in self.cards:
            val = card.value
            if val == 1:    # check if card value = 1
                aces += 1   # if it is, therefore it's an ace. aces++
            else:
                value += min(val, 10)   # if my card is 11, this means Jack, so I need to add 10 points.
                                        # I could also have a 7, 10 which is lower than 10 so I add 7
        if aces == 0:
            return value

        if value + 11 > 21:     # I can't treat even a single ace as 11
            return value + aces # # therefore I'll treat every ace as 1
        elif aces == 1:         # means I can treat at least 1 ace as 11
            return value + 11
        elif value + 11 + (aces - 1) <= 21:
            return value + 11 + (aces - 1)
        else:
            return value + aces

    # add a card when hit
    def add_card(self, card):
        self.cards.append(card)

    # hand representation
    def __str__(self):
        string_cards = [str(card) for card in self.cards]
        return ", ".join(string_cards)