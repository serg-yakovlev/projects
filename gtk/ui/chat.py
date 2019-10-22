import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
import login


if __name__ == '__main__':

    #print(dir(Gtk.Entry.connect.__name__))
    win = login.LoginWindow()
    win.connect("destroy", Gtk.main_quit)
    win.show_all()
    Gtk.main()
