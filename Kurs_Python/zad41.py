__author__ = 'Mira'
import timeit

from zad31 import *

class Kolekcja:
    def __init__(self, x):
        self.licznosc = x
    
    def __iter__(self):
        self.pointer = 1
        return self
    
    def __next__(self):
        if self.pointer == self.licznosc: 
            raise StopIteration
        self.pointer += 1
        return self.pointer

def pierwsze_iterowane(n):
    lista = []
    for i in Kolekcja(n):
        if is_prime(i)==True:
            lista.append(i)
    return lista

liczba = int(input("Podaj liczbe"))

print(pierwsze_iterowane(liczba))
print(prime_functional(liczba))
print(prime_comprehensions(liczba))

t = timeit.Timer('Zad1.pierwsze_funkcyjna(10)','import Zad1').repeat(1,0)
c = timeit.Timer('Zad1.pierwsze_iterowane(10)','import Zad1').repeat(1,0)
s = timeit.Timer('Zad1.pierwsze_skladana(10)','import Zad1').repeat(1,0)

print (t)
print(c)
print(s)
