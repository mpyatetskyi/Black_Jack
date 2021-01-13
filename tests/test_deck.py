from src.black_jack.resources.classes_full import Deck


def test_deck_init():
    my_deck = Deck()
    assert len(my_deck.deck) == 52
