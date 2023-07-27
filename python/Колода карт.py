
# import collections

# Card = collections.namedtuple('Card', ['rank', 'suit'])


# class FrenchDeck:
#     ranks = [str(n) for n in range(2, 11)] + list('JQKA')
#     print(ranks)
#     suits = 'spades diamonds clubs hearts'.split()

#     def __init__(self):
#         self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]

#     def __len__(self):
#         return len(self._cards)

#     def __getitem__(self, position):
#         return self._cards[position]
from random import choice


class Card:
    ranks = [str(i) for i in range(6, 11)] + list("ВДКТ")
    suits = 'пики бубны трефы червы'.split()

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return f"{self.rank} : {self.suit}"


class Deck:
    def __init__(self):
        self.cards = self.create_deck()

    def create_deck(self):
        return [Card(rank, suit) for suit in Card.suits for rank in Card.ranks]

    def __str__(self):
        return ''.join(str(card) for card in self.cards)

    def get_random_card(self):
        return choice(self.cards)


coloda = Deck()
print(coloda)
print(coloda.get_random_card())

