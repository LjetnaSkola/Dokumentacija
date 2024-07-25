from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
import socket
import threading
import time
import random


class ClientApp(App):
    def build(self):
        # Main layout
        layout = BoxLayout(orientation='vertical', padding=20, spacing=20)

        # Status label
        self.status_label = Label(text="Status: Idle", size_hint_y=None, height=60)
        layout.add_widget(self.status_label)

        # Server connection layout
        connection_grid = GridLayout(cols=3, spacing=10, size_hint_y=None, height=50)
        self.port_label = Label(text="Enter port:", size_hint_x=None, width=150)
        self.port_input = TextInput(hint_text="Enter port", size_hint_x=None, width=250)
        self.connect_button = Button(text="Connect", size_hint_y=None, height=50)
        self.connect_button.bind(on_press=self.connect_to_server)

        connection_grid.add_widget(self.port_label)
        connection_grid.add_widget(self.port_input)
        connection_grid.add_widget(self.connect_button)
        layout.add_widget(connection_grid)

        return layout

    def connect_to_server(self, instance):
        port = int(self.port_input.text)
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            self.client_socket.connect(('127.0.0.1', port))  # Assuming server is on the same machine
            self.status_label.text = "Status: Connected"
            # Start a new thread to handle server responses and sending messages
            self.server_thread = threading.Thread(target=self.receive_messages)
            self.server_thread.daemon = True
            self.server_thread.start()
            self.message_thread = threading.Thread(target=self.send_periodic_messages)
            self.message_thread.daemon = True
            self.message_thread.start()
        except Exception as e:
            self.status_label.text = f"Status: Error - {str(e)}"

    def receive_messages(self):
        try:
            while True:
                if self.client_socket:
                    data = self.client_socket.recv(1024)
                    if not data:
                        break
                    decoded_data = data.decode()
                    if decoded_data.startswith("TIME="):
                        print(f"Received Time: {decoded_data.split('=')[1]}")
                    else:
                        print(f"Received: {decoded_data}")
        except (ConnectionResetError, OSError) as e:
            print(f"Error receiving messages: {e}")
        finally:
            if self.client_socket:
                self.client_socket.close()
            self.status_label.text = "Status: Closed"

    def send_periodic_messages(self):
        while True:
            time.sleep(1)
            if hasattr(self, 'client_socket') and self.client_socket:
                try:
                    x = random.randint(1, 50)
                    y = random.randint(1, 50)
                    message = f"<x={x}|y={y}>"
                    self.client_socket.sendall(message.encode())
                except (OSError, ConnectionResetError) as e:
                    print(f"Error sending message: {e}")
                    break
            time.sleep(4)  # Wait for another 4 seconds (total 5 seconds)
            if hasattr(self, 'client_socket') and self.client_socket:
                try:
                    i_value = random.random() * 100  # Simulate I value
                    message = f"<I={i_value}>"
                    self.client_socket.sendall(message.encode())
                except (OSError, ConnectionResetError) as e:
                    print(f"Error sending message: {e}")
                    break


if __name__ == '__main__':
    ClientApp().run()
