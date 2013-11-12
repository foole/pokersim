from deck import Deck
from hand import Hand


MAX_HANDS = 10 #arbitrary
NUM_HOLE_CARDS = 2

class Dealer:
    def __init__(self, hands=9, shuffles=7):
        self.deck = Deck(shuffles)
        self.hands = self.create_hands(hands)

    def create_hands(self, hands):
        myhands = []
        if hands < 2 or hands > MAX_HANDS:
            print 'Invalid number of hands'
        else:
            for i in xrange(0,hands):
                myhands.append(Hand())
        return myhands

    def deal_hole(self):
        for i in xrange(0,NUM_HOLE_CARDS):
            for hand in self.hands:
                hand.add_card(self.deck.get_card())

    
    def print_hands(self):
        i = 1
        for hand in self.hands:
            card1,card2 = hand.get_cards()
            print 'Hand %d:\t%s%s\t%s%s' % (i,card1['rank'], card1['suit'],
                    card2['rank'], card2['suit'])
            i = i+1

