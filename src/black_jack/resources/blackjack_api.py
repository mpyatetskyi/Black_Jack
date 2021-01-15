from random import shuffle


'''Class Card is made to show the cards from the deck'''


class Card:

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return self.rank + " of " + self.suit


'''Class Deck is made to create a deck of cards,
 to shuffle the deck and to deal the cards'''


class Deck:

    def __init__(self):
        self.suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
        self.ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven',
                      'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
        self.deck = [Card(s, r) for s in self.suits for r in self.ranks]
        shuffle(self.deck)

    def __str__(self):
        deck_comp = ""
        for card in self.deck:
            deck_comp += "\n" + card.__str__()
        return "".join(deck_comp)

    def deal(self):
        if len(self.deck) > 1:
            return self.deck.pop()


'''Class Hand is made to create players (player and dealer),
adjust some cards from the deck to their hands
 and to count the value of cards in their hands'''


class Hand:

    def __init__(self):
        self.card_values = {'Two': 2, 'Three': 3, 'Four': 4,
                            'Five': 5, 'Six': 6, 'Seven': 7,
                            'Eight': 8, 'Nine': 9, 'Ten': 10,
                            'Jack': 10, 'Queen': 10, 'King': 10,
                            'Ace': 11}
        self.cards = []
        self.value = 0
        self.aces = 0

    def add_card(self, card):
        self.cards.append(card)
        self.value += self.card_values[card.rank]

        if card.rank == "Ace":
            self.aces += 1
        self.adjust_for_ace()

    def adjust_for_ace(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1

    def show_cards(self, hidden=False):
        if hidden:
            return self.cards[1]
        else:
            return self.cards

    @property
    def is_blackjack(self):
        return self.value == 21

    @property
    def hand_is_over(self):
        return self.value > 21


'''Class Chips is made to store the players total money,
 to add some money if he wins and subtract if he loose'''


class Chips:

    def __init__(self, total=100):
        self.total = total
        self.bet = 0

    def win_bet(self):
        self.total += self.bet

    def loose_bet(self):
        self.total -= self.bet

    def take_a_bet(self, bet):
        self.bet = bet


class Game:

    def __init__(self):
        pass

    def play_create(self):
        self.deck = Deck()

        self.player = Hand()
        self.dealer = Hand()

        self.player_chips = Chips()

        for _ in range(2):
            self.player.add_card(self.deck.deal())
            self.dealer.add_card(self.deck.deal())

        return self.deck, self.player, self.player_chips, self.dealer

    def _player_wins(self, player, dealer, chips):
        chips.win_bet()
        return "Player wins!!!"

    def _dealer_wins(self, player, dealer, chips):
        chips.loose_bet()
        return "Dealer wins"

    def _tie(self, player, dealer, chips):
        return "Tie. Nobody wins"

    def winners_check(self):
        if self.player.value > self.dealer.value:
            return self._player_wins(self.player,
                                     self.dealer,
                                     self.player_chips)
        elif self.player.value < self.dealer.value:
            return self._dealer_wins(self.player,
                                     self.dealer,
                                     self.player_chips)
        elif self.player.value == self.dealer.value:
            return self._tie(self.player,
                             self.dealer,
                             self.player_chips)

    def hit(self, hand):
        hand.add_card(self.deck.deal())
        return self.show_blackjack_results()
