from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.uix.label import Label
from kivy.clock import Clock
class PhoneApp(App):
    def build(self):

        self.message_history = []

        self.finalize_event = None
        self.last_key = None
        self.press_count = 0
        self.last_press_time = None
        self.chars = None

        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        self.text_input = TextInput(multiline=False, size_hint_y=None, height=40)
        layout.add_widget(self.text_input)

        keypad = GridLayout(rows=4, cols=3, spacing=10, size_hint_y=10, height=400)

        self.buttons = {
            '1': ',.?!', '2': 'abc', '3': 'def',
            '4': 'ghi', '5': 'jkl', '6': 'mno',
            '7': 'pqrs', '8': 'tuv', '9': 'wxyz',
            '*': '+', '0': ' ', '#': '#'
        }

        for key, chars in self.buttons.items():
            button = Button(text=key, size_hint_y=None, height=50)
            button.bind(on_press=self.button_pressed)
            keypad.add_widget(button)

        layout.add_widget(keypad)

        action_layout = BoxLayout(orientation='vertical', spacing=10)

        self.send_button = Button(text='Send',size_hint_y=None, height=50)
        self.send_button.bind(on_press=self.send_text)
        action_layout.add_widget(self.send_button)

        self.clear_button = Button(text='Clear',size_hint_y=None, height=50)
        self.clear_button.bind(on_press=self.clear_text)
        action_layout.add_widget(self.clear_button)

        layout.add_widget(action_layout)

        self.result_label = Label(text='Result will be displayed here.')
        layout.add_widget(self.result_label)

        self.history_layout = BoxLayout(orientation='vertical', spacing=10)
        self.history_scroll = ScrollView(size_hint=(1, 1))
        self.history_scroll.add_widget(self.history_layout)

        self.history_button = Button(text='History', size_hint_y=None, height=50)
        self.history_button.bind(on_press=self.show_history)

        layout.add_widget(self.history_scroll)
        layout.add_widget(self.history_button)

        return layout

    def button_pressed(self, instance):

        if self.finalize_event is not None:
            self.finalize_event.cancel()

        if self.last_key is not None and self.last_key != instance.text:
            self.add_char(self)
            self.last_key = instance.text
            self.button_pressed(instance)
            return

        self.chars = self.buttons[instance.text]

        if self.last_key is None:
            self.last_key = instance.text
            self.press_count += 1

        elif self.last_key == instance.text:
            self.press_count += 1

        self.finalize_event = Clock.schedule_once(self.add_char, 1)

    def add_char(self, instance):

        if self.press_count > len(self.chars):
            self.press_count %= len(self.chars)

        char = self.chars[self.press_count - 1]
        self.text_input.text += char

        self.press_count = 0
        self.last_key = None

    def send_text(self, instance):
        message = self.text_input.text
        if message:
            self.result_label.text = f'Sent: {message}'
            self.message_history.append(message)
            self.text_input.text = ''

    def clear_text(self, instance):
        self.text_input.text = ''
        self.result_label.text = 'Result will be displayed here'

    def show_history(self, instance):
        self.history_layout.clear_widgets()
        for message in self.message_history:
            self.history_layout.add_widget(Label(text=message, size_hint_y=None, height=40))



if __name__ == '__main__':
    PhoneApp().run()