__author__ = 'Mira'
from math import sqrt

def is_prime(n):
    iter = 2
    while iter <= sqrt(n):
        if n % iter == 0:
            return False
        else:
            iter += 1
    return True

def prime_functional(n):
    return list(filter(is_prime, range(2, n+1)))

def prime_comprehensions(n):
    return [x for x in range(2, n+1) if is_prime(x)==True]
