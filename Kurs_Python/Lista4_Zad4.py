__author__ = 'Mira'
from io import StringIO

class Worder(object):
    def __init__(self, stream):
        self.stream = stream
        self.firstchar = ''
    def __iter__(self):
        return self
    def __next__(self):
        word = self.firstchar
        term = False
        split = False
        while True:
            char = self.stream.read(1)
            if char == '':
                if word == '':
                    raise StopIteration
                self.firstchar = ''
                break
            if char.isalnum():
                if term:
                    self.firstchar = char
                    break
                word += char
            else:
                if char == '-':
                    split = True
                elif not(char == '\n' and split):
                    term = True
                    self.firstchar = ''
        return word

from collections import Counter

def stats(string):
    stats = Counter()
    stream = StringIO(string)
    for word in Worder(stream):
        stats[len(word)] += 1
    stream.close()
    return stats

string = """Zaprogramuj iterator który przetwarza strumień tekstowy i zwraca
kolejne słowa z tekstu (dla utrudnienia uwzględnij dzielenie słów na końcach wier-
szy), pomijając białe znaki i znaki interpunkcyjne. Korzystając z tej implementacji
zaprogramuj obliczanie statystyki długości słów w tekście, tj. ile jest słów długości 1,
ile długości 2 etc."""

print(stats(string))
