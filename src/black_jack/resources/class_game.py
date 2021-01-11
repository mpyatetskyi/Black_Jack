from src.black_jack.resources.classes_full import *

class Game:

    def __init__(self):
        pass

    def take_bet(self,chips):
        while True:

            try:
                chips.bet = int(input("How many chips would you like to bet? "))
            except:
                print("Sorry, please insert an integer")
            else:
                if chips.bet > chips.total:
                    print(f"Sorry,you don`t have enough money. You have only {chips.total}")
                else:
                    break

    def hit(self,deck, hand):
        single_card = deck.deal()
        hand.add_card(single_card)
        hand.adjust_for_ace()

    def show_some(self,player, dealer):
        print("Dealer`s hand:")
        print("One card hidden")
        print(dealer.cards[1])
        print('\n')
        print("Players hand:")
        for card in player.cards:
            print(card)
        print(player.value)

    def show_all(self,player, dealer):
        print("Dealer`s hand:")
        for card in dealer.cards:
            print(card)
        print(dealer.value)
        print('\n')
        print("Players hand:")
        for card in player.cards:
            print(card)
        print(player.value)

    def player_busts(self,player, dealer, chips):
        print("Player busts")
        chips.loose_bet()

    def player_wins(self,player, dealer, chips):
        print("Player wins!!!")
        chips.win_bet()

    def dealer_busts(self,player, dealer, chips):
        print("Dealer busts, Player wins")
        chips.win_bet

    def dealer_wins(self,player, dealer, chips):
        print("Dealer wins")
        chips.loose_bet()

    def tie(self,player, dealer, chips):
        print("Tie. Nobody wins")


    def play(self):

        playing = True

        while playing:

            self.deck = Deck()
            self.deck.shuffle()

            self.player_hand = Hand()
            self.dealer_hand = Hand()

            for _ in range (2):
                self.player_hand.add_card(self.deck.deal())
                self.dealer_hand.add_card(self.deck.deal())


            player_chips = Chips()

            self.take_bet(player_chips)

            self.show_some(self.player_hand,self.dealer_hand)


            while True and self.player_hand.value < 21:
                choice = input("Please choose h or s")
                if choice[0].lower() not in ['s','h']:
                    continue

                elif choice[0] == 'h':
                    self.player_hand.add_card(self.deck.deal())
                    self.show_some(self.player_hand, self.dealer_hand)
                    continue

                elif choice[0] == 's':
                    break

            self.show_all(self.player_hand, self.dealer_hand)

            if self.player_hand.value == 21:
                self.player_wins(self.player_hand,self.dealer_hand,player_chips)

            elif self.player_hand.value > 21:
                self.player_busts(self.player_hand, self.dealer_hand, player_chips)
            elif self.player_hand.value < 21:
                while self.dealer_hand.value <=17:
                    self.dealer_hand.add_card(self.deck.deal())

                self.show_all(self.player_hand,self.dealer_hand)

                if self.dealer_hand.value > 21:
                    dealer_busts(self.player_hand,self.dealer_hand,player_chips)

                elif self.dealer_hand.value > self.player_hand.value:
                    self.dealer_wins(self.player_hand, self.dealer_hand, player_chips)

                elif self.dealer_hand.value < self.player_hand.value:
                    player_wins(self.player_hand,self.dealer_hand,player_chips)

                else:
                    self.tie(self.player_hand,self.dealer_hand,player_chips)

            print(f'\n Players total money {player_chips.total}')

            again = input("Play Again? [Y/N] ")
            while again.lower() not in ["y", "n"]:
                again = input("Please enter Y or N ")
            if again.lower() == "n":
                print("Thanks for playing!")
                playing = False
            else:
                game_over = False



if __name__ == '__main__':
    game = Game()
    game.play()








