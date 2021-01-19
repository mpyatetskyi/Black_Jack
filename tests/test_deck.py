from src.black_jack.resources.blackjack_api import Deck


def test_deck_init():
    my_deck = Deck()
    assert len(my_deck.deck) == 52


def test_deck_deal():
    my_deck = Deck()
    my_deal = []
    my_deal.append(my_deck.deal())
    assert len(my_deal) == 1
