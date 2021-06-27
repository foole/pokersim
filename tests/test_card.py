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


@pytest.mark.parametrize("card_data, expected", [
    (('spade', 'ace'), "AS"),
    (('spade', 'king'), "KS"),
    (('spade', 'nine'), "9S"),
    (('spade', 'five'), "5S"),
    (('heart', 'ace'), "AH"),
    (('heart', 'queen'), "QH"),
    (('heart', 'eight'), "8H"),
    (('heart', 'four'), "4H"),
    (('diamond', 'ace'), "AD"),
    (('diamond', 'jack'), "JD"),
    (('diamond', 'seven'), "7D"),
    (('diamond', 'three'), "3D"),
    (('club', 'ace'), "AC"),
    (('club', 'ten'), "TC"),
    (('club', 'six'), "6C"),
    (('club', 'two'), "2C"),
])
def test_get_symbol(card_data, expected):
    card = Card(*card_data)
    assert card.get_symbol() == expected



@pytest.mark.parametrize("card_data, expected", [
    (('spade', 'ace'),      {'suit': SUITS['spade'], 'rank': RANKS['ace']}),
    (('spade', 'king'),     {'suit': SUITS['spade'], 'rank': RANKS['king']}),
    (('spade', 'nine'),     {'suit': SUITS['spade'], 'rank': RANKS['nine']}),
    (('spade', 'five'),     {'suit': SUITS['spade'], 'rank': RANKS['five']}),
    (('heart', 'ace'),      {'suit': SUITS['heart'], 'rank': RANKS['ace']}),
    (('heart', 'queen'),    {'suit': SUITS['heart'], 'rank': RANKS['queen']}),
    (('heart', 'eight'),    {'suit': SUITS['heart'], 'rank': RANKS['eight']}),
    (('heart', 'four'),     {'suit': SUITS['heart'], 'rank': RANKS['four']}),
    (('diamond', 'ace'),    {'suit': SUITS['diamond'], 'rank': RANKS['ace']}),
    (('diamond', 'jack'),   {'suit': SUITS['diamond'], 'rank': RANKS['jack']}),
    (('diamond', 'seven'),  {'suit': SUITS['diamond'], 'rank': RANKS['seven']}),
    (('diamond', 'three'),  {'suit': SUITS['diamond'], 'rank': RANKS['three']}),
    (('club', 'ace'),       {'suit': SUITS['club'], 'rank': RANKS['ace']}),
    (('club', 'ten'),       {'suit': SUITS['club'], 'rank': RANKS['ten']}),
    (('club', 'six'),       {'suit': SUITS['club'], 'rank': RANKS['six']}),
    (('club', 'two'),       {'suit': SUITS['club'], 'rank': RANKS['two']}),
])
def test_get_card(card_data, expected):
    card = Card(*card_data)
    assert card.get_card() == expected
