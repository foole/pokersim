import pytest

from pokersim.deck import (
        DEFAULT_SHUFFLES,
        Deck
)

EXPECTED_DECK_SYMBOLS = [
        'AS', 'KS', 'QS', 'JS', 'TS', '9S', '8S', '7S', '6S', '5S', '4S', '3S', '2S',
        'AH', 'KH', 'QH', 'JH', 'TH', '9H', '8H', '7H', '6H', '5H', '4H', '3H', '2H',
        'AD', 'KD', 'QD', 'JD', 'TD', '9D', '8D', '7D', '6D', '5D', '4D', '3D', '2D',
        'AC', 'KC', 'QC', 'JC', 'TC', '9C', '8C', '7C', '6C', '5C', '4C', '3C', '2C'
]


def extract_symbol(card):
    return "{}{}".format(card.rank['symbol'], card.suit['symbol'])


def extract_symbols(deck):
    return [extract_symbol(c) for c in deck.deck]


@pytest.mark.parametrize("shuffles, expected_shuffles", [
    (None, DEFAULT_SHUFFLES),
    (1, 1),
    (2, 2),
    (3, 3),
    (13, 13)
])
def test__init__(shuffles, expected_shuffles):
    if shuffles is not None:
        deck = Deck(shuffles=shuffles)
    else:
        deck = Deck()
    assert extract_symbols(deck) == EXPECTED_DECK_SYMBOLS
    assert deck.shuffles == expected_shuffles


@pytest.mark.parametrize("mock_deck, expected", [
        ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23], 23),
        ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], 12),
        ([1, 2, 3, 4, 5, 6], 6),
        ([1, 2, 3], 3),
        ([1, 2], 2),
        ([1], 1),
        ([], 0)
])
def test__len__(mock_deck, expected):
    deck = Deck()
    deck.deck = mock_deck
    assert len(deck) == expected


def test_fresh_deck():
    deck = Deck()
    deck.fresh_deck()
    assert extract_symbols(deck) == EXPECTED_DECK_SYMBOLS


@pytest.mark.parametrize("num_shuffles", [
        (1), (2), (7), (20)
])
def test_shuffle(num_shuffles):
    deck = Deck()
    assert extract_symbols(deck) == EXPECTED_DECK_SYMBOLS
    previous = EXPECTED_DECK_SYMBOLS
    for _ in range(num_shuffles):
        deck.shuffle()
        current = extract_symbols(deck)
        assert current != previous
        previous = current


def test_get_card():
    deck = Deck()
    expected_length = 52
    for expected_card in EXPECTED_DECK_SYMBOLS:
        actual_card = extract_symbol(deck.get_card())
        assert actual_card == expected_card
        assert len(deck) == expected_length
        expected_length -= 1
