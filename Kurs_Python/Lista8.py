__author__ = 'Mira'
# -*- coding: UTF-8 -*-
#napisane w python 2.7
import Tkinter
import shelve

class PhoneBookDb:
    def __init__(self):
        self.database = shelve.open('db.db')
    def add_contact(self,key, phonenumber, email):
        self.database[key] = [phonenumber,email]
    def delete_contact(self, key):
        del self.database[key]
    def find_contact(self, key):
        for ikey in self.database:
            if ikey==key:
                return self.database[key]
    def edit_contact(self,key, edphonenumber, edemail):
        self.database[key] = [edphonenumber,edemail]
        return self.database[key]

class PhoneBookGUI:
    def __init__(self):
        #inicjalizacja bazy danych
        self.data = PhoneBookDb()

        #inicjalizowanie okna
        self.window = Tkinter.Tk()
        self.window.geometry("550x300")
        self.window.title('PhoneBook')

        self.frame = Tkinter.Frame(self.window)
        self.frame.pack(fill=Tkinter.BOTH, expand=1)

        #tworzenie nowego kontaktu
        Tkinter.Label (self.frame, text = "Nowy kontakt").grid (row=0, column=1, columnspan=2)

        Tkinter.Label (self.frame, text = "Nazwa:").grid (row=1, column=1)
        self.v_nazwa = Tkinter.StringVar()
        self.e_nazwa = Tkinter.Entry(self.frame, textvariable=self.v_nazwa).grid(row=1,column=2)

        Tkinter.Label (self.frame, text = "Numer telefonu:").grid (row=2, column=1)
        self.v_numer = Tkinter.StringVar()
        self.e_telefon = Tkinter.Entry(self.frame, textvariable = self.v_numer).grid(row=2,column=2)

        Tkinter.Label (self.frame, text = "Adres e-mail:").grid (row=3, column=1)
        self.v_adres = Tkinter.StringVar()
        self.e_adres = Tkinter.Entry(self.frame, textvariable = self.v_adres).grid(row=3,column=2)

        self.add_person = Tkinter.Button(self.frame, text="Add",command=self.add, pady=2).grid(row=4,column=2)

        #Lista kontaktow
        Tkinter.Label(self.frame,text="Lista kontaktow").grid(row=0)
        self.listbox = Tkinter.Listbox(self.frame)
        for i in self.data.database:
            self.listbox.insert(Tkinter.END,i)
        self.listbox.bind("<<ListboxSelect>>", self.onSelect)
        self.listbox.grid(row=1, rowspan=4)

        #wyszukiwanie ludzi
        Tkinter.Label(self.frame,text="Szukaj:").grid(row=5)
        self.v_szukajka = Tkinter.StringVar()
        self.e_szukajka = Tkinter.Entry(self.frame, textvariable=self.v_szukajka).grid(row=5,column=1)
        self.find_person = Tkinter.Button(self.frame, text="Znajdz", command=self.findurlow, pady=2).grid(row=5,column=2)
        self.some_name = Tkinter.StringVar()
        self.some_name.set(" ")
        Tkinter.Label(self.frame,textvariable=self.some_name).grid(row=6,column=1)
        Tkinter.Label(self.frame,text="Numer:").grid(row=7,column=0)
        self.some_number = Tkinter.StringVar()
        self.some_name.set(" ")
        Tkinter.Label(self.frame,textvariable=self.some_number).grid(row=7,column=1)
        Tkinter.Label(self.frame,text="E-mail:").grid(row=8,column=0)
        self.some_adres = Tkinter.StringVar()
        self.some_adres.set(" ")
        Tkinter.Label(self.frame,textvariable=self.some_adres).grid(row=8,column=1)

    def onSelect(self, val):

        sender = val.widget
        idk = sender.curselection()
        key = sender.get(idk)

        self.some_name.set(key)
        self.some_number.set(self.data.database[key][0])
        self.some_adres.set(self.data.database[key][1])
        Tkinter.Button(self.frame, text="Usun", command=lambda: self.deleted(key)).grid(row=7,column=2)
        Tkinter.Button(self.frame, text="Edytuj", command = lambda:self.edit(key)).grid(row=8,column=2)

    def findurlow(self):
        key = self.v_szukajka.get()
        self.some_name.set(" ")
        self.some_adres.set(" ")
        self.some_number.set(" ")
        znaleziony = self.data.find_contact(key)
        self.some_name.set(key)
        self.some_number.set(znaleziony[0])
        self.some_adres.set(znaleziony[1])
        Tkinter.Button(self.frame,text="Usun", command=lambda: self.deleted(key)).grid(row=7,column= 2)
        Tkinter.Button(self.frame, text="Edytuj", command = lambda:self.edit(key)).grid(row=8,column=2)
    def add(self):
        self.data.add_contact(self.v_nazwa.get(),self.v_numer.get(),self.v_adres.get())
        self.listbox.insert(Tkinter.END,self.v_nazwa.get())
    def deleted(self,x):
        self.data.delete_contact(x)
        #self.listbox.delete(x)
        self.some_name.set("Kontakt zostal usuniety")
        self.some_adres.set(" ")
        self.some_number.set(" ")
    def edit(self,key):
        new_number = Tkinter.StringVar()
        new_number.set(self.data.database[key][0])
        Tkinter.Entry(self.frame, textvariable=new_number).grid(row=7,column=3)
        new_adres = Tkinter.StringVar()
        new_adres.set(self.data.database[key][1])
        Tkinter.Entry(self.frame, textvariable=new_adres).grid(row=8,column=3)
        Tkinter.Button(self.frame, text="OK", command=lambda:self.postedit(key,new_number.get(),new_adres.get())).grid(row=8,column = 4)
    def postedit(self,key,nvalue,nadres):
        self.data.edit_contact(key,nvalue,nadres)
        self.some_name.set("Kontakt zmieniony")
        self.some_adres.set(" ")
        self.some_number.set(" ")



app = PhoneBookGUI()
app.window.mainloop()