from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.popup import Popup
import socket
import threading
import time
import random
import matplotlib
matplotlib.use('Agg')  # Use the Agg backend for non-interactive plotting
import matplotlib.pyplot as plt
from io import BytesIO
from kivy.graphics.texture import Texture
from kivy.uix.image import Image


class ServerApp(App):
    def build(self):
        self.data_x = []
        self.data_y = []
        self.i_values = []

        # Layouts
        main_layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        # Status label
        self.status_label = Label(text="Status: Idle", size_hint_y=None, height=40)
        main_layout.add_widget(self.status_label)

        # Port input and button layout
        port_layout = GridLayout(cols=3, spacing=10, size_hint_y=None, height=40)
        self.port_input = TextInput(hint_text="Enter port", size_hint_x=None, width=150)
        self.create_socket_button = Button(text="Create Socket", size_hint_x=None, width=150)
        self.create_socket_button.bind(on_press=self.create_socket)

        port_layout.add_widget(self.port_input)
        port_layout.add_widget(self.create_socket_button)
        main_layout.add_widget(port_layout)

        # Message input and send button
        message_layout = GridLayout(cols=2, spacing=10, size_hint_y=None, height=40)
        self.message_input = TextInput(hint_text="Enter message", size_hint_x=None, width=300)
        self.send_message_button = Button(text="Send Message", size_hint_x=None, width=150, disabled=True)
        self.send_message_button.bind(on_press=self.send_message)

        message_layout.add_widget(self.message_input)
        message_layout.add_widget(self.send_message_button)
        main_layout.add_widget(message_layout)

        # Last message label
        self.last_message_label = Label(text="Last Message: None", size_hint_y=None, height=40)
        main_layout.add_widget(self.last_message_label)

        # Statistics and time button
        stats_layout = GridLayout(cols=3, spacing=10, size_hint_y=None, height=40)
        self.show_stats_button = Button(text="Show Statistics", size_hint_x=None, width=150, disabled=True)
        self.show_stats_button.bind(on_press=self.show_statistics)
        self.send_time_button = Button(text="Send Time", size_hint_x=None, width=150, disabled=True)
        self.send_time_button.bind(on_press=self.send_time)

        stats_layout.add_widget(self.show_stats_button)
        stats_layout.add_widget(self.send_time_button)
        main_layout.add_widget(stats_layout)

        return main_layout

    def create_socket(self, instance):
        port = int(self.port_input.text)
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind(('0.0.0.0', port))
        self.server_socket.listen(1)
        self.status_label.text = "Status: Listening"
        self.create_socket_button.disabled = True
        self.send_message_button.disabled = False
        self.show_stats_button.disabled = False
        self.send_time_button.disabled = False

        # Start a new thread to handle client connections
        self.client_thread = threading.Thread(target=self.accept_client)
        self.client_thread.daemon = True
        self.client_thread.start()

    def accept_client(self):
        try:
            self.client_socket, _ = self.server_socket.accept()
            self.status_label.text = "Status: Connected"
            while True:
                data = self.client_socket.recv(1024)
                if not data:
                    break
                decoded_data = data.decode()
                self.last_message_label.text = f"Last Message: {decoded_data}"
                self.process_message(decoded_data)
        except (ConnectionResetError, OSError) as e:
            print(f"Error with client connection: {e}")
        finally:
            if self.client_socket:
                self.client_socket.close()
            if self.server_socket:
                self.server_socket.close()
            self.status_label.text = "Status: Closed"
            self.create_socket_button.disabled = False
            self.send_message_button.disabled = True
            self.show_stats_button.disabled = True
            self.send_time_button.disabled = True

    def send_message(self, instance):
        message = self.message_input.text
        if hasattr(self, 'client_socket'):
            self.client_socket.sendall(message.encode())
            self.message_input.text = ""

    def send_time(self, instance):
        if hasattr(self, 'client_socket'):
            try:
                current_time = time.strftime('%Y-%m-%d %H:%M:%S')
                self.client_socket.sendall(f"TIME={current_time}".encode())
                print(f"Sent time: {current_time}")
            except Exception as e:
                print(f"Error sending time: {e}")

    def process_message(self, message):
        if message.startswith('<x=') and 'y=' in message:
            try:
                x = int(message.split('x=')[1].split('|')[0])
                y = int(message.split('y=')[1].strip('>'))
                if len(self.data_x) >= 10:
                    self.data_x.pop(0)
                    self.data_y.pop(0)
                self.data_x.append(x)
                self.data_y.append(y)
            except ValueError:
                pass
        elif message.startswith('<I='):
            try:
                i_value = float(message.split('<I=')[1].strip('>'))
                self.i_values.append(i_value)
                if len(self.i_values) > 10:
                    self.i_values.pop(0)
            except ValueError:
                pass

    def show_statistics(self, instance):
        try:
            if self.i_values:
                avg_i = sum(self.i_values) / len(self.i_values)
                print(f"Average I: {avg_i:.2f}")
                self.show_popup("Statistics", f"Average I: {avg_i:.2f}")

            if self.data_x and self.data_y:
                print(f"Data x: {self.data_x}")
                print(f"Data y: {self.data_y}")

                plt.figure(figsize=(6, 4))
                plt.plot(self.data_x, self.data_y, marker='o', linestyle='-')
                plt.title('Last 10 Values of x and y')
                plt.xlabel('x')
                plt.ylabel('y')
                plt.grid(True)

                buf = BytesIO()
                plt.savefig(buf, format='png')
                buf.seek(0)

                # Check buffer content
                buf_contents = buf.getvalue()
                if not buf_contents:
                    raise ValueError("Buffer is empty after saving plot")
                print(f"Buffer size: {len(buf_contents)} bytes")

                # Create the texture
                image = Image()
                texture = Texture.create(size=(600, 400), colorfmt='rgba')
                texture.blit_buffer(buf_contents, colorfmt='rgba', bufferfmt='ubyte')
                texture.flip_vertical()
                image.texture = texture

                buf.close()
                self.show_popup("Plot", "", image)
        except Exception as e:
            print(f"Error showing statistics: {e}")

    def show_popup(self, title, message, image=None):
        layout = BoxLayout(orientation='vertical')
        if message:
            layout.add_widget(Label(text=message, size_hint_y=None, height=40))
        if image:
            layout.add_widget(image)
        close_button = Button(text="Close", size_hint_y=None, height=50)
        close_button.bind(on_press=lambda instance: popup.dismiss())
        layout.add_widget(close_button)
        popup = Popup(title=title, content=layout, size_hint=(0.8, 0.8))
        popup.open()


if __name__ == '__main__':
    ServerApp().run()
