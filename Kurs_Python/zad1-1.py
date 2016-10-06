__author__ = 'Mira'
from random import randint

def dice():
    return randint(1,6)

class Player:
    def __init__(self):
        self._result = 0

    def roll(self):
        return dice() + dice()

    @property
    def result(self):
        return self._result

    def wins(self):
        self._result += 1

    def __eq__(self, other):
        return self.result == other.result

def play(player1, player2):
    result1 = player1.roll()
    result2 = player2.roll()
    print("Round: Player 1 {0} : {1} Player 2".format(result1, result2))
    if result1 > result2:
        player1.wins()
    if result2 > result1:
        player2.wins()
    print("{0} : {1}".format(player1.result, player2.result))

def game(times):
    player1 = Player()
    player2 = Player()
    for i in range(n):
       play(player1, player2) 
    
    if player1 == player2:
        while player1 == player2:
           play(player1, player2) 
    
    print("Player %s wins!\n" % (
        "1" if player1.result > player2.result else "2"))

n = int(input("How many times we should play?\n"))
game(n)
