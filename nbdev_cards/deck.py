# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/00_deck.ipynb.

# %% auto 0
__all__ = ['Deck']

# %% ../nbs/00_deck.ipynb 4
class Deck:
    """Class representing a deck of cards"""

    def __init__(
        self,
        cards: list[Card],  # List of cards
    ):
        self.cards = cards

    def __str__(self):
        return "; ".join(self.cards)

    __repr__ = __str__

    def __lt__(self, deck: "Deck"):  # Another deck to compare with
        for eigen_card in self.cards:
            for other_card in deck:
                if eigen_card > other_card:
                    return False
        return True

    def __gt__(self, deck: "Deck"):  # Another deck to compare with
        for eigen_card in self.cards:
            for other_card in deck:
                if eigen_card < other_card:
                    return False
        return True

    def __eq__(self, deck: "Deck"):  # Another deck to compare with
        for eigen_card in self.cards:
            for other_card in deck.cards:
                if eigen_card < other_card or eigen_card > other_card:
                    return False
        return True
