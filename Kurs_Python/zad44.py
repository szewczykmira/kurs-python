import string
from io import StringIO
from collections import Counter

class Worder(object):

    def __init__(self, stream):
        self.stream = stream
        self.iter = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        acc = ['\n','-']
        word = ''
        helper = self.iter
        if helper == len(self.stream):
            raise StopIteration
        while True:
            if self.stream[helper].isalnum() or self.stream[helper] in acc:
                if not self.stream[helper] in acc:
                    word += self.stream[helper]
                helper += 1
            else:
                helper += 1
                break
        self.iter = helper
        return word

def stats(text):
    stats = Counter()
    for word in Worder(text):
        stats[len(word)] += 1
    
    return stats

text = """Zaprogramuj iterator który przetwarza strumień tekstowy i zwraca
kolejne słowa z tekstu (dla utrudnienia uwzględnij dzielenie słów na końcach wier-
szy), pomijając białe znaki i znaki interpunkcyjne. Korzystając z tej implementacji
zaprogramuj obliczanie statystyki długości słów w tekście, tj. ile jest słów długości 1,
ile długości 2 etc."""

print(stats(text))
