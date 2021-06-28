import pytest

from copy import copy

from pokersim.deck import (
        DEFAULT_SHUFFLES,
        Deck
)

EXPECTED_DECK_SYMBOLS = [
        '2C', '3C', '4C', '5C', '6C', '7C', '8C', '9C', 'TC', 'JC', 'QC', 'KC', 'AC',
        '2D', '3D', '4D', '5D', '6D', '7D', '8D', '9D', 'TD', 'JD', 'QD', 'KD', 'AD',
        '2H', '3H', '4H', '5H', '6H', '7H', '8H', '9H', 'TH', 'JH', 'QH', 'KH', 'AH',
        '2S', '3S', '4S', '5S', '6S', '7S', '8S', '9S', 'TS', 'JS', 'QS', 'KS', 'AS'
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
    expected_cards = copy(EXPECTED_DECK_SYMBOLS)
    expected_cards.reverse()
    for expected_card in expected_cards:
        actual_card = extract_symbol(deck.get_card())
        expected_length -= 1
        assert actual_card == expected_card
        assert len(deck) == expected_length
