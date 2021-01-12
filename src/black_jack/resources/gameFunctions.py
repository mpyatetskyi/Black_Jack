def take_bet(chips):
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


def hit(deck, hand):
    single_card = deck.deal()
    hand.add_card(single_card)
    hand.adjust_for_ace()


def hit_or_stand(deck, hand):

    while True:
        x = input("Hit or stand? Enter h or s: ")

        if x[0].lower() == 'h':
            hit(deck, hand)

        elif x[0].lower() == 's':
            print("Player stands. Dealer`s turn")
            break

        else:
            print("Sorry, I don`t understand")
            continue
    return x

def show_some(player, dealer):
    print("Dealer`s hand:")
    print("One card hidden")
    print(dealer.cards[1])
    print('\n')
    print("Players hand:")
    for card in player.cards:
        print(card)
    print(player.value)


def show_all(player, dealer):
    print("Dealer`s hand:")
    for card in dealer.cards:
        print(card)
    print(dealer.value)
    print('\n')
    print("Players hand:")
    for card in player.cards:
        print(card)
    print(player.value)


def player_busts(player, dealer, chips):
    print("Player busts")
    chips.loose_bet()


def player_wins(player, dealer, chips):
    print("Player wins!!!")
    chips.win_bet()


def dealer_busts(player, dealer, chips):
    print("Dealer busts, Player wins")
    chips.win_bet


def dealer_wins(player, dealer, chips):
    print("Dealer wins")
    chips.loose_bet()


def tie(player, dealer, chips):
    print("Tie. Nobody wins")
