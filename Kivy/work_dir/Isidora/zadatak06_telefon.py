from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.clock import Clock


class TelephoneApp(App):
    def build(self):
        self.history = []
        self.message = ""
        self.character_map = {
            '1': ".,?!",
            '2': "abc",
            '3': "def",
            '4': "ghi",
            '5': "jkl",
            '6': "mno",
            '7': "pqrs",
            '8': "tuv",
            '9': "wxyz",
            '*': "*+",
            '0': "0 ",
            '#': "#"
        }
        self.button_press_count = {key: 0 for key in self.character_map.keys()}
        self.button_press_timers = {key: None for key in self.character_map.keys()}
        self.delay = 0.5  # 500 milliseconds delay

        root = BoxLayout(orientation='vertical', padding=10, spacing=10)

        self.text_input = TextInput(multiline=False, readonly=True, font_size=32)
        root.add_widget(self.text_input)

        grid = GridLayout(cols=3, spacing=10)
        for button_text in self.character_map.keys():
            button_label = f'{button_text}\n{self.character_map[button_text]}'
            btn = Button(
                text=button_label,
                font_size=20,
                halign='center',
                valign='middle',
                size_hint_y=None,
                height=70
            )
            btn.bind(on_press=self.on_button_press)
            grid.add_widget(btn)

        root.add_widget(grid)

        action_layout = BoxLayout(size_hint_y=None, height=70, spacing=10, padding=(0, 20, 0, 0))
        send_button = Button(
            text='Send',
            on_press=self.on_send,
        )
        clear_last_character_button = Button(
            text='Clear last character',
            on_press=self.on_clear_last_character
        )
        clear_button = Button(
            text='Clear',
            on_press=self.on_clear
        )
        history_button = Button(
            text='History',
            on_press=self.on_history
        )
        hide_history_button = Button(
            text='Hide history',
            on_press=self.on_history_hide
        )

        action_layout.add_widget(send_button)
        action_layout.add_widget(clear_last_character_button)
        action_layout.add_widget(clear_button)
        action_layout.add_widget(history_button)
        action_layout.add_widget(hide_history_button)

        root.add_widget(action_layout)

        self.history_label = Label(text='Message history will be displayed here.', size_hint_y=None, height=200)
        root.add_widget(self.history_label)

        return root

    def on_button_press(self, instance):
        button_text = instance.text.split('\n')[0]

        if self.button_press_timers[button_text] is not None:
            self.button_press_timers[button_text].cancel()

        self.button_press_count[button_text] += 1

        self.button_press_timers[button_text] = Clock.schedule_once(
            lambda dt: self.process_button_press(button_text), self.delay
        )

    def process_button_press(self, button_text):
        char_set = self.character_map[button_text]
        index = (self.button_press_count[button_text] - 1) % len(char_set)
        character = char_set[index]

        self.message += character
        self.text_input.text = self.message

        self.button_press_count[button_text] = 0

    def on_send(self, instance):
        self.history.append(self.message)
        self.history_label.text = self.message
        self.message = ""
        self.text_input.text = ""

    def on_clear_last_character(self, instance):
        if self.message:
            self.message = self.message[:-1]
            self.text_input.text = self.message

    def on_clear(self, instance):
        self.message = ""
        self.text_input.text = ""

    def on_history(self, instance):
        self.history_label.text = '\n'.join(self.history)

    def on_history_hide(self, instance):
        self.history_label.text = ""


if __name__ == '__main__':
    TelephoneApp().run()
