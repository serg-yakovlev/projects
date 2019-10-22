import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class ChatWindow(Gtk.Window):
    def __init__(self):
        super().__init__(title="Mega Chat | Login")
        self.login = login.LoginWindow()
        self.login.show_all()



# if __name__ == '__main__':

#     #print(dir(Gtk.Entry.connect.__name__))
#     win = login.LoginWindow()
#     win.connect("destroy", Gtk.main_quit)
#     win.show_all()
#     Gtk.main()
