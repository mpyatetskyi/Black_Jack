from src.black_jack.resources.blackjack_api import Hand
from src.black_jack.resources.blackjack_api import Card


def test_hand_init():
    my_hand = Hand()
    my_hand.add_card(Card('Hearts', 'Ace'))
    my_hand.add_card(Card('Diamonds', 'Ace'))
    assert len(my_hand.cards) == 2
    assert my_hand.value == 12

    my_hand.add_card(Card('Spades', 'Ace'))
    assert my_hand.value == 13
    assert len(my_hand.cards) == 3


def test_blackjack_True():
    my_hand = Hand()
    my_hand.add_card(Card('Spades', 'Ace'))
    my_hand.add_card(Card('Spades', 'Jack'))
    assert my_hand.is_blackjack is True


def test_hand_is_over_True():
    my_hand = Hand()
    my_hand.add_card(Card('Spades', 'Five'))
    my_hand.add_card(Card('Spades', 'Jack'))
    my_hand.add_card(Card('Diamonds', 'Jack'))
    assert my_hand.hand_is_over is True


def test_blackjack_False():
    my_hand = Hand()
    my_hand.add_card(Card('Spades', 'Five'))
    my_hand.add_card(Card('Spades', 'Six'))
    assert my_hand.is_blackjack is False


def test_hand_is_over_False():
    my_hand = Hand()
    my_hand.add_card(Card('Spades', 'Five'))
    my_hand.add_card(Card('Spades', 'Six'))
    my_hand.add_card(Card('Diamonds', 'Five'))
    assert my_hand.hand_is_over is False
