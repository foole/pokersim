#!/usr/bin/env python

from hand import Hand
from deck import Deck
from dealer import Dealer

from optparse import OptionParser
from pprint import pprint


def show_deck(deck, vertical=False):
    cards = ['%s%s' % (card['rank'],card['suit']) for card in deck]
    if vertical:
        for card in cards:
            print '%s' % card
    else:
        print cards


if __name__ == '__main__':
    parser = OptionParser()
    parser.add_option('-d', '--debug', dest='debug', default=False,
            help='Turn on debugging.')
    parser.add_option('-n', '--num-players', dest='players', default=5,
            type='int', help='Number of players to deal in.')
    parser.add_option('-s', '--num-shuffles', dest='shuffles', default=0,
            type='int', help='Number of shuffles for new deck.')
    parser.add_option('-v', '--verbose', dest='verbose', default=False,
            help='Turn on verbosity.')

    (opts,args) = parser.parse_args()


    croupier = Dealer(hands=opts.players, shuffles=opts.shuffles) 
    show_deck(croupier.deck.deck,True)

    for i in xrange(7):
        print
        croupier.shuffle(1)
        show_deck(croupier.deck.deck)
