__author__ = 'Mira'
import timeit

from math import *
def is_prime(n):
    itera = 2
    while itera<=sqrt(n):
        if n%itera==0:
            return False
        else:
            itera+=1
    return True
class Kolekcja:
    def __init__(self, x):
        self.licznosc = x
    def __iter__(self):
        self.pointer = 1
        return self
    def __next__(self):
        if self.pointer==self.licznosc: raise StopIteration
        self.pointer += 1
        return self.pointer

def pierwsze_funkcyjna(n):
    return list(filter(is_prime, range(2, n+1)))
def pierwsze_skladana(n):
    lista = [x for x in range(2, n+1) if is_prime(x)==True]
    return lista
def pierwsze_iterowane(n):
    lista = []
    for i in Kolekcja(n):
        if is_prime(i)==True:
            lista.append(i)
    return lista
liczba = int(input("Podaj liczbe"))
print(pierwsze_iterowane(liczba))
print(pierwsze_funkcyjna(liczba))
print(pierwsze_skladana(liczba))
t = timeit.Timer('Zad1.pierwsze_funkcyjna(10)','import Zad1').repeat(1,0)
c = timeit.Timer('Zad1.pierwsze_iterowane(10)','import Zad1').repeat(1,0)
s = timeit.Timer('Zad1.pierwsze_skladana(10)','import Zad1').repeat(1,0)
print (t)
print(c)
print(s)
