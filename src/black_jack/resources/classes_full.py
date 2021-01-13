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

    def __str__(self):
        deck_comp = ""
        for card in self.deck:
            deck_comp += "\n" + card.__str__()
        return "The deck has: " + deck_comp

    def shuffle(self):
        shuffle(self.deck)

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

    def adjust_for_ace(self):

        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1


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


class Game:

    def __init__(self):
        pass

    def take_bet(self, chips):
        while True:

            try:
                chips.bet = int(input("How many chips would"
                                      " you like to bet? "))
            except ValueError:
                print("Sorry, please insert an integer")
            else:
                if chips.bet > chips.total:
                    print(f"Sorry,you don`t have enough money."
                          f" You have only {chips.total}")
                else:
                    break

    def hit(self, deck, hand):
        single_card = deck.deal()
        hand.add_card(single_card)
        hand.adjust_for_ace()

    def show_some(self, player, dealer):
        print("Dealer`s hand:")
        print("One card hidden")
        print(dealer.cards[1])
        print('\n')
        print("Players hand:")
        for card in player.cards:
            print(card)
        print(player.value)

    def show_all(self, player, dealer):
        print("Dealer`s hand:")
        for card in dealer.cards:
            print(card)
        print(dealer.value)
        print('\n')
        print("Players hand:")
        for card in player.cards:
            print(card)
        print(player.value)

    def player_wins(self, player, dealer, chips):
        print("Player wins!!!")
        chips.win_bet()

    def player_busts(self, player, dealer, chips):
        print("Player busts")
        chips.loose_bet()

    def dealer_busts(self, player, dealer, chips):
        print("Dealer busts, Player wins")
        chips.win_bet()

    def dealer_wins(self, player, dealer, chips):
        print("Dealer wins")
        chips.loose_bet()

    def tie(self, player, dealer, chips):
        print("Tie. Nobody wins")

    def play(self):

        playing = True

        while playing:

            self.deck = Deck()
            self.deck.shuffle()

            self.player_hand = Hand()
            self.dealer_hand = Hand()

            for _ in range(2):
                self.player_hand.add_card(self.deck.deal())
                self.dealer_hand.add_card(self.deck.deal())

            player_chips = Chips()

            self.take_bet(player_chips)

            self.show_some(self.player_hand, self.dealer_hand)

            while True and self.player_hand.value < 21:
                choice = input("Please choose h or s")
                if choice[0].lower() not in ['s', 'h']:
                    continue

                elif choice[0] == 'h':
                    self.player_hand.add_card(self.deck.deal())
                    self.show_some(self.player_hand, self.dealer_hand)
                    continue

                elif choice[0] == 's':
                    break

            self.show_all(self.player_hand, self.dealer_hand)

            if self.player_hand.value == 21:
                self.player_wins(self.player_hand,
                                 self.dealer_hand,
                                 player_chips)

            elif self.player_hand.value > 21:
                self.player_busts(self.player_hand,
                                  self.dealer_hand,
                                  player_chips)
            elif self.player_hand.value < 21:
                while self.dealer_hand.value <= 17:
                    self.dealer_hand.add_card(self.deck.deal())

                self.show_all(self.player_hand, self.dealer_hand)

                if self.dealer_hand.value > 21:
                    self.dealer_busts(self.player_hand,
                                      self.dealer_hand,
                                      player_chips)

                elif self.dealer_hand.value > self.player_hand.value:
                    self.dealer_wins(self.player_hand,
                                     self.dealer_hand,
                                     player_chips)

                elif self.dealer_hand.value < self.player_hand.value:
                    self.player_wins(self.player_hand,
                                     self.dealer_hand,
                                     player_chips)

                else:
                    self.tie(self.player_hand,
                             self.dealer_hand,
                             player_chips)

            print(f'\n Players total money {player_chips.total}')

            again = input("Play Again? [Y/N] ")
            while again.lower() not in ["y", "n"]:
                again = input("Please enter Y or N ")
            if again.lower() == "n":
                print("Thanks for playing!")
                playing = False
            else:
                playing = True


if __name__ == '__main__':
    game = Game()
    game.play()
