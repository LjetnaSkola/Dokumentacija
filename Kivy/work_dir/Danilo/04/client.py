from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
import socket
import threading
import time
import random

class ClientApp(App):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.host = '127.0.0.1'  # Server's IP address
        self.port = 8080         # Server's port
        self.connected = False
        self.client_socket = None
        self.x_values = []
        self.y_values = []
        self.last_i_value = 0.0
        self.statistics_label = None
        self.connected_port_label = None
        self.status_label = None
        self.message_input = None
        self.send_button = None
        self.connected = False
        self.client_socket = None

    def build(self):
        root = BoxLayout(orientation='vertical', padding=20, spacing=10)

        self.status_label = Label(text='Status: Disconnected', font_size='20sp', color=(0, 0.7, 1, 1))
        self.connected_port_label = Label(text=f'Connected on port: {self.port}', font_size='20sp', color=(0, 0.7, 1, 1))
        self.message_input = TextInput(hint_text='Enter message', multiline=False)
        self.send_button = Button(text='Send Message', size_hint=(None, None), size=(150, 50))
        self.send_button.bind(on_press=self.send_message)
        self.statistics_label = Label(text='Average I: 0.0', font_size='20sp', color=(0, 0.7, 1, 1))

        root.add_widget(self.status_label)
        root.add_widget(self.connected_port_label)
        root.add_widget(self.message_input)
        root.add_widget(self.send_button)
        root.add_widget(self.statistics_label)

        self.connect_to_server()

        # Start sending periodic messages to the server
        self.start_sending_messages()

        return root

    def connect_to_server(self):
        if not self.connected:
            try:
                self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                self.client_socket.connect((self.host, self.port))
                self.connected = True
                self.status_label.text = 'Status: Connected'
                self.connected_port_label.text = f'Connected on port: {self.port}'
                self.send_button.disabled = False
            except ConnectionRefusedError:
                self.status_label.text = 'Status: Connection refused'
            except Exception as e:
                self.status_label.text = f'Status: Error - {str(e)}'
        else:
            self.status_label.text = 'Status: Already connected'

    def send_message(self, instance):
        if self.connected:
            message = self.message_input.text.strip()
            if message:
                try:
                    self.client_socket.sendall(message.encode())
                    self.status_label.text = f'Status: Message sent: {message}'
                except Exception as e:
                    self.status_label.text = f'Status: Error sending message - {str(e)}'
            else:
                self.status_label.text = 'Status: Empty message'
        else:
            self.status_label.text = 'Status: Not connected'

    def start_sending_messages(self):
        def send_periodic_messages():
            count = 0
            while True:
                count += 1
                x = random.randint(1, 50)
                y = random.randint(1, 50)
                message = f"<x={x}|y={y}>"
                try:
                    self.client_socket.sendall(message.encode())
                    self.status_label.text = f'Status: Periodic message sent: {message}'

                    if count % 5 == 0:
                        i_value = random.uniform(0.0, 100.0)
                        self.client_socket.sendall(f"<I={i_value}>".encode())
                        self.last_i_value = i_value
                        self.status_label.text = f'Status: Periodic I sent: {i_value}'
                except Exception as e:
                    self.status_label.text = f'Status: Error sending periodic message - {str(e)}'

                time.sleep(2)  # Send message every 2 seconds

        thread = threading.Thread(target=send_periodic_messages)
        thread.daemon = True
        thread.start()

    def on_stop(self):
        if self.connected:
            self.client_socket.close()

if __name__ == '__main__':
    ClientApp().run()
