from src.black_jack.resources.blackjack_api import Chips


def test_chips_default_init():
    my_chips = Chips()
    assert my_chips.total == 100


def test_chips_total():
    my_chips = Chips(500)
    assert my_chips.total == 500


def test_bet_default():
    my_chips = Chips()
    assert my_chips.bet == 0


def test_take_a_bet():
    my_chips = Chips()
    my_chips.take_a_bet(50)
    assert my_chips.bet == 50


def test_win_bet():
    my_chips = Chips()
    my_chips.take_a_bet(50)
    my_chips.win_bet()
    assert my_chips.total == 150


def test_loose_bet():
    my_chips = Chips()
    my_chips.take_a_bet(20)
    my_chips.loose_bet()
    assert my_chips.total == 80