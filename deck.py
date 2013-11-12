from random import shuffle


class Deck:
    def __init__(self, num_shuffles=7):
        self.deck = self.fresh_deck()
        self.shuffle(num_shuffles)

    def __len__(self):
        return len(self.deck)

    def fresh_deck(self):
        suits = { 'S': 'Spade', 'H': 'Heart', 'D': 'Diamond', 'C': 'Club' } 
        ranks = ['A','K','Q','J','T','9','8','7','6','5','4','3','2']
        deck = []
        for suit in ['S','H','D','C']:
            for rank in ranks:
                card = { 'rank': rank, 'suit': suit, 'suit_long': suits[suit] }
                deck.append(card)
        return deck

    def shuffle(self,num):
        for i in xrange(0,num):
            shuffle(self.deck)

    def get_card(self):
        card = self.deck.pop()
        return card
