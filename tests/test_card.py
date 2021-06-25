import pytest

from pokersim.card import (
        SUITS,
        RANKS,
        Card
)


@pytest.mark.parametrize("suit, rank, expected", [
    ('spade', 'ace', (SUITS['spade'], RANKS['ace'])),
    ('heart', 'ace', (SUITS['heart'], RANKS['ace'])),
    ('diamond', 'ace', (SUITS['diamond'], RANKS['ace'])),
    ('club', 'ace', (SUITS['club'], RANKS['ace'])),
    ('spade', 'two', (SUITS['spade'], RANKS['two'])),
    ('heart', 'king', (SUITS['heart'], RANKS['king'])),
    ('diamond', 'jack', (SUITS['diamond'], RANKS['jack'])),
    ('club', 'ten', (SUITS['club'], RANKS['ten'])),
])
def test_create_cards(suit, rank, expected):
    card = Card(suit, rank)
    assert card.rank == RANKS[rank]
    assert card.suit == SUITS[suit]


@pytest.mark.parametrize("suit, rank, expected", [
    ('spade', 'ace', 'Ace of Spades'),
    ('heart', 'ace', 'Ace of Hearts'),
    ('diamond', 'ace', 'Ace of Diamonds'),
    ('club', 'ace', 'Ace of Clubs'),
    ('spade', 'two', 'Two of Spades'),
    ('heart', 'king', 'King of Hearts'),
    ('diamond', 'jack', 'Jack of Diamonds'),
    ('club', 'ten', 'Ten of Clubs'),
])
def test__str__(suit, rank, expected):
    card = Card(suit, rank)
    assert str(card) == expected


@pytest.mark.parametrize("card1_data, card2_data, expected", [
    (('spade', 'ace'), ('spade', 'ace'), False),
    (('spade', 'ace'), ('spade', 'two'), False),
    (('spade', 'two'), ('spade', 'ace'), True),
    (('heart', 'ace'), ('heart', 'ace'), False),
    (('heart', 'ace'), ('heart', 'two'), False),
    (('heart', 'two'), ('heart', 'ace'), True),
    (('diamond', 'ace'), ('diamond', 'ace'), False),
    (('diamond', 'ace'), ('diamond', 'two'), False),
    (('diamond', 'two'), ('diamond', 'ace'), True),
    (('club', 'ace'), ('club', 'ace'), False),
    (('club', 'ace'), ('club', 'two'), False),
    (('club', 'two'), ('club', 'ace'), True),
    (('spade', 'ace'), ('heart', 'ace'), False),
    (('heart', 'ace'), ('spade', 'ace'), True),
    (('heart', 'ace'), ('diamond', 'ace'), False),
    (('diamond', 'ace'), ('heart', 'ace'), True),
    (('diamond', 'ace'), ('club', 'ace'), False),
    (('club', 'ace'), ('diamond', 'ace'), True),
    (('heart', 'ace'), ('diamond', 'ace'), False),
    (('diamond', 'ace'), ('heart', 'ace'), True),
])
def test__lt__(card1_data, card2_data, expected):
    card1 = Card(*card1_data)
    card2 = Card(*card2_data)
    card1 < card2


@pytest.mark.parametrize("card1_data, card2_data, expected", [
    (('spade', 'ace'), ('spade', 'ace'), True),
    (('spade', 'ace'), ('spade', 'two'), False),
    (('spade', 'two'), ('spade', 'ace'), False),
    (('heart', 'ace'), ('heart', 'ace'), True),
    (('heart', 'ace'), ('heart', 'two'), False),
    (('heart', 'two'), ('heart', 'ace'), False),
    (('diamond', 'ace'), ('diamond', 'ace'), True),
    (('diamond', 'ace'), ('diamond', 'two'), False),
    (('diamond', 'two'), ('diamond', 'ace'), False),
    (('club', 'ace'), ('club', 'ace'), True),
    (('club', 'ace'), ('club', 'two'), False),
    (('club', 'two'), ('club', 'ace'), False),
    (('spade', 'ace'), ('heart', 'ace'), False),
    (('heart', 'ace'), ('spade', 'ace'), False),
    (('heart', 'ace'), ('diamond', 'ace'), False),
    (('diamond', 'ace'), ('heart', 'ace'), False),
    (('diamond', 'ace'), ('club', 'ace'), False),
    (('club', 'ace'), ('diamond', 'ace'), False),
    (('heart', 'ace'), ('diamond', 'ace'), False),
    (('diamond', 'ace'), ('heart', 'ace'), False),
])
def test__eq__(card1_data, card2_data, expected):
    card1 = Card(*card1_data)
    card2 = Card(*card2_data)
    assert (card1 == card2) == expected


@pytest.mark.parametrize("card1_data, card2_data, expected", [
    (('spade', 'ace'), ('spade', 'ace'), False),
    (('spade', 'ace'), ('spade', 'two'), True),
    (('spade', 'two'), ('spade', 'ace'), False),
    (('heart', 'ace'), ('heart', 'ace'), False),
    (('heart', 'ace'), ('heart', 'two'), True),
    (('heart', 'two'), ('heart', 'ace'), False),
    (('diamond', 'ace'), ('diamond', 'ace'), False),
    (('diamond', 'ace'), ('diamond', 'two'), True),
    (('diamond', 'two'), ('diamond', 'ace'), False),
    (('club', 'ace'), ('club', 'ace'), False),
    (('club', 'ace'), ('club', 'two'), True),
    (('club', 'two'), ('club', 'ace'), False),
    (('spade', 'ace'), ('heart', 'ace'), True),
    (('heart', 'ace'), ('spade', 'ace'), False),
    (('heart', 'ace'), ('diamond', 'ace'), True),
    (('diamond', 'ace'), ('heart', 'ace'), False),
    (('diamond', 'ace'), ('club', 'ace'), True),
    (('club', 'ace'), ('diamond', 'ace'), False),
    (('heart', 'ace'), ('diamond', 'ace'), True),
    (('diamond', 'ace'), ('heart', 'ace'), False),
])
def test__gt__(card1_data, card2_data, expected):
    card1 = Card(*card1_data)
    card2 = Card(*card2_data)
    assert (card1 > card2) == expected
