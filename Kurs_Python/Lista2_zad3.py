__author__ = 'Mira'
def fibonacci(n):
    if n==0:
        return 0
    if n==1:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)
def silnia(n):
    if n==1:
        return 1
    else:
        print(n)
        return n*silnia(n-1)

