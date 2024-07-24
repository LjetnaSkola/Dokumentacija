from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty, ListProperty
import socket
import threading
import time
from datetime import datetime
import matplotlib.pyplot as plt

class Server(BoxLayout):
    status = StringProperty('Idle')
    last_message = StringProperty('Last Message: ')
    average_i = StringProperty('Average I: ')
    x_values = ListProperty()
    y_values = ListProperty()
    server_socket = None
    client_socket = None
    connected = False
    i_values = []

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.socket_thread = None

    def create_socket(self):
        if self.connected:
            self.status = "Already connected"
            return

        port = 12345  # Example port, can be replaced with user input
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind(('0.0.0.0', port))
        self.server_socket.listen(1)
        self.status = f"Listening on port {port}"
        self.ids.create_socket_button.disabled = True
        self.socket_thread = threading.Thread(target=self.accept_connections)
        self.socket_thread.start()

    def accept_connections(self):
        while True:
            try:
                self.client_socket, address = self.server_socket.accept()
                self.status = f"Connected to {address}"
                self.ids.send_message_button.disabled = False
                self.connected = True
                threading.Thread(target=self.receive_messages, daemon=True).start()
            except Exception as e:
                self.status = "Error occurred"
                print(f"Error: {e}")
                break

    def receive_messages(self):
        while self.connected:
            try:
                message = self.client_socket.recv(1024).decode('utf-8')
                if not message:
                    break
                self.last_message = f"Last Message: {message}"
                self.ids.last_message_label.text = self.last_message
                self.process_message(message)
            except Exception as e:
                self.status = "Error occurred"
                print(f"Error: {e}")
                break

        self.client_socket.close()
        self.server_socket.close()
        self.status = "Idle"
        self.connected = False
        self.ids.create_socket_button.disabled = False
        self.ids.send_message_button.disabled = True

    def process_message(self, message):
        if message.startswith('<x=') and '|y=' in message:
            parts = message[1:-1].split('|')
            x = int(parts[0].split('=')[1])
            y = int(parts[1].split('=')[1])
            self.x_values.append(x)
            self.y_values.append(y)
            if len(self.x_values) > 10:
                self.x_values.pop(0)
                self.y_values.pop(0)
        elif message.startswith('<I='):
            i_value = float(message[3:-1])
            self.i_values.append(i_value)
            if len(self.i_values) > 0:
                self.average_i = f"Average I: {sum(self.i_values) / len(self.i_values)}"
                self.ids.average_i_label.text = self.average_i

    def send_message(self):
        if self.client_socket:
            current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            self.client_socket.send(current_time.encode('utf-8'))
        else:
            self.status = "No client connected"

    def show_statistics(self):
        if len(self.x_values) > 0 and len(self.y_values) > 0:
            plt.plot(self.x_values, self.y_values, marker='o')
            plt.xlabel('X')
            plt.ylabel('Y')
            plt.title('Last 10 X and Y values')
            plt.show()
        else:
            self.status = "No data to show"


class ServerApp(App):
    def build(self):
        return Server()

if __name__ == '__main__':
    ServerApp().run()
