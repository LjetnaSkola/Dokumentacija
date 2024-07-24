from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from enum import Enum
import socket
import threading
from kivy.clock import Clock

class Status(Enum):
    IDLE = "idle"
    LIST = "listening"
    CONN = "connected"
    CLOSED = "closed"


class Server():
    status = Status.CLOSED
    host = ""
    port = 0
    last_message = ""

    def handle_client(self, client_socket, client_address):
        with client_socket:

            while True:
                data = client_socket.recv(1024)

                if not data: 
                    break

                print("DATA: " + str(data.decode("utf-8")))
                Server.last_message = str(data.decode("utf-8"))

    def start_server(self, host, port):
        Server.host = host
        Server.port = port
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
            server_socket.bind((host, port))

            server_socket.listen(5)
            print(f"Server listening on {Server.host}:{Server.port}")

            while True:
                client_socket, client_address = server_socket.accept()
                client_thread = threading.Thread(target=self.handle_client, args=(client_socket, client_address))
                client_thread.start()
                Server.status = Status.CONN



class SimpleApp(App):
    
    label2 = Label()
    def build(self):
        root = BoxLayout(orientation='vertical', padding=20, spacing=10)
        
        self.label = Label(text='Server Status: ' + Server.status.value, font_size='20sp', color=(0, 0.7, 1, 1))
        
        button1 = Button(text='Open Socket', size_hint=(None, None), size=(250, 150))
        button2 = Button(text='Send Message To Client', size_hint=(None, None), size=(250, 150))
        button_layout = BoxLayout(padding=10, spacing=10, size_hint_y=None, height=150)
        
        self.label2 = Label(text='Last Message: ' + Server.last_message, font_size='20sp', color=(0, 0.7, 1, 1))
        
        button1.bind(on_press=self.on_button1_press)
        button2.bind(on_press=self.on_button2_press)
        
        root.add_widget(self.label)
        button_layout.add_widget(button1)
        button_layout.add_widget(button2)
        root.add_widget(button_layout)
        root.add_widget(self.label2)
        Clock.schedule_interval(self.update_label, 1.0)
        
        return root
    
    def on_button1_press(self, instance):
        server = Server()
        Server.status = Status.LIST
        server_thread = threading.Thread(target=server.start_server, args=('127.0.0.1', 8080))
        server_thread.daemon=True
        server_thread.start()
        
    def on_button2_press(self, instance):
        print("Button 2 pressed")
        
    def on_button3_press(self, instance):
        print("Button 3 pressed")
        
    def update_label(self, dt):
        self.label.text = "Server Status: " + Server.status.value
        self.label2.text = "Last Message: " + Server.last_message


if __name__ == '__main__':
    SimpleApp().run()
