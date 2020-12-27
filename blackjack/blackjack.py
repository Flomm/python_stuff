# functions and objects
import time
import random

colors = ("Club", "Diamond", "Heart", "Spade")
ranks = ("two", "three", "four", "five", "six", "seven",
         "eight", "nine", "ten", "jack", "queen", "king", "ace")
value = {"two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7,
         "eight": 8, "nine": 9, "ten": 10, "jack": 10, "queen": 10, "king": 10, "ace": 11}


class Cards:

    def __init__(self, color, rank):

        self.color = color
        self.rank = rank

    def __str__(self):
        return f"{self.color} {self.rank}"


class Deck:

    def __init__(self):
        self.deck = []

        for color in colors:
            for rank in ranks:
                self.deck.append(Cards(color, rank))

    def __str__(self):
        deck_comp = ""
        for card in self.deck:
            deck_comp += '\n '+card.__str__()
        return 'The deck contains:' + deck_comp

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        single_card = self.deck.pop()
        return single_card


class Hand:
    def __init__(self):
        self.card = []
        self.value = 0

        self.aces = 0

    def add_card(self, card):
        self.card.append(card)
        self.value += value[card.rank]
        if card.rank == "ace":
            self.aces += 1

    def adjust_for_ace(self):
        while self.value < 21 and self.aces:
            self.value -= 10
            self.aces -= 1


class Chip:

    def __init__(self):
        self.total = 1000
        self.bet = 0

    def win_bet(self):
        self.total += self.bet

    def lose_bet(self):
        self.total -= self.bet


def take_bet(chip):

    while True:
        try:
            chip.bet = int(input('How many chips you would like to take? '))
        except ValueError:
            print('You have to enter a number!')
        else:
            if chip.bet > chip.total:
                print(
                    f"Unfortunately, you only have {player_chip.total} chips.")
            else:
                break


def hit(deck, hand):
    hand.add_card(deck.deal())
    hand.adjust_for_ace()


def hit_or_stand(deck, hand):
    global game

    while True:

        new_card = input("Would you like a new card? Y/N  ")

        if new_card[0].lower() == "y":
            hit(deck, hand)

        elif new_card[0].lower() == "n":
            game = False

        else:
            print("Please try again.")
            continue
        break


def show_some(player, dealer):
    print("\nThe dealer's cards:")
    print(" hidden card")
    print('', dealer.card[1])
    print("\nThe player's cards:", *player.card, sep='\n ')


def show_all(player, dealer):
    print("\nThe dealer's cards:", *dealer.card, sep='\n ')
    print("The dealer's cards =", dealer.value)
    print("\nThe player's cards:", *player.card, sep='\n ')
    print("The player's cards =", player.value)


def player_bust(player, dealer, chip):
    print("The player has more than 21!")
    chip.lose_bet()


def player_wins(player, dealer, chip):
    print("The player won!")
    chip.win_bet()


def dealer_busts(player, dealer, chip):
    print("The dealer has more than 21!")
    chip.win_bet()


def dealer_wins(player, dealer, chip):
    print("The dealer won!")
    chip.lose_bet()


def push(player, dealer):
    print("It's a tie!.")


game = True

player_chip = Chip()
print("Welcome to the Blackjack game!")
print(f"Starting chips: {player_chip.total}")

while True:

    time.sleep(2)
    deck = Deck()
    deck.shuffle()

    player_hand = Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())

    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())

    take_bet(player_chip)

    show_some(player_hand, dealer_hand)

    while game:

        hit_or_stand(deck, player_hand)

        show_some(player_hand, dealer_hand)

        if player_hand.value > 21:
            player_bust(player_hand, dealer_hand, player_chip)

            break

    if player_hand.value <= 21:
        while dealer_hand.value < 17:
            hit(deck, dealer_hand)

        show_all(player_hand, dealer_hand)

        if dealer_hand.value > 21:
            dealer_busts(player_hand, dealer_hand, player_chip)

        elif dealer_hand.value > player_hand.value:
            dealer_wins(player_hand, dealer_hand, player_chip)

        elif dealer_hand.value < player_hand.value:
            player_wins(player_hand, dealer_hand, player_chip)

        else:
            push(player_hand, dealer_hand)

    if player_chip.total == 0:
        print("You don't have any more chips! Game over.")
        break

    else:
        print(f"You currently hav {player_chip.total} chips!")

    new_game = input("Would you like to play again? Y/N   ")

    if new_game[0].lower() == 'y':
        game = True
        continue
    else:
        print("Thank you for playing!")
        break
