SUITS = {
        'spade':    { 'name': 'Spade',      'symbol': 'S', 'value': 4 },
        'heart':    { 'name': 'Heart',      'symbol': 'H', 'value': 3 },
        'diamond':  { 'name': 'Diamond',    'symbol': 'D', 'value': 2 },
        'club':     { 'name': 'Club',       'symbol': 'C', 'value': 1 }
}
RANKS = {
        'ace':      { 'name': 'Ace',    'symbol': 'A', 'value': 14 },
        'king':     { 'name': 'King',   'symbol': 'K', 'value': 13 },
        'queen':    { 'name': 'Queen',  'symbol': 'Q', 'value': 12 },
        'jack':     { 'name': 'Jack',   'symbol': 'J', 'value': 11 },
        'ten':      { 'name': 'Ten',    'symbol': 'T', 'value': 10 },
        'nine':     { 'name': 'Nine',   'symbol': '9', 'value': 9  },
        'eight':    { 'name': 'Eight',  'symbol': '8', 'value': 8  },
        'seven':    { 'name': 'Seven',  'symbol': '7', 'value': 7  },
        'six':      { 'name': 'Six',    'symbol': '6', 'value': 6  },
        'five':     { 'name': 'Five',   'symbol': '5', 'value': 5  },
        'four':     { 'name': 'Four',   'symbol': '4', 'value': 4  },
        'three':    { 'name': 'Three',  'symbol': '3', 'value': 3  },
        'two':      { 'name': 'Two',    'symbol': '2', 'value': 2  },
}


class Card:
    def __init__(self, suit, rank):
        """
        Initializes a card, setting a suit and rank.

        :param suit:            suit of the card
        :type suit:             string
        :param rank:            rank of the card
        :type rank:             string
        """
        self.suit = SUITS[suit]
        self.rank = RANKS[rank]


    def __str__(self):
        """
        Pretty string representation of the card.

        :return:                what the printing the card should show
        :rtype:                 string
        """
        return "{} of {}s".format(self.rank['name'], self.suit['name'])


    def __lt__(self, comp_card):
        """
        Returns true if self is less than <comp_card>. First we compare by suit:
        Spade > Heart > Diamond > Club. If suits are equal, we compare by rank:
        King > Queen > Jack > Ten > ... > Deuce.

        :param comp_card:       card to compare self to
        :type comp_card:        Card

        :return:                True if self less than <card>, otherwise False.
        :rtype:                 bool
        """
        if self.suit['value'] == comp_card.suit['value']:
            return self.rank['value'] < comp_card.rank['value']
        else:
            return self.suit['value'] < comp_card.suit['value']


    def __eq__(self, comp_card):
        """
        Returns true if self is equal to <comp_card>. This means that both suit and rank must match.

        :param comp_card:       card to compare self to
        :type comp_card:        Card

        :return:                True if self equal to <comp_card>, otherwise False.
        :rtype:                 bool
        """
        return (self.suit['value'] == comp_card.suit['value'] and
                self.rank['value'] == comp_card.rank['value'])


    def __gt__(self, comp_card):
        """
        Returns true if self is less than <comp_card>. First we compare by suit:
        Spade > Heart > Diamond > Club.
        If suits are equal, we compare by rank:
        King > Queen > Jack > Ten > ... > Deuce.

        :param comp_card:       card to compare self to
        :type comp_card:        Card

        :return:                True if self greater than <comp_card>, otherwise False.
        :rtype:                 bool
        """
        if self.suit['value'] == comp_card.suit['value']:
            return self.rank['value'] > comp_card.rank['value']
        else:
            return self.suit['value'] > comp_card.suit['value']


    def get_symbol(self):
        """
        Get the card represented as a two character "<rank><suit>" string.

        :return:                short representation of card of the form "<rank><string>"
        :rtype:                 string
        """
        return "{}{}".format(self.rank['symbol'], self.suit['symbol'])


    def get_card(self):
        """
        Get the card in a way that will be useable (i.e., a dict with a keys suit, rank).

        :return:                a useful representation of the card
        :rtype:                 dict
        """
        return { 'suit': self.suit, 'rank': self.rank }
