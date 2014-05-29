__author__ = 'Mira'
from random import randint
def rzut_kostka():
    return randint(1,6)

zawodnik1 = 0
zawodnik2 = 0

n = int(input("Ile tur ma sie wykonac?\n"))
for i in range(n):
    wynik1 = rzut_kostka()+rzut_kostka()
    wynik2 = rzut_kostka() + rzut_kostka()
    print("zawodnik1 wylosowal " + str(wynik1) + " oczek, a zawodnik2 wylosowal " + str(wynik2) + "oczek\n")
    if wynik1<wynik2:
        zawodnik2+=1
    else:
        zawodnik1+=1
    print("%s:%s\n" % (zawodnik1, zawodnik2))
if zawodnik1==zawodnik2:
    while zawodnik1==zawodnik2:
        wynik1 = rzut_kostka()+rzut_kostka()
        wynik2 = rzut_kostka() + rzut_kostka()
        print("zawodnik1 wylosowal " + str(wynik1) + " oczek, a zawodnik2 wylosowal " + str(wynik2) + "oczek\n")
        if wynik1<wynik2:
            zawodnik2+=1
        else:
            zawodnik1+=1
        print('%s:%s\n' % (zawodnik1, zawodnik2))
if zawodnik1>zawodnik2:
    print("Zwyciezyl zawodnik1\n")
else:
    print("Zwyciezyl zawodnik2\n")

