__author__ = 'Mira'
from random import randint

n = int(input("How many times we should play?\n"))

def dice():
    return randint(1,6)

def game(times):
    player1 = 0
    player2 = 0
    for i in xrange(n):
        result1 = dice() + dice()
        result2 = dice() + dice()
        print("Player1 gets %d, and player2 gets %d.\n".format(result1,
            result2))

        if result1 < result2:
            player2 += 1
        else:
            player1 += 1
        
        print("%s:%s\n" % (player1, player2))
    
    if player1 == player2:
        while player1 == player2:
            result1 = dice() + dice()
            result2 = dice() + dice()
            print("zawodnik1 wylosowal " + str(result1) + " oczek, a zawodnik2 wylosowal " + str(result2) + "oczek\n")
            if result1 < result2:
                player2 += 1
            else:
                player1 += 1
            print('%s:%s\n' % (player1, player2))
    
    print("Player %d wins!\n" % (1 if player1 > player2 else 2))

