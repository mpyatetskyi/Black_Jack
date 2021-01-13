from src.black_jack.resources.classes_full import Deck


def test_deck_init():
    my_deck = Deck()
    assert len(my_deck.deck) == 52


def add_card_init():
    my_deck = Deck()
    my_deck.deal()
    my_deck.deal()
    my_deck.deal()
    assert len(my_deck.deck) == 49
