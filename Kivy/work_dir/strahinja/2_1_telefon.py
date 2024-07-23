from kivy.uix.actionbar import BoxLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.actionbar import Label
from kivy.uix.codeinput import TextInput
from kivy.uix.actionbar import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.accordion import Widget
from kivy.app import App
from kivy.clock import Clock


class TelefonApp(App):
    def telefon(self):
        tel = GridLayout(rows=4, cols=3)
        self.buttons = [
            {"button": Button(text="1 (,.?!)"), "commands": ",.?!"},
            {"button": Button(text="2 (abc)"), "commands": "abc"},
            {"button": Button(text="3 (def)"), "commands": "def"},
            {"button": Button(text="4 (ghi)"), "commands": "ghi"},
            {"button": Button(text="5 (jkl)"), "commands": "jkl"},
            {"button": Button(text="6 (mno)"), "commands": "mno"},
            {"button": Button(text="7 (pqrs)"), "commands": "pqrs"},
            {"button": Button(text="8 (tuv)"), "commands": "tuv"},
            {"button": Button(text="9 (wxyz)"), "commands": "wxyz"},
            {"button": Button(text="*+"), "commands": "*+"},
            {"button": Button(text="0"), "commands": "0"},
            {"button": Button(text="#"), "commands": "#"},
        ]

        self.history = {}
        self.events = {}

        for b in self.buttons:
            self.history[b["commands"]] = -1
            b["button"].bind(
                on_press=lambda instance, cmd=b["commands"]: self.update_input(
                    self.press(cmd)
                )
            )
            tel.add_widget(b["button"])

        return tel

    def press(self, commands):
        self.debounce(commands)
        self.debounce_print(commands)
        self.history[commands] = (self.history[commands] + 1) % len(commands)
        return commands[self.history[commands]]

    def reset_history(self, commands):
        print("trigger reset")
        self.history[commands] = -1

    def update_input(self, character):
        if self.input_pos == len(self.input.text):
            self.input.text += character
        self.input.text = self.input.text[0 : self.input_pos] + character

    def advance_input_pos(self):
        self.input_pos += 1

    def build(self):
        self.input_pos = 0
        self.wait_time = 0.5
        self.events = {}
        self.events_print = {}
        self.buttons = []
        self.history = {}
        self.tel = self.telefon()
        self.input = TextInput()
        self.label = Label()
        self.clear = Button(text="Clear", on_press=lambda _: self.do_clear())
        self.send = Button(text="Send", on_press=lambda _: self.do_send())

        self.box = BoxLayout(orientation="vertical")
        self.box.add_widget(self.tel)
        self.box.add_widget(self.input)
        self.box.add_widget(self.send)
        self.box.add_widget(self.label)
        self.box.add_widget(self.clear)

        return self.box

    def do_clear(self):
        self.label.text = ""
        self.input.text = ""
        self.input_pos = 0

    def do_send(self):
        self.label.text = self.input.text
        self.input.text = ""
        self.input_pos = 0

    def debounce(self, commands):
        if commands in self.events and self.events[commands]:
            Clock.unschedule(self.events[commands])
            print(f"Cancelling existing event for command: {commands}")

        def reset_callback(dt):
            self.reset_history(commands)

        self.events[commands] = Clock.schedule_once(reset_callback, self.wait_time)
        print(
            f"Scheduled new event for command: {commands} with wait time: {self.wait_time}"
        )

    def debounce_print(self, commands):
        if commands in self.events_print and self.events_print[commands]:
            Clock.unschedule(self.events_print[commands])
            print(f"Cancelling existing event for command: {commands}")

        def reset_callback(dt):
            self.advance_input_pos()

        self.events_print[commands] = Clock.schedule_once(
            reset_callback, self.wait_time
        )
        print(
            f"Scheduled new event for command: {commands} with wait time: {self.wait_time}"
        )


if __name__ == "__main__":
    TelefonApp().run()
