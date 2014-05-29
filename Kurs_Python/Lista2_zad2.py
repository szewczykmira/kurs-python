__author__ = 'Mira'
class ObiektyDodawalne:
    def __add__(self, other):
        temp1 = self.__dict__
        temp2 = other.__dict__
        obiekt = ObiektyDodawalne()
        obiekt.__dict__.update(temp1)
        obiekt.__dict__.update(temp2)
        return obiekt
class Inna(ObiektyDodawalne):
    def __init__(self, arg1, arg2):
        self.jeden = arg1
        self.dwa = arg2
class JeszczeCos(ObiektyDodawalne):
    def __init__(self):
        self.cos = 7

pierwszy = Inna('siostra', 'brat')
drugi = JeszczeCos()
pierwszy.dynamiczne_pole = 'A bo moge'
drugi.dwa = 98
print(pierwszy.__dict__)
print(drugi.__dict__)
trzeci = pierwszy + drugi
print(trzeci.__dict__)


