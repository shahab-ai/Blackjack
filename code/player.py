from utils import *

class Player(object):
    def __init__(self, name):
        self.name = name
        self.hand = []

    def receive_card(self, card):
        self.hand.append(card)

    def reset(self):
        self.hand = []

    def __repr__(self):
        return "Cards in %s's hand: %s, Total=%d" % (self.name, self.hand, calc_cards_sum(self.hand))

class RegularPlayer(Player):
    def __init__(self, name, money, winningOdd=3/float(2)):
        super().__init__(name)
        self.money = money
        self.winningOdd = winningOdd

    def print_money(self):
        print("%s has $%d" % (self.name, self.money))

    def bet(self, amount):
        self.bet_amount = amount

    def lostRound(self):
        print("%s lost!" % (self.name))
        self.money -= self.bet_amount
        self.print_money()


    def wonRound(self):
        print("%s won!" % (self.name))
        self.money += self.bet_amount*self.winningOdd
        self.print_money()

class Dealer(Player):
    def __init__(self):
        super().__init__("Dealer")
