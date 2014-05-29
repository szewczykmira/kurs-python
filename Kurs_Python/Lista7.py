__author__ = 'Mira'
#Python 2.7
import gtk
import gobject

class Minutnik:
    def __init__(self):
        #inicjalizowanie glownego okna
        self.window = gtk.Window()
        self.window.connect("destroy", lambda wid: gtk.main_quit())
        self.window.connect("delete_event", lambda a1,a2:gtk.main_quit())
        self.window.set_border_width(50)
        self.window.set_title("Minutnik")
        #tworzenie boxa
        vbox = gtk.VBox()
        self.window.add(vbox)

        self.label = gtk.Label("What do you wanna cook?")
        vbox.pack_start(self.label)

        hbox = gtk.HBox()
        vbox.pack_start(hbox)

        button_eggs = gtk.Button("Eggs")
        button_eggs.connect("clicked", self.eggs)
        hbox.pack_start(button_eggs)

        button_rice = gtk.Button("Rice")
        button_rice.connect("clicked", self.rice)
        hbox.pack_start(button_rice)

        self.window.show_all()

    def eggs(self, sender):
        self.counter = 300
        gobject.timeout_add(1000, self.countdown_function)
        self.countdown_function()

    def rice(self,sender):
        self.counter = 600
        gobject.timeout_add(1000,self.countdown_function)
        self.countdown_function()

    def countdown_function(self):
        if self.counter > 0:
            self.label.set_text("Remaining: " + str(self.counter) + "s")
            self.counter -= 1
            return True
        else:
            self.label.set_text("Your meal is ready!")
            return False
if __name__ == "__main__":
    app = Minutnik()
    gtk.main()
