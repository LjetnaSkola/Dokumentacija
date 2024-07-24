from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty
import socket
import threading
import random
import time


class Client(BoxLayout):
    status = StringProperty('Idle')
    received_message = StringProperty('Received Message: ')

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.client_socket = None
        self.client_thread = None
        self.connected = False

    def connect_to_server(self):
        if self.connected:
            self.status = "Already connected"
            return

        port = 12345  # Example port, can be replaced with user input
        server_address = '127.0.0.1'

        try:
            self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.client_socket.connect((server_address, port))
            self.status = f"Connected to {server_address}:{port}"
            self.connected = True
            self.client_thread = threading.Thread(target=self.receive_messages)
            self.client_thread.start()
            self.start_sending_messages()
        except Exception as e:
            self.status = "Error connecting to server"
            self.client_socket = None
            self.connected = False
            print(f"Error: {e}")

    def receive_messages(self):
        while self.connected:
            try:
                message = self.client_socket.recv(1024).decode('utf-8')
                if not message:
                    break
                self.received_message = f"Received Message: {message}"
                self.ids.received_message_label.text = self.received_message
            except Exception as e:
                self.status = "Error receiving message"
                self.client_socket = None
                self.connected = False
                print(f"Error: {e}")
                break

        self.client_socket.close()
        self.status = "Closed"
        self.connected = False

    def start_sending_messages(self):
        def send_messages():
            while self.connected:
                try:
                    x = random.randint(1, 50)
                    y = random.randint(1, 50)
                    self.client_socket.send(f"<x={x}|y={y}>".encode('utf-8'))
                    time.sleep(2)

                    if self.connected:
                        i_value = random.random()
                        self.client_socket.send(f"<I={i_value}>".encode('utf-8'))
                        time.sleep(5)
                except Exception as e:
                    print(f"Error sending message: {e}")
                    self.client_socket = None
                    self.connected = False
                    break

        threading.Thread(target=send_messages).start()


class ClientApp(App):
    def build(self):
        return Client()


if __name__ == '__main__':
    ClientApp().run()
