import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, GdkPixbuf
import chat
import login
import redis
import  json
import os
import event

HOST = "127.0.0.1"
PORT = 5000


class ChatWindow(Gtk.Window):

    def __init__(self):
        super().__init__(title="Mega Chat | Login")
        event.Event(name="login")
        # self.login_win = login.LoginWindow(self.regy_date)
        # self.login_win.show_all()
        self.connection = None

        #self.set_allocation
        self.set_position(Gtk.WindowPosition.CENTER)
        self.set_size_request(800, 600)

        master_box = Gtk.Box()
        self.add(master_box)

        left_box = Gtk.Box(Gtk.Orientation.VERTICAL)
        left_box.set_size_request(200, -1)
        master_box.pack_start(left_box, False, True, 0)

        center_box = Gtk.Box(Gtk.Orientation.VERTICAL)
        center_box.set_size_request(200, -1)
        master_box.pack_start(center_box, False, True, 0)

        right_box = Gtk.Box(Gtk.Orientation.VERTICAL)
        right_box.set_size_request(200, -1)
        master_box.pack_start(right_box, False, True, 0)

        pict = GdkPixbuf.Pixbuf.new_from_file_at_scale(
        filename="avatar.jpg", 
        width=50, 
        height=50, 
        preserve_aspect_ratio=True)

        avatar = Gtk.Image.new_from_pixbuf(pict)

        # avatar = Gtk.Image()
        # avatar.set_from_file(
        #     os.path.join(
        #         os.path.dirname(os.path.abspath(__file__)),
        #         "avatar.jpg"
        #         )
        #     )
        # avatar.set_size_request(50,50)

        left_box.pack_start(avatar, False, True, 5)        

        user_label = Gtk.Label(label = "User name")
        left_box.pack_start(user_label, True, False,0)

        message_entry = Gtk.Entry()
        center_box.pack_start(message_entry, True, False, 0)

        favorite_label = Gtk.Label(label = "Favorites")
        right_box.pack_start(favorite_label, True, False,0)

        self.show_all()


    def regy_date():
        self.login.hide()
        storage = redis.StrictRedis()
        try:
            self.login = storage.get("login")
            self.password = storage.get("password")
        except redis.RedisError:
            print("No data")
            Gtk.main_quit()
        else:
            self.__create_connection()
            self.show_all()


    def __create_connection(self):
            self.connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.connection.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            # self.connection.setblocking(0)
            self.connection.connect((HOST,PORT))
            data = json.dumps({"login": self.login, "password": self.password})
            self.connection.send(data.encode("utf-8"))
            result = self.connection.reqv(2048)
            data = json.loads(result.decode("utf-8"))
            if data.get("status") != "OK":
                print(data.get("message"))
                Gtk.main_quit()
            else:
                self__run()


    def run(self):
            # self.epoll = select.epoll()
            # self.epoll.register(self.sock.fileno(), select.EPOLLIN)
        pass

if __name__ == '__main__':

    #print(dir(Gtk.Entry.connect.__name__))
    win = ChatWindow()
    win.connect("destroy", Gtk.main_quit)
    win.show_all()
    Gtk.main()