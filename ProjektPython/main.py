__author__ = 'Mira'
# -*- coding: UTF-8 -*-
#wygląd bazy danych: Money(data,ile, kategoria,dodatkoweinfo)
import tkinter
from tkinter import ttk
import sqlite3
import os
import threading


class NewDebter:
    def __init__(self):
        """Funkcja inicjalizująca klasę NewDebter a zarazem całą aplikację. Zainicjalizowane jest podłączenie bazy danych
        ktora zostala zaprogramowana przy uzyciu sqlite3 oraz graficznego interfejsu (tkinter)
        """
        self.sum = self.setSum()
        self.db_exist()
        #tworzenie okna
        self.window = tkinter.Tk()
        self.window.title("NewDebter 1.0")
        self.frame = tkinter.Frame(self.window, border=10, background='white')
        self.frame.pack(fill=tkinter.BOTH)
        #Przyciski do wyswietlania historii, wyswietalnia wydatkow wg kategorii i wskazywanie aktualnego stanu konta
        #wykonują one w nowych wątkach funkcje
        but = tkinter.Button(self.frame, text="Historia", background="pink", height='2', width=10,
                             command=lambda: threading.Thread(target=self.historia()))
        but.grid(row=0, column=0)
        but1 = tkinter.Button(self.frame, text="Wyświetl kategorię", background="pink", height=2,
                              command=lambda: threading.Thread(target=self.selectByCategory()))
        but1.grid(row=0, column=1)
        self.suma = tkinter.Label(self.frame, text=self.sum, background="white", height=2, width=10).grid(row=0,
                                                                                                          column=2)
        #dodawanie wydatku
        tkinter.Label(self.frame, text="Dodaj wydatek do bazy:", background="white", height=2).grid(row=1, column=1)
        tkinter.Label(self.frame, text="Kwota:", background="white", anchor="e").grid(row=2, column=0)
        self.kwota1 = tkinter.StringVar()
        tkinter.Entry(self.frame, text=self.kwota1, background="white").grid(row=2, column=1)
        tkinter.Label(self.frame, text="Kategoria:", background="white").grid(row=3, column=0)
        #takie dziwne cos
        self.box_value = tkinter.StringVar()
        self.box = ttk.Combobox(self.frame, textvariable=self.box_value, state='readonly')
        self.box['values'] = (
            'jedzenie', 'rozrywka', 'dlug', 'zwrot od wierzyciela', 'wyplata', 'ksiazki', 'rozwijanie sie')
        self.box.current(0)
        self.box.grid(row=3, column=1)
        tkinter.Label(self.frame, text="Dodatkowe dane:", background="white").grid(row=4, column=0)
        self.d_info = tkinter.StringVar()
        tkinter.Entry(self.frame, text=self.d_info, background='white').grid(row=4, column=1)
        tkinter.Button(self.frame, text="Dodaj!", background="pink", command=self.addRec).grid(row=4, column=2)
    def db_exist(self):
        if os.path.exists('newdb.db'):
            self.database = sqlite3.connect('newdb.db')
            self.dbcursor = self.database.cursor()
        else:
            self.database = sqlite3.connect('newdb.db')
            self.dbcursor = self.database.cursor()
            self.dbcursor.execute('create table Money(data date, ile real, kategoria text, dodatkoweinfo text)')
            self.database.commit()
    def setSum(self):
        """Sprawdza czy w folderze z aplikacją znajduje się plik kwota.txt, ktory zawiera kwote znajdujaca sie na koncie.
        Jezeli plik takowy nie istnieje pobiera daną i zapisuje ją w pliku o takiej nazwie
        @return: zwraca ilosc pieniedzy znajdujacych sie na koncie
        """
        if os.path.exists('kwota.txt'):
            file = open('kwota.txt', 'r')
            kwota = file.readline()
            file.close()
            return float(kwota)
        else:
            file = open('kwota.txt', 'w')
            kwota = 0.00
            file.write(str(kwota))
            file.close()
            return kwota

    def changeSum(self, newsum):
        """Po dodaniu nowego rekordu do bazy poprawia ilosc pieniedzy znajdujacych sie na koncie
        @param newsum:
        """
        file = open('kwota.txt', 'w')
        file.write(str(newsum))
        self.sum = newsum
        file.close()
        self.suma.set(self.sum)

    def addRec(self):
        """Dodaje do bazy danych rekord postaci aktualna data; ilosc pieniedzy wydanych, z jakiej kategorii oraz
        dodatkowe informacje. Po dodaniu rekordu, wykonuje funkcję zmiany sumy pieniędzy, która pozostała użytkownikowi
        """
        kwota = self.kwota1.get()
        kategoria = self.box.get()
        dinfo = self.d_info.get()
        with self.database:
            self.dbcursor.execute('insert into Money values (date("now"),?,?,?)',(kwota, kategoria, dinfo))
        if "zwrot od wierzyciela" == kategoria or kategoria == "wyplata":
            self.changeSum(float(self.sum) + float(kwota))
        else:
            self.changeSum(float(self.sum) - float(kwota))

    def selectByCategory(self):
        """Pozwala wyselekcjonować 10 ostatnich rekordów z bazy danych, ktore naleza do danej kategorii.
            Jest to ze strony GUI
        """
        self.okno = tkinter.Tk()
        self.okno.title('NewDebter 1.0')
        self.ramka = tkinter.Frame(self.okno)
        self.ramka.pack(fill=tkinter.BOTH)
        tkinter.Label(self.ramka, text="Ktora kategorie poszukujesz?").grid(row=0)
        #takie dziwne cos
        box_value = tkinter.StringVar()
        box = ttk.Combobox(self.ramka, textvariable=box_value, state='readonly')
        box['values'] = ('jedzenie', 'rozrywka', 'dlug', 'zwrot od wierzyciela', 'wyplata', 'ksiazki', 'rozwijanie sie')
        box.current(0)
        box.grid(row=1, column=0)
        tkinter.Button(self.ramka, text="OK", command=lambda: self.showByCategory(box.get())).grid(row=1, column=1)
        self.okno.mainloop()

    def showByCategory(self, kategory):
        """rozszerzenie funkcji selectByCategory: pobiera z niej informacje jaka kategoria nas interesuje a następnie
        wysyła zapytanie do bazy i wyświetla wyniki w nowym oknie
        @param kategory:
        """
        okienko = tkinter.Tk()
        okienko.title('NewDebter 1.0')
        rameczka = tkinter.Frame(okienko)
        rameczka.pack(fill=tkinter.BOTH)
        self.dbcursor.execute("select Data,Ile,D_info from Money where Kategoria=?", (kategory,))
        res = self.dbcursor.fetchall()
        tkinter.Label(rameczka, text="Data").grid(row=0, column=0)
        tkinter.Label(rameczka, text="Kwota").grid(row=0, column=1)
        tkinter.Label(rameczka, text="Inne").grid(row=0, column=3)
        i = 1
        for record in res:
            j = 0
            for k in record:
                tkinter.Label(rameczka, text=k).grid(row=i, column=j)
                j += 1
            i += 1
        okienko.mainloop()

    def historia(self):
        """Wyswietla w nowym oknie historię dodawanych rekordów
        """
        okno = tkinter.Tk()
        okno.title('Historia')
        ramka = tkinter.Frame(okno, border=5)
        ramka.pack(fill=tkinter.BOTH)
        tkinter.Label(ramka, text="Historia").grid(row=0, column=1)
        self.dbcursor.execute("select * from Money")
        result = self.dbcursor.fetchmany(10)
        tkinter.Label(ramka, text="Data").grid(row=1, column=0)
        tkinter.Label(ramka, text="Kwota").grid(row=1, column=1)
        tkinter.Label(ramka, text="Kategoria").grid(row=1, column=2)
        tkinter.Label(ramka, text="Inne").grid(row=1, column=3)
        i = 2
        for rekord in result:
            j = 0
            for k in rekord:
                tkinter.Label(ramka, text=k).grid(row=i, column=j)
                j += 1
            i += 1
        okno.mainloop()


smt = NewDebter()
smt.window.mainloop()
