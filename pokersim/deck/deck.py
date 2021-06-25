from random import shuffle

from pokersim.deck.card import (
        SUITS,
        RANKS,
        Card
)


DEFAULT_SHUFFLES = 7


class Deck:
    def __init__(self, shuffles=DEFAULT_SHUFFLES):
        """
        Initialize Deck(), creating a fresh deck and setting the number of
        shuffles.

        :param shuffles:        number of shuffles to do
        :type shuffles:         int
        """
        self.deck = self.fresh_deck()
        self.shuffles = shuffles


    def __len__(self):
        """
        Return the current length of the deck.

        :return:                number of cards left in the deck
        :rtype:                 int
        """
        return len(self.deck)


    def fresh_deck(self):
        """
        Create a new deck, spade -> heart -> diamond -> club, ace -> ... ->
        deuce.

        :return:                a deck of cards, unshuffled
        :rtype:                 list
        """
        deck = []
        for suit in SUITS:
            for rank in RANKS:
                deck.append(Card(suit, rank))
        return deck


    def shuffle(self, shuffles=DEFAULT_SHUFFLES):
        """
        Shuffle the deck <shuffles> times.

        :param shuffles:        number of times to shuffle
        :type shuffles:         int

        :return:                a shuffled deck of cards
        :rtype:                 list
        """
        shuffle(self.deck)


    def get_card(self):
        """
        Take the top card off the deck and return it.

        :return:                playing card
        :rtype:                 dict
        """
        return self.deck.pop()
