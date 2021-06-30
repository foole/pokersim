from pokersim.deck import Deck


DEFAULT_FLOP_SIZE = 3
DEFAULT_TURN_SIZE = 1
DEFAULT_RIVER_SIZE = 1


class Dealer:
    def __init__(self, players, hand_size):
        """
        Initialize a dealer. Dealer has a deck of cards and keeps track of
        players, and community cards.
        """
        self.players = players
        self.hand_size = hand_size
        self.deck = Deck()
        self.community  = []
        self.muck = []


    def deal(self):
        """
        Deal cards to each of the players.
        """
        for _ in range(self.hand_size):
            for player in self.players:
                self.players[player].append(self.deck.get_card())


    def burn_card(self):
        """
        Burn a card into the muck.
        """
        muck.append(self.deck.get_card())


    def get_community(self):
        """
        Get the community cards.

        :return:                    community cards
        :rtype:                     list
        """
        return self.community()


    def flop(self, flop_size=DEFAULT_FLOP_SIZE):
        """
        Deal the flop, adding each card to the community.

        :param flop_size:           number of cards to flop
        :type flop_size:            int
        """
        for _ in flop_size:
            self.community.append(self.deck.get_card())


    def turn(self, turn_size=DEFAULT_TURN_SIZE):
        """
        Deal the turn, adding each card to the community.

        :param turn_size:           number of cards in the turn
        :type turn_size:            int
        """
        for _ in turn_size:
            self.community.append(self.deck.get_card())


    def river(self, river_size=DEFAULT_RIVER_SIZE):
        """
        Deal the river, adding each card to the community.

        :param river_size:          number of cards in the river
        :type river_size:           int
        """
        for _ in river_size:
            self.community.append(self.deck.get_card())


    def get_hands(self):
        """
        Get the hands (should be best hand per player).

        :return:                    best hand for each player
        :rtype;                     dict (name of player, hand, hand label)
        """
        return self.hands


    def get_best_hand(self):
        """
        Compare each player's hand against one another and determine the best
        (could be a tie between multiple players).

        :return:                    each winning players hand
        :rtype;                     dict (name of player, hand, hand label)
        """
        pass
