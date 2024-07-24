from kivy.uix.settings import text_type
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
import matplotlib.pyplot as plt
from kivy.garden.matplotlib import FigureCanvasKivyAgg
from kivy.clock import Clock
import socket
import threading

from matplotlib.figure import Figure


class MainView(BoxLayout):
    status_label = ObjectProperty()
    start_listening_button = ObjectProperty()
    send_button = ObjectProperty()
    last_message_label = ObjectProperty()
    message = ObjectProperty()
    average_label = ObjectProperty()
    plot_button = ObjectProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.server_socket = None
        self.client_socket = None
        self.client_address = None
        self.start_listening_button.bind(on_press=self.start_listening)
        self.send_button.bind(on_press=self.do_send)
        self.send_button.disabled = True

        self.figure = Figure()
        self.ax = self.figure.add_subplot(111)
        self.canvas = FigureCanvasKivyAgg(self.figure)
        self.add_widget(self.canvas)

    def start_listening(self, *args):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind(("localhost", 8080))
        self.server_socket.listen(5)
        self.start_listening_button.disabled = True
        self.status_label.text = "Listening"
        threading.Thread(target=self.accept_connections, daemon=True).start()

    def accept_connections(self):
        while True:
            client_socket, client_address = self.server_socket.accept()
            self.client_socket = client_socket
            self.client_address = client_address
            Clock.schedule_once(self.update_status_connected)
            threading.Thread(
                target=self.handle_client, args=(client_socket,), daemon=True
            ).start()

    def update_status_connected(self, *args):
        self.status_label.text = "Connected"
        self.send_button.disabled = False

    def handle_client(self, client_socket):
        while True:
            try:
                data = client_socket.recv(1024)
                if not data:
                    break
                message_from_client = data.decode("utf-8")
                Clock.schedule_once(
                    lambda dt: self.update_last_message(message_from_client)
                )
            except:
                break
        self.client_socket = None
        Clock.schedule_once(self.update_status_listening)

    def update_status_listening(self, *args):
        self.status_label.text = "Listening"
        self.send_button.disabled = False

    def update_last_message(self, message):
        self.last_message_label.text = f"Last Message: {message}"

    def do_send(self, *args):
        if self.client_socket:
            message_to_client = self.message.text.encode("utf-8")
            self.client_socket.sendall(message_to_client)
            self.message.text = ""


class ServerApp(App):
    def build(self):
        return MainView()


if __name__ == "__main__":
    ServerApp().run()
