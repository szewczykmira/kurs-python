__author__ = 'Mira'
def rozklad(n):
    if n<=1:
        return n
    czynnik = 2
    temp=[]
    zliczacz = 0
    while czynnik <= n:
        if n%czynnik == 0:
            zliczacz+=1
            n/=czynnik
        else:
            if zliczacz!=0:
                temp.append((czynnik,zliczacz))
                zliczacz = 0
            czynnik+=1
    temp.append((czynnik,zliczacz))
    print(temp)
    return temp
liczba = int(input("Podaj liczbe: "))
rozklad(liczba)