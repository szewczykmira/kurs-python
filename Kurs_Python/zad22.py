__author__ = 'Mira'

class Additive:
    def __add__(self, other):
        self.__dict__.update(other.__dict__)
        return self

class Foo(Additive):
    def __init__(self, arg1, arg2):
        self.jeden = arg1
        self.dwa = arg2

class Bar(Additive):
    def __init__(self):
        self.cos = 7

first = Foo('siostra', 'brat')
second = Bar()
first.dynamics = "fooo"
second.two = 98
print("Dict of first: ", first.__dict__)
print("Dict of second: ", second.__dict__)
first + second
print("Dict of first + second", first.__dict__)
