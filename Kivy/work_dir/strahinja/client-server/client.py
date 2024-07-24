from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.clock import Clock
import socket
import threading
import random
import time


class MainView(BoxLayout):
    status_label = ObjectProperty()
    connect_button = ObjectProperty()
    time_label = ObjectProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.client_socket = None
        self.connect_button.bind(on_press=self.connect_to_server)
        self.send_data_thread = None
        self.receive_thread = None

    def connect_to_server(self, *args):
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        threading.Thread(target=self.connect_and_listen, daemon=True).start()

    def connect_and_listen(self):
        try:
            self.client_socket.connect(("localhost", 8080))
            Clock.schedule_once(self.update_status_connected)
            self.start_sending_data()
            self.start_receiving_data()
        except Exception as e:
            print(f"Connection error: {e}")
            Clock.schedule_once(self.update_status_closed)

    def start_sending_data(self):
        self.send_data_thread = threading.Thread(
            target=self.send_data_periodically, daemon=True
        )
        self.send_data_thread.start()

    def start_receiving_data(self):
        self.receive_thread = threading.Thread(
            target=self.receive_data_periodically, daemon=True
        )
        self.receive_thread.start()

    def send_data_periodically(self):
        while True:
            if self.client_socket:
                x = random.randint(1, 50)
                y = random.randint(1, 50)
                self.client_socket.send(f"<x={x}|y={y}>\n".encode("utf-8"))
                time.sleep(2)
                i_value = random.uniform(0, 100)
                self.client_socket.send(f"<I={i_value}>\n".encode("utf-8"))
                time.sleep(3)

    def receive_data_periodically(self):
        while True:
            try:
                data = self.client_socket.recv(1024).decode("utf-8")
                if data:
                    self.update_time_label(data)
            except Exception as e:
                print(f"Receive error: {e}")
                Clock.schedule_once(self.update_status_closed)
                break

    def update_status_connected(self, *args):
        self.status_label.text = "Connected"

    def update_status_closed(self, *args):
        self.status_label.text = "Closed"
        if self.client_socket:
            self.client_socket.close()
            self.client_socket = None

    def update_time_label(self, time_str, *args):
        self.time_label.text = f"Server Time: {time_str}"

    def on_stop(self):
        if self.client_socket:
            self.client_socket.close()


class ClientApp(App):
    def build(self):
        return MainView()


if __name__ == "__main__":
    ClientApp().run()
