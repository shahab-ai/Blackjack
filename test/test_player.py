import sys
sys.path.append('./code')

from ..code.player import RegularPlayer, Dealer
from ..code.deck import Card
import nose.tools as n

def test_player_init():
    player = RegularPlayer("Player", 100)
    n.assert_equal(player.name, "Player")
    n.assert_equal(player.money, 100)
    n.assert_equal(player.hand, [])

def test_player_str():
    player = RegularPlayer("Player", 100)
    n.assert_equal(str(player), "Cards in Player's hand: [], Total=0")

def test_player_recieve():
    player = RegularPlayer("Player", 100)
    card1 = Card("10","c")
    card2 = Card("8","h")
    player.receive_card(card1)
    player.receive_card(card2)
    n.assert_equal(str(player), "Cards in Player's hand: [10c, 8h], Total=18")

def test_player_reset():
    player = RegularPlayer("Player", 100)
    card = Card("10","c")
    player.receive_card(card)
    player.reset()
    n.assert_equal(player.hand, [])

def test_bet():
    player = RegularPlayer("Player", 100)
    n.assert_equal(player.money, 100)
    player.bet(5)
    player.lostRound()
    n.assert_equal(player.money, 95)
    player.bet(10)
    player.wonRound()
    n.assert_equal(player.money, 110)
