import pytest

from pokersim.dealer import Dealer

DECK_SIZE = 52
SYMBOL_MAP = {
        'A': 'ace',
        'K': 'king',
        'Q': 'queen',
        'J': 'jack',
        'T': 'ten',
        '9': 'nine',
        '8': 'eight',
        '7': 'seven',
        '6': 'six',
        '5': 'five',
        '4': 'four',
        '3': 'three',
        '2': 'two',
        'S': 'spade',
        'H': 'heart',
        'D': 'diamond',
        'C': 'club'
}


def make_test_deck(deck_size=DECK_SIZE):
    return ["card{}".format(i+1) for i in range(DECK_SIZE)]


def card_from_sym(card):
    suit = SYMBOL_MAP['suit'][card[0]]
    rank = SYMBOL_MAP['rank'][card[1]]
    return {'suit': SUITS[suit], 'rank': RANKS[rank]}


def get_hand(hand_sym):
    return [card_from_sym(card) for card in hand_sym]


# TODO: add mock for Deck, which instead returns output from make_test_deck
def test__init__():
    dealer = Dealer()
    assert len(dealer.deck) == DECK_SIZE
    assert dealer.community == []


@pytest.mark.parametrize("num_players, hand_size", [
    (2, 2),
    (2, 5),
    (5, 2),
    (5, 5),
    (10, 2),
    (10, 5)
])
def test_deal(num_players, hand_size):
    dealer = Dealer()
    dealer.deck = make_test_deck()
    dealer.deal()
    assert len(dealer.hands) == num_players
    for hand in dealer.hands:
        assert len(hand) == hand_size
    assert len(dealer.deck) == (DECK_SIZE - num_players * hand_size)


@pytest.mark.parametrize("num_players, hand_size", [
    (2, 2),
    (2, 5),
    (5, 2),
    (5, 5),
    (10, 2),
    (10, 5)
])
def test_burn_card(num_players, hand_size):
    dealer = Dealer()
    assert len(dealer.muck) == 0
    assert len(dealer.community) == 0
    for hand in dealer.hands:
        assert len(hand) == 0

    for i in range(3):
        dealer.burn_card()
        assert len(dealer.muck) == i + 1
        assert len(dealer.community) == 0
        for hand in dealer.hands:
            assert len(hand) == 0

@pytest.mark.parametrize("community", [
    ([]),
    (['card1', 'card2', 'card3']),
    (['card1', 'card2', 'card3', 'card4']),
    (['card1', 'card2', 'card3', 'card4', 'card5'])
])
def test_get_community(community):
    dealer = Dealer()
    dealer.community = community
    assert dealer.get_community == community


def test_flop():
    dealer = Dealer()
    expected = [
        { 'suit': SUITS['spade'], 'rank': RANKS['ace'] },
        { 'suit': SUITS['spade'], 'rank': RANKS['king'] },
        { 'suit': SUITS['spade'], 'rank': RANKS['queen'] },
    ]
    assert len(dealer.community) == 0
    assert len(dealer.deck) == 52
    dealer.flop()
    assert len(dealer.community) == 3
    assert len(dealer.deck) == 49
    assert dealer.community == expected


def test_turn():
    dealer = Dealer()
    dealer.community = ['card1', 'card2', 'card3']
    dealer.deck = dealer.deck[3:len(dealer.deck)]
    expected = [
        { 'suit': SUITS['spade'], 'rank': RANKS['Jack'] },
    ]
    assert len(dealer.community) == 3
    assert len(dealer.deck) == 49
    dealer.turn()
    assert len(dealer.community) == 4
    assert len(dealer.deck) == 48
    assert dealer.community[-1] == expected


def test_river():
    dealer = Dealer()
    dealer.community = ['card1', 'card2', 'card3', 'card4']
    dealer.deck = dealer.deck[4:len(dealer.deck)]
    expected = [
        { 'suit': SUITS['spade'], 'rank': RANKS['Ten'] },
    ]
    assert len(dealer.community) == 4
    assert len(dealer.deck) == 48
    dealer.turn()
    assert len(dealer.community) == 5
    assert len(dealer.deck) == 47
    assert dealer.community[-1] == expected


@pytest.mark.parametrize("num_hands,expected", [
    (0, []),
    (2, [['card1', 'card2'], ['card3', 'card4']]),
    (4, [['card1', 'card2'], ['card3', 'card4'], ['card5', 'card6'], ['card7', 'card8']]),
    (10, [['card1', 'card2'], ['card3', 'card4'], ['card5', 'card6'], ['card7', 'card8'],
          ['card9', 'card10'], ['card11', 'card12'], ['card13', 'card14'], ['card15', 'card16'],
          ['card17', 'card18'], ['card19', 'card20']])
])
def test_get_hands(num_hands, expected):
    dealer = Dealer()
    dealer.deck = make_test_deck()
    assert len(dealer.deck) == DECK_SIZE
    assert len(dealer.community) == 0
    assert len(dealer.muck) == 0
    assert len(dealer.hands) == num_hands
    assert dealer.hands == expected


@pytest.mark.parametrize("hands_sym, expected_syms", [
    ((['AS', 'KH', 'QC', 'JC', '2C'], ['AC', '3H', '4C', '5C', '6C']), (['AS', 'KH', 'QC', 'JC', '2C'])),
    ((['AS', 'KH', 'QC', 'JC', '2C'], ['AS', 'KC', '4C', '5C', '6C']), (['AS', 'KH', 'QC', 'JC', '2C'])),
    ((['AS', 'KH', 'QC', 'JC', '2C'], ['AS', 'KC', 'QH', '5C', '6C']), (['AS', 'KH', 'QC', 'JC', '2C'])),
    ((['AS', 'KH', 'QC', 'JC', '2C'], ['AS', 'KC', 'QH', 'JH', '6C']), (['AS', 'KH', 'QC', 'JC', '6C'])),
    ((['AS', 'AH', 'QC', 'JC', '2C'], ['KS', 'KC', '4C', '5C', '6C']), (['AS', 'AH', 'QC', 'JC', '2C'])),
    ((['AS', 'AH', 'QC', 'JC', '2C'], ['AC', 'AD', '4C', '5C', '6C']), (['AS', 'AH', 'QC', 'JC', '2C'])),
    ((['AS', 'AH', 'QC', 'JC', '2C'], ['AC', 'AD', 'QD', '5C', '6C']), (['AS', 'AH', 'QC', 'JC', '2C'])),
    ((['AS', 'AH', 'QC', 'JC', '2C'], ['AC', 'AD', 'QD', 'JD', '6C']), (['AS', 'AH', 'QC', 'JC', '6C'])),
    ((['AS', 'AH', 'QC', 'QD', '2C'], ['QH', 'QS', 'JC', 'JS', '6C']), (['AS', 'AH', 'QC', 'QD', '2C'])),
    ((['TS', 'TH', 'QC', 'QD', '2C'], ['QH', 'QS', 'JC', 'JS', '6C']), (['QH', 'QS', 'JC', 'JS', '6C'])),
    ((['JD', 'JH', 'QC', 'QD', '2C'], ['QH', 'QS', 'JC', 'JS', '6C']), (['QH', 'QS', 'JC', 'JS', '6C'])),
    ((['AS', 'AH', 'AC', 'QD', '2C'], ['QH', 'QS', 'QC', '5C', '6C']), (['AS', 'AH', 'AC', 'QD', '2C'])),
    ((['AS', 'KH', 'QC', 'JD', 'TC'], ['KS', 'QH', 'JC', 'TD', '9C']), (['AS', 'KH', 'QC', 'JD', 'TC'])),
    ((['AS', 'KH', 'QC', 'JD', 'TC'], ['AC', 'KD', 'QS', 'JH', 'TS']),
        (['AS', 'KH', 'QC', 'JD', 'TC'], ['AC', 'KD', 'QS', 'JH', 'TS'])),
    ((['AS', 'KS', 'QS', 'JS', '9S'], ['KD', 'QD', 'JD', 'TD', '2D']), (['AS', 'KS', 'QS', 'JS', '9S'])),
    ((['AS', 'KS', 'QS', 'JS', '9S'], ['AD', 'QD', 'JD', 'TD', '2D']), (['AS', 'KS', 'QS', 'JS', '9S'])),
    ((['AS', 'KS', 'QS', 'JS', '9S'], ['AD', 'KD', 'JD', 'TD', '2D']), (['AS', 'KS', 'QS', 'JS', '9S'])),
    ((['AS', 'KS', 'QS', 'JS', '9S'], ['AD', 'KD', 'QD', 'TD', '2D']), (['AS', 'KS', 'QS', 'JS', '9S'])),
    ((['AS', 'KS', 'QS', 'JS', '9S'], ['AD', 'KD', 'QD', 'JD', '2D']), (['AS', 'KS', 'QS', 'JS', '9S'])),
    ((['AS', 'KS', 'QS', 'JS', '9S'], ['AD', 'KD', 'QD', 'JD', '9D']),
        (['AS', 'KS', 'QS', 'JS', '9S'], ['AD', 'KD', 'QD', 'JD', '9D'])),
    ((['AS', 'AH', 'AC', 'JD', 'JC'], ['QH', 'QS', 'QC', '5C', '5H']), (['AS', 'AH', 'AC', 'JD', 'JC'])),
    ((['AS', 'AH', 'AC', 'AD', 'JC'], ['QH', 'QS', 'QC', 'QD', '5H']), (['AS', 'AH', 'AC', 'AD', 'JC'])),
    ((['TC', '9C', '8C', '7C', 'JC'], ['9H', '8H', '7H', '6H', 'TH']), (['TC', '9C', '8C', '7C', 'JC'])),
    ((['TC', '9C', '8C', '7C', 'JC'], ['9H', '8H', '7H', 'JH', 'TH']),
        (['TC', '9C', '8C', '7C', 'JC'], ['9H', '8H', '7H', 'JH', 'TH'])),
    ((['TC', 'JC', 'AC', 'KC', 'QC'], ['KH', 'QH', '9H', 'JH', 'TH']), (['TC', 'JC', 'AC', 'KC', 'QC']))
])
def test_get_best_hand(hands_sym, expected_syms):
    hands = [get_hand(hand_sym) for hand_sym in hands_sym]
    expected = [get_hand(expected_sym) for expected_sym in expected_syms]
    dealer = Dealer()
    dealer.hands = hands
    best_hands = dealer.best_hand()
    sort(best_hands)
    sort(expected)
    assert best_hands == expected
