from deck import Deck
from player import RegularPlayer, Dealer
from utils import *
import random


class Blackjack(object):
    def __init__(self, human=True, number_of_players=1):
        self.deck = Deck()
        self.deck.shuffle()
        self.human_mode = human
        self.create_players(number_of_players)


    def create_players(self, number_of_players):
        self.players = []
        if self.human_mode:
            number_of_players = int(input('How many players are in the game? '))
            for i in range(number_of_players):
                name = input("Enter player number %d name: " % (i+1))
                money = int(input("Enter player number %d budget: " % (i+1)))
                player = RegularPlayer(name, money)
                player.print_money()
                self.players.append(player)
        else:
            if number_of_players == 1:
                name = "Player"
                money = 100
                player = RegularPlayer(name, money)
                player.print_money()
                self.players.append(player)
            else:
                for i in range(number_of_players):
                    name = "Player"+str(i+1)
                    money = random.randint(100,500)
                    player = RegularPlayer(name, money)
                    player.print_money()
                    self.players.append(player)
        self.dealer = Dealer()


    def play_game(self):
        while self.players:
            print ("----------------------------------------------------------")
            self.play_round()
            for player in self.players.copy():
                player.reset()
                if self.bankrupt(player) or self.quit(player):
                    self.players.remove(player)
            self.dealer.reset()


    def play_round(self):
        print("Start playing...")
        # Player plays
        for player in self.players:
            self.deal(player)
            self.deal(player)
            print(player)

        self.deal(self.dealer)
        print(self.dealer)
        self.deal(self.dealer)

        for player in self.players:
            print("%s plays..." % player.name)
            self.get_bet(player)
            while self.hit_or_stay(player):
                self.deal(player)

        print("Dealer plays...")
        print(self.dealer)
        # Dealer plays
        while calc_cards_sum(self.dealer.hand) <= 16:
            self.deal(self.dealer)

        print("All hands:")
        for player in self.players:
            print(player)
        print(self.dealer)

        for player in self.players:
            if calc_cards_sum(player.hand) > 21:
                player.lostRound()

            elif calc_cards_sum(self.dealer.hand) > 21:
                player.wonRound()

            elif calc_cards_sum(player.hand) > calc_cards_sum(self.dealer.hand):
                player.wonRound()

            elif calc_cards_sum(player.hand) < calc_cards_sum(self.dealer.hand):
                player.lostRound()
            else:
                print("No one won (Push)!")


    def deal(self, player):
        player.hand.append(self.deck.draw_card())

    def get_bet(self, player):
        amount = 0
        if not self.human_mode:
            amount = random.randint(1,int(player.money))
            print("%s bets $%d" % (player.name, amount))
            player.bet(amount)
        else:
            while not (amount > 0 and amount <= player.money):
                amount = int(input("Enter your bet amount in $ : "))
            player.bet(amount)

    def hit_or_stay(self, player):
        print(player)
        if self.human_mode:
            hit_or_stay = input("Hit or Stay? [H/S] ").lower()
            if hit_or_stay == 'h':
                return True
            elif hit_or_stay == 's':
                return False
            else:
                raise Exception("Wrong input!")
            return
        else:
            return random.randint(0,1)

    def quit(self, player):
        if self.human_mode:
            continue_game = input("%s would you like to continue? [Y/N] "
                                  % player.name).lower()
            if continue_game == 'y':
                return False
            elif continue_game == 'n':
                return True
            else:
                raise Exception("Wrong input!")
        else:
            return random.randint(0,1)

    def bankrupt(self, player):
        if player.money <= 0:
            print("%s is bankrupt!" % (player.name))
            return True

        return False


if __name__ == '__main__':
    game = Blackjack()
    game.play_game()
