__author__ = 'Mira'
from math import *
def is_prime(n):
    iter = 2
    while iter<=sqrt(n):
        if n%iter==0:
            return False
        else:
            iter+=1
    return True

def pierwsze_funkcyjna(n):
    return list(filter(is_prime, range(2, n+1)))
def pierwsze_skladana(n):
    lista = [x for x in range(2, n+1) if is_prime(x)==True]
    return lista
liczba = int(input("Podaj liczbe"))
print(pierwsze_funkcyjna(liczba))
print(pierwsze_skladana(liczba))


